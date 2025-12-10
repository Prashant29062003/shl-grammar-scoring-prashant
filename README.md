# **Grammar Scoring Engine (HF Inference)**

A FastAPI-based backend that performs:
✔ Automatic Speech Recognition (ASR) using **Whisper**
✔ Grammar correction using **Grammar Error Corrector v1**
✔ Grammar scoring using **WER (Word Error Rate)**
✔ Returns corrected text + score out of 100
✔ Fully local HuggingFace inference

---

## 🚀 **Features**

* Upload an audio file (WAV, MP3, M4A, FLAC, OGG)
* Convert audio → text using Whisper (`openai/whisper-small`)
* Correct the transcription using grammar correction (`prithivida/grammar_error_correcter_v1`)
* Compute WER between ASR text and corrected text
* Produce a final grammar score (0–100)
* Debug endpoint included to validate environment + NumPy availability

---

## 🧩 **Project Structure**

```
shl-grammar-scoring/
│
├── app/
│   ├── main.py
│   ├── audio.py
│   ├── config.py
│   ├── transcriber.py
│   ├── grammar.py
│   ├── scoring.py
│   └── __init__.py
│
├── scripts/
│   └── test_api.py
│
└── README.md
```

---

## 🔧 **Installation**

### 1️⃣ Create virtual environment

```sh
python -m venv .venv
```

### 2️⃣ Activate environment

**Windows**

```sh
.venv\Scripts\activate
```

### 3️⃣ Install dependencies

```sh
pip install -r requirements.txt
```

### 4️⃣ Ensure NumPy is installed correctly

(Important for Whisper)

```sh
pip install --upgrade --force-reinstall numpy --only-binary=:all:
```

---

## ▶️ **Run FastAPI Server**

```sh
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Server starts at:

```
http://127.0.0.1:8000
```

Interactive API docs:

```
http://127.0.0.1:8000/docs
```

---

## 🧪 **Test API (Python script)**

Example request:

```sh
python scripts/test_api.py
```

---

## 🛠 **API Endpoints**

### **1. Health Check**

```
GET /health
```

Response:

```json
{ "status": "ok" }
```

---

### **2. Debug Environment**

(Checks Python path + NumPy availability)

```
GET /debug
```

Example response:

```json
{
  "python": "D:\\shl-grammar-scoring\\.venv\\Scripts\\python.exe",
  "numpy_version": "2.2.6",
  "numpy_available": true
}
```

---

### **3. Score API (Main Feature)**

```
POST /score/
```

#### **Request:**

Upload audio file (`wav/mp3/m4a/ogg/flac`).

#### **Response:**

```json
{
  "filename": "input.wav",
  "asr_text": "I am speaking something",
  "corrected_text": "I am saying something.",
  "wer": 0.14,
  "grammar_score_0_100": 86
}
```

---

## 🧠 **How It Works Internally**

### **1. ASR (Audio → Text)**

```python
asr_pipeline = pipeline("automatic-speech-recognition", model=HF_ASR_MODEL)
```

### **2. Grammar Correction**

```python
corrected = grammar_pipeline(text)[0]['generated_text']
```

### **3. Grammar Score**

WER is computed:

```
score = (1 - wer) * 100
```

---

## ❗ Common Issues

### **Issue: "Numpy is not available"**

Fix:

```sh
pip install --upgrade --force-reinstall numpy --only-binary=:all:
```

Check environment:

```sh
curl http://127.0.0.1:8000/debug
```

### **Whisper model slow or crashing?**

Install PyTorch with CUDA (if GPU available).

---

## 📄 **License**

Copyright (c) 2025 Prashant Kumar
