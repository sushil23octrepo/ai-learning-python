import numpy as np

from openai import OpenAI

# ============================================================
# MODULE 06 — EMBEDDINGS FUNDAMENTALS
#
# Goal:
# Learn how text can be converted into numerical vectors,
# how those vectors can be compared using cosine similarity,
# and how embeddings become the foundation for:
#
# - semantic search
# - vector databases
# - RAG
# - document retrieval
# - similarity matching
#
# IMPORTANT:
#
# Embeddings do NOT generate natural-language answers.
#
# They convert text into vectors that represent semantic meaning.
# ============================================================


# ------------------------------------------------------------
# 1. CREATE OPENAI CLIENT
# ------------------------------------------------------------

client = OpenAI()


# ------------------------------------------------------------
# 2. SIMPLE EMBEDDING EXAMPLE
# ------------------------------------------------------------

text = """
Dependency injection allows an object's dependencies
to be provided from outside the object.
"""

response = client.embeddings.create(
    model="text-embedding-3-small",
    input=text,
)

embedding = response.data[0].embedding


# ------------------------------------------------------------
# 3. INSPECT THE EMBEDDING
# ------------------------------------------------------------

# An embedding is a list of floating-point numbers.
#
# Example conceptually:
#
# [
#     0.0123,
#     -0.0456,
#     0.0789,
#     ...
# ]
#
# We normally do not print the complete vector because it can
# contain many values.

print(
    "Embedding vector length:",
    len(embedding),
)

print(
    "First 10 values:",
    embedding[:10],
)


# ------------------------------------------------------------
# 4. MULTIPLE TEXTS IN ONE REQUEST
# ------------------------------------------------------------

texts = [
    "The user forgot their password.",
    "The customer cannot remember the login password.",
    "The weather is sunny today.",
]


response = client.embeddings.create(
    model="text-embedding-3-small",
    input=texts,
)


# ------------------------------------------------------------
# 5. EXTRACT INDIVIDUAL EMBEDDINGS
# ------------------------------------------------------------

embedding_1 = response.data[0].embedding
embedding_2 = response.data[1].embedding
embedding_3 = response.data[2].embedding


# ------------------------------------------------------------
# 6. COSINE SIMILARITY
# ------------------------------------------------------------

# Cosine similarity compares the direction of two vectors.
#
# Higher similarity:
# -> meanings are more similar
#
# Lower similarity:
# -> meanings are less similar
#
# Formula:
#
#        A · B
# ---------------------
# ||A|| * ||B||
#
# We already studied NumPy, so we can calculate this using:
#
# np.dot()
# np.linalg.norm()


def cosine_similarity(vector_a, vector_b):
    vector_a = np.array(vector_a)

    vector_b = np.array(vector_b)

    similarity = np.dot(
        vector_a,
        vector_b,
    ) / (np.linalg.norm(vector_a) * np.linalg.norm(vector_b))

    return similarity


# ------------------------------------------------------------
# 7. COMPARE SEMANTIC SIMILARITY
# ------------------------------------------------------------

password_similarity = cosine_similarity(
    embedding_1,
    embedding_2,
)

weather_similarity = cosine_similarity(
    embedding_1,
    embedding_3,
)


print()

print(
    "Password vs password similarity:",
    password_similarity,
)

print(
    "Password vs weather similarity:",
    weather_similarity,
)


# ------------------------------------------------------------
# 8. DETERMINE WHICH PAIR IS MORE SIMILAR
# ------------------------------------------------------------

if password_similarity > weather_similarity:

    print("The two password-related sentences are more " "semantically similar.")

else:

    print(
        "The password sentence and weather sentence are " "more semantically similar."
    )


# ------------------------------------------------------------
# 9. SEMANTIC SEARCH IDEA
# ------------------------------------------------------------

documents = [
    "Employees receive 20 annual leave days.",
    "Passwords must contain at least 12 characters.",
    "Expense claims must be submitted within 30 days.",
]


query = """
How many vacation days do employees receive?
"""


# Create embeddings for all documents.

document_response = client.embeddings.create(
    model="text-embedding-3-small",
    input=documents,
)


# Create an embedding for the user's query.

query_response = client.embeddings.create(
    model="text-embedding-3-small",
    input=query,
)


query_embedding = query_response.data[0].embedding


# ------------------------------------------------------------
# 10. COMPARE QUERY WITH EACH DOCUMENT
# ------------------------------------------------------------

similarities = []


for item in document_response.data:

    document_embedding = item.embedding

    similarity = cosine_similarity(
        query_embedding,
        document_embedding,
    )

    similarities.append(similarity)


# ------------------------------------------------------------
# 11. FIND THE MOST SIMILAR DOCUMENT
# ------------------------------------------------------------

best_index = int(np.argmax(similarities))


