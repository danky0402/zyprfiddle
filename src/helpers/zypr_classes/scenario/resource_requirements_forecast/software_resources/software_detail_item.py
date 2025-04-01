from typing import Any, Optional 
import inspect
from datetime import datetime
from dataclasses import dataclass

@dataclass
class SoftwareDetailItem:
    LicenseId: int
    LicenseType: str
    LicenseMetric: str
    ContractType: str
    Tag: Optional[Any]
    IntervalNbr: float
    TimeStart: float
    TimeEnd: float
    DateStart: datetime
    DateEnd: datetime
    Required: int
    Available: int
    Excess: int


    @classmethod
    def deserialize_obj(cls, data: object):
        # Get the constructor parameters of the dataclass
        params = inspect.signature(cls).parameters
        
        # Filter the object to only include valid parameters
        filtered_data = {k: v for k, v in data.items() if k in params}
        
        # Create an instance of the dataclass using the filtered data
        return cls(**filtered_data)
    