import numpy as np

from openai import OpenAI

client = OpenAI()


def cosine_similarity(vector_a, vector_b):
    vector_a = np.array(vector_a)
    vector_b = np.array(vector_b)

    return np.dot(
        vector_a,
        vector_b,
    ) / (np.linalg.norm(vector_a) * np.linalg.norm(vector_b))


documents = [
    "Multi-factor authentication is required for administrator accounts.",
    "Employees receive 20 paid leave days each year.",
    "Database backups are retained for 30 days.",
    "Passwords must be at least 12 characters long.",
    "Expense reports require manager approval.",
]

query = """
What is the password length requirement?
"""

document_response = client.embeddings.create(
    model="text-embedding-3-small",
    input=documents,
)

query_response = client.embeddings.create(
    model="text-embedding-3-small",
    input=query,
)

query_embedding = query_response.data[0].embedding

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

results.sort(
    key=lambda item: item["similarity"],
    reverse=True,
)

best_match = results[0]

context = best_match["document"]

instructions = """
You are a company policy assistant.

Answer the question using only the provided context.

If the context does not contain enough information,
say that the information is not available in the provided context.

Keep the answer concise.
"""

user_input = f"""
Context:
{context}

Question:
{query}
"""

response = client.responses.create(
    model="gpt-5.6",
    instructions=instructions,
    input=user_input,
)

print("Retrieved Context:", context)

print()

print("Answer:", response.output_text)
