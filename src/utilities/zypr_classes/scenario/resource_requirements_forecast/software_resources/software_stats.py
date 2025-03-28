import inspect
from dataclasses import dataclass

@dataclass
class SoftwareStats:
    ServerLicensesUtilization: float = 0
    ServerAvgExcessLicenses: int = 0
    ServerPeakExcessLicenses: int = 0
    ProcessorLicensesUtilization: float = 0
    ProcessorAvgExcessLicenses: int = 0
    ProcessorPeakExcessLicenses: int = 0
    CoreLicensesUtilization: float = 0
    CoreAvgExcessLicenses: int = 0
    CorePeakExcessLicenses: int = 0
    
    @classmethod
    def deserialize_from_dict(cls, data: dict):
        # Get the constructor parameters of the dataclass
        params = inspect.signature(cls).parameters
        
        # Filter the dictionary to only include valid parameters
        filtered_data = {k: v for k, v in data.items() if k in params}
        
        # Create an instance of the dataclass using the filtered data
        return cls(**filtered_data)

    # def deserialize_object(cls, data):
    #     # Get the constructor parameters of the dataclass
    #     #params = inspect.signature(cls).parameters
        
    #     # Filter the dictionary to only include valid parameters
    #     #filtered_data = {k: v for k, v in data.items() if k in params}
    #     if not inspect.isclass(cls):
    #         raise TypeError("Expected a class")
    
    #     if not isinstance(data, dict):
    #         raise TypeError("Expected a dictionary for data")
       
    #     obj = cls.__new__(cls)

    #     # Create an instance of the dataclass using the filtered data
    #     for key, value in data.items():
    #         if hasattr(obj, key):
    #             setattr(obj, key, value)
        
    #     obj.__init__(**data)
        
    #     return obj #cls(**filtered_data)