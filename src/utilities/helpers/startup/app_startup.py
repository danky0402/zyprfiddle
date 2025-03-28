import os
import json

from utilities.helpers.application_settings import ApplicationSettings
from src.utilities.zypr_classes.scenario.scenario import Scenario


class Startup:
    def __init__(self):
        self._app_settings = None
        self._scenario = None

    @property
    def ApplicationSettings(self):
        return self._app_settings
        
    
    @property
    def Scenario(self):
        return self._scenario
    
    def Load(self):
            file_path = os.path.join(str(os.getcwd()), "helpers", "secrets.json")
            if os.path.exists(file_path):
                with open(file_path, 'r') as file:
                    dict = json.load(file)
                   
                self._app_settings = ApplicationSettings(dict['ZyprApiKey'],
                                                 dict['GoogleClientId'],
                                                 dict['GoogleClientSecret'])
               
            else:
                print("Missing secrets.json file")

    # def Deserialize(self):
    #         file_path = os.path.join(str(os.getcwd()), "content", "scenario.json")
    #         if os.path.exists(file_path):
    #             with open(file_path, 'r') as file:
    #                     dict = json.load(file)

    #                     self._scenario = Scenario(dict["Id"],
    #                                               dict["ScenarioStatus"],
    #                                               dict["Progress"],
    #                                               dict["Settings"],
    #                                               dict["ValidationPassed"],
    #                                               dict["ResourceRequirementsForecast"],
    #                                               dict["CalendarizedForecast"],
    #                                               dict["Calendars"],
    #                                               dict["ValidationResults"],
    #                                               dict["NoSolutionGraphs"])
                
    def Deserialize(self):
            file_path = os.path.join(str(os.getcwd()), "content", "scenario.json")
            if os.path.exists(file_path):
                with open(file_path, 'r') as file:
                        dict = json.load(file)
                        print(type(dict))
                        self._scenario = Scenario(dict)                   
            else:
                print("Missing secrets.json file")


startup = Startup()

startup.Deserialize()
print(startup.Scenario.Progress.Started)

print(startup.Scenario.ResourceRequirementsForecast)

print(startup.Scenario.ResourceRequirementsForecast.FinancialStats.TotalCost)
print(startup.Scenario.ResourceRequirementsForecast.SoftwareStats.CoreLicensesUtilization)
print(startup.Scenario.ResourceRequirementsForecast.FacilityStats.RackUnitAvgSlots)

print("Financial Summary entry: " + str(startup.Scenario.ResourceRequirementsForecast.FinancialSummary[0].TotalCumCost))

print("Software Summary entry: " + str(startup.Scenario.ResourceRequirementsForecast.SoftwareSummary[0].DateEnd))
print("Software Detail entry: " + str(startup.Scenario.ResourceRequirementsForecast.SoftwareDetail[0].DateEnd))

print("Facility Summary entry: " + str(startup.Scenario.ResourceRequirementsForecast.FacilitySummary[0].DateEnd))
print("Facility Detail entry: " + str(startup.Scenario.ResourceRequirementsForecast.FacilityDetail[0].DateEnd))

print("Validation Results: " + str(startup.Scenario.ValidationResults[0].InspectedItemName))

print("Settings: " + str(startup.Scenario.Settings.ScenarioName))
print("Settings Pool Id: " + str(startup.Scenario.Settings.Pool.Id))

print("First Calendar Type: " + str(startup.Scenario.Calendars[0].Type))
print("First Calendar - First Schedule Date End: " + str(startup.Scenario.Calendars[0].Schedules[0].DateEnd))

print("Calendarized Forecast - Software Total Cost: " + str(startup.Scenario.CalendarizedForecast.Financial[7].SoftwareTotal))
print("Calendarized Forecast - Stack: " + str(startup.Scenario.CalendarizedForecast.SoftwareInventory[7].Stack[0].LicenseMetric))
print("Calendarized Forecast - Server Qty: " + str(startup.Scenario.CalendarizedForecast.HardwareInventory[7].ServerQtyStart))
print("Calendarized Forecast - Server: " + str(startup.Scenario.CalendarizedForecast.HardwareTransactions[7].ServerQtyAdds))
print("Calendarized Forecast - Facility: " + str(startup.Scenario.CalendarizedForecast.FacilityResources[7].KilowattHrs))

# print("Zypr Api Key: " + startup.ApplicationSettings.ZyprApiKey)
# print("Google Client Id: " + startup.ApplicationSettings.GoogleClientId)
# print("Google Client Secret: " + startup.ApplicationSettings.GoogleClientSecret)
