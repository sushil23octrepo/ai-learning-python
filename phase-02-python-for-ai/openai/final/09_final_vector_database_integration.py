import chromadb

from openai import OpenAI

# ============================================================
# MODULE 09 — VECTOR DATABASE INTEGRATION
#
# Goal:
# Replace manual cosine-similarity search with a real
# vector database.
#
# In this module:
#
# - OpenAI creates embeddings
# - Chroma stores embeddings
# - Chroma performs vector similarity search
# - GPT uses retrieved context to generate the final answer
#
#
# HIGH-LEVEL ARCHITECTURE:
#
# Documents
#     ↓
# OpenAI Embeddings
#     ↓
# Chroma Vector Database
#
#
# User Question
#     ↓
# Query Embedding
#     ↓
# Chroma Similarity Search
#     ↓
# Top-K Documents
#     ↓
# Build Context
#     ↓
# GPT
#     ↓
# Final Answer
# ============================================================


# ------------------------------------------------------------
# 1. CREATE CLIENTS
# ------------------------------------------------------------

# OpenAI client:
# Used for embeddings and final GPT generation.

client = OpenAI()


# Chroma client:
# Used for storing and searching vector embeddings.
#
# chromadb.Client() is suitable for local/in-memory learning.
# We will study persistent storage later.

chroma_client = chromadb.Client()


# ------------------------------------------------------------
# 2. DOCUMENT COLLECTION
# ------------------------------------------------------------

# Each document contains:
#
# id
# -> unique identifier
#
# text
# -> actual searchable content
#
# source
# -> metadata describing where the content came from

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

    # OpenAI converts each document into a vector.
    #
    # All documents are embedded in one request.

    embedding_response = client.embeddings.create(
        model="text-embedding-3-small",
        input=texts,
    )

    # Extract vectors from the response.

    embeddings = [item.embedding for item in embedding_response.data]

    # --------------------------------------------------------
    # 5. CREATE CHROMA COLLECTION
    # --------------------------------------------------------

    # A collection is a logical container for:
    #
    # - document IDs
    # - document text
    # - embeddings
    # - metadata

    collection = chroma_client.create_collection(name="company_policies")

    # --------------------------------------------------------
    # 6. STORE DOCUMENTS IN VECTOR DATABASE
    # --------------------------------------------------------

    collection.add(
        ids=[document["id"] for document in documents],
        documents=texts,
        metadatas=[{"source": document["source"]} for document in documents],
        embeddings=embeddings,
    )

    # --------------------------------------------------------
    # 7. USER QUESTION
    # --------------------------------------------------------

    query = """
What is the minimum password length?
"""

    # --------------------------------------------------------
    # 8. CREATE QUERY EMBEDDING
    # --------------------------------------------------------

    # The query must use the SAME embedding model as the
    # documents so that the vectors can be meaningfully
    # compared.

    query_response = client.embeddings.create(
        model="text-embedding-3-small",
        input=query,
    )

    query_embedding = query_response.data[0].embedding

    # --------------------------------------------------------
    # 9. SEARCH VECTOR DATABASE
    # --------------------------------------------------------

    # n_results=2 means:
    #
    # retrieve the Top 2 most relevant vector matches.

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=2,
    )

    # --------------------------------------------------------
    # 10. UNDERSTAND RESULT STRUCTURE
    # --------------------------------------------------------

    # Chroma returns nested result collections because it can
    # accept multiple query embeddings.
    #
    # Since we supplied only one query:
    #
    # results["documents"][0]
    #
    # contains the documents for our first query.

    retrieved_documents = results["documents"][0]

    retrieved_metadatas = results["metadatas"][0]

    # --------------------------------------------------------
    # 11. PRINT RETRIEVED DOCUMENTS + SOURCES
    # --------------------------------------------------------

    print("USER QUESTION:")
    print(query.strip())

    print()

    print("RETRIEVED DOCUMENTS:")

    for index, (
        document,
        metadata,
    ) in enumerate(
        zip(
            retrieved_documents,
            retrieved_metadatas,
        ),
        start=1,
    ):

        print()
        print(f"{index}. {document}")

        print(
            "Source:",
            metadata["source"],
        )

    # --------------------------------------------------------
    # 12. BUILD RAG CONTEXT
    # --------------------------------------------------------

    # retrieved_documents is a Python list.
    #
    # Instead of placing the raw list representation into the
    # GPT prompt, combine the documents into a clean string.

    context = "\n\n".join(retrieved_documents)

    # --------------------------------------------------------
    # 13. DEFINE GPT BEHAVIOR
    # --------------------------------------------------------

    instructions = """
You are a company policy assistant.

Answer the user's question using only the provided context.

If the provided context does not contain enough information
to answer the question, say that the information is not
available in the provided context.

Keep the answer concise.
"""

    # --------------------------------------------------------
    # 14. BUILD FINAL RAG INPUT
    # --------------------------------------------------------

    user_input = f"""
Context:
{context}

Question:
{query}
"""

    # --------------------------------------------------------
    # 15. GENERATE FINAL ANSWER
    # --------------------------------------------------------

    response = client.responses.create(
        model="gpt-5.6",
        instructions=instructions,
        input=user_input,
    )

    # --------------------------------------------------------
    # 16. PRINT FINAL ANSWER
    # --------------------------------------------------------

    print()
    print("FINAL ANSWER:")

    print(response.output_text)


except Exception as ex:

    print(f"Vector search / RAG failed: {ex}")


# ============================================================
# IMPORTANT REVISION NOTES
# ============================================================


