import os
from dotenv import load_dotenv
from pathlib import Path


# Load .env from project root
load_dotenv(dotenv_path=Path(__file__).parent.parent / ".env")

HF_TOKEN = os.getenv("HF_TOKEN")

HF_ASR_MODEL = os.getenv("HF_ASR_MODEL")
HF_GRAMMAR_MODEL = os.getenv("HF_GRAMMAR_MODEL")

MAX_CHARS = os.getenv("MAX_CHARS")
