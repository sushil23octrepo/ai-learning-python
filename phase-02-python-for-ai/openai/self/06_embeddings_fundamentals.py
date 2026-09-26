from openai import OpenAI
import numpy as np

client = OpenAI()


# text = """
# Dependency injection allows an object's dependencies
# to be provided from outside the object.
# """


# response = client.embeddings.create(
#     model="text-embedding-3-small",
#     input=text,
# )


# embedding = response.data[0].embedding


# print(
#     "Vector length:",
#     len(embedding),
# )

# print(
#     "First 10 values:",
#     embedding[:10],
# )

# print("==================")
# for item in response.data:
#     print(
#         item.index,
#         len(item.embedding),
#     )


def cosine_similarity(vector_a, vector_b):
    vector_a = np.array(vector_a)
    vector_b = np.array(vector_b)

    magnitute_a = np.linalg.norm(vector_a)
    magnitute_b = np.linalg.norm(vector_b)

    dot_product = np.dot(vector_a, vector_b)

    if magnitute_a == 0 or magnitute_b == 0:
        raise ValueError("Cosine similarity is undefined for a zero vector.")

    cs_result = dot_product / (magnitute_a * magnitute_b)
    return cs_result


texts = [
    "The user forgot their password.",
    "The customer cannot remember the login password.",
    "The weather is sunny today.",
]

response = client.embeddings.create(model="text-embedding-3-small", input=texts)

embedding_1 = response.data[0].embedding
embedding_2 = response.data[1].embedding
embedding_3 = response.data[2].embedding


similarity_1_2 = cosine_similarity(
    embedding_1,
    embedding_2,
)

similarity_1_3 = cosine_similarity(
    embedding_1,
    embedding_3,
)


print(
    "Password vs password:",
    similarity_1_2,
)

print(
    "Password vs weather:",
    similarity_1_3,
)
