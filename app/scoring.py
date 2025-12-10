from jiwer import wer

def compute_wer_and_score(original: str, corrected: str):
    error = wer(original, corrected)
    score = max(0, 1 - error)
    return error, round(score * 100, 2)
