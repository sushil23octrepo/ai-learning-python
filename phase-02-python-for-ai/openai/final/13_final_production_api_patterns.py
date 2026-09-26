from dataclasses import dataclass

from openai import OpenAI

# ============================================================
# MODULE 13 — PRODUCTION API ARCHITECTURE
# AND SERVICE-LAYER PATTERNS
#
# Goal:
# Structure OpenAI integration in a way that is reusable,
# testable, maintainable, and suitable for a real backend.
#
# MAIN IDEA:
#
# Do NOT scatter OpenAI SDK calls throughout controllers,
# views, and business logic.
#
# Prefer:
#
# Controller / API View
#        ↓
# Business / Application Service
#        ↓
# OpenAI Service
#        ↓
# OpenAI SDK
#
#
# This gives us:
#
# - centralized model configuration
# - centralized OpenAI client usage
# - cleaner controllers
# - better testability
# - easier error handling
# - easier provider/model replacement
# - separation of responsibilities
# ============================================================


# ============================================================
# 1. APPLICATION RESPONSE MODEL
# ============================================================

# Instead of returning the raw OpenAI SDK response everywhere,
# we convert it into our own application-level object.
#
# This prevents the rest of the application from depending
# directly on OpenAI SDK response structure.


@dataclass
class AIResponse:
    text: str
    response_id: str
    input_tokens: int
    output_tokens: int
    total_tokens: int


# ============================================================
# 2. APPLICATION-SPECIFIC EXCEPTION
# ============================================================

# We do not want every controller/business service to know
# about every possible low-level OpenAI SDK exception.
#
# Instead, OpenAIService translates lower-level failures into
# an exception owned by our application.


class AIServiceError(Exception):
    pass


# ============================================================
# 3. OPENAI SERVICE
# ============================================================

# Responsibility:
#
# OpenAIService knows HOW to communicate with OpenAI.
#
# It should handle things such as:
#
# - OpenAI client
# - model selection
# - API calls
# - response normalization
# - provider-specific error translation
#
#
# It should NOT contain unrelated business rules such as:
#
# - employee leave rules
# - ride cancellation rules
# - support ticket workflow
# - authorization decisions


class OpenAIService:

    def __init__(
        self,
        model="gpt-5.6",
    ):
        # ----------------------------------------------------
        # Create the OpenAI client once for this service.
        # ----------------------------------------------------

        self.client = OpenAI()

        # ----------------------------------------------------
        # Keep model configuration centralized.
        # ----------------------------------------------------

        self.model = model

    def generate_response(
        self,
        prompt,
        instructions=None,
        max_output_tokens=300,
    ):
        """
        Send a text-generation request to OpenAI.

        Parameters:
        - prompt:
          actual request/content sent to the model

        - instructions:
          application-controlled behavior

        - max_output_tokens:
          upper limit for generated output

        Returns:
        - AIResponse

        Raises:
        - AIServiceError
        """

        try:

            # ------------------------------------------------
            # Call OpenAI Responses API.
            # ------------------------------------------------

            response = self.client.responses.create(
                model=self.model,
                instructions=instructions,
                input=prompt,
                max_output_tokens=max_output_tokens,
            )

            # ------------------------------------------------
            # Normalize OpenAI SDK response into our own
            # application response object.
            # ------------------------------------------------

            return AIResponse(
                text=response.output_text,
                response_id=response.id,
                input_tokens=response.usage.input_tokens,
                output_tokens=response.usage.output_tokens,
                total_tokens=response.usage.total_tokens,
            )

        except Exception as ex:

            # ------------------------------------------------
            # Hide provider-specific exception details from
            # upper application layers.
            #
            # "from ex" preserves the original exception as
            # the cause for logging/debugging.
            # ------------------------------------------------

            raise AIServiceError("AI request failed.") from ex


# ============================================================
# 4. BUSINESS / APPLICATION SERVICE
# ============================================================

# Responsibility:
#
# SecurityAssistantService knows WHAT the application wants
# to achieve.
#
# It understands:
#
# - security-assistant behavior
# - how to build the security prompt
# - what context/question to send
#
#
# It does NOT need to know:
#
# - how OpenAI client is initialized
# - OpenAI SDK response structure
# - where the API key comes from


