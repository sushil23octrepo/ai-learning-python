import numpy as np

from openai import OpenAI

# ============================================================
# OPENAI API EXERCISE 08
# MANUAL RAG PIPELINE
# Reference solution.
# ============================================================


# ------------------------------------------------------------
# 1. CREATE CLIENT
# ------------------------------------------------------------

client = OpenAI()


# ------------------------------------------------------------
# 2. COSINE SIMILARITY
# ------------------------------------------------------------


def cosine_similarity(
    vector_a,
    vector_b,
):
    vector_a = np.array(vector_a)

    vector_b = np.array(vector_b)

    return np.dot(
        vector_a,
        vector_b,
    ) / (np.linalg.norm(vector_a) * np.linalg.norm(vector_b))


# ------------------------------------------------------------
# 3. DOCUMENTS
# ------------------------------------------------------------

documents = [
    "Employees receive 20 paid leave days each year.",
    "Administrator accounts must use multi-factor authentication.",
    "Password reset links expire after 30 minutes.",
    "Database backups are performed every night.",
    "Employees may work remotely up to two days per week.",
]


# ------------------------------------------------------------
# 4. USER QUESTION
# ------------------------------------------------------------

query = """
How long is a password reset link valid?
"""


try:

    # --------------------------------------------------------
    # 5. CREATE DOCUMENT EMBEDDINGS
    # --------------------------------------------------------

    document_response = client.embeddings.create(
        model="text-embedding-3-small",
        input=documents,
    )

    # --------------------------------------------------------
    # 6. CREATE QUERY EMBEDDING
    # --------------------------------------------------------

    query_response = client.embeddings.create(
        model="text-embedding-3-small",
        input=query,
    )

    query_embedding = query_response.data[0].embedding

    # --------------------------------------------------------
    # 7. CALCULATE SIMILARITY
    # --------------------------------------------------------

    results = []

    for index, item in enumerate(document_response.data):

        similarity = cosine_similarity(
            query_embedding,
            item.embedding,
        )

        results.append(
            {
                "document": documents[index],
                "similarity": similarity,
            }
        )

    # --------------------------------------------------------
    # 8. SORT RESULTS
    # --------------------------------------------------------

    results.sort(
        key=lambda item: item["similarity"],
        reverse=True,
    )

    # --------------------------------------------------------
    # 9. RETRIEVE TOP 2
    # --------------------------------------------------------

    top_k = 2

    top_results = results[:top_k]

    # --------------------------------------------------------
    # 10. PRINT RETRIEVED RESULTS
    # --------------------------------------------------------

    print("Top 2 Retrieved Documents:")

    for index, result in enumerate(
        top_results,
        start=1,
    ):

        print(
            f"{index}. "
            f"{result['document']} "
            f"- Similarity: {result['similarity']:.4f}"
        )

    # --------------------------------------------------------
    # 11. COMBINE CONTEXT
    # --------------------------------------------------------

    context = "\n\n".join(result["document"] for result in top_results)

    # --------------------------------------------------------
    # 12. APPLICATION INSTRUCTIONS
    # --------------------------------------------------------

    instructions = """
You are a company policy assistant.

Answer the user's question using only the provided context.

If the context does not contain enough information,
say that the information is not available in the
provided context.

Keep the answer concise.
"""

    # --------------------------------------------------------
    # 13. BUILD INPUT
    # --------------------------------------------------------

    user_input = f"""
Context:
{context}

Question:
{query}
"""

    # --------------------------------------------------------
    # 14. GENERATE ANSWER
    # --------------------------------------------------------

    response = client.responses.create(
        model="gpt-5.6",
        instructions=instructions,
        input=user_input,
    )

    # --------------------------------------------------------
    # 15. PRINT FINAL ANSWER
    # --------------------------------------------------------

    print()
    print("Final Answer:")

    print(response.output_text)


except Exception as ex:

    print(f"RAG request failed: {ex}")
