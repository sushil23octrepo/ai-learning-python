import chromadb

from openai import OpenAI

# ------------------------------------------------------------
# 1. CREATE CLIENTS
# ------------------------------------------------------------

chroma_client = chromadb.Client()
client = OpenAI()


# ------------------------------------------------------------
# 2. DOCUMENTS
# ------------------------------------------------------------

documents = [
    {
        "id": "hr-1",
        "text": "Employees receive 20 paid leave days per year.",
        "source": "hr_policy",
    },
    {
        "id": "security-1",
        "text": "Passwords must contain at least 12 characters.",
        "source": "security_policy",
    },
    {
        "id": "security-2",
        "text": "Administrator accounts require multi-factor authentication.",
        "source": "security_policy",
    },
    {
        "id": "finance-1",
        "text": "Expense claims must be submitted within 30 days.",
        "source": "finance_policy",
    },
    {
        "id": "remote-1",
        "text": "Employees may work remotely two days per week.",
        "source": "remote_work_policy",
    },
]


try:

    # --------------------------------------------------------
    # 3. EXTRACT DOCUMENT TEXT
    # --------------------------------------------------------

    texts = [document["text"] for document in documents]

    # --------------------------------------------------------
    # 4. CREATE DOCUMENT EMBEDDINGS
    # --------------------------------------------------------

    embedding_response = client.embeddings.create(
        model="text-embedding-3-small",
        input=texts,
    )

    embeddings = [item.embedding for item in embedding_response.data]

    # --------------------------------------------------------
    # 5. CREATE VECTOR COLLECTION
    # --------------------------------------------------------

    collection = chroma_client.create_collection(name="company_policies")

    # --------------------------------------------------------
    # 6. STORE DOCUMENTS + EMBEDDINGS + METADATA
    # --------------------------------------------------------

    collection.add(
        ids=[item["id"] for item in documents],
        documents=texts,
        metadatas=[{"source": item["source"]} for item in documents],
        embeddings=embeddings,
    )

    # --------------------------------------------------------
    # 7. USER QUERY
    # --------------------------------------------------------

    query = """
What is the minimum password length?
"""

    # --------------------------------------------------------
    # 8. CREATE QUERY EMBEDDING
    # --------------------------------------------------------

    query_response = client.embeddings.create(
        model="text-embedding-3-small",
        input=query,
    )

    query_embedding = query_response.data[0].embedding

    # --------------------------------------------------------
    # 9. SEARCH VECTOR DATABASE
    # --------------------------------------------------------

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=2,
    )

    # --------------------------------------------------------
    # 10. PRINT RETRIEVED DOCUMENTS + METADATA
    # --------------------------------------------------------

    retrieved_documents = results["documents"][0]

    retrieved_metadatas = results["metadatas"][0]

    print("Retrieved Documents:")

    for document, metadata in zip(
        retrieved_documents,
        retrieved_metadatas,
    ):
        print()
        print("Document:", document)
        print("Source:", metadata["source"])

    # --------------------------------------------------------
    # 11. BUILD CONTEXT
    # --------------------------------------------------------

    context = "\n\n".join(retrieved_documents)

    # --------------------------------------------------------
    # 12. GPT INSTRUCTIONS
    # --------------------------------------------------------

    instructions = """
You are a company policy assistant.

Answer the question using only the provided context.

If the provided context does not contain the answer,
say that the information is not available.

Keep the answer concise.
"""

    # --------------------------------------------------------
    # 13. GENERATE FINAL ANSWER
    # --------------------------------------------------------

    response = client.responses.create(
        model="gpt-5.6",
        instructions=instructions,
        input=f"""
Context:
{context}

Question:
{query}
""",
    )

    # --------------------------------------------------------
    # 14. PRINT ANSWER
    # --------------------------------------------------------

    print()
    print("Answer:")

    print(response.output_text)


except Exception as ex:

    print(f"Vector search / RAG failed: {ex}")
