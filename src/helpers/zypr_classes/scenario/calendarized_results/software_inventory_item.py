import inspect
from datetime import datetime
from dataclasses import dataclass

from src.helpers.zypr_classes.scenario.calendarized_results.software_stack_item import SoftwareStackItem

@dataclass
class SoftwareInventoryItem:
    def __init__(self, forecast):
        self._report_period: str = forecast["ReportPeriod"]
        self._period_nbr: int = forecast["PeriodNbr"]
        self._report_period_start: datetime = forecast["ReportPeriodStart"]
        self._report_period_end: datetime = forecast["ReportPeriodEnd"]
        self._stack: list[SoftwareStackItem] = self.deserialize_software_stack(forecast["Stack"])

    @property
    def ReportPeriod(self) -> str:
        return self._report_period
    
    @property
    def PeriodNbr(self) -> int:
        return self._period_nbr
    
    @property
    def ReportPeriodStart(self) -> datetime:
        return self._report_period_start

    @property
    def ReportPeriodEnd(self) -> datetime:
        return self._report_period_end

    @property
    def Stack(self) -> list[SoftwareStackItem]:
        return self._stack

    
    def deserialize_software_stack(self, stack):
        lst = []
        if stack != None and len(stack) > 0:
            for x in stack:
                lst.append(SoftwareStackItem.deserialize_obj(x))
        return lst