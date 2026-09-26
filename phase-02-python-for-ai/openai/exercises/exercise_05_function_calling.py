import json

from openai import OpenAI

client = OpenAI()


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


tools = [
    {
        "type": "function",
        "name": "get_order_status",
        "description": "Get the status of an order.",
        "parameters": {
            "type": "object",
            "properties": {
                "order_id": {
                    "type": "integer",
                    "description": "Order ID",
                }
            },
            "required": ["order_id"],
            "additionalProperties": False,
        },
        "strict": True,
    }
]


user_input = "What is the status of order 1002?"


response = client.responses.create(
    model="gpt-5.6",
    input=user_input,
    tools=tools,
)


for item in response.output:

    if item.type == "function_call":

        arguments = json.loads(item.arguments)

        status = get_order_status(arguments["order_id"])

        second_response = client.responses.create(
            model="gpt-5.6",
            previous_response_id=response.id,
            input=[
                {
                    "type": "function_call_output",
                    "call_id": item.call_id,
                    "output": status,
                }
            ],
            tools=tools,
        )

        print(second_response.output_text)
