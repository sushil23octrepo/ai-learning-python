from openai import OpenAI

# ============================================================
# MODULE 10 — CONVERSATION STATE / MULTI-TURN CONVERSATIONS
#
# Goal:
# Understand how to continue a conversation across multiple
# OpenAI API calls.
#
# IMPORTANT:
#
# Independent API requests do NOT automatically share
# conversation history.
#
# To continue a conversation using the Responses API, we can
# use:
#
#     previous_response_id
#
#
# CORE FLOW:
#
# Request 1
#    ↓
# Response 1
#    ↓
# response_1.id
#    ↓
# Request 2 uses:
# previous_response_id=response_1.id
#    ↓
# Response 2
#    ↓
# response_2.id
#    ↓
# Request 3 continues from response_2.id
#
#
# This provides conversation continuity.
# ============================================================


# ------------------------------------------------------------
# 1. CREATE OPENAI CLIENT
# ------------------------------------------------------------

client = OpenAI()


# ============================================================
# PART 1 — INDEPENDENT REQUESTS
# ============================================================


# ------------------------------------------------------------
# 2. FIRST INDEPENDENT REQUEST
# ------------------------------------------------------------

# Suppose the user tells the model some information.

first_response = client.responses.create(
    model="gpt-5.6",
    input="""
My favorite programming language is Python.
""",
)

print("FIRST RESPONSE:")
print(first_response.output_text)


# ------------------------------------------------------------
# 3. SECOND INDEPENDENT REQUEST
# ------------------------------------------------------------

# This is a completely separate request.
#
# We are NOT supplying previous_response_id.
#
# Therefore, we should not design the application assuming
# that this request automatically knows what happened above.

second_response = client.responses.create(
    model="gpt-5.6",
    input="""
What is my favorite programming language?
""",
)

print()
print("SECOND INDEPENDENT RESPONSE:")
print(second_response.output_text)


# ============================================================
# PART 2 — CONTINUE CONVERSATION WITH previous_response_id
# ============================================================


# ------------------------------------------------------------
# 4. START A NEW CONVERSATION
# ------------------------------------------------------------

response_1 = client.responses.create(
    model="gpt-5.6",
    input="""
My favorite programming language is Python.
""",
)

print()
print("CONVERSATION TURN 1:")
print(response_1.output_text)

print(
    "Response ID:",
    response_1.id,
)


# ------------------------------------------------------------
# 5. CONTINUE FROM RESPONSE 1
# ------------------------------------------------------------

# previous_response_id connects this request to the previous
# response.
#
# The new request continues the same conversation.

response_2 = client.responses.create(
    model="gpt-5.6",
    previous_response_id=response_1.id,
    input="""
What is my favorite programming language?
""",
)

print()
print("CONVERSATION TURN 2:")
print(response_2.output_text)

print(
    "Response ID:",
    response_2.id,
)


# ============================================================
# PART 3 — MULTIPLE CONVERSATION TURNS
# ============================================================


# ------------------------------------------------------------
# 6. DEFINE REUSABLE APPLICATION INSTRUCTIONS
# ------------------------------------------------------------

# IMPORTANT:
#
# When using previous_response_id, do not assume that earlier
# instructions automatically continue to govern every future
# request.
#
# A clear and safe application pattern is to supply the
# application instructions again on each request.

instructions = """
You are a concise software architecture assistant.

Answer clearly for an experienced software developer.
Use a maximum of 3 sentences.
"""


# ------------------------------------------------------------
# 7. TURN 1
# ------------------------------------------------------------

project_response_1 = client.responses.create(
    model="gpt-5.6",
    instructions=instructions,
    input="""
I am building an employee management system.
""",
)

print()
print("PROJECT CONVERSATION — TURN 1:")
print(project_response_1.output_text)

print(
    "Response ID:",
    project_response_1.id,
)


# ------------------------------------------------------------
# 8. TURN 2
# ------------------------------------------------------------

# Continue from the most recent response.

project_response_2 = client.responses.create(
    model="gpt-5.6",
    instructions=instructions,
    previous_response_id=project_response_1.id,
    input="""
The backend uses Django REST Framework.
""",
)

print()
print("PROJECT CONVERSATION — TURN 2:")
print(project_response_2.output_text)

print(
    "Response ID:",
    project_response_2.id,
)


