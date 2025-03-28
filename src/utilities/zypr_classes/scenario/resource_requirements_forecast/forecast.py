import json

#   financials
from src.utilities.zypr_classes.scenario.resource_requirements_forecast.financial_resources.financial_stats import FinancialStats
from src.utilities.zypr_classes.scenario.resource_requirements_forecast.financial_resources.financial_summary_item import FinancialSummaryItem 


#   hardware resources
from src.utilities.zypr_classes.scenario.resource_requirements_forecast.hardware_resources.hardware_stats import HardwareStats
from src.utilities.zypr_classes.scenario.resource_requirements_forecast.hardware_resources.hardware_summary_item import HardwareSummaryItem
from src.utilities.zypr_classes.scenario.resource_requirements_forecast.hardware_resources.hardware_detail_item import HardwareDetailItem

#   software resources
from src.utilities.zypr_classes.scenario.resource_requirements_forecast.software_resources.software_stats import SoftwareStats
from src.utilities.zypr_classes.scenario.resource_requirements_forecast.software_resources.software_summary_item import SoftwareSummaryItem
from src.utilities.zypr_classes.scenario.resource_requirements_forecast.software_resources.software_detail_item import SoftwareDetailItem

#   facility resources
from src.utilities.zypr_classes.scenario.resource_requirements_forecast.facility_resources.facility_stats import FacilityStats
from src.utilities.zypr_classes.scenario.resource_requirements_forecast.facility_resources.facility_summary_item import FacilitySummaryItem
from src.utilities.zypr_classes.scenario.resource_requirements_forecast.facility_resources.facility_detail_item import FacilityDetailItem


class ResourceRequirementsForecast:
    def __init__(self, forecast):
            self._financial_stats = None 
            self._financial_summary = []
            self._hardware_stats = None
            self._hardware_summary = []
            self._hardware_detail = []
            self._software_stats = None
            self._software_summary = []
            self._software_detail = []
            self._facility_stats = None
            self._facility_summary = []
            self._facility_detail = []

            #   method to load objects
            self.deserialize(forecast)
            

    @property
    def FinancialStats(self) -> FinancialStats | None:
        return self._financial_stats
    
    @property
    def FinancialSummary(self) -> list[FinancialSummaryItem] | None:
        return self._financial_summary
    
    @property
    def HardwareStats(self) -> HardwareStats | None:
        return self._hardware_stats
    
    @property
    def HardwareSummary(self) -> list[HardwareSummaryItem] | None:
        return self._hardware_summary

    @property
    def HardwareDetail(self) -> list[HardwareDetailItem] | None:
        return self._hardware_detail

    @property
    def SoftwareStats(self) -> SoftwareStats | None:
        return self._software_stats
    
    @property
    def SoftwareSummary(self) -> list[SoftwareSummaryItem] | None:
        return self._software_summary

    @property
    def SoftwareDetail(self) -> list[SoftwareDetailItem] | None:
        return self._software_detail
    
    @property
    def FacilityStats(self) -> FacilityStats | None:
        return self._facility_stats
    
    @property
    def FacilitySummary(self) -> list[FacilitySummaryItem] | None:
        return self._facility_summary

    @property
    def FacilityDetail(self) -> list[FacilityDetailItem] | None:
        return self._facility_detail


#   object deserializations

    def deserialize(self, forecast):
        #   dictionaries summaries 
        if forecast is None:
            return None

        self._financial_stats =  FinancialStats.deserialize_from_dict(forecast["FinancialStats"])
        self._hardware_stats =  HardwareStats.deserialize_from_dict(forecast["HardwareStats"])
        self._software_stats =  SoftwareStats.deserialize_from_dict(forecast["SoftwareStats"])
        self._facility_stats =  FacilityStats.deserialize_from_dict(forecast["FacilityStats"])

        # objects   
         
        if "FinancialSummary" in forecast.keys():  
            for x in forecast["FinancialSummary"]:
                self._financial_summary.append(FinancialSummaryItem.deserialize_obj(x))
        
        if "HardwareSummary" in forecast.keys():
            for x in forecast["HardwareSummary"]:
                self._hardware_summary.append(HardwareSummaryItem.deserialize_obj(x))

        if "HardwareDetail" in forecast.keys():
            for x in forecast["HardwareDetail"]:
                self._hardware_detail.append(HardwareDetailItem.deserialize_obj(x))    

        if "SoftwareSummary" in forecast.keys():
            for x in forecast["SoftwareSummary"]:
                self._software_summary.append(SoftwareSummaryItem.deserialize_obj(x))  

        if "SoftwareDetail" in forecast.keys():
            for x in forecast["SoftwareDetail"]:
                self._software_detail.append(SoftwareDetailItem.deserialize_obj(x))  
            
        if "FacilitySummary" in forecast.keys():
            for x in forecast["FacilitySummary"]:
                self._facility_summary.append(FacilitySummaryItem.deserialize_obj(x))  
        
        if "FacilityDetail" in forecast.keys():
            for x in forecast["FacilityDetail"]:
                self._facility_detail.append(FacilityDetailItem.deserialize_obj(x)) 
            
       
        
        
        