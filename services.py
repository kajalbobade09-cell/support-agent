from google import genai


class AIservice:
    def __init__(self):

     def generate_content(self,prompt):
        response = self.client.models.generate_content(
            model = "gemini-2.5-flash", content=prompt)
        return response.text
        