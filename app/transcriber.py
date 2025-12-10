# app/transcriber.py

import requests
from app.config import HF_TOKEN, HF_ASR_MODEL

ASR_API_URL = f"https://api-inference.huggingface.co/models/{HF_ASR_MODEL}"

headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def transcribe_bytes(audio_bytes: bytes) -> str:
    """Send audio to HF Whisper (hosted)."""
    response = requests.post(ASR_API_URL, headers=headers, data=audio_bytes)

    if response.status_code != 200:
        raise Exception(f"HF ASR Error: {response.text}")

    return response.json().get("text", "")