# ------------------------------------------------------------
# WHAT PROBLEM DOES A VECTOR DATABASE SOLVE?
# ------------------------------------------------------------

# In previous modules, we manually:
#
# 1. created document embeddings
# 2. looped through every document
# 3. calculated cosine similarity
# 4. sorted results
# 5. selected Top-K
#
#
# That works for small datasets.
#
# But with:
#
# 10,000
# 100,000
# 1,000,000+
#
# vectors, manual comparison becomes inefficient.
#
#
# A vector database is designed to:
#
# - store vectors
# - index vectors
# - perform similarity search
# - retrieve Top-K matches
# - store metadata
# - filter results


# ============================================================
# RESPONSIBILITY OF EACH COMPONENT
# ============================================================

# OpenAI Embedding Model:
#
# Text
#   ↓
# Vector
#
#
# Chroma:
#
# Store vectors
# +
# Search vectors
#
#
# GPT:
#
# Retrieved Context
# +
# User Question
#   ↓
# Natural-language answer


# ============================================================
# IMPORTANT:
# VECTOR DATABASE DOES NOT CREATE GPT ANSWERS
# ============================================================

# Chroma does NOT answer:
#
# "What is the minimum password length?"
#
#
# Chroma retrieves:
#
# "Passwords must contain at least 12 characters."
#
#
# GPT then turns that retrieved information into a useful
# answer.


# ============================================================
# MANUAL SEARCH VS VECTOR DATABASE
# ============================================================

# MODULE 08:
#
# for every document:
#     cosine_similarity(...)
#
# results.sort(...)
#
# results[:top_k]
#
#
# MODULE 09:
#
# collection.query(
#     query_embeddings=[query_embedding],
#     n_results=2,
# )
#
#
# The vector database performs retrieval for us.


# ============================================================
# DOCUMENT DATA MODEL
# ============================================================

# A useful vector-store record usually includes:
#
# ID
#
# Text
#
# Embedding
#
# Metadata


# Example:
#
# {
#     "id": "security-1",
#     "text": "...",
#     "source": "security_policy"
# }


# ============================================================
# WHY METADATA MATTERS
# ============================================================

# Retrieved text tells us:
#
# WHAT information was found.
#
#
# Metadata tells us:
#
# WHERE the information came from.
#
#
# Real metadata might include:
#
# source
# filename
# page
# section
# department
# tenant_id
# created_at
# document_type


# ============================================================
# METADATA WILL LATER HELP WITH:
# ============================================================

# citations
#
# source display
#
# filtering
#
# authorization
#
# tenant isolation
#
# document tracking


# ============================================================
# SAME EMBEDDING MODEL RULE
# ============================================================

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
# Both should use the same embedding model so they are
# represented in the same vector space.


# ============================================================
# INGESTION VS QUERY TIME
# ============================================================


# ------------------------------------------------------------
# INGESTION TIME
# ------------------------------------------------------------

# Documents
#     ↓
# Extract Text
#     ↓
# Chunk
#     ↓
# Generate Embeddings
#     ↓
# Store in Vector DB


# ------------------------------------------------------------
# QUERY TIME
# ------------------------------------------------------------

# User Question
#     ↓
# Generate Query Embedding
#     ↓
# Search Vector DB
#     ↓
# Retrieve Top-K
#     ↓
# GPT
#     ↓
# Answer


# ------------------------------------------------------------
# IMPORTANT PRODUCTION RULE
# ------------------------------------------------------------

# Do NOT regenerate document embeddings for every user query.
#
#
# Document embeddings should normally be created during
# ingestion and stored persistently.


# ============================================================
# IN-MEMORY CLIENT
# ============================================================

# We currently use:
#
# chromadb.Client()
#
#
# This is appropriate for learning.
#
# It should not be treated as our final enterprise storage
# architecture.
#
#
# Later we will study:
#
# persistent vector storage
# document ingestion
# updates
# duplicate handling
# metadata filtering


# ============================================================
# REAL ENTERPRISE VECTOR OPTIONS
# ============================================================

# Depending on application requirements, vector storage may
# eventually use technologies such as:
#
# PostgreSQL + pgvector
# Azure AI Search
# Pinecone
# Qdrant
# Weaviate
# Elasticsearch vector search
#
#
# The retrieval concepts remain fundamentally similar.


# ============================================================
# VECTOR DATABASE + RAG FLOW
# ============================================================

#                     INGESTION
#
# Documents
#     ↓
# Chunk
#     ↓
# OpenAI Embeddings
#     ↓
# Vector Database
#
#
#                       QUERY
#
# User Question
#     ↓
# Query Embedding
#     ↓
# Vector Database
#     ↓
# Top-K Documents
#     ↓
# Build Context
#     ↓
# GPT
#     ↓
# Grounded Answer


# ============================================================
# EVOLUTION OF OUR LEARNING
# ============================================================

# MODULE 06
#
# Text
#   ↓
# Embeddings


# MODULE 07
#
# Embeddings
#   ↓
# Manual Semantic Search


# MODULE 08
#
# Manual Semantic Search
#   ↓
# Manual RAG


# MODULE 09
#
# Vector Database
#   ↓
# Vector Search
#   ↓
# RAG


# ============================================================
# CORE PATTERN TO REMEMBER
# ============================================================

# Documents
#     ↓
# Embed
#     ↓
# Store
#
#
# Question
#     ↓
# Embed
#     ↓
# Search
#     ↓
# Retrieve
#     ↓
# Generate
#
#
# In short:
#
# EMBED
# → STORE
# → SEARCH
# → RETRIEVE
# → GENERATE
