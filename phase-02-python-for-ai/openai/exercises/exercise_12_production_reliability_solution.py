import time

from openai import OpenAI

# ============================================================
# OPENAI API EXERCISE 12
# PRODUCTION RELIABILITY
#
# Goal:
#
# Create a reusable OpenAI request function that:
#
# - retries failed requests
# - uses exponential backoff
# - measures latency
# - prints token usage
# - limits retry attempts
# ============================================================


# ------------------------------------------------------------
# 1. CREATE CLIENT
# ------------------------------------------------------------

client = OpenAI()


# ------------------------------------------------------------
# 2. REUSABLE REQUEST FUNCTION
# ------------------------------------------------------------


def send_request(
    prompt,
    max_attempts=3,
):

    for attempt in range(
        1,
        max_attempts + 1,
    ):

        # ----------------------------------------------------
        # START LATENCY TIMER
        # ----------------------------------------------------

        start_time = time.perf_counter()

        try:

            # ------------------------------------------------
            # SEND REQUEST
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
            # PRINT SUCCESS METRICS
            # ------------------------------------------------

            print()

            print(f"Attempt {attempt}: SUCCESS")

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
            # RETURN RESPONSE
            # ------------------------------------------------

            return response

        except Exception as ex:

            # ------------------------------------------------
            # PRINT FAILURE
            # ------------------------------------------------

            latency = time.perf_counter() - start_time

            print()

            print(f"Attempt {attempt}: FAILED")

            print(f"Latency: {latency:.2f} seconds")

            print(
                "Error:",
                ex,
            )

            # ------------------------------------------------
            # FINAL ATTEMPT?
            # ------------------------------------------------

            if attempt == max_attempts:

                print("No retry attempts remaining.")

                raise

            # ------------------------------------------------
            # EXPONENTIAL BACKOFF
            # ------------------------------------------------

            wait_seconds = 2 ** (attempt - 1)

            print(f"Retrying in " f"{wait_seconds} second(s)...")

            time.sleep(wait_seconds)


# ------------------------------------------------------------
# 3. TEST REQUEST
# ------------------------------------------------------------

prompt = """
Explain the difference between authentication and
authorization in 3 sentences.
"""


try:

    response = send_request(
        prompt=prompt,
        max_attempts=3,
    )

    # --------------------------------------------------------
    # 4. PRINT FINAL RESPONSE
    # --------------------------------------------------------

    print()
    print("Final Response:")

    print(response.output_text)


except Exception as ex:

    print()
    print("Request failed after all retries:")

    print(ex)
