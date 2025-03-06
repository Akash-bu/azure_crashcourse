
from openai import AzureOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    azure_endpoint = os.getenv("endpoint"),
    api_key = os.getenv("api_key"),
    api_version = "2024-02-01"
)

response = client.chat.completions.create(
    model = "gpt-35-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are an helpful assistant."
        },
        {
            "role": "user",
            "content": "What is the capital of the United States?"
        },
        {
            "role": "assistant",
            "content": "The capital of the United States is Washington, D.C."
        },
        {
            "role":"user",
            "content":"What is the capital of France?"
        }
    ]
)

print(response.choices[0].message.content)
print(response.choices[0].message.role)