class SecurityAssistantService:

    def __init__(
        self,
        openai_service,
    ):
        # ----------------------------------------------------
        # Dependency Injection
        # ----------------------------------------------------
        #
        # OpenAIService is supplied from outside rather than
        # created internally.
        #
        # This makes the class easier to test and replace.

        self.openai_service = openai_service

    def answer_question(
        self,
        question,
        context,
    ):
        """
        Answer a security-policy question using only supplied
        context.
        """

        # ----------------------------------------------------
        # Business/application instructions
        # ----------------------------------------------------

        instructions = """
You are a security-policy assistant.

Answer the user's question using only the supplied context.

If the information is not available in the supplied context,
say that the information is not available.

Do not invent security-policy information.

Keep the answer concise.
"""

        # ----------------------------------------------------
        # Build the request sent through our generic AI
        # service.
        # ----------------------------------------------------

        prompt = f"""
Context:
{context}

Question:
{question}
"""

        # ----------------------------------------------------
        # Business service delegates the actual OpenAI call
        # to OpenAIService.
        # ----------------------------------------------------

        return self.openai_service.generate_response(
            prompt=prompt,
            instructions=instructions,
            max_output_tokens=200,
        )


# ============================================================
# 5. APPLICATION CODE
# ============================================================

# In a real Django/DRF project, object creation may happen
# through application configuration, dependency wiring,
# factories, or service containers.
#
# For this standalone learning example, we create them here.


openai_service = OpenAIService()


security_service = SecurityAssistantService(openai_service)


# ------------------------------------------------------------
# 6. SAMPLE SECURITY CONTEXT
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
    # 9. PRINT NORMALIZED APPLICATION RESPONSE
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


# ============================================================
# IMPORTANT REVISION NOTES
# ============================================================


# ------------------------------------------------------------
# WHY NOT CALL OPENAI DIRECTLY FROM EVERY CONTROLLER?
# ------------------------------------------------------------

# BAD STRUCTURE:
#
# DRF View
#    ↓
# OpenAI client creation
# prompt construction
# model selection
# retry logic
# parsing
# token handling
# business rules
#
#
# If many endpoints do this:
#
# duplication increases
# maintenance becomes difficult
# testing becomes harder
# model/config changes affect many files


# ============================================================
# BETTER STRUCTURE
# ============================================================

# Angular
#    ↓
# DRF View / Controller
#    ↓
# Application / Business Service
#    ↓
# AI Service
#    ↓
# OpenAI


# ============================================================
# RESPONSIBILITIES
# ============================================================


# ------------------------------------------------------------
# CONTROLLER / API VIEW
# ------------------------------------------------------------

# Should mainly:
#
# receive request
# validate request data
# authenticate user
# authorize user
# call application service
# return API response
#
#
# Controllers should remain thin.


# ------------------------------------------------------------
# BUSINESS / APPLICATION SERVICE
# ------------------------------------------------------------

# Should understand:
#
# application use case
# business workflow
# business-specific prompt
# orchestration
#
#
# Example:
#
# SecurityAssistantService
# PolicyAssistantService
# ChatService
# DocumentIngestionService


# ------------------------------------------------------------
# OPENAI SERVICE
# ------------------------------------------------------------

# Should understand:
#
# OpenAI SDK
# model configuration
# request creation
# response normalization
# provider-specific errors
#
#
# Business services should not need to know OpenAI SDK details.


# ============================================================
# WHY CREATE AIResponse?
# ============================================================

# Without our own response model:
#
# application code depends directly on:
#
# response.output_text
# response.id
# response.usage.input_tokens
# ...
#
#
# With AIResponse:
#
# application code depends on:
#
# result.text
# result.response_id
# result.total_tokens
#
#
# This creates an abstraction boundary.


# ============================================================
# BENEFIT OF RESPONSE ABSTRACTION
# ============================================================

# Suppose OpenAI SDK structure changes later.
#
#
# WITHOUT abstraction:
#
# many files may need modification.
#
#
# WITH abstraction:
#
# update OpenAIService mapping
#
# other services can continue using AIResponse.


# ============================================================
# CENTRALIZED MODEL CONFIGURATION
# ============================================================

# Instead of repeating:
#
# model="gpt-5.6"
#
# in many places:
#
# OpenAIService stores:
#
# self.model
#
#
# Later this can come from:
#
# environment variable
# Django settings
# configuration service


# ============================================================
# CONFIGURATION EXAMPLE
# ============================================================

# In Django:
#
# OPENAI_MODEL = os.getenv(
#     "OPENAI_MODEL",
#     "gpt-5.6",
# )
#
#
# Then:
#
# OpenAIService(
#     model=settings.OPENAI_MODEL
# )


# ============================================================
# DEPENDENCY INJECTION
# ============================================================

# We use:
#
# SecurityAssistantService(
#     openai_service
# )
#
#
# instead of:
#
# class SecurityAssistantService:
#
#     def __init__(self):
#         self.openai_service = OpenAIService()
#
#
# WHY?
#
# Dependency injection makes dependencies explicit and
# replaceable.


