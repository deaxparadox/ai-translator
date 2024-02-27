import pathlib

# Path(__file__).resolve().parent.parent
BASE_DIR = pathlib.Path(__file__).resolve().parent.parent


ALLOWED_HOSTS = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:9000",
    "http://localhost:10000",
    "http://127.0.0.1",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:9000",
    "http://127.0.0.1:10000",
    # "https://www.freecodecamp.org"
]

# ALLOWED_HOSTS = ["*"]


ALLOWED_METHODS = ["*"]
ALLOWED_HEADERS = ["*"]
# transcirber = 