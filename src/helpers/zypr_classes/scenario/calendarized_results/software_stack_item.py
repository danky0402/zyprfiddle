import inspect
from dataclasses import dataclass

@dataclass
class SoftwareStackItem:
    LicenseId: int
    LicenseType: str
    LicenseMetric: str
    ContractType: str
    RequiredQtyStart: int
    RequiredQtyEnd: int
    AvailableQtyStart: int
    AvailableQtyEnd: int
    ExcessQtyStart: int
    ExcessQtyEnd: int

    @classmethod
    def deserialize_obj(cls, data: object):
        # Get the constructor parameters of the dataclass
        params = inspect.signature(cls).parameters
        
        # Filter the object to only include valid parameters
        filtered_data = {k: v for k, v in data.items() if k in params}
        
        # Create an instance of the dataclass using the filtered data
        return cls(**filtered_data)
