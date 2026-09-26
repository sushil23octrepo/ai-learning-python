import time

from openai import OpenAI

# ============================================================
# MODULE 12 — PRODUCTION RELIABILITY
#
# Topics covered:
#
# - token usage
# - latency measurement
# - retries
# - exponential backoff
# - transient vs permanent failures
# - rate limits
# - timeouts
# - logging
# - idempotency awareness
# - fallback behavior
#
#
# IMPORTANT IDEA:
#
# A production AI integration should not only work when
# everything is perfect.
#
# It should also behave predictably when:
#
# - the network is slow
# - OpenAI is temporarily unavailable
# - rate limits are reached
# - requests fail
# - retries are needed
#
#
# CORE FLOW:
#
# Request
#   ↓
# Measure latency
#   ↓
# Send OpenAI call
#   ↓
# Success?
#   ↓
# YES -> log usage + return response
#
# NO
#   ↓
# Retry if appropriate
#   ↓
# Exponential backoff
#   ↓
# Eventually fail safely
# ============================================================


# ------------------------------------------------------------
# 1. CREATE OPENAI CLIENT
# ------------------------------------------------------------

client = OpenAI()


# ------------------------------------------------------------
# 2. REUSABLE REQUEST FUNCTION
# ------------------------------------------------------------


def send_openai_request(
    prompt,
    max_attempts=3,
):
    """
    Send an OpenAI request with basic production-oriented
    reliability features.

    Features:
    - limited retry count
    - latency measurement
    - token usage logging
    - exponential backoff
    - exception propagation after final failure

    NOTE:
    This learning example retries all exceptions.

    In production, retries should be limited to transient
    errors such as:
    - rate limits
    - temporary service failures
    - connection errors
    - timeouts

    Permanent errors such as:
    - bad request
    - unsupported parameter
    - authentication failure
    should normally fail immediately.
    """

    for attempt in range(
        1,
        max_attempts + 1,
    ):

        # ----------------------------------------------------
        # Measure request latency.
        # ----------------------------------------------------

        start_time = time.perf_counter()

        try:

            # ------------------------------------------------
            # SEND OPENAI REQUEST
            # ------------------------------------------------

            response = client.responses.create(
                model="gpt-5.6",
                input=prompt,
                max_output_tokens=200,
            )

            # ------------------------------------------------
            # CALCULATE LATENCY
            # ------------------------------------------------

            latency = time.perf_counter() - start_time

            # ------------------------------------------------
            # LOG SUCCESS DETAILS
            # ------------------------------------------------

            print()
            print("REQUEST SUCCESSFUL")

            print(
                "Attempt:",
                attempt,
            )

            print(f"Latency: {latency:.2f} seconds")

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

            # ------------------------------------------------
            # RETURN SUCCESSFUL RESPONSE
            # ------------------------------------------------

            return response

        except Exception as ex:

            # ------------------------------------------------
            # CALCULATE FAILED-REQUEST LATENCY
            # ------------------------------------------------

            latency = time.perf_counter() - start_time

            # ------------------------------------------------
            # LOG FAILURE
            # ------------------------------------------------

            print()
            print(f"Attempt {attempt} failed.")

            print(f"Latency before failure: " f"{latency:.2f} seconds")

            print(
                "Error:",
                ex,
            )

            # ------------------------------------------------
            # STOP AFTER FINAL ATTEMPT
            # ------------------------------------------------

            if attempt == max_attempts:

                print()
                print("Maximum retry attempts reached.")

                raise

            # ------------------------------------------------
            # EXPONENTIAL BACKOFF
            # ------------------------------------------------

            # Attempt 1 fails:
            #
            # 2 ** (1 - 1)
            # = 1 second
            #
            #
            # Attempt 2 fails:
            #
            # 2 ** (2 - 1)
            # = 2 seconds
            #
            #
            # Attempt 3 would be final in this example,
            # so no further retry occurs.

            wait_seconds = 2 ** (attempt - 1)

            print(f"Retrying in " f"{wait_seconds} second(s)...")

            time.sleep(wait_seconds)


# ------------------------------------------------------------
# 3. USE THE RELIABLE REQUEST FUNCTION
# ------------------------------------------------------------

prompt = """
Explain the difference between authentication and
authorization in 3 sentences.
"""


try:

    response = send_openai_request(
        prompt=prompt,
        max_attempts=3,
    )

    # --------------------------------------------------------
    # PRINT FINAL MODEL RESPONSE
    # --------------------------------------------------------

    print()
    print("FINAL RESPONSE:")

    print(response.output_text)


