from fastapi import FastAPI, UploadFile, File, HTTPException
from services.data_service import DataService
from schemas.data_schemas import DataSummary
import logging
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

# Настройка логирования
logging.basicConfig(filename="logs/app.log", level=logging.INFO)

app = FastAPI()
data_service = DataService()

@app.post("/upload/", response_model=DataSummary)
async def upload_file(file: UploadFile = File(...)):
    try:
        result = await data_service.process_file(file)
        return result
    except Exception as e:
        logging.error(f"Error processing file: {e}")
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/health/")
async def health_check():
    return {"status": "ok"}