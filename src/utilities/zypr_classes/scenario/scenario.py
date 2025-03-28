from typing import Optional
from datetime import datetime

from src.utilities.zypr_classes.scenario.simulation_states_item import SimulationStateItem
from src.utilities.zypr_classes.scenario.progress import Progress
from src.utilities.zypr_classes.scenario.settings.settings import Settings
from src.utilities.zypr_classes.scenario.resource_requirements_forecast.forecast import ResourceRequirementsForecast
from src.utilities.zypr_classes.scenario.calendarized_results.calendarized_forecast import CalendarizedForecast
from src.utilities.zypr_classes.scenario.validation_passed.inspected_item import InspectedItem
from src.utilities.zypr_classes.scenario.calendars.calendar_item import CalendarItem
from src.utilities.zypr_classes.scenario.no_solution_graphs import NoSolutionGraphs
from src.utilities.zypr_classes.scenario.error_item import ErrorItem

class Scenario:
    
    def __init__(self,
                 id: str,
                 timestamp: datetime,
                 userId: str,
                 statusNbr: int,
                 statusDescription: str,
                 progress: Optional[Progress] = None,
                 resourceRequirementsForecast: Optional[ResourceRequirementsForecast] = None,
                 calendarizedForecast: Optional[CalendarizedForecast] = None,
                 calendars: Optional[list[CalendarItem]] = None,
                 simulationStates: Optional[list[SimulationStateItem]] = None,
                 validationPassed : bool = None,
                 validationResults: Optional[list[InspectedItem]] = None,
                 noSolutionGraphs = None,
                 errors : Optional[list[ErrorItem]] = None,      
                 settings: Optional[Settings] = None
                 ):
        
                self._id = id
                self._timestamp = timestamp
                self._user_id = userId
                self._status_nbr = statusNbr
                self._status_description = statusDescription
                self._simulation_states = self.deserialize_simulation_states(simulationStates)
                self._progress = Progress.deserialize_from_dict(progress)
                self._settings : Settings = Settings(settings)
                self._validation_passed = bool(validationPassed)
                self._resource_requirements_forecast : Optional[ResourceRequirementsForecast] = ResourceRequirementsForecast(resourceRequirementsForecast)
                self._calendarized_forecast : Optional[list[CalendarItem]] = CalendarizedForecast(calendarizedForecast) 
                self._calendars : Optional[list[CalendarItem]] = self.deserialize_calendars(calendars)
                self._validation_results : Optional[list[InspectedItem]] = self.deserialize_validation_results(validationResults)                      #   deserialize into a property
                self._no_solution_graphs : Optional[NoSolutionGraphs] = NoSolutionGraphs.deserialize_dict(noSolutionGraphs)
                self._errors : Optional[list[ErrorItem]] = self.deserialize_errors(errors)


    def __init__(self,  *args):
            #print(len(args[0]))    # args returns a tuple
            #print(type(args[0]))
            #print(isinstance(args[0], dict))
            if not isinstance(args[0], dict) or len(args[0]) == 0: return None

            else:
                _dict = args[0]

                self._id = _dict["Id"] if "Id" in _dict.keys() else None 
                
                self._timestamp = _dict["Timestamp"] if "Timestamp" in _dict.keys() else None

                self._status_nbr = _dict["StatusNbr"] if "StatusNbr" in _dict.keys() else None

                self._status_description = _dict["StatusDescription"] if "StatusDescription" in _dict.keys() else None
                
                self._user_id = _dict["UserId"] if "UserId" in _dict.keys() else None
                
                self._simulation_states =  self.deserialize_simulation_states(_dict["SimulationStates"]) if "SimulationStates" in _dict.keys() else None
                
                self._progress = Progress.deserialize_dict(_dict["Progress"]) if "Progress" in _dict.keys() else None 
                
                self._validation_passed = _dict["ValidationPassed"] if "ValidationPassed" in _dict.keys() else None  
                
                self._resource_requirements_forecast : Optional[ResourceRequirementsForecast] = ResourceRequirementsForecast(_dict["ResourceRequirementsForecast"]) if "ResourceRequirementsForecast" in _dict.keys() and _dict["ResourceRequirementsForecast"] is not None else None  
                
                self._calendarized_forecast : Optional[list[CalendarItem]] = CalendarizedForecast(_dict["CalendarizedForecast"]) if "CalendarizedForecast" in _dict.keys() and _dict["CalendarizedForecast"] is not None else None 
                
                self._calendars : Optional[list[CalendarItem]] = self.deserialize_calendars(_dict["Calendars"]) if "Calendars" in _dict.keys() and _dict["Calendars"] is not None else None
                
                self._validation_results : Optional[list[InspectedItem]] = self.deserialize_validation_results(_dict["ValidationResults"]) if "ValidationResults" in _dict.keys() and _dict["ValidationResults"] is not None else None                     
                
                self._settings : Settings = Settings(_dict["Settings"]) if "Settings" in _dict.keys() and _dict["Settings"] is not None else None
                
                self._no_solution_graphs = NoSolutionGraphs.deserialize_dict(_dict["NoSolutionGraphs"]) if "NoSolutionGraphs" in _dict.keys() else None
                
                self._errors = self.deserialize_errors(_dict["Errors"]) if "Errors" in _dict.keys() and _dict["Errors"] is not None  else None

            
    
    @property
    def Id(self) -> str:
        return self._id
    
    @property
    def Timestamp(self) -> datetime:
        return self._id
    
    @property
    def StatusNbr(self) -> int:
        return self._status_nbr
    
    @property
    def StatusDescription(self) -> str:
        return self._status_description
    
    @property
    def UserId(self) -> str:
        return self._user_id
        
    @property
    def SimulationStates(self) -> list[SimulationStateItem] | None:
        return self._simulation_states
    
    @property
    def Progress(self) -> Progress | None:
        return self._progress
    
    @property
    def ValidationPassed(self) -> bool | None:
        return self._validation_passed

    @property
    def ResourceRequirementsForecast(self) -> ResourceRequirementsForecast | None:
        return self._resource_requirements_forecast
    
    @property
    def CalendarizedForecast(self) -> Optional[CalendarizedForecast] | None:
        return self._calendarized_forecast

    @property
    def Calendars(self) -> list[CalendarItem] | None:
        return self._calendars

    @property
    def NoSolutionGraphs(self) -> Optional[NoSolutionGraphs] | None:
        return self._no_solution_graphs 
    
    @property
    def ValidationResults(self) -> list[InspectedItem] | None:
        return self._validation_results 
    
    @property
    def Settings(self) -> Settings | None:
        return self._settings 
    
    @property
    def Errors(self) -> list[ErrorItem] | None :
        return self._errors 
    
    def deserialize_errors(self, errors):
        lst = []
        if errors == None or len(errors) == 0:
            return None
        
        for result in errors:
                lst.append(ErrorItem.deserialize_obj(result))
        return lst
    
    def deserialize_simulation_states(self, simulationStates):
        lst = []
        if simulationStates == None or len(simulationStates) == 0:
            return None
        
        for result in simulationStates:
                lst.append(SimulationStateItem.deserialize_obj(result))
        return lst

    def deserialize_validation_results(self, validationResults):
        lst = []
        if validationResults == None or len(validationResults) == 0:
            return None
        
        for result in validationResults:
            lst.append(InspectedItem.deserialize_obj(result))
        return lst
        
    def deserialize_calendars(self, calendars):
        lst = []
        if calendars == None or len(calendars) == 0:
            return None
        
        for calendar in calendars:
               lst.append(CalendarItem(calendar))
        return lst