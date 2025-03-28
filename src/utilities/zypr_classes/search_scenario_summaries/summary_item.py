from typing import Optional 
from datetime import datetime
from dataclasses import dataclass
import inspect

@dataclass
class SummaryItem:
    Id:str
    StatusNbr:int
    StatusDescription:str
    ScenarioName:Optional[str]
    PoolName:Optional[str] 
    PoolId:Optional[str]
    ModelEffectiveDate: datetime
    CreatedDate:datetime

    @classmethod
    def deserialize_obj(cls, data: object):
        # Get the constructor parameters of the dataclass
        params = inspect.signature(cls).parameters
        
        # Filter the object to only include valid parameters
        filtered_data = {k: v for k, v in data.items() if k in params}
        
        # Create an instance of the dataclass using the filtered data
        return cls(**filtered_data)