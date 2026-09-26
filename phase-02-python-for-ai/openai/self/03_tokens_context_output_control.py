from openai import OpenAI

client = OpenAI()

# response = client.responses.create(
#     model="gpt-5.6", input="Explain dependency injection simply.", max_output_tokens=16
# )

# print(response.output_text)


response = client.responses.create(
    model="gpt-5.6",
    input="Explain dependency injection",
)

print(response.output_text)

print()
print(response.usage)

print("Input tokens:", response.usage.input_tokens)
print("Output tokens", response.usage.output_tokens)
print("Total tokens", response.usage.total_tokens)
