import json
from time import perf_counter
from xmlrpc import client
from openai import OpenAI
import os

client = OpenAI()

prompt = input("Enter a test prompt: ")

def call_model(prompt):
    
    client = OpenAI()
    api_key=os.environ.get("OPENAI_API_KEY")

    response = client.responses.create(
        model="gpt-5.6-sol",
        instructions="You are a helpful assistant.",
        input=prompt,
)
    return response

def run_experiment(prompt):

    start = perf_counter()

    response = call_model(prompt)

    elapsed = perf_counter() - start

    return {
        "model": "fake",
        "prompt": prompt,
        "response": response,
        "elapsed_seconds": elapsed,
    }


def main():
    
    prompt = input("Enter a test prompt: ")

    result = run_experiment(prompt)

    print("\nResponse:", result["response"])

    with open("results.jsonl", "a", encoding="utf-8") as file:
        file.write(json.dumps(result) + "\n")


if __name__ == "__main__":
    main()