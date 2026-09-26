import json

from openai import OpenAI

# ============================================================
# OPENAI API EXERCISE 14
# LLM APPLICATION SECURITY
#
# Goal:
#
# Demonstrate that:
#
# - OpenAI may request a tool call
# - the backend still performs authorization
# - a normal employee cannot access another employee's data
# - an administrator can access authorized data
# ============================================================


# ------------------------------------------------------------
# 1. CREATE OPENAI CLIENT
# ------------------------------------------------------------

client = OpenAI()


# ------------------------------------------------------------
# 2. SAMPLE EMPLOYEE DATA
# ------------------------------------------------------------

employees = {
    101: {
        "name": "Amit",
        "leave_balance": 12,
    },
    102: {
        "name": "Priya",
        "leave_balance": 8,
    },
}


# ------------------------------------------------------------
# 3. CURRENT USER MODEL
# ------------------------------------------------------------


class CurrentUser:

    def __init__(
        self,
        employee_id,
        is_admin=False,
    ):
        self.employee_id = employee_id
        self.is_admin = is_admin


# ------------------------------------------------------------
# 4. SECURE BACKEND FUNCTION
# ------------------------------------------------------------


def get_employee_leave_balance(
    current_user,
    employee_id,
):
    """
    Return employee leave balance only when the current user
    is authorized.

    Rules:

    Normal employee:
    -> may access only their own leave balance

    Administrator:
    -> may access any employee's leave balance
    """

    # --------------------------------------------------------
    # Authorization check
    # --------------------------------------------------------

    if employee_id != current_user.employee_id and not current_user.is_admin:
        raise PermissionError("Not authorized to view this employee's leave balance.")

    # --------------------------------------------------------
    # Validate employee exists
    # --------------------------------------------------------

    employee = employees.get(employee_id)

    if employee is None:
        raise ValueError("Employee not found.")

    # --------------------------------------------------------
    # Return authorized result
    # --------------------------------------------------------

    return {
        "employee_id": employee_id,
        "name": employee["name"],
        "leave_balance": employee["leave_balance"],
    }


# ------------------------------------------------------------
# 5. DEFINE OPENAI TOOL
# ------------------------------------------------------------

tools = [
    {
        "type": "function",
        "name": "get_employee_leave_balance",
        "description": ("Get the remaining leave balance for an employee."),
        "parameters": {
            "type": "object",
            "properties": {
                "employee_id": {
                    "type": "integer",
                    "description": "Employee ID",
                }
            },
            "required": ["employee_id"],
            "additionalProperties": False,
        },
        "strict": True,
    }
]


# ------------------------------------------------------------
# 6. REUSABLE TEST FUNCTION
# ------------------------------------------------------------


