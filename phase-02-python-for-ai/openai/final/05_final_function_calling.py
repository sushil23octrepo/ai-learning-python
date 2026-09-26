import json

from openai import OpenAI

# ============================================================
# MODULE 05 — FUNCTION CALLING / CUSTOM TOOLS
#
# Goal:
# Learn how OpenAI can decide that it needs one of our
# application functions, provide arguments for that function,
# and then continue the response after our Python code executes
# the real function.
#
# IMPORTANT:
# OpenAI does NOT directly execute our Python function.
#
# Flow:
#
# User
#   ↓
# OpenAI
#   ↓
# function_call
#   ↓
# Our Python code executes the function
#   ↓
# function_call_output
#   ↓
# OpenAI
#   ↓
# Final natural-language answer
# ============================================================


# ------------------------------------------------------------
# 1. CREATE OPENAI CLIENT
# ------------------------------------------------------------

client = OpenAI()


# ------------------------------------------------------------
# 2. CREATE THE REAL APPLICATION FUNCTION
# ------------------------------------------------------------

# In this example, we use a Python dictionary as fake data.
#
# In a real enterprise application, this function could call:
#
# - PostgreSQL
# - SQL Server
# - REST API
# - internal microservice
# - Azure service
# - another backend system


def get_order_status(order_id):
    orders = {
        1001: "Processing",
        1002: "Shipped",
        1003: "Delivered",
    }

    return orders.get(
        order_id,
        "Order not found",
    )


# ------------------------------------------------------------
# 3. DESCRIBE THE FUNCTION TO OPENAI
# ------------------------------------------------------------

# The model cannot automatically inspect our Python function.
#
# Therefore, we must describe:
#
# - function name
# - what the function does
# - arguments it expects
# - argument types
#
# JSON Schema is used to describe the parameters.

tools = [
    {
        "type": "function",
        # Must match the function we want our application to call.
        "name": "get_order_status",
        # Helps the model understand when this function is useful.
        "description": "Get the status of an order.",
        # JSON Schema for function arguments.
        "parameters": {
            "type": "object",
            "properties": {
                "order_id": {
                    "type": "integer",
                    "description": "Order ID",
                }
            },
            # order_id must be supplied.
            "required": ["order_id"],
            # Do not allow unexpected parameters.
            "additionalProperties": False,
        },
        # Ask the model to strictly follow the schema.
        "strict": True,
    }
]


# ------------------------------------------------------------
# 4. USER REQUEST
# ------------------------------------------------------------

user_input = """
What is the status of order 1002?
"""


# ------------------------------------------------------------
# 5. FIRST OPENAI REQUEST
# ------------------------------------------------------------

# We send both:
#
# - user question
# - tools available to the model
#
# OpenAI now decides whether a tool is required.

response = client.responses.create(
    model="gpt-5.6",
    input=user_input,
    tools=tools,
)


# ------------------------------------------------------------
# 6. INSPECT RESPONSE OUTPUT
# ------------------------------------------------------------

# response.output may contain one or more output items.
#
# One possible item type is:
#
# function_call
#
# Example conceptually:
#
# function_call
#   name      = get_order_status
#   arguments = {"order_id": 1002}
#   call_id   = unique call identifier


for item in response.output:

    # --------------------------------------------------------
    # 7. CHECK WHETHER THE MODEL REQUESTED A FUNCTION
    # --------------------------------------------------------

    if item.type == "function_call":

        # ----------------------------------------------------
        # 8. READ FUNCTION NAME
        # ----------------------------------------------------

        # item.name tells us which function the model wants.
        #
        # In this simple example we only have one function,
        # but real applications may have many tools.

        print(
            "Function requested:",
            item.name,
        )

        # ----------------------------------------------------
        # 9. PARSE FUNCTION ARGUMENTS
        # ----------------------------------------------------

        # item.arguments is JSON text.
        #
        # Example:
        #
        # '{"order_id":1002}'
        #
        # json.loads() converts the JSON string into a
        # normal Python dictionary.

        arguments = json.loads(item.arguments)

        # ----------------------------------------------------
        # 10. READ ARGUMENT VALUE
        # ----------------------------------------------------

        order_id = arguments["order_id"]

        # ----------------------------------------------------
        # 11. EXECUTE THE REAL PYTHON FUNCTION
        # ----------------------------------------------------

        # This is where OUR application performs the actual
        # business operation.
        #
        # OpenAI is not executing this function.

        status = get_order_status(order_id)

        # ----------------------------------------------------
        # 12. SEND FUNCTION RESULT BACK TO OPENAI
        # ----------------------------------------------------

        # We now make another API request.
        #
        # previous_response_id connects this request with the
        # previous response.
        #
        # function_call_output tells OpenAI:
        #
        # "Here is the result of the function you requested."

        second_response = client.responses.create(
            model="gpt-5.6",
            previous_response_id=response.id,
            input=[
                {
                    "type": "function_call_output",
                    # call_id links this output to the
                    # original function request.
                    "call_id": item.call_id,
                    # This is the actual result returned
                    # by our application function.
                    "output": status,
                }
            ],
            # Include the tool definitions again.
            tools=tools,
        )

        # ----------------------------------------------------
        # 13. PRINT FINAL NATURAL-LANGUAGE ANSWER
        # ----------------------------------------------------

        print()
        print(second_response.output_text)


