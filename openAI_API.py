import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.aimlapi.com/v1",
    api_key="359251ce1dd64b5d9fb54d0c2069dce2",    
)

response = client.chat.completions.create(
    model="deepseek/deepseek-r1",
    messages=[
        {
            "role": "system",
            "content": "You are an AI assistant who knows everything.",
        },
        {
            "role": "user",
            "content": "Tell me, why is the sky blue? in Spanish",
        },
    ],
)

message = response.choices[0].message.content

print(f"Assistant: {message}")