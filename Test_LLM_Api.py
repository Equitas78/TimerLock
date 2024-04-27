# Example: reuse your existing OpenAI setup
from openai import OpenAI
import time


def riddle(tries):
  
  for i in range(tries-1):
    print(f"Attempt {i}:")
  # Point to the local server
    client = OpenAI(base_url="http://localhost:11434/v1", api_key="lm-studio")

    completion = client.chat.completions.create(
      messages=[
        {"role": "system", "content": "Start from scratch. Provide me with a riddle solvable by an 11 year old. Do not provie the answer."}
        ], 
      model="TheBloke/Mistral-7B-Instruct-v0.1-GGUF/mistral-7b-instruct-v0.1.Q2_K.gguf",
      max_tokens=1000,
      temperature=0.7
    )
    time.sleep(10)

    response = completion.choices[0].message
    print(f"Riddle: {response}")

    user_input = input("Enter your response: ")

    response_prompt = [{"role": "user", "content": user_input + ". Answer if correct with yes or no."}]

    Response_Completion = client.chat.completions.create(
      messages=response_prompt, 
      model="TheBloke/Mistral-7B-Instruct-v0.1-GGUF/mistral-7b-instruct-v0.1.Q2_K.gguf",
      max_tokens=100,
      temperature=0.7
    )

    time.sleep(5)

    result = Response_Completion.choices[0].message
    print(f"Result: {result}")
    if result == "yes":
      break

riddle(2)