from transformers import pipeline

MODEL_NAME = "Helsinki-NLP/opus-mt-en-hi"

print("\n\tLoading NLP models")
transcriber = pipeline(model=MODEL_NAME)
print("\tModel Loaded")
print()