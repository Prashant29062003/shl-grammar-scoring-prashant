# Grammar Scoring Engine

**Voice → Text → Grammar Correction → Score**

This project implements an end-to-end AI pipeline that accepts a user’s audio file, converts it into text using an ASR (speech-to-text) model, corrects grammar using an NLP model, and computes grammar score using WER (Word Error Rate). The pipeline is hosted as a FastAPI backend.

---

## 1. Project Structure

```
project/
│
├── app/
│   ├── __init__.py
│   ├── audio.py              # Read audio bytes
│   ├── config.py             # Model configuration (ASR + Grammar)
│   ├── grammar.py            # Grammar correction logic
│   ├── main.py               # FastAPI server
│   ├── scoring.py            # WER + Grammar scoring logic
│   └── transcriber.py        # Speech-to-text processing
│
├── data/
│   ├── kaggle_audio/         # Audio samples from Kaggle dataset
│   └── scored_results.csv    # Output file for batch processing
│
├── scripts/
│   ├── batch_process.py      # Batch scoring multiple audio files
│   └── test_api.py           # Local API testing script
│
├── .env                      # Optional env variables
├── .gitignore
├── PRD.md                    # Product Requirements Document
├── README.md
└── requirements.txt
```

---

## 2. Features

* Upload audio file and receive:

  * Speech-to-text transcription
  * Corrected grammar text
  * Grammar score (0–100)
  * WER value
* Batch process entire Kaggle dataset
* REST API via FastAPI
* Hugging Face Transformer models
* Simple, modular Python architecture

---

## 3. Installation

### Step 1 — Create virtual environment

```bash
python -m venv .venv
```

Activate:

Windows:

```bash
.venv\Scripts\activate
```

Mac/Linux:

```bash
source .venv/bin/activate
```

### Step 2 — Install requirements

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

If Whisper requires PyTorch:

```bash
pip install torch --index-url https://download.pytorch.org/whl/cu121
```

---

## 4. Configure Models

`app/config.py`:

```python
HF_ASR_MODEL = "openai/whisper-small"
HF_GRAMMAR_MODEL = "prithivida/grammar_error_correcter_v1"
MAX_CHARS = 500
```

You may update the ASR model if needed.

---

## 5. Running the API Server

Start FastAPI:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

---

## 6. API Documentation (Swagger)

Available automatically at:

```
http://127.0.0.1:8000/docs
```

---

## 7. Endpoints

### Health Check

```
GET /health
```

Response:

```json
{"status": "ok"}
```

### Grammar Scoring API

```
POST /score/
```

Upload form field:

* `file`: audio file (.wav, .mp3, .m4a, .flac, .ogg)

Sample response:

```json
{
  "filename": "audio.wav",
  "asr_text": "this is a example",
  "corrected_text": "This is an example.",
  "wer": 0.18,
  "grammar_score_0_100": 82
}
```

---

## 8. Test the API

### Using test script

```bash
python scripts/test_api.py
```

### Using curl (Linux/macOS)

```bash
curl -X POST -F "file=@data/kaggle_audio/sample.wav" http://127.0.0.1:8000/score/
```

### PowerShell

```powershell
Invoke-WebRequest -Method POST -InFile "data/kaggle_audio/sample.wav" `
  -Uri "http://127.0.0.1:8000/score/" -ContentType "audio/wav"
```

---

## 9. Batch Processing (Kaggle Dataset)

Run:

```bash
python scripts/batch_process.py
```

Output is saved in:

```
data/scored_results.csv
```

---

## 10. Troubleshooting

### FFmpeg missing

Install FFmpeg:

Windows:

```
choco install ffmpeg
```

Ubuntu:

```
sudo apt install ffmpeg
```

macOS:

```
brew install ffmpeg
```

### Torch not installed

```
pip install torch --index-url https://download.pytorch.org/whl/cu121
```

### Whisper model too slow

Swap to a smaller model:

* `openai/whisper-tiny`
* `openai/whisper-base`
* `distil-whisper/distil-small.en`

---

## 11. Notes

* This project uses free Hugging Face models.
* No API key required.
* Works offline once models are downloaded.

## 📄 **License**

Copyright (c) 2025 Prashant Kumar
