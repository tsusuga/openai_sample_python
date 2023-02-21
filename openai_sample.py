import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = "むかしむかし"
model = "davinci-codex"
temperature = 0.5
max_tokens = 100
n = 1

response = openai.Completion.create(
  engine = model,
  prompt = prompt,
  temperature = temperature,
  max_tokens = max_tokens,
  n = n
)

print(response.choices[0].text)