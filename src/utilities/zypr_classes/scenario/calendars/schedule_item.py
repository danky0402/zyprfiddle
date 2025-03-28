import inspect
from typing import Optional
from datetime import datetime
from dataclasses import dataclass

@dataclass
class ScheduleItem:
    Type: str
    TimeStart: float
    TimeEnd: float
    Duration: float
    DateStart: datetime
    DateEnd: datetime
    AlsoAnnualTrueUp: Optional[bool] = False
    
    @classmethod
    def deserialize_dict(cls, data: dict):
        # Get the constructor parameters of the dataclass
        params = inspect.signature(cls).parameters

        # Filter the object to only include valid parameters
        filtered_data = {k: v for k, v in data.items() if k in params}

        # Create an instance of the dataclass using the filtered data
        return cls(**filtered_data)
    
    