from fastapi import FastAPI, UploadFile, File, HTTPException

from app.transcriber import transcribe_bytes
from app.grammar import correct_grammar
from app.scoring import compute_wer_and_score

app = FastAPI(title="Grammar Scoring Engine (HF Inference)")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/score/")
async def score_endpoint(file: UploadFile = File(...)):
    if not file.filename.lower().endswith((".wav", ".mp3", ".m4a", ".flac", ".ogg")):
        raise HTTPException(status_code=400, detail="Upload an audio file")

    audio_bytes = await file.read()
    if len(audio_bytes) == 0:
        raise HTTPException(status_code=400, detail="Empty file uploaded")

    try:
        text = transcribe_bytes(audio_bytes)
        corrected_text = correct_grammar(text)
        wer_value, score = compute_wer_and_score(text, corrected_text)

        return {
            "filename": file.filename,
            "asr_text": text,
            "corrected_text": corrected_text,
            "wer": round(wer_value, 4),
            "grammar_score_0_100": score
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Processing failed: {e}")
