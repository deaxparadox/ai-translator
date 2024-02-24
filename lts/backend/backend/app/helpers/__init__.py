from app.settings.local import transcriber


def translate(english: str) -> str:
    return transcriber(english)[0]["translation_text"]