# ============================================================
# TESTABILITY BENEFIT
# ============================================================

# During unit testing, we can inject a fake service.
#
#
# Example conceptually:
#
# class FakeOpenAIService:
#
#     def generate_response(...):
#         return AIResponse(...)
#
#
# security_service = SecurityAssistantService(
#     FakeOpenAIService()
# )
#
#
# No real OpenAI API call is required.


# ============================================================
# UNIT TEST VS INTEGRATION TEST
# ============================================================

# UNIT TEST:
#
# Business Service
#       ↓
# FakeOpenAIService
#
#
# Benefits:
#
# fast
# deterministic
# no network
# no API cost


# INTEGRATION TEST:
#
# OpenAIService
#       ↓
# Real OpenAI API
#
#
# Used to verify:
#
# credentials
# SDK integration
# actual API behavior


# ============================================================
# ERROR TRANSLATION
# ============================================================

# OpenAI SDK may raise provider-specific exceptions.
#
#
# Instead of exposing those everywhere:
#
# OpenAIService
#
# converts them into:
#
# AIServiceError
#
#
# Upper application layers depend on OUR exception type.


# ============================================================
# WHY USE "raise ... from ex"?
# ============================================================

# Example:
#
# raise AIServiceError(
#     "AI request failed"
# ) from ex
#
#
# This gives users/application code a clean error:
#
# AI request failed
#
#
# while preserving the original exception internally for:
#
# debugging
# logging
# troubleshooting


# ============================================================
# DO NOT RETURN RAW PROVIDER ERRORS TO ANGULAR
# ============================================================

# Avoid:
#
# {
#   "error":
#   "openai.BadRequestError: some internal details..."
# }
#
#
# Prefer controlled responses:
#
# {
#   "error":
#   "AI service is temporarily unavailable."
# }
#
#
# Technical details belong in secure server logs.


# ============================================================
# WHY RETURN FULL APPLICATION RESPONSE?
# ============================================================

# Sometimes business code needs more than just text.
#
#
# For example:
#
# response_id
# -> conversation continuation
#
# token counts
# -> monitoring / cost
#
# text
# -> API response
#
#
# Therefore AIResponse contains all commonly needed data.


# ============================================================
# FUTURE PROJECT SERVICE STRUCTURE
# ============================================================

# apps/
#
# ai/
# ├── services/
# │   ├── openai_service.py
# │   ├── embedding_service.py
# │   ├── retrieval_service.py
# │   ├── rag_service.py
# │   └── tool_service.py
#
# conversations/
# ├── services/
# │   └── chat_service.py
#
# knowledge/
# ├── services/
# │   └── document_ingestion_service.py
#
# evaluation/
# ├── services/
# │   └── evaluation_service.py


# ============================================================
# EXAMPLE MODULE 15 FLOW
# ============================================================

# Angular
#    ↓
# POST /api/ai/chat
#    ↓
# DRF Chat View
#    ↓
# ChatService
#    ↓
# RetrievalService
#    ↓
# Vector Search
#    ↓
# OpenAIService
#    ↓
# OpenAI
#    ↓
# AIResponse
#    ↓
# ChatService
#    ↓
# DRF Response
#    ↓
# Angular


# ============================================================
# THIN CONTROLLER PRINCIPLE
# ============================================================

# DRF View should mostly do:
#
# validate
# authorize
# call service
# serialize response
#
#
# Avoid putting:
#
# prompt construction
# vector-search loops
# OpenAI calls
# retry algorithms
# complex business rules
#
# directly inside the view.


# ============================================================
# ABSTRACTION BENEFIT
# ============================================================

# Today:
#
# OpenAIService
#
# uses:
#
# OpenAI Responses API
#
#
# Tomorrow the implementation might change.
#
# Business code should ideally remain mostly unchanged because
# it depends on the service abstraction rather than SDK details.


# ============================================================
# CORE DESIGN PRINCIPLE
# ============================================================

# Business logic should depend on:
#
# OUR SERVICE INTERFACE
#
# rather than:
#
# EXTERNAL SDK IMPLEMENTATION DETAILS


# ============================================================
# FINAL MENTAL MODEL
# ============================================================

# Controller
#     ↓
# Business Service
#     ↓
# AI Service
#     ↓
# External Provider
#
#
# Each layer should have a clear responsibility.


# ============================================================
# MODULE 15 CONNECTION
# ============================================================

# Module 15 will apply this architecture to the enterprise
# AI Knowledge & Support Assistant.
#
#
# We will not build:
#
# one giant DRF view
#
#
# We will build separate components for:
#
# chat
# embeddings
# retrieval
# RAG
# document ingestion
# tools
# evaluations
# OpenAI communication
