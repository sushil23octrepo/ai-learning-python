from openai import OpenAI

# ============================================================
# OPENAI API EXERCISE 03
# TOKENS, CONTEXT, AND OUTPUT CONTROL
# Reference solution.
# ============================================================


# ------------------------------------------------------------
# 1. CREATE CLIENT
# ------------------------------------------------------------

client = OpenAI()


# ------------------------------------------------------------
# 2. APPLICATION INSTRUCTIONS
# ------------------------------------------------------------

instructions = """
You are a concise application-security tutor.
Explain concepts clearly for experienced developers.
Use a maximum of 3 sentences.
"""


# ------------------------------------------------------------
# 3. USER INPUT
# ------------------------------------------------------------

user_input = """
Explain the difference between authentication and authorization.
"""


# ------------------------------------------------------------
# 4. SEND REQUEST
# ------------------------------------------------------------

try:
    response = client.responses.create(
        model="gpt-5.6",
        instructions=instructions,
        input=user_input,
        max_output_tokens=200,
    )

    # --------------------------------------------------------
    # 5. PRINT GENERATED RESPONSE
    # --------------------------------------------------------

    print(response.output_text)

    # --------------------------------------------------------
    # 6. PRINT TOKEN USAGE
    # --------------------------------------------------------

    print()

    print(
        "Input tokens:",
        response.usage.input_tokens,
    )

    print(
        "Output tokens:",
        response.usage.output_tokens,
    )

    print(
        "Total tokens:",
        response.usage.total_tokens,
    )

except Exception as ex:
    print(f"OpenAI request failed: {ex}")
