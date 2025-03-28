
from typing import Optional
import inspect
from dataclasses import dataclass

@dataclass
class Progress:
    Started: Optional[bool]
    Completed: Optional[bool]
    PercentComplete: Optional[int]
    TransactionCount: Optional[int]
    SequenceCount: Optional[int]

    @classmethod
    def deserialize_dict(cls, data: dict):

        if data is None:
            return None

        # Get the constructor parameters of the dataclass
        params = inspect.signature(cls).parameters
        
        # Filter the dictionary to only include valid parameters
        filtered_data = {k: v for k, v in data.items() if k in params}
        
        # Create an instance of the dataclass using the filtered data
        return cls(**filtered_data)

   