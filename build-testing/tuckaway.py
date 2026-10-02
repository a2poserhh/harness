from openai import OpenAI

client = OpenAI()

prompt = input("Enter a test prompt: ")


def call_model(prompt):
response = client.responses.create(
    model="gpt-5.6-sol",
    instructions="You are a helpful assistant.",
    input=prompt,
)

print(response.output_text)