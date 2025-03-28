import inspect
from dataclasses import dataclass


@dataclass
class HardwareStats:
    PerfCaptureYield: float
    AvgUtilization: float
    AnnualRemovalPercent: float
    AnnualAddPercent: float
    ServerAvgAge: float
    ServerAvgRemovalAge: float
    ServerAvgQty: float
    ServerMaxQty: int
    ServerMaxQtyTime: int
    ServerAvgPerf: int
    ProcessorAvgQty: float
    ProcessorMaxQty: int
    ProcessorMaxQtyTime: int
    ProcessorAvgPerf: int
    CoreAvgQty: float
    CoreMaxQty: int
    CoreMaxQtyTime: float
    CoreAvgPerf: float

    @classmethod
    def deserialize_from_dict(cls, data: dict):
        # Get the constructor parameters of the dataclass
        params = inspect.signature(cls).parameters
        
        # Filter the dictionary to only include valid parameters
        filtered_data = {k: v for k, v in data.items() if k in params}
        
        # Create an instance of the dataclass using the filtered data
        return cls(**filtered_data)

     