# ------------------------------------------------------------
# 9. TURN 3
# ------------------------------------------------------------

# Continue from response 2, because that is now the latest
# point in the conversation.

project_response_3 = client.responses.create(
    model="gpt-5.6",
    instructions=instructions,
    previous_response_id=project_response_2.id,
    input="""
What backend framework am I using?
""",
)

print()
print("PROJECT CONVERSATION — TURN 3:")
print(project_response_3.output_text)

print(
    "Response ID:",
    project_response_3.id,
)


# ============================================================
# PART 4 — REUSABLE CHAT FUNCTION
# ============================================================


# ------------------------------------------------------------
# 10. SIMPLE LEARNING EXAMPLE
# ------------------------------------------------------------

# The following demonstrates how an application could keep
# track of the latest OpenAI response ID.
#
# IMPORTANT:
#
# This global-variable approach is ONLY for learning.
#
# Do NOT use one global response ID for all users in a real
# web application.

latest_response_id = None


def send_message(message):
    global latest_response_id

    # --------------------------------------------------------
    # Build request arguments dynamically.
    # --------------------------------------------------------

    request_data = {
        "model": "gpt-5.6",
        "instructions": """
You are a concise software architecture assistant.
Use a maximum of 3 sentences.
""",
        "input": message,
    }

    # --------------------------------------------------------
    # If we already have a response ID, continue from it.
    # --------------------------------------------------------

    if latest_response_id is not None:

        request_data["previous_response_id"] = latest_response_id

    # --------------------------------------------------------
    # Send request.
    # --------------------------------------------------------

    response = client.responses.create(**request_data)

    # --------------------------------------------------------
    # Save latest response ID for the next turn.
    # --------------------------------------------------------

    latest_response_id = response.id

    # --------------------------------------------------------
    # Return final text.
    # --------------------------------------------------------

    return response.output_text


# ------------------------------------------------------------
# 11. USE THE CHAT FUNCTION
# ------------------------------------------------------------

print()
print("REUSABLE CHAT EXAMPLE:")


print(send_message("I am building an inventory application."))


print(send_message("The backend uses Django REST Framework."))


print(send_message("What backend framework am I using?"))


# ============================================================
# PART 5 — MANUAL MESSAGE-HISTORY APPROACH
# ============================================================


# ------------------------------------------------------------
# 12. ANOTHER WAY TO MAINTAIN CONTEXT
# ------------------------------------------------------------

# previous_response_id is not the only way to provide
# conversation context.
#
# Your application can explicitly send previous messages.
#
# This gives the application direct control over which
# messages are included.

messages = [
    {
        "role": "user",
        "content": """
My favorite programming language is Python.
""",
    },
    {
        "role": "assistant",
        "content": """
Understood.
""",
    },
    {
        "role": "user",
        "content": """
What is my favorite programming language?
""",
    },
]


history_response = client.responses.create(
    model="gpt-5.6",
    instructions="""
Answer the user's question concisely.
""",
    input=messages,
)


print()
print("MANUAL MESSAGE HISTORY:")

print(history_response.output_text)


# ============================================================
# IMPORTANT REVISION NOTES
# ============================================================


# ------------------------------------------------------------
# WHAT IS CONVERSATION STATE?
# ------------------------------------------------------------

# Conversation state is information from earlier turns that
# allows later requests to understand the ongoing discussion.
#
#
# Example:
#
# Turn 1:
#
# "My backend uses Django REST Framework."
#
#
# Turn 2:
#
# "What framework am I using?"
#
#
# Turn 2 only makes sense if the earlier information is
# available as conversation context.


# ============================================================
# INDEPENDENT REQUESTS
# ============================================================

# Two independent calls:
#
# response_1 = client.responses.create(...)
#
# response_2 = client.responses.create(...)
#
#
# do NOT automatically mean:
#
# response_2 knows everything from response_1.
#
#
# Conversation context must be explicitly continued or
# provided by the application.


# ============================================================
# previous_response_id
# ============================================================

# Basic pattern:
#
# response_1 = client.responses.create(
#     model="gpt-5.6",
#     input="..."
# )
#
#
# response_2 = client.responses.create(
#     model="gpt-5.6",
#     previous_response_id=response_1.id,
#     input="..."
# )
#
#
# previous_response_id means:
#
# "Continue the conversation from this previous response."


