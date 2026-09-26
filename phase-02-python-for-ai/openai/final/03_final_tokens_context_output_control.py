from openai import OpenAI

# ============================================================
# MODULE 03 — TOKENS, CONTEXT, AND OUTPUT CONTROL
# Complete reference implementation for later revision.
#
# NOTE:
# For gpt-5.6, do not use temperature in these examples.
# The model rejected that parameter during testing.
# ============================================================


# ------------------------------------------------------------
# 1. CREATE CLIENT
# ------------------------------------------------------------

client = OpenAI()


# ------------------------------------------------------------
# 2. BASIC REQUEST
# ------------------------------------------------------------

response = client.responses.create(
    model="gpt-5.6",
    input="Explain dependency injection in simple language.",
)

print(response.output_text)


# ------------------------------------------------------------
# 3. SEMANTIC OUTPUT CONTROL
# ------------------------------------------------------------

# This controls the style and expected length through prompting.
response = client.responses.create(
    model="gpt-5.6",
    input="""
Explain dependency injection.
Use a maximum of 2 sentences.
""",
)

print(response.output_text)


# ------------------------------------------------------------
# 4. TECHNICAL OUTPUT LIMIT
# ------------------------------------------------------------

# max_output_tokens sets an upper limit on model output.
response = client.responses.create(
    model="gpt-5.6",
    input="""
Explain dependency injection simply.
Use a maximum of 3 sentences.
""",
    max_output_tokens=200,
)

print(response.output_text)


# ------------------------------------------------------------
# 5. OUTPUT CONTROL — TWO DIFFERENT IDEAS
# ------------------------------------------------------------

# Prompt instruction:
#
# "Use maximum 3 sentences."
#
# -> semantic / behavior control
#
#
# max_output_tokens=200
#
# -> technical upper limit
#
#
# These are related but not the same thing.


# ------------------------------------------------------------
# 6. INSPECT TOKEN USAGE
# ------------------------------------------------------------

response = client.responses.create(
    model="gpt-5.6",
    input="Explain authentication in two sentences.",
)

print(response.output_text)

print()

print("Input tokens:", response.usage.input_tokens)
print("Output tokens:", response.usage.output_tokens)
print("Total tokens:", response.usage.total_tokens)


# ------------------------------------------------------------
# 7. SHORT PROMPT VS LONGER PROMPT
# ------------------------------------------------------------

short_prompt = """
Explain dependency injection in one sentence.
"""

response = client.responses.create(
    model="gpt-5.6",
    input=short_prompt,
)

print("\nSHORT RESPONSE:")
print(response.output_text)

print("Input tokens:", response.usage.input_tokens)
print("Output tokens:", response.usage.output_tokens)
print("Total tokens:", response.usage.total_tokens)


long_prompt = """
Explain dependency injection in detail.

Include:
- definition
- simple example
- benefits
- disadvantages
- when to use it
"""

response = client.responses.create(
    model="gpt-5.6",
    input=long_prompt,
    max_output_tokens=500,
)

print("\nLONGER RESPONSE:")
print(response.output_text)

print("Input tokens:", response.usage.input_tokens)
print("Output tokens:", response.usage.output_tokens)
print("Total tokens:", response.usage.total_tokens)


# ------------------------------------------------------------
# 8. USING instructions + input
# ------------------------------------------------------------

instructions = """
You are a senior backend engineering tutor.
Give precise and concise technical answers.
Use a maximum of 3 sentences.
"""

response = client.responses.create(
    model="gpt-5.6",
    instructions=instructions,
    input="Explain dependency injection.",
    max_output_tokens=200,
)

print("\nTECHNICAL RESPONSE:")
print(response.output_text)

print()
print("Input tokens:", response.usage.input_tokens)
print("Output tokens:", response.usage.output_tokens)
print("Total tokens:", response.usage.total_tokens)


# ------------------------------------------------------------
# 9. ERROR HANDLING
# ------------------------------------------------------------

try:
    response = client.responses.create(
        model="gpt-5.6",
        instructions="""
You are a concise software engineering tutor.
Use a maximum of 3 sentences.
""",
        input="Explain inversion of control.",
        max_output_tokens=200,
    )

    print(response.output_text)

    print()
    print("Input tokens:", response.usage.input_tokens)
    print("Output tokens:", response.usage.output_tokens)
    print("Total tokens:", response.usage.total_tokens)

except Exception as ex:
    print(f"OpenAI request failed: {ex}")


# ============================================================
# IMPORTANT REVISION
# ============================================================

# Token:
# -> a small unit of text processed by the model


# Input tokens:
# -> tokens sent to the model
#
# Examples:
# instructions
# user input
# conversation history
# retrieved documents


# Output tokens:
# -> tokens generated by the model


# Total tokens:
# -> input tokens + output-related token usage


# Usage:
#
# response.usage.input_tokens
# response.usage.output_tokens
# response.usage.total_tokens


# Output length control:
#
# Prompt:
# "Use maximum 3 sentences."
#
# Technical limit:
# max_output_tokens=200


# ------------------------------------------------------------
# IMPORTANT:
# ------------------------------------------------------------

# Do NOT use:
#
# temperature=...
#
# in our gpt-5.6 examples.
#
# During actual API testing, gpt-5.6 returned:
#
# Unsupported parameter: 'temperature'
#
# We will study model reasoning controls separately later.


# ============================================================
# CONTEXT WINDOW IDEA
# ============================================================

# The context available to the model can include:
#
# instructions
# user request
# previous messages
# documents
# tool results
#
# More context generally means:
#
# more input tokens
# potentially higher cost
# potentially higher latency
#
# Good architecture sends only relevant context.


# ============================================================
# RAG CONNECTION
# ============================================================

# BAD:
#
# Send every company document to the model.
#
#
# BETTER:
#
# User Question
#       ↓
# Search / Retrieval
#       ↓
# Find relevant document chunks
#       ↓
# Send only relevant context
#       ↓
# OpenAI
#
#
# Benefits:
#
# fewer tokens
# lower cost
# lower latency
# less irrelevant information
