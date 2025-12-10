# 📝 **PRD — Grammar Scoring Engine from Voice Samples**

---

# 1. **Project Overview**

Build a system that:

1. Takes an audio file from the user (voice sample)
2. Converts speech → text (using Whisper or Faster-Whisper)
3. Corrects grammar in the text (using a Transformers-based model)
4. Compares original text and corrected text
5. Computes **Grammar Score**
6. Returns result through a FastAPI backend

This system will give an objective grammar score for spoken English.

---

# 2. **Objectives**

### 🎯 Primary Goals

* Convert spoken audio to text accurately
* Automatically correct grammar
* Generate a numeric score from 0–100 indicating grammar quality
* Provide detailed feedback
* Expose everything through an easy API endpoint

### 🎯 Secondary Goals

* Batch transcriptions for Kaggle dataset
* Standardized CSV-based scoring results
* Deployable on local or cloud

---

# 3. **Key Features**

### **1. Audio Transcription**

* Input: `.wav`, `.mp3` formats
* Model: `faster-whisper` (CPU friendly)
* Output: Raw transcript

### **2. Grammar Correction**

* Input: Transcript
* Model: `transformers` (T5, BART, or GPT-based)
* Output: Grammatically corrected text

### **3. Grammar Scoring**

Using metrics:

* **WER (Word Error Rate)** via `jiwer`
* Grammar mismatch score
* Fluency & correctness estimation (rule-based + model-based)

Output:

* Score (0–100)
* Errors list
* Corrected sentence

### **4. API Layer**

* Framework: FastAPI
* Endpoint: `/score/`
* Input: Upload audio file
* Output (JSON):

```json
{
  "original": "...",
  "corrected": "...",
  "score": 86.4
}
```

### **5. Batch Processing**

* Transcribe entire Kaggle dataset
* Save output in CSV format:

  * file_name
  * original_text
  * corrected_text
  * score

---

# 4. **System Architecture**

```
User → FastAPI → Transcription Engine (Whisper)
                     ↓
             Grammar Correction Model (T5/GPT)
                     ↓
          Grammar Score + Error Breakdown
                     ↓
                   Output JSON
```

---

# 5. **Tech Stack**

### **Backend**

* Python 3.10
* FastAPI
* Uvicorn

### **AI Models**

* Faster-Whisper (speech-to-text)
* HuggingFace Transformers (grammar correction)

### **Libraries**

* librosa / soundfile (audio handling)
* jiwer (scoring)
* PyTorch CPU
* python-multipart (file uploads)

### **Dataset (Kaggle)**

* Voice dataset containing `.wav` files + transcript CSV

---

# 6. **API Endpoints**

### **POST /score/**

Upload an audio file and get grammar score.

### **POST /batch-transcribe/**

Process all audio files in dataset directory.

### **GET /health/**

Health check.

---

# 7. **Scoring Logic**

### Step-by-step:

1. Whisper transcription
2. Grammar correction
3. Compute WER:

   ```
   wer = WER(original_text, corrected_text)
   ```
4. Convert to score:

   ```
   score = max(0, 100 - wer * 100)
   ```

Optional:

* Grammar rule violation penalties
* Filler word detection

---

# 8. **Future Enhancements**

* User dashboard
* Confidence scoring
* Accent detection
* Real-time streaming speech scoring

---

# 9. **Dataset Requirements**

Your dataset **must contain**:

* A CSV file with text transcripts
* A folder with **.wav files**

Example structure:

```
data/
 ├─ raw/
 │     ├─ metadata.csv
 │     ├─ audio/
 │     │     ├─ 001.wav
 │     │     ├─ 002.wav
 │     │     └─ ...
```

