# Project Overview: Using OpenRouter, LiteLLM, and Agents

This project demonstrates how to use **OpenRouter**, **LiteLLM**, and AI **Agents** in a Python environment.

---

## What is OpenRouter?

OpenRouter is a service that acts as a **middleman** between your application and multiple AI language model providers (like OpenAI, Anthropic, etc.).  
- It manages your API keys centrally.  
- It routes your requests to different AI backends based on availability and configuration.  
- This means you can switch AI providers easily without changing your code.  
- OpenRouter simplifies managing multiple AI APIs with a single unified interface.

---

## What is LiteLLM?

LiteLLM is a **lightweight Python library** that makes it easy to send text prompts and get responses from AI models.  
- It handles the communication details with AI providers or OpenRouter.  
- You only need to call simple Python functions to generate text, translate, summarize, or any other AI tasks.  
- LiteLLM supports multiple AI backends through OpenRouter or direct connections.

---

## What are Agents?

Agents are **small, specialized components** that perform specific AI tasks.  
- For example, one agent can translate text, another can summarize it.  
- Each agent is responsible for one task and can be used independently or combined.  
- Agents help organize complex AI workflows by dividing tasks into manageable parts.

---

## Setting Up Your Environment

### Activation Command

- On **Windows (PowerShell):**

```bash
.venv\Scripts\activate
```
- On **Linux/macOS:**

```bash
source .venv/bin/activate
```

---

## All Packages Installation Command

```
pip install google-generative-ai requests litellm openrouter uvicorn fastapi
```

---

## Summary of Installed Packages

**litellm**: Python client for easy interaction with AI language models

**Google Generative Ai**: Google’s generative AI client 

**openrouter**: Service to manage and route API requests to different AI providers

**requests**: HTTP client library for Python (if required)

---

**Build with ❤ by [Faria Mustaqim](https://github.com/Zaibunis)**



