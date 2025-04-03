
from src.helpers.zypr_classes.scenario.scenario import Scenario
from src.helpers.zypr_classes.search_scenario_summaries.scenario_summaries import SearchScenarioSummaries


class Deserialize:
    @staticmethod
    def Scenario(value, *args): 
        return Scenario(value, args)
    
    # def SearchScenarioSummaries(value): 
    #     return SearchScenarioSummaries(value)

    #   add other methods as necessary



