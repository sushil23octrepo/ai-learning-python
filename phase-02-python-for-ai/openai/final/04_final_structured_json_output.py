import json

from openai import OpenAI

# ============================================================
# MODULE 04 — STRUCTURED JSON OUTPUT
# Complete reference implementation for later revision.
# ============================================================


# ------------------------------------------------------------
# 1. CREATE CLIENT
# ------------------------------------------------------------

client = OpenAI()


# ------------------------------------------------------------
# 2. BASIC STRUCTURED OUTPUT
# ------------------------------------------------------------

response = client.responses.create(
    model="gpt-5.6",
    input="""
Analyze this support ticket:

"I cannot log in after resetting my password.
I need access urgently."
""",
    text={
        "format": {
            "type": "json_schema",
            "name": "support_ticket_analysis",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {
                    "category": {"type": "string"},
                    "priority": {"type": "string"},
                    "sentiment": {"type": "string"},
                },
                "required": ["category", "priority", "sentiment"],
                "additionalProperties": False,
            },
        }
    },
)

print(response.output_text)


# ------------------------------------------------------------
# 3. RESTRICT VALUES USING enum
# ------------------------------------------------------------

response = client.responses.create(
    model="gpt-5.6",
    input="""
Analyze this support ticket:

"I cannot log in after resetting my password.
I need access urgently."
""",
    text={
        "format": {
            "type": "json_schema",
            "name": "support_ticket_analysis",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {
                    "category": {"type": "string"},
                    "priority": {"type": "string", "enum": ["Low", "Medium", "High"]},
                    "sentiment": {
                        "type": "string",
                        "enum": ["Positive", "Neutral", "Negative"],
                    },
                },
                "required": ["category", "priority", "sentiment"],
                "additionalProperties": False,
            },
        }
    },
)

print(response.output_text)


# ------------------------------------------------------------
# 4. PARSE JSON STRING INTO PYTHON DICTIONARY
# ------------------------------------------------------------

# response.output_text contains JSON text.
#
# json.loads() converts that JSON string into a Python dict.

result = json.loads(response.output_text)

print()
print("Category:", result["category"])
print("Priority:", result["priority"])
print("Sentiment:", result["sentiment"])


# ------------------------------------------------------------
# 5. STRUCTURED OUTPUT WITH instructions
# ------------------------------------------------------------

instructions = """
You are a support-ticket classification assistant.

Analyze the ticket carefully.
Return only information required by the schema.
"""

ticket = """
My account was locked after several failed login attempts.
This is blocking me from completing urgent work.
"""

response = client.responses.create(
    model="gpt-5.6",
    instructions=instructions,
    input=ticket,
    text={
        "format": {
            "type": "json_schema",
            "name": "ticket_classification",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {
                    "category": {"type": "string"},
                    "priority": {"type": "string", "enum": ["Low", "Medium", "High"]},
                    "requires_follow_up": {"type": "boolean"},
                },
                "required": ["category", "priority", "requires_follow_up"],
                "additionalProperties": False,
            },
        }
    },
)

result = json.loads(response.output_text)

print()
print("Category:", result["category"])
print("Priority:", result["priority"])
print("Requires Follow Up:", result["requires_follow_up"])


# ------------------------------------------------------------
# 6. ARRAY OUTPUT
# ------------------------------------------------------------

response = client.responses.create(
    model="gpt-5.6",
    input="""
Analyze the following issue:

The user cannot log in.
They already reset their password.
They also report that the account appears locked.
""",
    text={
        "format": {
            "type": "json_schema",
            "name": "issue_analysis",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {
                    "issues": {"type": "array", "items": {"type": "string"}}
                },
                "required": ["issues"],
                "additionalProperties": False,
            },
        }
    },
)

result = json.loads(response.output_text)

print()
print("Issues:")

for issue in result["issues"]:
    print("-", issue)


# ------------------------------------------------------------
# 7. NESTED OBJECT EXAMPLE
# ------------------------------------------------------------