# ============================================================
# IMPORTANT REVISION NOTES
# ============================================================


# ------------------------------------------------------------
# FUNCTION CALLING DOES NOT MEAN:
# ------------------------------------------------------------

# OpenAI directly executes:
#
# get_order_status(1002)
#
# That does NOT happen.


# ------------------------------------------------------------
# WHAT ACTUALLY HAPPENS:
# ------------------------------------------------------------

# User:
#
# "What is the status of order 1002?"
#
#            ↓
#
# OpenAI decides:
#
# "I need get_order_status."
#
#            ↓
#
# OpenAI produces something conceptually like:
#
# function_call
#
# name:
# get_order_status
#
# arguments:
# {"order_id": 1002}
#
#            ↓
#
# Python application executes:
#
# get_order_status(1002)
#
#            ↓
#
# Result:
#
# "Shipped"
#
#            ↓
#
# Python sends function_call_output back to OpenAI
#
#            ↓
#
# OpenAI produces final response:
#
# "Order 1002 has been shipped."


# ============================================================
# IMPORTANT OBJECTS
# ============================================================

# response.output
#
# Contains output items produced by the model.


# item.type
#
# Tells us what kind of output item this is.
#
# Example:
#
# "function_call"


# item.name
#
# Name of the requested function.


# item.arguments
#
# JSON string containing function arguments.


# json.loads(item.arguments)
#
# Converts JSON arguments into a Python dictionary.


# item.call_id
#
# Unique identifier for this function call.
#
# We send this back with function_call_output so OpenAI knows
# which function call the result belongs to.


# response.id
#
# Identifier for the first model response.


# previous_response_id=response.id
#
# Continues from the previous response instead of treating the
# second request as completely unrelated.


# ============================================================
# TOOL DEFINITION STRUCTURE
# ============================================================

# tools = [
#     {
#         "type": "function",
#         "name": "function_name",
#         "description": "What the function does",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 ...
#             },
#             "required": [
#                 ...
#             ],
#             "additionalProperties": False
#         },
#         "strict": True
#     }
# ]


# ============================================================
# FUNCTION CALLING VS STRUCTURED OUTPUT
# ============================================================

# STRUCTURED OUTPUT
#
# OpenAI
#   ↓
# structured JSON
#   ↓
# application
#
# Use when the model should RETURN structured information.


# FUNCTION CALLING
#
# OpenAI
#   ↓
# asks application to call a function
#   ↓
# application executes function
#   ↓
# result returned to OpenAI
#
# Use when the model needs DATA or ACTIONS from the application.


# ============================================================
# REAL ENTERPRISE EXAMPLES
# ============================================================

# Functions could be:
#
# get_customer(customer_id)
#
# get_order_status(order_id)
#
# get_ride(ride_id)
#
# search_orders(customer_id)
#
# get_employee_leave_balance(employee_id)
#
# create_support_ticket(...)
#
# send_email(...)
#
# check_inventory(product_id)
#
# create_invoice(...)
#
# lookup_policy(...)


# ============================================================
# SECURITY RULE
# ============================================================

# Never assume that because OpenAI requested a function call,
# the operation should automatically be allowed.
#
# Your backend must still enforce:
#
# authentication
# authorization
# input validation
# business rules
# ownership checks
# audit logging
#
# Example:
#
# OpenAI may request:
#
# cancel_ride(123)
#
# Your backend must still verify:
#
# - Is the user authenticated?
# - Does the user have permission?
# - Does ride 123 exist?
# - Is cancellation allowed?
# - Is the ride already completed?
#
# Function calling does NOT replace backend security.


# ============================================================
# ENTERPRISE ARCHITECTURE
# ============================================================

# Angular
#    ↓
# User question
#    ↓
# DRF backend
#    ↓
# OpenAI
#    ↓
# function_call
#    ↓
# DRF service / database / external API
#    ↓
# function result
#    ↓
# OpenAI
#    ↓
# Final response
#    ↓
# DRF
#    ↓
# Angular


# ============================================================
# CORE PATTERN TO REMEMBER
# ============================================================

# 1. Define real Python function
#
# 2. Describe function using tools
#
# 3. Send tools to OpenAI
#
# 4. Model returns function_call
#
# 5. Parse item.arguments
#
# 6. Execute real Python function
#
# 7. Send function_call_output
#
# 8. Continue using previous_response_id
#
# 9. Read final response


# ============================================================
# SIMPLE MENTAL MODEL
# ============================================================

# OpenAI decides:
#
# WHAT function should be called
# and
# WHAT arguments should be passed.
#
#
# Your application decides:
#
# WHETHER the operation is allowed
# and
# ACTUALLY executes the function.
