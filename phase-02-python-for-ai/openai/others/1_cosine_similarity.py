"""
============================================================
TOPIC: COSINE SIMILARITY WITH NUMPY
============================================================

Purpose:
- Understand what cosine similarity is.
- Understand the mathematics behind it.
- Understand how NumPy implements the calculation.
- Understand why cosine similarity is heavily used in AI embeddings.
- Understand edge cases and practical considerations.

------------------------------------------------------------
1. WHAT IS COSINE SIMILARITY?
------------------------------------------------------------

Cosine similarity measures how similar two vectors are based on
their DIRECTION rather than their absolute magnitude/length.

Formula:

    cosine_similarity(A, B)

        A dot B
    = -----------
      ||A|| ||B||

Where:

    A dot B
        = dot product between vectors A and B

    ||A||
        = magnitude / Euclidean norm of vector A

    ||B||
        = magnitude / Euclidean norm of vector B


General Interpretation:

     1.0  -> vectors point in the same direction
     0.0  -> vectors are perpendicular
    -1.0  -> vectors point in opposite directions


Important:

Cosine similarity is mainly interested in DIRECTION.

It does not directly compare how large the vectors are.


============================================================
2. WHY VECTORS?
============================================================

A vector is simply an ordered collection of numbers.

Example:

    vector_a = [1, 2, 3]

It can be imagined as a point/direction in a multidimensional space.

In AI, an embedding is also a vector.

For example, conceptually:

    "dog"
        ->
    [0.12, -0.34, 0.78, ..., 0.11]

Real embedding vectors may contain hundreds or thousands
of numeric dimensions.

Those numbers encode characteristics learned by the model.


============================================================
3. BASIC PYTHON IMPLEMENTATION
============================================================
"""

import numpy as np


def cosine_similarity(vector_a, vector_b):
    vector_a = np.array(vector_a, dtype=float)
    vector_b = np.array(vector_b, dtype=float)

    dot_product = np.dot(vector_a, vector_b)

    magnitude_a = np.linalg.norm(vector_a)
    magnitude_b = np.linalg.norm(vector_b)

    similarity = dot_product / (magnitude_a * magnitude_b)

    return similarity


"""
============================================================
4. STEP 1 - CONVERT TO NUMPY ARRAYS
============================================================

Input:

    vector_a = [1, 2, 3]
    vector_b = [2, 4, 6]

These are normal Python lists.

We convert them:

    vector_a = np.array(vector_a)
    vector_b = np.array(vector_b)

Result:

    array([1., 2., 3.])
    array([2., 4., 6.])

Why use NumPy?

Because NumPy provides mathematical vector operations such as:

    np.dot()
    np.linalg.norm()

Using dtype=float is useful because vector mathematics commonly
works with decimal values.


============================================================
5. STEP 2 - DOT PRODUCT
============================================================

Suppose:

    A = [1, 2, 3]
    B = [2, 4, 6]

The dot product is:

    A dot B

    = (1 * 2)
      + (2 * 4)
      + (3 * 6)

    = 2 + 8 + 18

    = 28

NumPy:

    np.dot(A, B)

returns:

    28


General dot product:

    A = [a1, a2, a3]
    B = [b1, b2, b3]

    A dot B
        =
    a1*b1 + a2*b2 + a3*b3


Important:

Dot product by itself is influenced by both:

    - direction
    - magnitude

That is why cosine similarity also divides by the magnitudes.


============================================================
6. STEP 3 - VECTOR MAGNITUDE
============================================================

Magnitude means the length of a vector.

For:

    A = [1, 2, 3]

Magnitude is:

    sqrt(
        1^2 +
        2^2 +
        3^2
    )

    = sqrt(
        1 + 4 + 9
    )

    = sqrt(14)

    approximately 3.7417


NumPy calculates this with:

    np.linalg.norm(A)


For:

    B = [2, 4, 6]

Magnitude:

    sqrt(
        2^2 +
        4^2 +
        6^2
    )

    = sqrt(
        4 + 16 + 36
    )

    = sqrt(56)

    approximately 7.4833


============================================================
7. FULL COSINE SIMILARITY CALCULATION
============================================================

A = [1, 2, 3]
B = [2, 4, 6]


Step 1:

    dot product = 28


Step 2:

    magnitude(A)
        approximately 3.7417

    magnitude(B)
        approximately 7.4833


Step 3:

    denominator

        3.7417 * 7.4833

        approximately 28


Step 4:

    cosine similarity

        28
        --
        28

        = 1


Result:

    1.0


Meaning:

A and B point in exactly the same direction.


Notice:

    B = A * 2

A and B have different magnitudes.

But their direction is identical.

Therefore:

    cosine similarity = 1


============================================================
8. SAME DIRECTION EXAMPLE
============================================================
"""