best_document = documents[best_index]


print()
print(
    "User query:",
    query.strip(),
)

print(
    "Most relevant document:",
    best_document,
)

print(
    "Similarity:",
    similarities[best_index],
)


# ------------------------------------------------------------
# 12. ERROR-HANDLING EXAMPLE
# ------------------------------------------------------------

try:

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input="What is dependency injection?",
    )

    embedding = response.data[0].embedding

    print()
    print("Embedding generated successfully.")

    print(
        "Vector length:",
        len(embedding),
    )

except Exception as ex:

    print(f"Embedding request failed: {ex}")


# ============================================================
# IMPORTANT REVISION NOTES
# ============================================================


# ------------------------------------------------------------
# WHAT IS AN EMBEDDING?
# ------------------------------------------------------------

# Text:
#
# "Dependency injection"
#
#        ↓
#
# Embedding model
#
#        ↓
#
# Numerical vector:
#
# [0.01, -0.23, 0.47, ...]
#
#
# The vector represents the semantic meaning of the text.


# ------------------------------------------------------------
# EMBEDDING MODEL VS GPT MODEL
# ------------------------------------------------------------

# GPT model:
#
# gpt-5.6
#
# Used for:
#
# - answering questions
# - reasoning
# - generating text
# - function calling
# - structured output


# Embedding model:
#
# text-embedding-3-small
#
# Used for:
#
# - text -> vector
# - semantic similarity
# - search
# - retrieval
# - vector databases
# - RAG


# ------------------------------------------------------------
# API DIFFERENCE
# ------------------------------------------------------------

# Text generation:
#
# client.responses.create(...)
#
#
# Embeddings:
#
# client.embeddings.create(...)


# ------------------------------------------------------------
# RESPONSE DIFFERENCE
# ------------------------------------------------------------

# Text generation:
#
# response.output_text
#
#
# Embeddings:
#
# response.data[0].embedding


# ------------------------------------------------------------
# MULTIPLE INPUTS
# ------------------------------------------------------------

# We can create several embeddings in one request:
#
# texts = [
#     "Sentence 1",
#     "Sentence 2",
#     "Sentence 3",
# ]
#
#
# response = client.embeddings.create(
#     model="text-embedding-3-small",
#     input=texts,
# )
#
#
# Then:
#
# response.data[0].embedding
# response.data[1].embedding
# response.data[2].embedding


# ------------------------------------------------------------
# COSINE SIMILARITY
# ------------------------------------------------------------

# Used to compare two embedding vectors.
#
# Conceptually:
#
# higher similarity
# -> more similar meaning
#
# lower similarity
# -> less similar meaning
#
#
# Example:
#
# "forgot password"
#
# and
#
# "cannot remember login password"
#
# should be more similar than:
#
# "forgot password"
#
# and
#
# "weather is sunny"


# ------------------------------------------------------------
# KEYWORD SEARCH VS SEMANTIC SEARCH
# ------------------------------------------------------------

# Keyword search:
#
# "vacation"
#
# may not directly match:
#
# "annual leave"
#
#
# Semantic search can understand that:
#
# vacation days
# ≈
# annual leave


# ============================================================
# SEMANTIC SEARCH FLOW
# ============================================================

# Documents
#    ↓
# Generate embeddings
#    ↓
# Store vectors
#
#
# User query
#    ↓
# Generate query embedding
#    ↓
# Compare with document vectors
#    ↓
# Find most similar document


# ============================================================
# RAG CONNECTION
# ============================================================

# Embeddings are one of the core building blocks of RAG.
#
#
# User question
#      ↓
# Generate embedding
#      ↓
# Search vector database
#      ↓
# Retrieve relevant document chunks
#      ↓
# Send chunks + question to GPT
#      ↓
# Generate grounded answer


# ------------------------------------------------------------
# VERY IMPORTANT DISTINCTION
# ------------------------------------------------------------

# Embeddings:
#
# FIND relevant information.
#
#
# GPT:
#
# USES the information to generate an answer.


# ============================================================
# FUTURE ENTERPRISE ARCHITECTURE
# ============================================================

#               INGESTION
#
# Company Documents
#        ↓
# Split into chunks
#        ↓
# Embedding Model
#        ↓
# Vectors
#        ↓
# Vector Database
#
#
#                SEARCH
#
# User Question
#        ↓
# Query Embedding
#        ↓
# Vector Similarity Search
#        ↓
# Relevant Chunks
#        ↓
# GPT
#        ↓
# Final Answer


# ============================================================
# CORE PATTERN TO REMEMBER
# ============================================================

# Text
#   ↓
# Embedding Model
#   ↓
# Vector
#   ↓
# Cosine Similarity
#   ↓
# Semantic Search
#   ↓
# Vector Database
#   ↓
# RAG
