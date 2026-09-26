from openai import OpenAI


class OpenAIService:
    def __init__(self):
        self.client = OpenAI()
        self.model = "gpt-5.6"

    def generate_response(self, prompt):
        response = self.client.responses.create(model=self.model, input=prompt)

        return response.output_text
