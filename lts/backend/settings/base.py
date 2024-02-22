import pathlib

# Path(__file__).resolve().parent.parent
BASE_DIR = pathlib.Path(__file__).resolve().parent.parent


ALLOWED_HOSTS = [
    "localhost",
    "localhost:8000",
    "localhost:9000",
    "localhost:1000",
    "127.0.0.1",
    "127.0.0.1:8000",
    "127.0.0.1:9000",
    "127.0.0.1:1000",
]


ALLOWED_METHODS = ["*"]
ALLOWED_HEADERS = ["*"]
# transcirber = 