a = [1, 2, 3]
b = [2, 4, 6]

print("Same direction:")
print(cosine_similarity(a, b))


"""
Expected:

    1.0


Meaning:

The vectors are perfectly aligned.


============================================================
9. PERPENDICULAR VECTOR EXAMPLE
============================================================

Consider:

    A = [1, 0]
    B = [0, 1]

Dot product:

    1*0 + 0*1

    = 0

Magnitude of both vectors:

    1

Therefore:

    similarity = 0 / (1 * 1)

    = 0


Geometrically:

    A points horizontally.

    B points vertically.

The angle between them is:

    90 degrees

and:

    cos(90 degrees) = 0
"""

a = [1, 0]
b = [0, 1]

print("\nPerpendicular:")
print(cosine_similarity(a, b))


"""
============================================================
10. OPPOSITE DIRECTION EXAMPLE
============================================================

Consider:

    A = [1, 0]
    B = [-1, 0]

A points right.

B points left.

They point in completely opposite directions.

Dot product:

    1*(-1) + 0*0

    = -1

Magnitude:

    ||A|| = 1
    ||B|| = 1

Similarity:

    -1 / (1 * 1)

    = -1
"""

a = [1, 0]
b = [-1, 0]

print("\nOpposite direction:")
print(cosine_similarity(a, b))


"""
============================================================
11. IMPORTANT: MAGNITUDE VS DIRECTION
============================================================

Consider:

    A = [1, 2]

    B = [10, 20]


B is much larger.

But:

    B = A * 10


They point in exactly the same direction.

Therefore:

    cosine similarity = 1


This demonstrates one of the most important properties:

Cosine similarity ignores scale.

It cares about orientation/direction.


This is especially useful in AI because two embedding vectors
may have different magnitudes but still represent highly similar
semantic meaning.


============================================================
12. CONNECTION WITH ANGLE
============================================================

The dot product formula from linear algebra is:

    A dot B
        =
    ||A|| * ||B|| * cos(theta)

Where:

    theta = angle between A and B


Rearrange it:

                         A dot B
    cos(theta) = ------------------------
                   ||A|| * ||B||


That rearranged equation is exactly cosine similarity.

Therefore:

    cosine similarity

is literally:

    cosine of the angle between two vectors.


Examples:

    theta = 0 degrees

        cos(0) = 1

        Same direction.


    theta = 90 degrees

        cos(90) = 0

        Perpendicular.


    theta = 180 degrees

        cos(180) = -1

        Opposite direction.


============================================================
13. WHY COSINE SIMILARITY IS USED IN AI
============================================================

Modern AI systems often convert data into embeddings.

For example:

    text
    image
    document
    product
    user query

may be represented as vectors.


Conceptually:

    embedding("dog")

might be:

    [0.10, 0.71, -0.12, ...]


and:

    embedding("puppy")

might be:

    [0.11, 0.68, -0.10, ...]


Because "dog" and "puppy" have related meanings,
their embedding vectors may point in similar directions.


We can calculate:

    cosine_similarity(
        dog_embedding,
        puppy_embedding
    )

and get a relatively high similarity.


But:

    cosine_similarity(
        dog_embedding,
        database_embedding
    )

may be much lower.


Important:

The actual similarity values depend on:

    - embedding model
    - dimensionality
    - training
    - dataset
    - normalization

There is no universal rule such as:

    similarity > 0.8 always means similar.


============================================================
14. SIMPLE AI-LIKE EXAMPLE
============================================================
"""

query_embedding = [0.8, 0.1, 0.3]

document_1 = [0.75, 0.12, 0.28]
document_2 = [-0.2, 0.8, 0.1]

similarity_1 = cosine_similarity(
    query_embedding,
    document_1,
)

similarity_2 = cosine_similarity(
    query_embedding,
    document_2,
)

print("\nAI-style example:")

print(
    "Query vs Document 1:",
    similarity_1,
)

print(
    "Query vs Document 2:",
    similarity_2,
)


