import requests
import json

OLLAMA_API_URL = "http://localhost:11434/api/generate"

def query_ollama(prompt, model="gemma3:4b"):
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_API_URL, json=payload)
    response.raise_for_status()
    data = response.json()
    return data["response"]
