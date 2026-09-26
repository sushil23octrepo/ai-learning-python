from openai import OpenAI

client = OpenAI()

prompt = """
Explain Dependency injection in simple language
 Use a maximum of 2 sentences
"""

response = client.responses.create(model="gpt-5.6", input=prompt)


print()
print(response.output_text)
