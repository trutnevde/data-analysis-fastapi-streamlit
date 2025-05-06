from typing import List, Dict, Tuple
from pydantic import BaseModel

class DataSummary(BaseModel):
    columns: List[str]
    shape: Tuple[int, int]
    summary: Dict[str, Dict]