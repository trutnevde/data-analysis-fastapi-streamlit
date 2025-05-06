import pandas as pd
from repositories.data_repository import DataRepository
from schemas.data_schemas import DataSummary


class DataService:
    def __init__(self):
        self.repository = DataRepository()

    async def process_file(self, file) -> DataSummary:
        # Сохраняем файл
        file_path = await self.repository.save_file(file)

        # Читаем данные
        df = pd.read_csv(file_path)

        # Вычисляем статистику
        summary = {
            "columns": df.columns.tolist(),
            "shape": df.shape,
            "summary": df.describe().to_dict()
        }
        return DataSummary(**summary)