from flat import Flat
from datetime import datetime
import uuid
from pprint import pprint
import calendar

class Bill:
    """
    Object that contains data about a bill, such as total amount and period.
    """
    def __init__(self,period:str,flat=Flat, recurrent_expenses:dict = {}):
        self.recurrent_expenses = recurrent_expenses
        self.expenses = {}
        self.flat = flat
        self.id = str(uuid.uuid4())
        self.create_monthly_bill()
        self.period = datetime.strptime(period, "%Y-%m")
        self.start_of_period = self.period.replace(day=1)
        self.end_of_period = self.period.replace(day=calendar.monthrange(self.period.year, self.period.month)[1])
    
    def add_update_recurrent_expense(self, expense:dict):
        self.recurrent_expenses.update(expense)

    def get_recurrent_expenses(self):
        return self.recurrent_expenses

    def remove_recurrent_expense(self, expense:dict):
        self.recurrent_expenses.pop(expense)
    
    def create_monthly_bill(self):
        year = datetime.now().year
        month = datetime.now().month
        if year not in self.expenses:
            self.expenses[year] = {}
        if month not in self.expenses[year]:
            self.expenses[year][month] = {
                "metadata":{
                    "created_at": datetime.now(),
                    "updated_at": datetime.now(),
                    "recurrent_expenses_added": False
                },
                "expenses":{}
            }
        # Add recurrent expenses
        self.expenses[year][month]["expenses"].update(self.recurrent_expenses)
        self.expenses[year][month]["metadata"]["recurrent_expenses_added"] = True
    
    def update_expense(self, expense:dict) -> None:
        year = datetime.now().year
        month = datetime.now().month

        if not self.expenses[year]:
            self.create_monthly_bill()
        
        self.expenses[year][month]["expenses"].update(expense)
        self.expenses[year][month]["metadata"]["updated_at"] = datetime.now()
    
    def add_expense(self, expense:dict) -> None:
        """Adds an expense to expenses
        
        Keyword arguments:
        argument -- description
        Return: return_description
        """
        
        year = datetime.now().year
        month = datetime.now().month

        if not self.expenses[year]:
            self.create_monthly_bill()
        
        self.expenses[year][month]["expenses"].update(expense)
        
    def check_if_monthly_bill_exists(self) -> bool:
        year = self.period.year
        month = self.period.month
        if not self.expenses.get(year):
            return False
        if not self.expenses[year].get(month):
            return False
    
    def total_bill(self) -> float:
        year = self.period.year
        month = self.period.month
        try:
            total = float(sum(self.expenses[year][month]["expenses"].values()))
        except KeyError:
            raise Exception("Monthly bill does not exists")
        return total
    
    def equal_split(self) -> float:
        total = self.total_bill()
        num_flatmates = len(self.flat.lessors)
        return total/num_flatmates
    
    def days_in_flat_split(self) -> float:
        year = self.period.year
        month = self.period.month
        total = self.total_bill()
        total_days = 0
        for flatmate in self.flat.lessors:
            total_days += flatmate.days_in_flat(f"{year}-{month:02d}-01", f"{year}-{month:02d}-{calendar.monthrange(year, month)[1]}")
        
        pay_per_flatmate = total/total_days
        res = {
            "total_days": total_days,
            "total_bill": total,
            "rate": pay_per_flatmate,
            "flatmates":{}
            }
        for flatmate in self.flat.lessors:
            res["flatmates"][flatmate.full_name()] = {
                "days_in_flat": flatmate.days_in_flat(f"{year}-{month:02d}-01", f"{year}-{month:02d}-{calendar.monthrange(year, month)[1]}"),
                "amount_to_pay": round(pay_per_flatmate * flatmate.days_in_flat(f"{year}-{month:02d}-01", f"{year}-{month:02d}-{calendar.monthrange(year, month)[1]}"),2)
            }
        
        return res
