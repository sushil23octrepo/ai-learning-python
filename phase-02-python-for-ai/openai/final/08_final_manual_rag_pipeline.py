import numpy as np

from openai import OpenAI

# ============================================================
# MODULE 08 — MANUAL RAG PIPELINE
#
# Goal:
# Build a complete Retrieval-Augmented Generation (RAG)
# pipeline manually using:
#
# - embeddings
# - cosine similarity
# - semantic retrieval
# - Top-K results
# - GPT generation using retrieved context
#
#
# RAG = Retrieval + Augmented Context + Generation
#
#
# HIGH-LEVEL FLOW:
#
# User Question
#      ↓
# Create query embedding
#      ↓
# Compare with document embeddings
#      ↓
# Retrieve most relevant documents
#      ↓
# Build context
#      ↓
# Send context + question to GPT
#      ↓
# Generate grounded answer
# ============================================================


# ------------------------------------------------------------
# 1. CREATE OPENAI CLIENT
# ------------------------------------------------------------

client = OpenAI()


# ------------------------------------------------------------
# 2. COSINE SIMILARITY FUNCTION
# ------------------------------------------------------------

# Cosine similarity compares two embedding vectors.
#
# Higher value:
# -> more semantically similar
#
# Lower value:
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

# In this learning example, each string acts like one
# complete document/chunk.
#
# In a real RAG system, these would normally be chunks
# extracted from larger PDFs, policies, knowledge-base
# articles, database records, etc.

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

    # For learning purposes, we generate the document
    # embeddings here.
    #
    # In production, document embeddings are normally created
    # during ingestion and stored so that they are not
    # regenerated for every user query.

    document_response = client.embeddings.create(
        model="text-embedding-3-small",
        input=documents,
    )

    # --------------------------------------------------------
    # 6. CREATE QUERY EMBEDDING
    # --------------------------------------------------------

    # The query uses the SAME embedding model as the documents
    # so that both are represented in the same vector space.

    query_response = client.embeddings.create(
        model="text-embedding-3-small",
        input=query,
    )

    query_embedding = query_response.data[0].embedding

    # --------------------------------------------------------
    # 7. CALCULATE SIMILARITY FOR EACH DOCUMENT
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
    # 8. SORT BY RELEVANCE
    # --------------------------------------------------------

    # Highest similarity should appear first.

    results.sort(
        key=lambda item: item["similarity"],
        reverse=True,
    )

    # --------------------------------------------------------
    # 9. TOP-K RETRIEVAL
    # --------------------------------------------------------

    # Instead of returning only one document, we retrieve the
    # top few relevant results.
    #
    # This is called Top-K retrieval.
    #
    # Here:
    #
    # K = 2

    top_k = 2

    top_results = results[:top_k]

    # --------------------------------------------------------
    # 10. PRINT RETRIEVED DOCUMENTS
    # --------------------------------------------------------

    print("USER QUESTION:")
    print(query.strip())

    print()
    print(f"TOP {top_k} RETRIEVED DOCUMENTS:")

    for index, result in enumerate(
        top_results,
        start=1,
    ):

        print(
            f"{index}. "
            f"{result['document']} "
            f"(Similarity: {result['similarity']:.4f})"
        )

    # --------------------------------------------------------
    # 11. BUILD THE RAG CONTEXT
    # --------------------------------------------------------

    # GPT needs the retrieved information as text.
    #
    # We combine the Top-K documents into one context string.

    context = "\n\n".join(result["document"] for result in top_results)

    # --------------------------------------------------------
    # 12. DEFINE MODEL BEHAVIOR
    # --------------------------------------------------------

    # The model should use only the retrieved context.
    #
    # This is important because our goal is a grounded answer,
    # rather than an answer based on unsupported assumptions.

    instructions = """
You are a company policy assistant.

Answer the user's question using only the provided context.

If the context does not contain enough information to answer
the question, say that the information is not available in
the provided context.

Keep the answer concise.
"""

    # --------------------------------------------------------
    # 13. BUILD GPT INPUT
    # --------------------------------------------------------

    user_input = f"""
Context:
{context}

Question:
{query}
"""

    # --------------------------------------------------------
    # 14. GENERATE THE FINAL ANSWER
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
    print("FINAL RAG ANSWER:")

    print(response.output_text)


except Exception as ex:

    print(f"RAG request failed: {ex}")


# ============================================================
# IMPORTANT REVISION NOTES
# ============================================================


# ------------------------------------------------------------
# WHAT IS RAG?
# ------------------------------------------------------------

# RAG stands for:
#
# Retrieval-Augmented Generation
#
#
# It combines:
#
# RETRIEVAL
# -> find relevant external information
#
# with
#
# GENERATION
# -> use an LLM to generate an answer from that information


# ============================================================
# COMPLETE RAG FLOW
# ============================================================

# User Question
#      ↓
# Query Embedding
#      ↓
# Semantic Search
#      ↓
# Top-K Relevant Documents
#      ↓
# Build Context
#      ↓
# Context + Question
#      ↓
# GPT
#      ↓
# Grounded Answer


