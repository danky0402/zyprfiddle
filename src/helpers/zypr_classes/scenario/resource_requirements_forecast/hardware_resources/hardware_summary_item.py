import inspect
import datetime
from typing import Optional
from dataclasses import dataclass


@dataclass
class HardwareSummaryItem:
    IntervalNbr: int
    TimeStart: float
    TimeEnd: float
    DateStart: datetime 
    DateEnd: datetime
    DemandStart: int
    DemandDelta: float
    DemandEnd: float
    UtilizationStart: int
    UtilizationEnd: float
    ServerIncQty: int
    ProcessorIncQty: int
    CoreIncQty: int
    PerfInc: int
    ServerQty: int
    ProcessorQty: int
    CoreQty: int
    PerfTotal: int
    ServerPerf: float
    ProcessorPerf: float
    CorePerf: float
    ServerAvgAge: Optional[float]
    ServerAvgRemovalAge: float
    TransactionPercentAdd: float
    TransactionPercentRemove: float
    PerfCaptureRate: float

    @classmethod
    def deserialize_obj(cls, data: object):
        # Get the constructor parameters of the dataclass
        params = inspect.signature(cls).parameters
        
        # Filter the object to only include valid parameters
        filtered_data = {k: v for k, v in data.items() if k in params}
        
        # Create an instance of the dataclass using the filtered data
        return cls(**filtered_data)


    