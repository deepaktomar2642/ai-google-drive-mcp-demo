import openai
import os


openai.api_key = os.getenv("OPENAI_API_KEY")


def summarize_text(text):
response = openai.ChatCompletion.create(
model="gpt-4",
messages=[{"role": "user", "content": f"Summarize this text:\n{text}"}]
)
return response.choices[0].message.content


def generate_file(prompt):
response = openai.ChatCompletion.create(
model="gpt-4",
messages=[{"role": "user", "content": prompt}]
)
return response.choices[0].message.content


def rewrite_text(text, instruction):
response = openai.ChatCompletion.create(
model="gpt-4",
messages=[{"role": "user", "content": f"{instruction}:\n{text}"}]
)
return response.choices[0].message.content
