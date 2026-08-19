# SupaNexus

Unified API access to multiple AI models through one simple endpoint.

SupaNexus helps developers integrate and use multiple AI models with a single API interface.

## Why SupaNexus?

Managing multiple AI providers can be complicated:

- Different API formats
- Multiple authentication systems
- Separate SDK integrations
- Different provider requirements

SupaNexus provides a unified solution:

- One consistent API format
- OpenAI-compatible SDK
- Simple API authentication
- Centralized AI model access


## Supported Models

SupaNexus provides access to multiple AI models through one API.

Currently supported models include:

- Qwen
- DeepSeek
- Kimi
- GLM
- Doubao

More models will be added continuously.


## Quick Start

### 1. Install OpenAI SDK

```bash
pip install openai
```

### 2. Configure API Client

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
            "content": "Hello!"
        }
    ]
)

print(response.choices[0].message.content)
```
