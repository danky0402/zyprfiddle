import inspect
from datetime import datetime
from dataclasses import dataclass

@dataclass
class User:
    FirstName: str
    Email: str
    Role: str
    Organization: str
    ApiExpirationDate: datetime
    DaysRemaining: int
    Created: datetime
    Timestamp: datetime

    @classmethod
    def Deserialize(cls, data: dict):

        if data is None:
            return None

        # Get the constructor parameters of the dataclass
        params = inspect.signature(cls).parameters
        
        # Filter the dictionary to only include valid parameters
        filtered_data = {k: v for k, v in data.items() if k in params}
        
        # Create an instance of the dataclass using the filtered data
        return cls(**filtered_data)