from openai import OpenAI

# ============================================================
# OPENAI API EXERCISE 10
# CONVERSATION STATE
#
# Goal:
# Continue a three-turn software-project conversation using
# previous_response_id.
# ============================================================


# ------------------------------------------------------------
# 1. CREATE CLIENT
# ------------------------------------------------------------

client = OpenAI()


# ------------------------------------------------------------
# 2. REUSABLE APPLICATION INSTRUCTIONS
# ------------------------------------------------------------

instructions = """
You are a concise software architecture assistant.

Answer clearly for an experienced software developer.
Use a maximum of 3 sentences.
"""


try:

    # --------------------------------------------------------
    # 3. TURN 1
    # --------------------------------------------------------

    response_1 = client.responses.create(
        model="gpt-5.6",
        instructions=instructions,
        input="""
I am building an employee portal.
""",
    )

    print("TURN 1:")

    print(response_1.output_text)

    print(
        "Response ID:",
        response_1.id,
    )

    # --------------------------------------------------------
    # 4. TURN 2
    # --------------------------------------------------------

    # Continue from Turn 1.

    response_2 = client.responses.create(
        model="gpt-5.6",
        instructions=instructions,
        previous_response_id=response_1.id,
        input="""
The frontend uses Angular and the backend uses
Django REST Framework.
""",
    )

    print()
    print("TURN 2:")

    print(response_2.output_text)

    print(
        "Response ID:",
        response_2.id,
    )

    # --------------------------------------------------------
    # 5. TURN 3
    # --------------------------------------------------------

    # Continue from Turn 2, which is now the latest response.

    response_3 = client.responses.create(
        model="gpt-5.6",
        instructions=instructions,
        previous_response_id=response_2.id,
        input="""
What technologies am I using for the frontend and backend?
""",
    )

    print()
    print("TURN 3:")

    print(response_3.output_text)

    print(
        "Response ID:",
        response_3.id,
    )


except Exception as ex:

    print(f"Conversation request failed: {ex}")
