from dotenv import load_dotenv
import openai
import os

load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_KEY")
openai.api_key = OPENAI_KEY
initial_prompt = [{"role": "user", "content": "Pretend you are my sweet girlfriend and you always speak in english."}]
messages = initial_prompt.copy()

response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
response_text = response["choices"][0]["message"]["content"]
print(response_text)

messages.append({"role": "assistant", "content": response_text})

def contact_the_eldritch_god(prompt):
    messages.append({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=messages)
    response_text = response["choices"][0]["message"]["content"]
    print(response_text)
    messages.append({"role": "assistant", "content": response_text})
    return response_text

def reset_prompts():
    messages = initial_prompt.copy()


