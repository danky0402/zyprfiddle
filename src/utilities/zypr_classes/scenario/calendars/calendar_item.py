from src.utilities.zypr_classes.scenario.calendars.schedule_item import ScheduleItem

class CalendarItem:
    def __init__(self, calendar):
                self._type  = calendar["Type"]
                self._calendar_basis = calendar["CalendarBasis"]
                self._license_id: int = calendar["LicenseId"]
                self._license_class = calendar["LicenseClass"]
                self._license_metric = calendar["LicenseMetric"]
                self._schedules: list[ScheduleItem] = self.deserialize_schedule(calendar)
    
    @property
    def Type(self) -> str:
        return self._type
    @property
    def CalendarBasis(self) -> str:
        return self._calendar_basis
    
    @property
    def LicenseId(self) -> int:
        return self._license_id
    
    @property
    def LicenseClass(self) -> str:
        return self._license_class
    
    @property
    def LicenseMetric(self) -> str:
        return self._license_metric

    @property
    def Schedules(self) -> list[ScheduleItem]:
        return self._schedules

    def deserialize_schedule(self, calendar):
        lst = []
        for x in calendar["Schedules"]:
            lst.append(ScheduleItem.deserialize_dict(x))
        return lst 

