from openai import OpenAI

client = OpenAI()
prompt = input("Enter a test prompt: ")

def call_model(prompt):
    response = client.responses.create(
        model=""
    )