except Exception as ex:

    # --------------------------------------------------------
    # APPLICATION-LEVEL FAILURE HANDLING
    # --------------------------------------------------------

    print()
    print("OpenAI request ultimately failed:")

    print(ex)


# ============================================================
# IMPORTANT REVISION NOTES
# ============================================================


# ------------------------------------------------------------
# WHY TOKEN USAGE MATTERS
# ------------------------------------------------------------

# API usage is affected by:
#
# input tokens
# +
# output tokens
# +
# model pricing
#
#
# Therefore:
#
# measure token usage
#
# instead of:
#
# guessing usage.


# ------------------------------------------------------------
# USE response.usage
# ------------------------------------------------------------

# Useful fields:
#
# response.usage.input_tokens
#
# response.usage.output_tokens
#
# response.usage.total_tokens


# ============================================================
# COST CONTROL
# ============================================================

# Cost can be reduced by:
#
# - using concise prompts
# - avoiding unnecessary conversation history
# - retrieving only relevant RAG chunks
# - limiting excessive output
# - caching where appropriate
# - storing document embeddings instead of regenerating them


# ============================================================
# RAG COST CONSIDERATION
# ============================================================

# RAG commonly involves:
#
# 1. query embedding request
#
# 2. model generation request
#
#
# Document ingestion separately requires:
#
# document embedding requests
#
#
# Therefore costs can be thought of as:
#
# ingestion cost
# +
# query embedding cost
# +
# generation cost


# ============================================================
# LATENCY
# ============================================================

# Latency means:
#
# how long the request takes.
#
#
# Python measurement:
#
# start = time.perf_counter()
#
# request()
#
# latency = time.perf_counter() - start


# ============================================================
# WHY LATENCY MATTERS
# ============================================================

# A technically correct AI feature can still provide poor
# user experience if every request takes too long.
#
#
# Track latency to understand:
#
# - user experience
# - model performance
# - retrieval overhead
# - network issues
# - performance regressions


# ============================================================
# TRANSIENT VS PERMANENT FAILURES
# ============================================================


# ------------------------------------------------------------
# TRANSIENT FAILURES
# ------------------------------------------------------------

# These may succeed if retried:
#
# temporary server error
# connection failure
# timeout
# rate limit
# temporary network problem


# ------------------------------------------------------------
# PERMANENT FAILURES
# ------------------------------------------------------------

# Retrying the same request usually does NOT help:
#
# invalid request
# unsupported parameter
# invalid schema
# authentication failure
# invalid model name


# ------------------------------------------------------------
# EXAMPLE
# ------------------------------------------------------------

# Error:
#
# Unsupported parameter: temperature
#
#
# Retrying 10 times will not fix it.
#
#
# The request itself must be corrected.


# ============================================================
# EXPONENTIAL BACKOFF
# ============================================================

# Instead of:
#
# retry
# retry
# retry
# retry
#
#
# we progressively increase delay.
#
#
# Example:
#
# first retry:
# wait 1 second
#
# second retry:
# wait 2 seconds
#
# third retry:
# wait 4 seconds
#
#
# Formula used:
#
# 2 ** (attempt - 1)


# ============================================================
# WHY BACKOFF HELPS
# ============================================================

# If an external service is overloaded,
# retrying immediately may make the problem worse.
#
#
# Backoff:
#
# reduces request pressure
#
# gives temporary problems time to recover
#
# improves system stability


# ============================================================
# ALWAYS LIMIT RETRIES
# ============================================================

# BAD:
#
# while True:
#     retry()
#
#
# This could retry forever.
#
#
# BETTER:
#
# max_attempts = 3
#
#
# Eventually the application should stop and handle the
# failure appropriately.


# ============================================================
# RATE LIMITS
# ============================================================

# APIs may limit usage based on things such as:
#
# requests
# tokens
# time period
# model/account limits
#
#
# If usage exceeds limits:
#
# the API may reject requests temporarily.
#
#
# This is commonly a retryable situation,
# but retrying should use backoff.


# ============================================================
# TIMEOUTS
# ============================================================

# External API calls should not be allowed to wait forever.
#
#
# Production applications should have explicit timeout
# strategies.
#
#
# Conceptually:
#
# external dependency
#      ↓
# timeout
#      ↓
# retry/fallback/fail safely
#
#
# Exact timeout configuration depends on the current SDK
# version and should be checked against the official API/SDK
# documentation when implementing production configuration.


# ============================================================
# DO NOT RETRY SIDE EFFECTS BLINDLY
# ============================================================

