import inspect
from datetime import datetime
from dataclasses import dataclass

@dataclass
class FinancialItem:
    ReportPeriod: str
    PeriodNbr: int
    ReportPeriodStart: datetime
    ReportPeriodEnd: datetime
    Server: int
    Assignment: int
    PerpetualLicense: int
    Support: int
    Subscription: float
    SoftwareTotal: int
    Power: float
    Facility: float
    Total: int

    @classmethod
    def deserialize_obj(cls, data: object):
        # Get the constructor parameters of the dataclass
        params = inspect.signature(cls).parameters
        
        # Filter the object to only include valid parameters
        filtered_data = {k: v for k, v in data.items() if k in params}
        
        # Create an instance of the dataclass using the filtered data
        return cls(**filtered_data)
