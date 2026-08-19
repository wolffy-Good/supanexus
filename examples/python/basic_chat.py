from openai import OpenAI


client = OpenAI(
    api_key="YOUR_SUPANEXUS_API_KEY",
    base_url="https://api.supanexus.ai/v1"
)


response = client.chat.completions.create(
    model="your-model",
    messages=[
        {
            "role": "user",
            "content": "Hello SupaNexus"
        }
    ]
)


print(response.choices[0].message.content)
