from datetime import datetime

#   financial
from src.utilities.zypr_classes.scenario.calendarized_results.financial_item import FinancialItem

#   hardware resources
from src.utilities.zypr_classes.scenario.calendarized_results.hardware_inventory_item import HardwareInventoryItem
from src.utilities.zypr_classes.scenario.calendarized_results.hardware_transaction_item import HardwareTransactionItem

#   software resources
from src.utilities.zypr_classes.scenario.calendarized_results.software_inventory_item import SoftwareInventoryItem

#   facility resources
from src.utilities.zypr_classes.scenario.calendarized_results.facility_resource_item import FacilityResourceItem


class CalendarizedForecast:
    def __init__(self, forecast):
            self._timeseries_date_start: datetime = None
            self._timeseries_date_end: datetime = None
            self._financial = [] 
            self._hardware_inventory = []
            self._hardware_transactions = []
            self._software_inventory = []
            self._facility_resources = []

            #   method to load objects
            self.deserialize(forecast)

    
    @property
    def Financial(self) -> list[FinancialItem]:
        return self._financial
    
    @property
    def HardwareInventory(self) -> list[HardwareInventoryItem]:
        return self._hardware_inventory
    
    @property
    def HardwareTransactions(self) -> list[HardwareTransactionItem]:
        return self._hardware_transactions

    @property
    def SoftwareInventory(self) -> list[SoftwareInventoryItem]:
        return self._software_inventory

    @property
    def FacilityResources(self) -> list[FacilityResourceItem]:
        return self._facility_resources
    
    def deserialize(self, forecast):

        if forecast is None:
            return None
        
        self._timeseries_date_start: datetime = forecast["TimeSeriesDateStart"] if "TimeSeriesDateStart" in forecast.keys() else None
        self._timeseries_date_end: datetime = forecast["TimeSeriesDateEnd"] if "TimeSeriesDateStart" in forecast.keys() else None

        if "Financial" not in forecast.keys():
            return None
        
        for x in forecast["Financial"]:
            self._financial.append(FinancialItem.deserialize_obj(x))
        
        if "HardwareInventory" not in forecast.keys():
            return None
        
        for x in forecast["HardwareInventory"]:
            self._hardware_inventory.append(HardwareInventoryItem.deserialize_obj(x))

        if "HardwareTransactions" not in forecast.keys():
            return None
        
        for x in forecast["HardwareTransactions"]:
            self._hardware_transactions.append(HardwareTransactionItem.deserialize_obj(x))    

        if "SoftwareInventory" not in forecast.keys():
            return None
        
        for x in forecast["SoftwareInventory"]:
            self._software_inventory.append(SoftwareInventoryItem(x))  

        if "FacilityResources" not in forecast.keys():
            return None
        
        for x in forecast["FacilityResources"]:
            self._facility_resources.append(FacilityResourceItem.deserialize_obj(x)) 
        