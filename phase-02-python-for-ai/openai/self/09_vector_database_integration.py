import chromadb
from openai import OpenAI

client = OpenAI()
chroma_client = chromadb.Client()


documents = [
    {
        "id": "policy-1",
        "text": "Employees receive 20 paid leave days each year.",
        "source": "employee_policy",
    },
    {
        "id": "security-1",
        "text": "Administrator accounts must use multi-factor authentication.",
        "source": "security_policy",
    },
    {
        "id": "security-2",
        "text": "Password reset links expire after 30 minutes.",
        "source": "security_policy",
    },
    {
        "id": "backup-1",
        "text": "Database backups are performed every night.",
        "source": "backup_policy",
    },
]

texts = [document["text"] for document in documents]

embedding_response = client.embeddings.create(
    model="text-embedding-3-small", input=texts
)

embeddings = [item.embedding for item in embedding_response.data]

collection = chroma_client.create_collection(name="company_policies")

collection.add(
    ids=[document["id"] for document in documents],
    documents=texts,
    metadatas=[{"source": doc["source"]} for doc in documents],
    embeddings=embeddings,
)

query = """
How long can I use a password reset link?
"""

query_response = client.embeddings.create(model="text-embedding-3-small", input=query)
query_embedding = query_response.data[0].embedding

results = collection.query(query_embeddings=[query_embedding], n_results=2)

print("Retrieved Documents:")

for document in results["documents"][0]:
    print("-", document)

context = "\n\n".join(results["documents"][0])

print()
print(context)


instructions = """
You are a company policy assistant.

Answer the question using only the provided context.

If the provided context does not contain the answer,
say that the information is not available.

Keep the answer concise.
"""


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


print()
print("Answer:")
print(response.output_text)
