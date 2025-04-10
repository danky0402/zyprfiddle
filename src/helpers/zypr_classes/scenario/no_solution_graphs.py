import inspect
from dataclasses import dataclass

@dataclass
class NoSolutionGraphs:
    FailedGraphNbr: int
    EdgeNbr: int
    NodeY: int
    NodeX: int
    Message: str
    AtRelativeTargetTime: float
    AtAbsoluteTargetTime: float
    LowestConstraintMetricVarianceRate: float
   

    @classmethod
    def deserialize_dict(cls, data: dict):
        if data is None or len(data) == 0: return None
       
        
        # Get the constructor parameters of the dataclass
        params = inspect.signature(cls).parameters
        
        # Filter the dictionary to only include valid parameters
        filtered_data = {k: v for k, v in data.items() if k in params}
        
        # Create an instance of the dataclass using the filtered data
        return cls(**filtered_data)