def run_leave_balance_request(
    current_user,
    question,
):
    """
    Ask OpenAI which tool should be called, then perform
    backend authorization before executing the tool.
    """

    print()
    print("=" * 60)

    print(
        "Current User Employee ID:",
        current_user.employee_id,
    )

    print(
        "Current User Is Admin:",
        current_user.is_admin,
    )

    print(
        "Question:",
        question,
    )

    # --------------------------------------------------------
    # FIRST OPENAI REQUEST
    # --------------------------------------------------------

    response = client.responses.create(
        model="gpt-5.6",
        instructions="""
You are an employee-support assistant.

Use the available tool when the user asks about employee
leave balances.

The backend is responsible for authorization.
""",
        input=question,
        tools=tools,
    )

    # --------------------------------------------------------
    # FIND FUNCTION CALL
    # --------------------------------------------------------

    for item in response.output:

        if item.type != "function_call":
            continue

        print()
        print(
            "Tool Requested:",
            item.name,
        )

        # ----------------------------------------------------
        # PARSE TOOL ARGUMENTS
        # ----------------------------------------------------

        arguments = json.loads(item.arguments)

        employee_id = arguments["employee_id"]

        print(
            "Employee Requested:",
            employee_id,
        )

        # ----------------------------------------------------
        # BACKEND AUTHORIZATION + EXECUTION
        # ----------------------------------------------------

        try:

            result = get_employee_leave_balance(
                current_user=current_user,
                employee_id=employee_id,
            )

            print(
                "Authorization Result:",
                "ALLOWED",
            )

            # ------------------------------------------------
            # Convert tool result to JSON for sending back.
            # ------------------------------------------------

            tool_output = json.dumps(result)

        except PermissionError as ex:

            print(
                "Authorization Result:",
                "DENIED",
            )

            print(
                "Reason:",
                ex,
            )

            # ------------------------------------------------
            # Send controlled tool result instead of exposing
            # protected employee data.
            # ------------------------------------------------

            tool_output = json.dumps({"error": "Not authorized"})

        except ValueError as ex:

            print(
                "Tool Result:",
                "FAILED",
            )

            print(
                "Reason:",
                ex,
            )

            tool_output = json.dumps({"error": str(ex)})

        # ----------------------------------------------------
        # SEND TOOL RESULT BACK TO OPENAI
        # ----------------------------------------------------

        final_response = client.responses.create(
            model="gpt-5.6",
            previous_response_id=response.id,
            input=[
                {
                    "type": "function_call_output",
                    "call_id": item.call_id,
                    "output": tool_output,
                }
            ],
            tools=tools,
        )

        # ----------------------------------------------------
        # PRINT FINAL MODEL RESPONSE
        # ----------------------------------------------------

        print()
        print("Assistant Response:")

        print(final_response.output_text)


# ============================================================
# TEST CASE 1 — NORMAL EMPLOYEE
# ============================================================

# Employee 101 asks for employee 102's data.
#
# Expected:
#
# DENIED

current_user = CurrentUser(
    employee_id=101,
    is_admin=False,
)


run_leave_balance_request(
    current_user=current_user,
    question="""
What is the leave balance for employee 102?
""",
)


# ============================================================
# TEST CASE 2 — ADMIN USER
# ============================================================

# Same user is now acting with administrator permission.
#
# Expected:
#
# ALLOWED

current_user = CurrentUser(
    employee_id=101,
    is_admin=True,
)


run_leave_balance_request(
    current_user=current_user,
    question="""
What is the leave balance for employee 102?
""",
)


# ============================================================
# EXPECTED CONCEPTUAL OUTPUT
# ============================================================

# NORMAL USER:
#
# Current User Employee ID: 101
# Current User Is Admin: False
#
# Tool Requested:
# get_employee_leave_balance
#
# Employee Requested:
# 102
#
# Authorization Result:
# DENIED
#
#
# The model does NOT receive Priya's leave balance.


# ADMIN USER:
#
# Current User Employee ID: 101
# Current User Is Admin: True
#
# Tool Requested:
# get_employee_leave_balance
#
# Employee Requested:
# 102
#
# Authorization Result:
# ALLOWED
#
# Assistant Response:
# Employee 102 has 8 leave days remaining.


# ============================================================
# IMPORTANT SECURITY LESSON
# ============================================================

# OpenAI can request:
#
# get_employee_leave_balance(
#     employee_id=102
# )
#
#
# But OpenAI does NOT determine:
#
# whether current user may access employee 102.
#
#
# Authorization is performed here:
#
# if (
#     employee_id != current_user.employee_id
#     and not current_user.is_admin
# ):
#     raise PermissionError(...)


# ============================================================
# SECURITY FLOW
# ============================================================

# User
#   ↓
# OpenAI interprets intent
#   ↓
# OpenAI requests tool
#   ↓
# Python backend parses arguments
#   ↓
# Backend performs authorization
#
#             ↓
#       ALLOWED / DENIED
#
#       ↙             ↘
#
# execute            reject
#
#   ↓                  ↓
#
# result          controlled error
#
#       ↘             ↙
#
#       OpenAI receives result
#               ↓
#          Final response


# ============================================================
# MOST IMPORTANT TAKEAWAY
# ============================================================

# LLM:
#
# decides which tool might be useful.
#
#
# BACKEND:
#
# decides whether the current user has permission.
#
#
# Therefore:
#
# NEVER TRUST A TOOL CALL AS AUTHORIZATION.
