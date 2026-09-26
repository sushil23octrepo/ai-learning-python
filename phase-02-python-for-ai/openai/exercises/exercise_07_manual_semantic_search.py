import numpy as np

from openai import OpenAI

# ============================================================
# OPENAI API EXERCISE 07
# MANUAL SEMANTIC SEARCH
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
    "Multi-factor authentication is required for administrator accounts.",
    "Employees receive 20 paid leave days each year.",
    "Database backups are retained for 30 days.",
    "Passwords must be at least 12 characters long.",
    "Expense reports require manager approval.",
]


# ------------------------------------------------------------
# 4. USER QUERY
# ------------------------------------------------------------

query = """
What is the password length requirement?
"""


try:

    # --------------------------------------------------------
    # 5. GENERATE DOCUMENT EMBEDDINGS
    # --------------------------------------------------------

    document_response = client.embeddings.create(
        model="text-embedding-3-small",
        input=documents,
    )

    # --------------------------------------------------------
    # 6. GENERATE QUERY EMBEDDING
    # --------------------------------------------------------

    query_response = client.embeddings.create(
        model="text-embedding-3-small",
        input=query,
    )

    query_embedding = query_response.data[0].embedding

    # --------------------------------------------------------
    # 7. CALCULATE SIMILARITIES
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
    # 9. PRINT ALL RANKED RESULTS
    # --------------------------------------------------------

    print("Ranked Results:")

    for index, result in enumerate(
        results,
        start=1,
    ):

        print(f"{index}. " f"{result['document']} " f"- {result['similarity']:.4f}")

    # --------------------------------------------------------
    # 10. PRINT BEST MATCH
    # --------------------------------------------------------

    best_match = results[0]

    print()
    print("Best Match:")

    print(best_match["document"])

    print(
        "Similarity:",
        best_match["similarity"],
    )

    # --------------------------------------------------------
    # 11. TOP-2 RESULTS
    # --------------------------------------------------------

    top_k = 2

    top_results = results[:top_k]

    print()
    print("Top 2 Results:")

    for index, result in enumerate(
        top_results,
        start=1,
    ):

        print(f"{index}. " f"{result['document']} " f"- {result['similarity']:.4f}")


except Exception as ex:

    print(f"Semantic search failed: {ex}")