"""
Document 1 should have a higher cosine similarity.

Conceptually:

    query
        ->
    "Python async programming"

Document 1
        ->
    "Understanding async and await in Python"

Document 2
        ->
    "How to prepare Italian pasta"

The first document should usually have an embedding direction
closer to the query.


============================================================
15. NORMALIZATION
============================================================

A normalized vector has magnitude 1.

To normalize:

    normalized_vector
        =
    vector / magnitude(vector)


Example:

    A = [3, 4]

Magnitude:

    sqrt(3^2 + 4^2)

    = 5


Normalized:

    [3/5, 4/5]

    = [0.6, 0.8]


Magnitude of:

    [0.6, 0.8]

is:

    1


NumPy:

    normalized_a = (
        vector_a
        / np.linalg.norm(vector_a)
    )


Important Relationship:

If A and B are already normalized:

    ||A|| = 1
    ||B|| = 1

Then cosine similarity becomes:

        A dot B
    ----------------
        1 * 1

which is simply:

    A dot B


Therefore:

For normalized embeddings:

    dot product
        ==
    cosine similarity

mathematically.


This can be useful for performance because dot product is simpler
to calculate repeatedly.


============================================================
16. NORMALIZATION EXAMPLE
============================================================
"""

vector = np.array(
    [3, 4],
    dtype=float,
)

normalized_vector = vector / np.linalg.norm(vector)

print("\nNormalized vector:")
print(normalized_vector)

print(
    "Normalized magnitude:",
    np.linalg.norm(normalized_vector),
)


"""
Expected approximately:

    [0.6 0.8]

Magnitude:

    1.0


============================================================
17. ZERO VECTOR PROBLEM
============================================================

Consider:

    A = [0, 0, 0]

Magnitude:

    ||A|| = 0


Cosine similarity requires:

                    A dot B
    similarity = ----------------
                  ||A|| * ||B||


If:

    ||A|| = 0

then the denominator becomes:

    0

Division by zero occurs.

Mathematically:

Cosine similarity for a zero vector is undefined.


Therefore production code should handle zero vectors.


============================================================
18. SAFER IMPLEMENTATION
============================================================
"""


def safe_cosine_similarity(vector_a, vector_b):
    vector_a = np.array(
        vector_a,
        dtype=float,
    )

    vector_b = np.array(
        vector_b,
        dtype=float,
    )

    magnitude_a = np.linalg.norm(vector_a)
    magnitude_b = np.linalg.norm(vector_b)

    if magnitude_a == 0 or magnitude_b == 0:
        raise ValueError("Cosine similarity is undefined for a zero vector.")

    dot_product = np.dot(
        vector_a,
        vector_b,
    )

    return dot_product / (magnitude_a * magnitude_b)


"""
============================================================
19. VECTOR DIMENSIONS MUST MATCH
============================================================

Valid:

    A = [1, 2, 3]
    B = [4, 5, 6]

Both contain:

    3 dimensions


Invalid:

    A = [1, 2]
    B = [4, 5, 6]

These vectors represent different dimensional spaces.

The dot product requires compatible shapes.


For embeddings this normally happens automatically because
one embedding model returns vectors of a fixed dimension.


For example conceptually:

    model X
        ->
    every embedding might have dimension 1536

Therefore:

    query embedding
    document embedding
    product embedding

generated by that same model have compatible dimensions.


============================================================
20. NUMPY OPERATIONS USED
============================================================

np.array()

Purpose:
    Convert Python sequence into a NumPy array.


np.dot(a, b)

Purpose:
    Calculate dot product.


np.linalg.norm(a)

Purpose:
    Calculate vector magnitude / Euclidean norm.


Example:

    vector = np.array([3, 4])

    np.linalg.norm(vector)

returns:

    5


because:

    sqrt(3^2 + 4^2)

    = sqrt(9 + 16)

    = sqrt(25)

    = 5


============================================================
21. MANUAL IMPLEMENTATION WITHOUT NUMPY
============================================================

Understanding the manual implementation is useful because it
shows exactly what NumPy is doing.
"""


def cosine_similarity_manual(vector_a, vector_b):
    dot_product = 0
    magnitude_a_squared = 0
    magnitude_b_squared = 0

    for a, b in zip(vector_a, vector_b):
        dot_product += a * b

        magnitude_a_squared += a * a
        magnitude_b_squared += b * b

    magnitude_a = magnitude_a_squared**0.5
    magnitude_b = magnitude_b_squared**0.5

    return dot_product / (magnitude_a * magnitude_b)


print("\nManual implementation:")

print(
    cosine_similarity_manual(
        [1, 2, 3],
        [2, 4, 6],
    )
)


