import inspect
from datetime import datetime
from dataclasses import dataclass


@dataclass
class HardwareInventoryItem:
    ReportPeriod: str
    PeriodNbr: int
    ReportPeriodStart: datetime
    ReportPeriodEnd: datetime
    ServerQtyStart: int
    ServerQtyEnd: int
    ProcessorQtyStart: int
    ProcessorQtyEnd: int
    CoreQtyStart: int
    CoreQtyEnd: int

    @classmethod
    def deserialize_obj(cls, data: object):
        # Get the constructor parameters of the dataclass
        params = inspect.signature(cls).parameters
        
        # Filter the object to only include valid parameters
        filtered_data = {k: v for k, v in data.items() if k in params}
        
        # Create an instance of the dataclass using the filtered data
        return cls(**filtered_data)