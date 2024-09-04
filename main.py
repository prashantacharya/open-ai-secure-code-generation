import os
import json
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

client = OpenAI()

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content

def get_first_completed_prompt():
    with open('prompts.json', 'r') as f:
        data = json.load(f)

        first_prompt_obj = data[0]

        return first_prompt_obj["NL Prompt"].replace("<language>", first_prompt_obj["Language"])


prompt = get_first_completed_prompt()
response = get_completion(prompt)
print(response)
