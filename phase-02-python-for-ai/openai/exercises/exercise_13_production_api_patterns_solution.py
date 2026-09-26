from dataclasses import dataclass

from openai import OpenAI

# ============================================================
# OPENAI API EXERCISE 13
# PRODUCTION API PATTERNS
#
# Goal:
# Build:
#
# - AIResponse
# - AIServiceError
# - OpenAIService
# - SecurityAssistantService
#
# and keep business logic separated from OpenAI SDK details.
# ============================================================


# ------------------------------------------------------------
# 1. APPLICATION RESPONSE MODEL
# ------------------------------------------------------------


@dataclass
class AIResponse:
    text: str
    response_id: str
    input_tokens: int
    output_tokens: int
    total_tokens: int


# ------------------------------------------------------------
# 2. APPLICATION-SPECIFIC ERROR
# ------------------------------------------------------------


class AIServiceError(Exception):
    pass


# ------------------------------------------------------------
# 3. OPENAI SERVICE
# ------------------------------------------------------------


class OpenAIService:

    def __init__(
        self,
        model="gpt-5.6",
    ):
        self.client = OpenAI()
        self.model = model

    def generate_response(
        self,
        prompt,
        instructions=None,
        max_output_tokens=300,
    ):

        try:

            response = self.client.responses.create(
                model=self.model,
                instructions=instructions,
                input=prompt,
                max_output_tokens=max_output_tokens,
            )

            return AIResponse(
                text=response.output_text,
                response_id=response.id,
                input_tokens=response.usage.input_tokens,
                output_tokens=response.usage.output_tokens,
                total_tokens=response.usage.total_tokens,
            )

        except Exception as ex:

            raise AIServiceError("AI request failed.") from ex


# ------------------------------------------------------------
# 4. SECURITY BUSINESS SERVICE
# ------------------------------------------------------------


class SecurityAssistantService:

    def __init__(
        self,
        openai_service,
    ):
        # Dependency injected from outside.
        self.openai_service = openai_service

    def answer_question(
        self,
        question,
        context,
    ):

        instructions = """
You are a security-policy assistant.

Answer the user's question using only the supplied context.

If the information is not available in the supplied context,
say that the information is not available.

Do not invent information.

Keep the answer concise.
"""

        prompt = f"""
Context:
{context}

Question:
{question}
"""

        return self.openai_service.generate_response(
            prompt=prompt,
            instructions=instructions,
            max_output_tokens=200,
        )


# ------------------------------------------------------------
# 5. CREATE SERVICES
# ------------------------------------------------------------

openai_service = OpenAIService()


security_service = SecurityAssistantService(openai_service)


# ------------------------------------------------------------
# 6. SECURITY CONTEXT
# ------------------------------------------------------------

context = """
Passwords must contain at least 12 characters.
Administrator accounts require multi-factor authentication.
Password reset links expire after 30 minutes.
"""


# ------------------------------------------------------------
# 7. USER QUESTION
# ------------------------------------------------------------

question = """
How long is a password reset link valid?
"""


# ------------------------------------------------------------
# 8. CALL BUSINESS SERVICE
# ------------------------------------------------------------

try:

    result = security_service.answer_question(
        question=question,
        context=context,
    )

    # --------------------------------------------------------
    # 9. PRINT RESULT
    # --------------------------------------------------------

    print(
        "Answer:",
        result.text,
    )

    print(
        "Response ID:",
        result.response_id,
    )

    print(
        "Input Tokens:",
        result.input_tokens,
    )

    print(
        "Output Tokens:",
        result.output_tokens,
    )

    print(
        "Total Tokens:",
        result.total_tokens,
    )


except AIServiceError as ex:

    print(
        "AI service error:",
        ex,
    )
