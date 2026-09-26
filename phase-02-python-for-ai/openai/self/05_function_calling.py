from openai import OpenAI
import json

client = OpenAI()


def get_employee_leave_balance(employee_id):
    leave_data = {
        101: 12,
        102: 7,
        103: 18,
    }

    return leave_data.get(
        employee_id,
        "Employee not found",
    )


tools = [
    {
        "type": "function",
        "name": "get_employee_leave_balance",
        "description": "Get the remaining leave balance for an employee.",
        "parameters": {
            "type": "object",
            "properties": {
                "employee_id": {"type": "integer", "description": "Employee Id"}
            },
            "required": ["employee_id"],
            "additionalProperties": False,
        },
        "strict": True,
    }
]

user_input = "How many leave days does employee 101 have?"

response = client.responses.create(
    model="gpt-5.6",
    input=user_input,
    tools=tools,
)

for item in response.output:
    if item.type == "function_call":
        arguments = json.loads(item.arguments)
        result = get_employee_leave_balance(arguments["employee_id"])

        second_response = client.responses.create(
            model="gpt-5.6",
            previous_response_id=response.id,
            input=[
                {
                    "type": "function_call_output",
                    "call_id": item.call_id,
                    "output": str(result),
                }
            ],
            tools=tools,
        )
        print(second_response.output_text)
