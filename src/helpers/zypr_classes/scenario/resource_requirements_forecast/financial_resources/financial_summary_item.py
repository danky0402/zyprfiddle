import inspect
from dataclasses import dataclass
from datetime import datetime

@dataclass
class FinancialSummaryItem:
    IntervalNbr: int
    TimeStart: float
    TimeEnd: float
    DateStart: datetime
    DateEnd: datetime
    ServerIncCost: int
    AssignmentIncCost: int
    PerpetualLicenseIncCost: int
    SupportIncCost: int
    SubscriptionIncCost: int
    PowerIncCost: int
    FacilityIncCost: int
    TotalIncCost: int
    ServerCumCost: int
    AssignmentCumCost: int
    PerpetualLicenseCumCost: int
    SupportCumCost: int
    SubscriptionCumCost: int
    PowerCumCost: int
    FacilityCumCost: int
    TotalCumCost: int
    TotalCostPerPerf: float
    AnnualizedTotalCost: int
    AnnualizedTotalCostPerPerf: float
    Kratio: float | None


    @classmethod
    def deserialize_obj(cls, data: object):
        # Get the constructor parameters of the dataclass
        params = inspect.signature(cls).parameters

        # Filter the object to only include valid parameters
        filtered_data = {k: v for k, v in data.items() if k in params}

        # Create an instance of the dataclass using the filtered data
        return cls(**filtered_data)
    