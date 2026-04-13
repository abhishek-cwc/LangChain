import requests
import os
from dotenv import load_dotenv

load_dotenv()


class GitHubLLM:
    def __init__(self, model="gpt-4o-mini", temperature=0.7, max_completion_tokens=50):
        self.model = model
        self.temperature = temperature
        self.max_completion_tokens = max_completion_tokens
        self.url = "https://models.github.ai/inference/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {os.getenv('GITHUB_TOKEN')}",
            "Content-Type": "application/json"
        }

    
    def invoke_llm_with_meesage(self, messages):
        role_map = {
            "SystemMessage": "system",
            "HumanMessage": "user",
            "AIMessage": "assistant"
        }

        formatted_messages = []

        for msg in messages:
            role = role_map.get(msg.__class__.__name__)
            if role:
                formatted_messages.append({
                    "role": role,
                    "content": msg.content
                })

        payload = {
            "model": self.model,
            "messages": formatted_messages,
            "temperature": self.temperature,
            "max_completion_tokens": self.max_completion_tokens
        }

        print("\n✅ FINAL PAYLOAD:\n", payload)  # debug

        response = requests.post(self.url, headers=self.headers, json=payload)

        if response.status_code != 200:
            return f"Error {response.status_code}: {response.text}"

        return response.json()["choices"][0]["message"]["content"]

    def invoke(self, prompt):
        payload = {
            "model": self.model,
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "temperature": self.temperature,
            "max_completion_tokens": self.max_completion_tokens
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