import inspect
from typing import Any, Optional
from datetime import datetime
from dataclasses import dataclass


@dataclass
class HardwareDetailItem:
    IntervalNbr: int
    UniqueIdentifier: str
    Tag: Optional[Any]
    TimeStart: float
    TimeEnd: float
    DateStart: datetime
    DateEnd: datetime
    SourceIntervalNbr: int
    ServerQty: int
    ProcessorQty: int
    CoreQty: int
    PerfTotal: int
    ServerPerf: int
    ProcessorPerf: int
    CorePerf: float
    ProcessorSetSize: int
    CoreSetSize: int
    ServerSize: int
    WattsRating: int
    TotalKilowattHrs: int
    TransactionResidualValue: int

    @classmethod
    def deserialize_obj(cls, data: object):
        # Get the constructor parameters of the dataclass
        params = inspect.signature(cls).parameters
        
        # Filter the object to only include valid parameters
        filtered_data = {k: v for k, v in data.items() if k in params}
        
        # Create an instance of the dataclass using the filtered data
        return cls(**filtered_data)