# ============================================================
# ALWAYS CONTINUE FROM THE LATEST RESPONSE
# ============================================================

# Example:
#
# response_1
#     ↓
# response_2
#     ↓
# response_3
#
#
# Request 3 normally uses:
#
# previous_response_id=response_2.id
#
#
# because response_2 represents the latest point in the
# conversation.


# ============================================================
# RESPONSE ID
# ============================================================

# Every response has an ID:
#
# response.id
#
#
# Example:
#
# print(response.id)
#
#
# That ID can be stored by the application and later used as:
#
# previous_response_id=response.id


# ============================================================
# INSTRUCTIONS AND MULTI-TURN REQUESTS
# ============================================================

# A useful application pattern is:
#
# instructions = """
# You are a concise software assistant.
# """
#
#
# Then supply those instructions on every request.
#
#
# Example:
#
# response_1 = client.responses.create(
#     model="gpt-5.6",
#     instructions=instructions,
#     input="..."
# )
#
#
# response_2 = client.responses.create(
#     model="gpt-5.6",
#     instructions=instructions,
#     previous_response_id=response_1.id,
#     input="..."
# )
#
#
# This keeps application behavior explicit and predictable.


# ============================================================
# TWO MAIN CONVERSATION-STATE PATTERNS
# ============================================================


# ------------------------------------------------------------
# PATTERN 1 — previous_response_id
# ------------------------------------------------------------

# OpenAI-managed conversation continuation.
#
#
# Request
#   ↓
# response.id
#   ↓
# next request uses previous_response_id
#
#
# Advantages:
#
# - simple
# - convenient
# - less message reconstruction code


# ------------------------------------------------------------
# PATTERN 2 — APPLICATION-MANAGED HISTORY
# ------------------------------------------------------------

# Your application stores messages itself:
#
# [
#     user message,
#     assistant response,
#     user message,
#     assistant response,
# ]
#
#
# Then sends the desired history with the next request.
#
#
# Advantages:
#
# - explicit control
# - easier trimming
# - easier summarization
# - application-owned history
# - useful for persistence and auditing


# ============================================================
# CONVERSATION STATE IS NOT THE SAME AS PERMANENT MEMORY
# ============================================================

# Suppose:
#
# User:
# "I prefer dark mode."
#
#
# If that preference must still exist months later, the
# application should normally store it in its own database.
#
#
# Example:
#
# user_preferences
#
# user_id
# theme
# language
# timezone
#
#
# Do not treat model conversation context as your enterprise
# application's permanent source of truth.


# ============================================================
# CONVERSATION STATE VS APPLICATION DATABASE
# ============================================================

# Conversation state:
#
# Helps the model understand the current discussion.
#
#
# Application database:
#
# Stores durable business/application information.
#
#
# Example:
#
# Conversation:
#
# "What were we discussing earlier?"
#
#
# Database:
#
# user profile
# orders
# permissions
# preferences
# audit history
# workflow state


# ============================================================
# CONVERSATION STATE VS RAG
# ============================================================

# Conversation State asks:
#
# "What has already been discussed?"
#
#
# RAG asks:
#
# "What external knowledge is relevant to this question?"
#
#
# Example:
#
# Conversation:
#
# User previously said:
# "I am an administrator."
#
#
# RAG:
#
# Security policy says:
# "Administrators must use MFA."
#
#
# A real AI application can combine:
#
# conversation history
# +
# retrieved documents
# +
# current question
#     ↓
# GPT


# ============================================================
# CONVERSATION STATE VS TOOL CALLING
# ============================================================

# Conversation state:
#
# remembers/continues the discussion.
#
#
# Tool calling:
#
# asks the application to execute a capability.
#
#
# Example:
#
# User:
# "What was the order number we discussed?"
#
# -> conversation state
#
#
# User:
# "What is the current status of that order?"
#
# -> tool call may query the order system
#
#
# These concepts often work together.


# ============================================================
# TOKEN / CONTEXT IMPACT
# ============================================================

# Long conversations contain increasing amounts of context.
#
#
# Example:
#
# Turn 1
# Turn 2
# Turn 3
# ...
# Turn 500
#
#
# Eventually this affects:
#
# - token usage
# - cost
# - latency
# - context-window usage
#
#
# Production applications may therefore use:
#
# recent-message windows
# summaries
# RAG
# extracted important facts
# application-managed persistent memory


