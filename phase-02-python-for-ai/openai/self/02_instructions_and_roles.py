from openai import OpenAI

client = OpenAI()

# response = client.responses.create(
#     model="gpt-5.6",
#     instructions="""You are a senior software engineering tutor.
# Explain concepts in simple language.
# Use a maximum of 4 sentences.""",
#     input="Explain dependency injection.",
# )

# print(response.usage)
# print(response.output_text)

response = client.responses.create(
    model="gpt-5.6",
    input=[
        {
            "role": "developer",
            "content": "Explain concepts for experienced developers.",
        },
        {"role": "user", "content": "Explain dependency injection."},
    ],
)

print(response.output_text)
