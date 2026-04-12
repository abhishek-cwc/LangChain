import requests
import os
from dotenv import load_dotenv

load_dotenv()


class GitHubLLM:
    def __init__(self, model="gpt-4o-mini"):
        self.model = model
        self.url = "https://models.github.ai/inference/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {os.getenv('GITHUB_TOKEN')}",
            "Content-Type": "application/json"
        }

    def invoke(self, prompt):
        payload = {
            "model": self.model,
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7
        }

        response = requests.post(self.url, headers=self.headers, json=payload)

        # ❌ error handling
        if response.status_code != 200:
            return f"Error {response.status_code}: {response.text}"

        # 🔥 debug raw response
        print("\n🔥 RAW RESPONSE:\n")
        print(response.json())
        print("\n🔥 END RESPONSE\n")

        # ✅ final output
        return response.json()["choices"][0]["message"]["content"]