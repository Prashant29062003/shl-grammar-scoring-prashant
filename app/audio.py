import os

def read_audio_file(path: str) -> bytes:
    """Read audio file as bytes for API submission."""
    with open(path, "rb") as f:
        return f.read()
