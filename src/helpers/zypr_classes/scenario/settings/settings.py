import inspect
from datetime import datetime
from typing import Optional
from src.helpers.zypr_classes.scenario.settings.pool import Pool

class Settings:
    def __init__(self, settings):
        self._scenario_name = None          
        self._model_effective_date : Optional[datetime] = None
        self._scenario_create_date : datetime = None
        self._email_results : bool = None 
        self._calendarized_forecast : bool = None
        self._pool = None

        self.deserialize(settings)
    
    
    @property
    def ScenarioName(self) -> str | None:
        return self._scenario_name
    @property
    def ScenarioCreateDate(self) -> datetime | None:
        return self._scenario_create_date
    
    @property
    def ModelEffectiveDate(self) -> Optional[datetime] | None:
        return self._model_effective_date
    
    @property
    def EmailResults(self) -> bool | None:
        return self._email_results
    
    @property
    def CalendarizeForecast(self) -> bool | None:
        return self._calendarized_forecast

    @property
    def Pool(self) -> Pool | None:
        return self._pool

        

    @classmethod
    def deserialize_dict(cls, data: dict):
        # Get the constructor parameters of the dataclass
        params = inspect.signature(cls).parameters
        
        # Filter the object to only include valid parameters
        filtered_data = {k: v for k, v in data.items() if k in params}
        
        # Create an instance of the dataclass using the filtered data
        return cls(**filtered_data)

    def deserialize(self, settings):

        if settings is None:
            return None 

        self._scenario_create_date : datetime = settings["ScenarioCreateDate"] if "ScenarioCreateDate" in settings.keys() else None
        self._email_results : bool = settings["EmailResults"] if "EmailResults" in settings.keys() else None
        self._calendarized_forecast : bool = settings["CalendarizeForecast"] if "CalendarizeForecast" in settings.keys() else None

        #   conditional properties
        if "ScenarioName" in settings: 
            self._scenario_name = settings["ScenarioName"] 
        
        if "ModelEffectiveDate" in settings: 
            self._model_effective_date = settings["ModelEffectiveDate"] 
        

        #   dictionaries summaries
          
        self._pool =  Pool.deserialize_dict(settings["Pool"])
