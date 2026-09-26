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
    "Employees receive 20 annual leave days.",
    "Passwords must contain at least 12 characters.",
    "Expense claims must be submitted within 30 days.",
    "Employees can work remotely two days per week.",
]

query = """
How many vacation days do employees get?
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
    similarity = cosine_similarity(query_embedding, item.embedding)
    results.append({"document": documents[index], "similarity": similarity})


results.sort(key=lambda item: item["similarity"], reverse=True)

print("Search results:")

for result in results:
    print(
        result["similarity"],
        "-",
        result["document"],
    )

best_match = results[0]

print()
print(
    "Best match:",
    best_match["document"],
)
