import numpy as np

from openai import OpenAI

# ============================================================
# OPENAI API EXERCISE 06
# EMBEDDINGS FUNDAMENTALS
# Reference solution.
# ============================================================


# ------------------------------------------------------------
# 1. CREATE CLIENT
# ------------------------------------------------------------

client = OpenAI()


# ------------------------------------------------------------
# 2. COSINE SIMILARITY FUNCTION
# ------------------------------------------------------------


def cosine_similarity(vector_a, vector_b):

    vector_a = np.array(vector_a)

    vector_b = np.array(vector_b)

    return np.dot(
        vector_a,
        vector_b,
    ) / (np.linalg.norm(vector_a) * np.linalg.norm(vector_b))


# ------------------------------------------------------------
# 3. TEXTS TO COMPARE
# ------------------------------------------------------------

texts = [
    "Employees receive 20 paid leave days each year.",
    "Workers are entitled to 20 days of annual vacation.",
    "The database backup runs every night.",
]


# ------------------------------------------------------------
# 4. CREATE EMBEDDINGS
# ------------------------------------------------------------

try:

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=texts,
    )

    # --------------------------------------------------------
    # 5. EXTRACT VECTORS
    # --------------------------------------------------------

    embedding_1 = response.data[0].embedding

    embedding_2 = response.data[1].embedding

    embedding_3 = response.data[2].embedding

    # --------------------------------------------------------
    # 6. CALCULATE SIMILARITIES
    # --------------------------------------------------------

    leave_similarity = cosine_similarity(
        embedding_1,
        embedding_2,
    )

    backup_similarity = cosine_similarity(
        embedding_1,
        embedding_3,
    )

    # --------------------------------------------------------
    # 7. PRINT RESULTS
    # --------------------------------------------------------

    print(
        "Sentence 1 vs Sentence 2:",
        leave_similarity,
    )

    print(
        "Sentence 1 vs Sentence 3:",
        backup_similarity,
    )

    # --------------------------------------------------------
    # 8. DETERMINE MOST SIMILAR PAIR
    # --------------------------------------------------------

    print()

    if leave_similarity > backup_similarity:

        print("Sentence 1 and Sentence 2 are more " "semantically similar.")

    else:

        print("Sentence 1 and Sentence 3 are more " "semantically similar.")

    # --------------------------------------------------------
    # 9. PRINT VECTOR LENGTH
    # --------------------------------------------------------

    print()

    print(
        "Embedding vector length:",
        len(embedding_1),
    )


except Exception as ex:

    print(f"Embedding request failed: {ex}")
