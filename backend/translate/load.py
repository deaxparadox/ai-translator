from transformers import pipeline

MODEL_NAME = "Helsinki-NLP/opus-mt-en-hi"

transcriber = pipeline(model=MODEL_NAME)