# ============================================================
# RETRIEVAL PART
# ============================================================

# Retrieval answers:
#
# "Which information is most relevant to the user's question?"
#
#
# In our implementation:
#
# embeddings
# +
# cosine similarity
# +
# sorting
# +
# Top-K
#
# perform the retrieval.


# ============================================================
# GENERATION PART
# ============================================================

# Generation answers:
#
# "How should this retrieved information be turned into a
# useful natural-language answer?"
#
#
# GPT receives:
#
# retrieved context
# +
# user question


# ============================================================
# IMPORTANT DISTINCTION
# ============================================================

# Embedding model:
#
# FIND relevant information.
#
#
# GPT:
#
# USE relevant information to produce an answer.
#
#
# Embeddings do not generate the final RAG answer.


# ============================================================
# WHY PROVIDE CONTEXT TO GPT?
# ============================================================

# GPT does not automatically know private company information.
#
# Example:
#
# Company policy:
#
# "Password reset links expire after 30 minutes."
#
#
# GPT only knows this policy for the request if our application
# supplies that information as context.


# ============================================================
# WHY USE "ONLY THE PROVIDED CONTEXT"?
# ============================================================

# We want the answer grounded in retrieved information.
#
# Without grounding instructions, a model may answer from its
# general knowledge even when company-specific information is
# missing.
#
#
# A useful instruction is:
#
# "If the provided context does not contain the answer,
# say that the information is unavailable."


# ============================================================
# TOP-K RETRIEVAL
# ============================================================

# Top-K means:
#
# retrieve the K most relevant documents/chunks.
#
#
# Example:
#
# top_k = 2
#
# -> retrieve the two highest-ranked results
#
#
# Why use more than one?
#
# Because a question may require information from multiple
# pieces of documentation.


# ============================================================
# IMPORTANT PRODUCTION CONCEPT:
# INGESTION VS QUERY TIME
# ============================================================


# ------------------------------------------------------------
# INGESTION TIME
# ------------------------------------------------------------

# Documents
#      ↓
# Extract text
#      ↓
# Split into chunks
#      ↓
# Create embeddings
#      ↓
# Store text + vectors
#
#
# This is generally done once when documents are added or
# updated.


# ------------------------------------------------------------
# QUERY TIME
# ------------------------------------------------------------

# User Question
#      ↓
# Create query embedding
#      ↓
# Search stored vectors
#      ↓
# Retrieve Top-K chunks
#      ↓
# Send to GPT
#
#
# We should NOT regenerate every document embedding for every
# user request in a production application.


# ============================================================
# WHY OUR CURRENT IMPLEMENTATION IS "MANUAL"
# ============================================================

# We manually:
#
# 1. create document embeddings
# 2. loop through every embedding
# 3. calculate cosine similarity
# 4. sort results
#
#
# This is fine for learning and small datasets.
#
#
# With thousands or millions of document chunks, we normally
# use a vector database / vector index.


# ============================================================
# VECTOR DATABASE WILL REPLACE THIS PART
# ============================================================

# Current manual code:
#
# for every document:
#     calculate cosine similarity
#
#
# Later:
#
# vector_database.search(
#     query_embedding,
#     top_k=5
# )
#
#
# The conceptual retrieval process remains the same.


# ============================================================
# RAG VS MODEL TRAINING
# ============================================================

# RAG does NOT permanently teach the model our documents.
#
# The relevant document context is supplied at runtime.
#
#
# RAG:
#
# external knowledge
# +
# runtime retrieval
#
#
# Fine-tuning:
#
# changes model behavior through training
#
#
# These solve different problems.


# ============================================================
# WHAT HAPPENS IF RETRIEVAL IS BAD?
# ============================================================

# RAG quality depends heavily on retrieval quality.
#
#
# Poor retrieval:
#
# wrong context
#      ↓
# model receives irrelevant information
#      ↓
# poor answer
#
#
# Important retrieval concepts we will study later:
#
# - chunking
# - metadata
# - Top-K tuning
# - similarity thresholds
# - reranking
# - retrieval evaluation


# ============================================================
# ENTERPRISE RAG ARCHITECTURE
# ============================================================

#                   INGESTION
#
# PDFs / Documents / Database
#          ↓
# Extract Text
#          ↓
# Chunk Documents
#          ↓
# Embedding Model
#          ↓
# Vector Database
#
#
#                     QUERY
#
# Angular
#    ↓
# User Question
#    ↓
# DRF
#    ↓
# Query Embedding
#    ↓
# Vector Database Search
#    ↓
# Top-K Relevant Chunks
#    ↓
# GPT
#    ↓
# Answer + Sources
#    ↓
# DRF
#    ↓
# Angular


# ============================================================
# CORE PATTERN TO REMEMBER
# ============================================================

# Question
#     ↓
# Embed
#     ↓
# Retrieve
#     ↓
# Build Context
#     ↓
# Generate
#     ↓
# Answer
#
#
# In short:
#
# RAG =
# Retrieval + Context + Generation
