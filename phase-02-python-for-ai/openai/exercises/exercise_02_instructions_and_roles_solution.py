from openai import OpenAI

# ============================================================
# OPENAI API EXERCISE 02
# INSTRUCTIONS AND ROLES
# Reference solution.
# ============================================================


# ------------------------------------------------------------
# 1. CREATE CLIENT
# ------------------------------------------------------------

client = OpenAI()


# ------------------------------------------------------------
# 2. APPLICATION-CONTROLLED INSTRUCTIONS
# ------------------------------------------------------------

instructions = """
You are a senior Python tutor.
Explain code in simple language.
Use a maximum of 4 sentences.
"""


# ------------------------------------------------------------
# 3. CODE TO EXPLAIN
# ------------------------------------------------------------

code = """
def calculate_total(price, quantity):
    return price * quantity
"""


# ------------------------------------------------------------
# 4. BUILD DYNAMIC USER INPUT
# ------------------------------------------------------------

user_input = f"""
Explain this Python code:

{code}
"""


# ------------------------------------------------------------
# 5. SEND REQUEST
# ------------------------------------------------------------

try:
    response = client.responses.create(
        model="gpt-5.6",
        instructions=instructions,
        input=user_input,
    )

    # --------------------------------------------------------
    # 6. PRINT GENERATED RESPONSE
    # --------------------------------------------------------

    print(response.output_text)

except Exception as ex:
    print(f"OpenAI request failed: {ex}")