"""
The loop:

    for a, b in zip(vector_a, vector_b):

pairs:

    1 with 2
    2 with 4
    3 with 6


Then calculates:

Dot product:

    1*2 + 2*4 + 3*6


Magnitude A squared:

    1^2 + 2^2 + 3^2


Magnitude B squared:

    2^2 + 4^2 + 6^2


This manual implementation is educational.

For real numerical work, NumPy is preferable.


============================================================
22. COSINE SIMILARITY VS EUCLIDEAN DISTANCE
============================================================

Cosine similarity asks:

    "Are these vectors pointing in similar directions?"


Euclidean distance asks:

    "How physically far apart are these vectors?"


Example:

    A = [1, 2]

    B = [10, 20]


Cosine similarity:

    1

because they point in the same direction.


But Euclidean distance between them is large.


Therefore they measure different things.


Cosine similarity:
    Direction-based.

Euclidean distance:
    Distance-based.


Both are useful depending on the application.


============================================================
23. COSINE SIMILARITY IN RAG
============================================================

In Retrieval-Augmented Generation (RAG), a common flow is:

    User Query
        |
        v
    Generate Query Embedding
        |
        v
    Compare Query Embedding
    with Document Embeddings
        |
        v
    Calculate Similarity Scores
        |
        v
    Select Most Similar Documents
        |
        v
    Send Retrieved Context to LLM


Conceptual example:

    query_embedding

compared with:

    document_1_embedding
    document_2_embedding
    document_3_embedding


Scores:

    document_1 -> 0.91
    document_2 -> 0.76
    document_3 -> 0.25


The retrieval system might rank:

    document_1
    document_2
    document_3


Important:

Production vector databases often perform these calculations
internally.

Examples of vector-search concepts include:

    cosine similarity
    dot product
    Euclidean distance


============================================================
24. PERFORMANCE IDEA
============================================================

Suppose:

    query embedding dimension = d

Comparing one query with one document requires processing
approximately d dimensions.

Therefore one cosine comparison is roughly:

    O(d)


If comparing against n document vectors:

    O(n * d)


For very large vector collections, checking every vector
one by one becomes expensive.

That is why vector databases/indexes use specialized
nearest-neighbor search algorithms.


============================================================
25. COMMON MISTAKES
============================================================

1. Forgetting the denominator

Wrong:

    np.dot(A, B)

This is dot product, not necessarily cosine similarity.


2. Zero vectors

    [0, 0, 0]

cause a zero magnitude.


3. Different dimensions

    [1, 2]

vs:

    [1, 2, 3]

cannot be compared as corresponding vectors.


4. Assuming one universal similarity threshold

There is no rule such as:

    > 0.8 = always similar

Thresholds should be evaluated for the specific:

    model
    dataset
    application


5. Confusing similarity with distance

Higher cosine similarity:

    generally means more similar direction.

Some vector systems expose cosine distance instead.

Distance and similarity may use different conventions.


============================================================
26. FINAL VERSION
============================================================
"""


def final_cosine_similarity(vector_a, vector_b):
    """
    Calculate cosine similarity between two vectors.

    Returns:
        float:
            1   -> same direction
            0   -> perpendicular
           -1   -> opposite direction

    Raises:
        ValueError:
            If either vector has zero magnitude.
    """

    vector_a = np.array(
        vector_a,
        dtype=float,
    )

    vector_b = np.array(
        vector_b,
        dtype=float,
    )

    magnitude_a = np.linalg.norm(vector_a)
    magnitude_b = np.linalg.norm(vector_b)

    if magnitude_a == 0 or magnitude_b == 0:
        raise ValueError("Cannot calculate cosine similarity " "for a zero vector.")

    dot_product = np.dot(
        vector_a,
        vector_b,
    )

    return dot_product / (magnitude_a * magnitude_b)


"""
============================================================
27. REVISION CHEAT SHEET
============================================================

Cosine Similarity:

                      A dot B
    similarity = -------------------
                    ||A|| * ||B||


Dot Product:

    [a, b, c] dot [x, y, z]

    = ax + by + cz


Magnitude:

    ||A||

    = sqrt(
        a^2 + b^2 + c^2
      )


NumPy:

    np.dot(A, B)
        -> dot product

    np.linalg.norm(A)
        -> magnitude


Meaning:

     1
        same direction

     0
        perpendicular

    -1
        opposite direction


Core Intuition:

    Magnitude:
        How long is the vector?

    Cosine Similarity:
        How similar is its direction?


AI:

    Text/Image/etc.
        ->
    Embedding Vector
        ->
    Compare vectors
        ->
    Similarity score


For normalized vectors:

    cosine similarity
        =
    dot product


Most Important Things to Remember:

1. Cosine similarity compares vector direction.

2. Dot product forms the numerator.

3. Product of magnitudes normalizes the dot product.

4. Similar embedding directions often indicate semantic similarity.

5. Zero vectors must be handled.

6. Similarity thresholds are application/model dependent.

7. Cosine similarity is commonly used in embedding search and RAG.
"""
