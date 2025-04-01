import inspect
from datetime import datetime
from dataclasses import dataclass

@dataclass
class SoftwareSummaryItem:
    IntervalNbr: int
    TimeStart: float
    TimeEnd: float
    DateStart: datetime
    DateEnd: datetime
    ServerStackQty: int = None 
    ServerRequiredQty: int = None
    ServerAvailableQty: int = None
    ServerUtilization: float = None
    ProcessorStackQty: int = None
    ProcessorRequiredQty: int = None
    ProcessorAvailableQty: int = None
    ProcessorUtilization: float = None
    CoreStackQty: int = None
    CoreRequiredQty: int = None
    CoreAvailableQty: int = None
    CoreUtilization: float = None
    

    @classmethod
    def deserialize_obj(cls, data: object):

        # Get the constructor parameters of the dataclass
        params = inspect.signature(cls).parameters
        
        # Filter the object to only include valid parameters
        filtered_data = {k: v for k, v in data.items() if k in params}
        
        # Create an instance of the dataclass using the filtered data
        return cls(**filtered_data)