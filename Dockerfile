# Backend
FROM python:3.10-slim as backend
WORKDIR /app/backend
COPY backend/requirements.txt .
RUN pip install -r requirements.txt
COPY backend/ .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# Frontend
FROM python:3.10-slim as frontend
WORKDIR /app/frontend
COPY frontend/requirements.txt .
RUN pip install -r requirements.txt
COPY frontend/ .
CMD ["streamlit", "run", "app.py", "--server.port", "8501", "--server.address", "0.0.0.0"]