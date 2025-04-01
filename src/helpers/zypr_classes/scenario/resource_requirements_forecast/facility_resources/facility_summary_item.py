import inspect
from datetime import datetime
from dataclasses import dataclass

@dataclass
class FacilitySummaryItem:
    IntervalNbr: int
    TimeStart: float
    TimeEnd: float
    DateStart: datetime
    DateEnd: datetime
    RackUnitSlotQtyInc: int
    RackUnitSlotQtyCum: int
    ComputeCapacityPerRackUnitSlot: int
    KilowattHrsInc: int
    KilowattHrsAnnualized: int
    KilowattHrsAnnualizedPerCapacityUnit: float
    KilowattHrsAnnualizedPerRackUnitSlot: float

    @classmethod
    def deserialize_obj(cls, data: object):
        # Get the constructor parameters of the dataclass
        params = inspect.signature(cls).parameters
        
        # Filter the object to only include valid parameters
        filtered_data = {k: v for k, v in data.items() if k in params}
        
        # Create an instance of the dataclass using the filtered data
        return cls(**filtered_data)