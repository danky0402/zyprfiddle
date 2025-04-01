from typing import Optional 

from src.helpers.zypr_classes.search_scenario_summaries.summary_item import SummaryItem


class SearchScenarioSummaries:
    def __init__(self, count:int, summaries:list[dict]):
            self._count = count
            self._summaries = summaries 
        
    @property
    def Count(self) -> int:
        return self._count
    
    @property
    def Summaries(self) -> list[SummaryItem]:
        return self.__get_deserialize_summary_item(self._summaries)
    
    def __get_deserialize_summary_item(self, summaries):
        lst: list[SummaryItem] = []
        for summary in summaries:
                lst.append(SummaryItem.deserialize_obj(summary))
        return lst
        
    