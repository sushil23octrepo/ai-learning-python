from openai import OpenAI
import json

client = OpenAI()

response = client.responses.create(
    model="gpt-5.6",
    input="""
Analyze this support ticket:

"I cannot log in after resetting my password.
I need access urgently."
""",
    text={
        "format": {
            "type": "json_schema",
            "name": "support_ticket_analysis",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {
                    "category": {"type": "string"},
                    "priority": {"type": "string", "enum": ["Low", "Medium", "High"]},
                    "sentiment": {"type": "string"},
                },
                "required": ["category", "priority", "sentiment"],
                "additionalProperties": False,
            },
        }
    },
)

result = json.loads(response.output_text)

print(result)
