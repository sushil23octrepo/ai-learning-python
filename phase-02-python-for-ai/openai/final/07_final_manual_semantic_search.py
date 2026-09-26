import numpy as np

from openai import OpenAI

# ============================================================
# MODULE 07 — MANUAL SEMANTIC SEARCH
#
# Goal:
# Build a small semantic search engine manually using:
#
# - OpenAI embeddings
# - cosine similarity
# - ranking
# - Top-K retrieval
#
# This demonstrates the core retrieval mechanism that will
# later be handled more efficiently by a vector database.
#
#
# HIGH-LEVEL FLOW:
#
# Documents
#     ↓
# Generate document embeddings
#     ↓
#
# User query
#     ↓
# Generate query embedding
#     ↓
#
# Compare query vector with document vectors
#     ↓
# Calculate cosine similarity
#     ↓
# Rank documents
#     ↓
# Return most relevant document(s)
# ============================================================


# ------------------------------------------------------------
# 1. CREATE OPENAI CLIENT
# ------------------------------------------------------------

client = OpenAI()


# ------------------------------------------------------------
# 2. COSINE SIMILARITY FUNCTION
# ------------------------------------------------------------

# Embeddings are vectors.
#
# To determine how semantically similar two pieces of text
# are, we can compare their vectors using cosine similarity.
#
# Formula:
#
#               A · B
# similarity = -------
#              |A| |B|
#
# Higher similarity:
# -> more semantically similar
#
# Lower similarity:
# -> less semantically similar


def cosine_similarity(vector_a, vector_b):
    vector_a = np.array(vector_a)
    vector_b = np.array(vector_b)

    return np.dot(
        vector_a,
        vector_b,
    ) / (np.linalg.norm(vector_a) * np.linalg.norm(vector_b))


# ------------------------------------------------------------
# 3. DOCUMENT COLLECTION
# ------------------------------------------------------------

# Think of these as small pieces of company documentation.
#
# Later, these could instead be:
#
# - PDF chunks
# - policy documents
# - knowledge-base articles
# - database records
# - support documentation
# - security policies

documents = [
    "Multi-factor authentication is required for administrator accounts.",
    "Employees receive 20 paid leave days each year.",
    "Database backups are retained for 30 days.",
    "Passwords must be at least 12 characters long.",
    "Expense reports require manager approval.",
]


# ------------------------------------------------------------
# 4. USER SEARCH QUERY
# ------------------------------------------------------------

query = """
What is the password length requirement?
"""


try:

    # --------------------------------------------------------
    # 5. GENERATE DOCUMENT EMBEDDINGS
    # --------------------------------------------------------

    # We send all documents in one request.
    #
    # Each document receives its own embedding vector.
    #
    # Conceptually:
    #
    # Document 0 -> Vector 0
    # Document 1 -> Vector 1
    # Document 2 -> Vector 2
    # ...

    document_response = client.embeddings.create(
        model="text-embedding-3-small",
        input=documents,
    )

    # --------------------------------------------------------
    # 6. GENERATE QUERY EMBEDDING
    # --------------------------------------------------------

    # The user's query must be converted into the SAME
    # embedding space as our documents.
    #
    # Therefore, we use the same embedding model.

    query_response = client.embeddings.create(
        model="text-embedding-3-small",
        input=query,
    )

    # There is only one query, so its embedding is located
    # at index 0.

    query_embedding = query_response.data[0].embedding

    # --------------------------------------------------------
    # 7. CREATE RESULT COLLECTION
    # --------------------------------------------------------

    # Each result will contain:
    #
    # {
    #     "document": "...",
    #     "similarity": ...
    # }

    results = []

    # --------------------------------------------------------
    # 8. COMPARE QUERY AGAINST EVERY DOCUMENT
    # --------------------------------------------------------

    for index, item in enumerate(document_response.data):

        # Compare the query embedding against this
        # document's embedding.

        similarity = cosine_similarity(
            query_embedding,
            item.embedding,
        )

        # Keep the original document together with
        # its similarity score.

        results.append(
            {
                "document": documents[index],
                "similarity": similarity,
            }
        )

    # --------------------------------------------------------
    # 9. SORT RESULTS BY SIMILARITY
    # --------------------------------------------------------

    # Higher cosine similarity means a more relevant
    # semantic match.
    #
    # Therefore:
    #
    # reverse=True
    #
    # puts the highest similarity first.

    results.sort(
        key=lambda item: item["similarity"],
        reverse=True,
    )

    # --------------------------------------------------------
    # 10. PRINT ALL RANKED RESULTS
    # --------------------------------------------------------

    print("SEARCH QUERY:")
    print(query.strip())

    print()

    print("RANKED RESULTS:")

    for index, result in enumerate(
        results,
        start=1,
    ):

        print(
            f"{index}. "
            f"{result['document']} "
            f"(Similarity: {result['similarity']:.4f})"
        )

    # --------------------------------------------------------
    # 11. GET BEST MATCH
    # --------------------------------------------------------

    # Because results are sorted descending,
    #
    # results[0]
    #
    # is the most semantically similar document.

    best_match = results[0]

    print()
    print("BEST MATCH:")

    print(best_match["document"])

    print(
        "Similarity:",
        best_match["similarity"],
    )

    # --------------------------------------------------------
    # 12. TOP-K RETRIEVAL
    # --------------------------------------------------------

    # Instead of retrieving only one document, applications
    # frequently retrieve several relevant documents.
    #
    # K means how many results we want.
    #
    # Here:
    #
    # K = 2

    top_k = 2

    top_results = results[:top_k]

    print()
    print(f"TOP {top_k} RESULTS:")

    for index, result in enumerate(
        top_results,
        start=1,
    ):

        print(
            f"{index}. "
            f"{result['document']} "
            f"(Similarity: {result['similarity']:.4f})"
        )


