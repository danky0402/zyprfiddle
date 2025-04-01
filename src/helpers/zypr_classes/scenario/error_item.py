import inspect
from dataclasses import dataclass

@dataclass
class ErrorItem:
    Type: str
    Message: str
    
    @classmethod
    def deserialize_obj(cls, data: dict):
        if data is None or len(data) == 0: return None
       
        # Get the constructor parameters of the dataclass
        params = inspect.signature(cls).parameters
        
        # Filter the object to only include valid parameters
        filtered_data = {k: v for k, v in data.items() if k in params}
        
        # Create an instance of the dataclass using the filtered data
        return cls(**filtered_data)