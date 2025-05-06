import os
from fastapi import UploadFile

class DataRepository:
    UPLOAD_DIR = "data/"

    async def save_file(self, file: UploadFile) -> str:
        os.makedirs(self.UPLOAD_DIR, exist_ok=True)
        file_path = os.path.join(self.UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)
        return file_path