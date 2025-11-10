import uuid
from datetime import datetime
from dateutil.relativedelta import relativedelta
import calendar

class Flatmate:
    """
    Object that contains data about a flatmate, like name, last name, age, and start date
    """
    def __init__(self, name, last_name, age, start_date):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.start_date = start_date
        self.id = str(uuid.uuid4())
        self.leaves = {}
    
    def full_name(self):
        return f"{self.name} {self.last_name}"

    def days_in_flat(self, start_date:str, end_date:str) -> float:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        leave_days = self.leaves.get(end.year, {}).get(end.month, 0)
        if leave_days == 0:
            return float((end-start).days)
        return float((end - start).days - leave_days.days)
    
    def add_leave_days(self, start_leave:str, end_leave:str) -> None:
        # Sets leave and return date
        leave_date = datetime.strptime(start_leave, "%Y-%m-%d")
        return_date = datetime.strptime(end_leave, "%Y-%m-%d")
        
        # Calculate the number of days of leave for each month
        current_date = leave_date
        while current_date <= return_date:
            month = current_date.month
            year = current_date.year
            _, eom_day = calendar.monthrange(year, month)
            eom = datetime(year, month, eom_day)
            if eom > return_date:
                last_day = return_date
            else:
                last_day = eom
            # Calculate the last day of the current month
            delta = last_day - current_date
            if year not in self.leaves:
                self.leaves[year] = {}
            self.leaves[year].update({
                    month: delta
                })
            current_date = last_day + relativedelta(days=1)

            

        
