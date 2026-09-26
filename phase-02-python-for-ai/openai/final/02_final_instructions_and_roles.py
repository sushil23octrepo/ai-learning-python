from openai import OpenAI

# ============================================================
# MODULE 02 — INSTRUCTIONS, ROLES, AND PROMPT STRUCTURE
# Complete reference implementation for later revision.
# ============================================================


# ------------------------------------------------------------
# 1. CREATE OPENAI CLIENT
# ------------------------------------------------------------

# OpenAI() automatically reads the OPENAI_API_KEY
# environment variable.
client = OpenAI()


# ------------------------------------------------------------
# 2. SIMPLE INPUT-ONLY REQUEST
# ------------------------------------------------------------

response = client.responses.create(
    model="gpt-5.6",
    input="Explain dependency injection in simple language.",
)

print(response.output_text)


# ------------------------------------------------------------
# 3. SEPARATE APPLICATION INSTRUCTIONS FROM USER INPUT
# ------------------------------------------------------------

instructions = """
You are a senior software engineering tutor.
Explain concepts in simple language.
Use a maximum of 4 sentences.
"""

user_input = """
Explain dependency injection.
"""

response = client.responses.create(
    model="gpt-5.6",
    instructions=instructions,
    input=user_input,
)

print(response.output_text)


# ------------------------------------------------------------
# 4. WHY USE instructions?
# ------------------------------------------------------------

# instructions:
# -> application-controlled behavior
# -> tone
# -> response style
# -> restrictions
# -> business rules
#
# input:
# -> dynamic request from the user

instructions = """
You are an application-security tutor.
Explain security topics for experienced developers.
Keep the response concise.
Use at most 5 bullet points.
"""

user_input = "Explain CSRF."

response = client.responses.create(
    model="gpt-5.6",
    instructions=instructions,
    input=user_input,
)

print(response.output_text)


# ------------------------------------------------------------
# 5. STRUCTURED MESSAGE ROLES
# ------------------------------------------------------------

response = client.responses.create(
    model="gpt-5.6",
    input=[
        {
            "role": "developer",
            "content": """
You are a concise Python tutor.
Explain concepts for experienced developers.
""",
        },
        {
            "role": "user",
            "content": "Explain Python decorators.",
        },
    ],
)

print(response.output_text)


# ------------------------------------------------------------
# 6. ROLE MEANINGS
# ------------------------------------------------------------

# developer
# -> rules controlled by the application
#
# user
# -> end-user request
#
# assistant
# -> model-generated response
#
# In early lessons, using:
#
#     instructions + input
#
# is often simpler.
#
# Structured roles become especially useful later for:
#
# conversation history
# multi-turn conversations
# tool calling
# agent workflows


# ------------------------------------------------------------
# 7. REAL-WORLD CODE REVIEW EXAMPLE
# ------------------------------------------------------------

developer_instructions = """
You are a senior Python code reviewer.

When reviewing code:
- Explain what the code does.
- Identify correctness issues.
- Mention security concerns if relevant.
- Mention readability improvements.
- Keep the response concise.
"""

code = """
def divide(a, b):
    return a / b
"""

user_input = f"""
Review this Python code:

{code}
"""

response = client.responses.create(
    model="gpt-5.6",
    instructions=developer_instructions,
    input=user_input,
)

print(response.output_text)


# ------------------------------------------------------------
# 8. DYNAMIC USER INPUT EXAMPLE
# ------------------------------------------------------------

instructions = """
You are a backend-development tutor.
Explain concepts clearly for experienced developers.
Use a maximum of 4 sentences.
"""

topic = "JWT authentication"

response = client.responses.create(
    model="gpt-5.6",
    instructions=instructions,
    input=f"Explain {topic}.",
)

print(response.output_text)


# ------------------------------------------------------------
# 9. ERROR HANDLING
# ------------------------------------------------------------

instructions = """
You are a concise Python tutor.
Use simple language.
"""

user_input = "Explain list comprehensions."

try:
    response = client.responses.create(
        model="gpt-5.6",
        instructions=instructions,
        input=user_input,
    )

    print(response.output_text)

except Exception as ex:
    print(f"OpenAI request failed: {ex}")


# ============================================================
# IMPORTANT REVISION
# ============================================================

# Basic request:
#
# response = client.responses.create(
#     model="gpt-5.6",
#     input="Your prompt",
# )


# Application behavior:
#
# response = client.responses.create(
#     model="gpt-5.6",
#     instructions="Application rules",
#     input="User request",
# )


# Structured roles:
#
# input=[
#     {
#         "role": "developer",
#         "content": "Application-controlled rules"
#     },
#     {
#         "role": "user",
#         "content": "User request"
#     }
# ]


# ============================================================
# CORE IDEA
# ============================================================

# instructions
# -> application behavior
#
# input
# -> actual user request
#
# developer role
# -> trusted application instructions
#
# user role
# -> dynamic end-user input
#
# assistant role
# -> model response


# ============================================================
# ENTERPRISE ARCHITECTURE IDEA
# ============================================================

# Angular
#    ↓
# user question
#    ↓
# DRF backend
#    ↓
# fixed application instructions
# +
# dynamic user input
#    ↓
# OpenAI API
#    ↓
# response
#    ↓
# Angular
#
# Keep application rules on the backend.
# Do not let frontend/user input replace trusted instructions.
