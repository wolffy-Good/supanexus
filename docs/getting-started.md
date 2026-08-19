# Getting Started

SupaNexus provides a unified API interface for accessing multiple AI models through a single endpoint.

## Overview

Instead of managing multiple AI providers separately, developers can use one consistent API format to access different LLM providers.

SupaNexus helps developers simplify AI integration by providing:

- Unified API format
- Simple authentication
- OpenAI-compatible SDK support
- Centralized model access

## Authentication

Create an API key from your SupaNexus dashboard.

All API requests require authentication using your API key.

## API Configuration

### Base URL

```text
https://api.supanexus.ai/v1
```

### Authorization

Include your API key in the request header:

```md
```http
Authorization: Bearer YOUR_API_KEY
```

## OpenAI SDK Compatibility

SupaNexus is compatible with the OpenAI API format.

You can use existing OpenAI SDK libraries with minimal changes.

Example:

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