# Read operation:
#
# get_order_status()
#
# may usually be safer to retry.
#
#
# Write/action operations:
#
# create_invoice()
# send_payment()
# send_email()
# cancel_ride()
#
# require more care.


# ============================================================
# DUPLICATE SIDE-EFFECT PROBLEM
# ============================================================

# Example:
#
# create_invoice()
#      ↓
# invoice successfully created
#      ↓
# network failure occurs before response reaches client
#      ↓
# client thinks request failed
#      ↓
# retries
#      ↓
# second invoice may be created
#
#
# This is why production systems may use:
#
# idempotency keys
# unique operation IDs
# duplicate detection
# transaction controls


# ============================================================
# IDEMPOTENCY
# ============================================================

# Idempotent operation:
#
# repeating the same operation does not create additional
# unintended effects.
#
#
# Example conceptually:
#
# Request ID:
#
# cancel-ride-123-operation-456
#
#
# If the same operation is received twice:
#
# backend detects it already ran
#
# and does not execute it twice.


# ============================================================
# LOGGING
# ============================================================

# Useful production metrics may include:
#
# request ID
# user ID
# model
# input tokens
# output tokens
# total tokens
# latency
# attempt count
# status
# error type
# timestamp


# ============================================================
# DO NOT LOG SECRETS
# ============================================================

# Never intentionally log:
#
# OpenAI API keys
# passwords
# access tokens
# private credentials
#
#
# Also be careful with:
#
# private documents
# health data
# financial information
# sensitive user prompts
#
#
# Observability must respect security and privacy.


# ============================================================
# FALLBACK BEHAVIOR
# ============================================================

# When OpenAI is unavailable, the application should have an
# intentional behavior.
#
#
# Examples:
#
# show temporary error
#
# use cached answer
#
# queue work for later
#
# return search results without AI generation
#
# disable AI-only action temporarily
#
#
# Avoid:
#
# OpenAI unavailable
#       ↓
# entire enterprise application crashes


# ============================================================
# CACHING
# ============================================================

# Some work should not be repeated unnecessarily.
#
#
# Example:
#
# Document embeddings
#
# should normally be generated once during ingestion and
# stored.
#
#
# They should NOT be regenerated for every user question.


# ============================================================
# ANGULAR + DRF ARCHITECTURE
# ============================================================

# Angular
#    ↓
# DRF
#    ↓
# AI Service Layer
#    ↓
# validation
# timeout
# retry
# logging
# token tracking
# guardrails
#    ↓
# OpenAI


# ============================================================
# WHY BACKEND SHOULD OWN RELIABILITY
# ============================================================

# Angular should NOT directly:
#
# store OpenAI API key
# implement OpenAI rate-limit logic
# control model configuration
# perform server-side authorization
#
#
# These belong in the backend.


# ============================================================
# PRODUCTION REQUEST PIPELINE
# ============================================================

# User Request
#      ↓
# Authentication
#      ↓
# Authorization
#      ↓
# Input Validation
#      ↓
# AI Request
#      ↓
# Timeout
#      ↓
# Retry transient failures
#      ↓
# Validate AI output
#      ↓
# Log metrics
#      ↓
# Return result


# ============================================================
# OBSERVABILITY
# ============================================================

# A production system should be able to answer:
#
# How many AI calls are being made?
#
# What is the average latency?
#
# How many requests fail?
#
# How many retries occur?
#
# How many tokens are consumed?
#
# Which model is being used?
#
# Which prompt version is being used?
#
#
# If we cannot answer these questions,
# diagnosing production problems becomes difficult.


# ============================================================
# IMPORTANT LIMITATION OF THIS LEARNING EXAMPLE
# ============================================================

# This function currently catches:
#
# Exception
#
# and retries everything.
#
#
# That is useful for understanding retry mechanics.
#
# It is NOT the final enterprise pattern.
#
#
# Production implementation should classify failures and
# retry only transient errors.


# ============================================================
# CORE MENTAL MODEL
# ============================================================

# API call
#    ↓
# Measure
#    ↓
# Did it succeed?
#
# YES
#  ↓
# log metrics
#  ↓
# return
#
#
# NO
#  ↓
# Is it retryable?
#
# YES
#  ↓
# wait with backoff
#  ↓
# retry
#
#
# NO
#  ↓
# fail safely


# ============================================================
# FINAL TAKEAWAY
# ============================================================

# Production reliability is NOT:
#
# "Retry everything."
#
#
# Production reliability means:
#
# measure
#
# limit
#
# retry appropriate failures
#
# use backoff
#
# prevent duplicate side effects
#
# log outcomes
#
# apply timeouts
#
# fail gracefully
