import os
from flask import current_app
from openai import OpenAI

client = OpenAI(
    base_url=current_app.config['OPENAI_BASE_URL'],
    api_key=current_app.config['OPENAI_API_KEY'],
)

response = client.chat.completions.create(
    model="deepseek/deepseek-r1",
     messages=[
                {
                    "role": "system",
                    "content": "You are an AI assistant who knows everything, designed to solve practical cases for the development of soft skills related to different contexts and professional areas.",
                },
                {
                    "role": "user",
                    "content": f"Propose some of the possible alternatives in which I might be exposed in a real practical scenario, including responses and questions, given the conditions provided in the data: El participante deberá utilizar técnicas de negociación y métodos de resolución de conflictos para mediar entre los departamentos de finanzas y ventas, asegurando una asignación justa de recursos y presupuestos.",
                },
            ],
)

message = response.choices[0].message.content

print(f"Assistant: {message}")