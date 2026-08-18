# SupaNexus

> A developer-focused AI gateway that simplifies working with multiple LLM providers through one unified API interface.


## Why SupaNexus?

Building AI applications often requires working with multiple model providers.

Each provider comes with different:

- API formats
- Authentication methods
- SDKs
- Pricing systems
- Usage limits

Switching between providers can become a bigger challenge than building the application itself.

SupaNexus provides a unified layer that helps developers manage and interact with multiple AI models through a consistent workflow.


## Features

- Unified API interface
- Multiple LLM provider support
- Simple model switching
- Developer-friendly integration
- Usage tracking and management


## Supported Models

SupaNexus is designed to work with various modern AI models, including:

- GPT models
- Claude models
- Qwen models
- DeepSeek models
- Other LLM providers


## Quick Example

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://api.supanexus.ai/v1"
)

response = client.chat.completions.create(
    model="your-model",
    messages=[
        {
            "role": "user",
            "content": "Hello, SupaNexus!"
        }
    ]
)

print(response.choices[0].message.content)
