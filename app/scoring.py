from jiwer import wer

def compute_wer_and_score(original: str, corrected: str):
    error = wer(original, corrected)
    score = max(0, 1 - error) * 100
    return error, round(score, 2)
