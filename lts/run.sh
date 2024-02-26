cd backend/backend
alembic revision --autogenerate
alembic upgrade head
uvicorn app.main:app --reload --port 9000 --host 0.0.0.0