except Exception as ex:

    print(f"Semantic search failed: {ex}")


# ============================================================
# IMPORTANT REVISION NOTES
# ============================================================


# ------------------------------------------------------------
# WHAT IS SEMANTIC SEARCH?
# ------------------------------------------------------------

# Traditional keyword search searches for matching words.
#
# Semantic search searches for matching MEANING.
#
#
# Example:
#
# Document:
#
# "Employees receive 20 annual leave days."
#
#
# User query:
#
# "How much vacation time do workers receive?"
#
#
# The exact wording is different:
#
# annual leave
# vs
# vacation time
#
#
# But embeddings can represent their similar meaning.


# ============================================================
# SEMANTIC SEARCH FLOW
# ============================================================

# Documents
#     ↓
# Embedding Model
#     ↓
# Document Vectors
#
#
# User Query
#     ↓
# Embedding Model
#     ↓
# Query Vector
#
#
# Query Vector
#     ↓
# Compare against Document Vectors
#     ↓
# Cosine Similarity
#     ↓
# Rank Results
#     ↓
# Best Match / Top-K Results


# ============================================================
# IMPORTANT: SAME EMBEDDING MODEL
# ============================================================

# Document embeddings and query embeddings should be created
# using the same embedding model.
#
#
# Example:
#
# Documents:
#
# text-embedding-3-small
#
#
# Query:
#
# text-embedding-3-small
#
#
# This ensures that the vectors exist in the same semantic
# vector space and can meaningfully be compared.


# ============================================================
# INGESTION TIME VS QUERY TIME
# ============================================================

# This distinction is VERY important for production RAG.


# ------------------------------------------------------------
# INGESTION TIME
# ------------------------------------------------------------

# Documents
#     ↓
# Split into chunks
#     ↓
# Generate embeddings
#     ↓
# Store text + vectors
#
#
# This normally happens when documents are:
#
# - added
# - uploaded
# - updated
# - indexed


# ------------------------------------------------------------
# QUERY TIME
# ------------------------------------------------------------

# User question
#     ↓
# Generate query embedding
#     ↓
# Search existing stored vectors
#     ↓
# Retrieve relevant documents
#
#
# We should NOT regenerate every document embedding whenever
# a user asks a question.


# ============================================================
# LEARNING EXAMPLE VS PRODUCTION
# ============================================================

# Our current learning code does:
#
# Query arrives
#      ↓
# Generate document embeddings
#      ↓
# Generate query embedding
#      ↓
# Search
#
#
# This is fine for learning with 5 documents.


# Production architecture:
#
# INGESTION:
#
# Documents
#      ↓
# Generate embeddings once
#      ↓
# Store embeddings


# QUERY:
#
# User query
#      ↓
# Generate ONLY query embedding
#      ↓
# Search stored vectors


# ============================================================
# WHAT IS TOP-K?
# ============================================================

# Top-K means:
#
# Return the K highest-ranked results.
#
#
# Example:
#
# top_k = 3
#
# means:
#
# return the 3 most relevant documents.


# ------------------------------------------------------------
# WHY NOT ALWAYS RETURN ONLY TOP 1?
# ------------------------------------------------------------

# A user's answer may require information from multiple
# documents.
#
# For example:
#
# Question:
#
# "What are our password and MFA requirements?"
#
#
# Relevant document 1:
#
# Password policy
#
#
# Relevant document 2:
#
# MFA policy
#
#
# Retrieving several documents gives the LLM more relevant
# context.


# ============================================================
# SIMILARITY THRESHOLD
# ============================================================

# Ranking always produces a "best" result.
#
# But the best result might still be a poor match.
#
# Therefore production systems may also use a minimum
# similarity threshold.
#
#
# Conceptually:
#
# if similarity >= threshold:
#     use document
# else:
#     no relevant document
#
#
# IMPORTANT:
#
# There is no universal similarity threshold such as 0.5
# that works for every application.
#
# Thresholds should be determined through evaluation using
# the application's real data.


# ============================================================
# WHY A VECTOR DATABASE?
# ============================================================

# Our manual implementation compares:
#
# Query
#
# against
#
# EVERY document vector.
#
#
# With 5 documents:
#
# easy.
#
#
# With millions of vectors:
#
# inefficient to perform manually in Python.


# Vector databases are designed to:
#
# - store vectors
# - index vectors
# - perform similarity search efficiently
# - retrieve Top-K matches
# - store metadata
# - filter results


# ============================================================
# CONNECTION TO RAG
# ============================================================

# RAG = Retrieval-Augmented Generation
#
#
# RETRIEVAL:
#
# User Question
#      ↓
# Query Embedding
#      ↓
# Semantic Search
#      ↓
# Top-K Relevant Chunks
#
#
# AUGMENTATION:
#
# Question
# +
# Relevant Chunks
#
#
# GENERATION:
#
#      ↓
# GPT
#      ↓
# Grounded Answer


# ============================================================
# CORE CONCEPT TO REMEMBER
# ============================================================

# Embeddings
#     ↓
# Semantic Similarity
#     ↓
# Ranking
#     ↓
# Top-K Retrieval
#     ↓
# Vector Database
#     ↓
# RAG
