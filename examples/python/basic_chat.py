from openai import OpenAI


client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://api.supanexus.ai/v1"
)


response = client.chat.completions.create(
    model="qwen",
    messages=[
        {
            "role": "user",
            "content": "Hello, introduce yourself."
        }
    ]
)


print(response.choices[0].message.content)