response = client.responses.create(
    model="gpt-5.6",
    input="""
Analyze this support ticket:

"My login stopped working after changing my password.
Please fix this quickly."
""",
    text={
        "format": {
            "type": "json_schema",
            "name": "nested_ticket_analysis",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {
                    "category": {"type": "string"},
                    "customer": {
                        "type": "object",
                        "properties": {
                            "sentiment": {
                                "type": "string",
                                "enum": ["Positive", "Neutral", "Negative"],
                            },
                            "needs_follow_up": {"type": "boolean"},
                        },
                        "required": ["sentiment", "needs_follow_up"],
                        "additionalProperties": False,
                    },
                },
                "required": ["category", "customer"],
                "additionalProperties": False,
            },
        }
    },
)

result = json.loads(response.output_text)

print()
print("Category:", result["category"])

print("Sentiment:", result["customer"]["sentiment"])

print("Needs Follow Up:", result["customer"]["needs_follow_up"])


# ------------------------------------------------------------
# 8. ERROR HANDLING
# ------------------------------------------------------------

try:
    response = client.responses.create(
        model="gpt-5.6",
        instructions="""
You are a concise code-review assistant.
Return only fields required by the schema.
""",
        input="""
Review this Python code:

def divide(a, b):
    return a / b
""",
        text={
            "format": {
                "type": "json_schema",
                "name": "code_review",
                "strict": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "summary": {"type": "string"},
                        "has_issue": {"type": "boolean"},
                        "severity": {
                            "type": "string",
                            "enum": ["Low", "Medium", "High"],
                        },
                        "issues": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["summary", "has_issue", "severity", "issues"],
                    "additionalProperties": False,
                },
            }
        },
    )

    result = json.loads(response.output_text)

    print()
    print("Summary:", result["summary"])
    print("Has Issue:", result["has_issue"])
    print("Severity:", result["severity"])

    print("Issues:")

    for issue in result["issues"]:
        print("-", issue)

except Exception as ex:
    print(f"OpenAI request failed: {ex}")


# ============================================================
# IMPORTANT REVISION
# ============================================================

# Plain text:
#
# Good when the result is mainly for humans.


# Structured JSON:
#
# Good when the result will be consumed by:
#
# backend code
# frontend applications
# databases
# APIs
# workflows


# ------------------------------------------------------------
# JSON SCHEMA IMPORTANT FIELDS
# ------------------------------------------------------------

# "type": "json_schema"
#
# -> tells OpenAI to use structured JSON output


# "name": "..."
#
# -> gives the schema a meaningful name


# "strict": True
#
# -> requires strict schema adherence


# "properties"
#
# -> fields allowed in the object


# "required"
#
# -> fields that must exist


# "additionalProperties": False
#
# -> prevents unexpected extra fields


# "enum"
#
# -> restricts a field to specific values


# Example:
#
# "severity": {
#     "type": "string",
#     "enum": [
#         "Low",
#         "Medium",
#         "High"
#     ]
# }


# ------------------------------------------------------------
# JSON STRING TO PYTHON DICT
# ------------------------------------------------------------

# response.output_text
#
# -> JSON-formatted string


# json.loads(...)
#
# -> Python dictionary


# Example:
#
# result = json.loads(
#     response.output_text
# )
#
# print(result["severity"])


# ============================================================
# ENTERPRISE ARCHITECTURE
# ============================================================

# Angular
#    ↓
# DRF API
#    ↓
# OpenAI
#    ↓
# JSON Schema
#    ↓
# predictable structured response
#    ↓
# Python dictionary
#    ↓
# DRF JSON response
#    ↓
# Angular


# ============================================================
# KEY IDEA
# ============================================================

# Natural-language output
# -> flexible
# -> human friendly
#
# Structured output
# -> predictable
# -> machine friendly
#
# For enterprise API integration,
# structured output is often the better choice.