# ============================================================
# VERY IMPORTANT WEB-APPLICATION RULE
# ============================================================

# Do NOT use one global:
#
# latest_response_id
#
# for every user in a production web application.
#
#
# Why?
#
# User A and User B could accidentally share conversation
# state.
#
#
# Instead, associate conversation state with:
#
# user
# +
# conversation/session


# ============================================================
# EXAMPLE DATABASE DESIGN
# ============================================================

# A production application might have:
#
#
# ChatConversation
#
# id
# user_id
# latest_response_id
# created_at
# updated_at
#
#
# ChatMessage
#
# id
# conversation_id
# role
# content
# created_at


# ============================================================
# ANGULAR + DRF EXAMPLE
# ============================================================

# Angular Chat UI
#       ↓
# User sends message
#       ↓
# POST /api/chat
#       ↓
# DRF
#       ↓
# Load conversation
#       ↓
# Get latest_response_id
#       ↓
# OpenAI Responses API
#       ↓
# Save new response.id
#       ↓
# Return answer
#       ↓
# Angular


# ============================================================
# MULTIPLE USERS
# ============================================================

# User A:
#
# conversation_id = 101
# latest_response_id = response_A
#
#
# User B:
#
# conversation_id = 202
# latest_response_id = response_B
#
#
# These conversation chains must remain separate.


# ============================================================
# EXAMPLE BACKEND FLOW
# ============================================================

# Request:
#
# POST /chat
#
# {
#     "conversation_id": 101,
#     "message": "What framework am I using?"
# }
#
#
# DRF:
#
# 1. Authenticate user
#
# 2. Load conversation 101
#
# 3. Verify the user owns/can access conversation 101
#
# 4. Read latest_response_id
#
# 5. Call OpenAI using previous_response_id
#
# 6. Save new response.id
#
# 7. Save user + assistant messages if required
#
# 8. Return assistant response


# ============================================================
# SECURITY CONSIDERATIONS
# ============================================================

# Conversation state must still respect:
#
# authentication
# authorization
# tenant isolation
# privacy
# retention policies
# audit requirements
#
#
# Never allow:
#
# User A
#
# to continue or retrieve:
#
# User B's conversation.


# ============================================================
# STATE / MEMORY TERMINOLOGY
# ============================================================

# It is useful to distinguish:
#
#
# 1. CURRENT REQUEST CONTEXT
#
# Data supplied to one model request.
#
#
# 2. CONVERSATION STATE
#
# Earlier turns used to continue the current conversation.
#
#
# 3. APPLICATION MEMORY
#
# Durable information stored by your application.
#
#
# 4. RAG KNOWLEDGE
#
# External documents retrieved because they are relevant to
# the current question.


# ============================================================
# SIMPLE MENTAL MODEL
# ============================================================

# Current Question
#      +
# Conversation State
#      +
# Relevant RAG Context
#      +
# Application Instructions
#      ↓
# GPT
#      ↓
# Response


# ============================================================
# EVOLUTION OF OUR OPENAI API LEARNING
# ============================================================

# MODULE 01
#
# First API request


# MODULE 02
#
# Instructions + roles


# MODULE 03
#
# Tokens + output control


# MODULE 04
#
# Structured output


# MODULE 05
#
# Function calling


# MODULE 06
#
# Embeddings


# MODULE 07
#
# Manual semantic search


# MODULE 08
#
# Manual RAG


# MODULE 09
#
# Vector database RAG


# MODULE 10
#
# Multi-turn conversation state


# ============================================================
# CORE PATTERN TO REMEMBER
# ============================================================

# First request:
#
# response_1
#
#        ↓
#
# response_1.id
#
#        ↓
#
# Second request:
#
# previous_response_id=response_1.id
#
#        ↓
#
# response_2
#
#        ↓
#
# response_2.id
#
#        ↓
#
# Continue conversation


# ============================================================
# FINAL TAKEAWAY
# ============================================================

# previous_response_id
#
# -> provides conversation continuity
#
#
# response.id
#
# -> identifies the response that the next request can
#    continue from
#
#
# Your application database
#
# -> should own durable user/business state
#
#
# RAG
#
# -> supplies relevant external knowledge
#
#
# These are related concepts, but they solve different
# problems.
