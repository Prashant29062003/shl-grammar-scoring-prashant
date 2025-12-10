# app/grammar.py
import requests
from app.config import HF_TOKEN, HF_GRAMMAR_MODEL

GRAMMAR_API_URL = f"https://api-inference.huggingface.co/models/{HF_GRAMMAR_MODEL}"

headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def correct_grammar(text: str) -> str:
    payload = {"inputs": text}
    response = requests.post(GRAMMAR_API_URL, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(f"HF Grammar Error: {response.text}")

    return response.json()[0]["generated_text"]
