from flat import Flat
from flatmate import Flatmate
from bill import Bill
from report import Report

flatmates = [Flatmate("John", "Doe", 25, "2023-01-15"), Flatmate("Jane", "Smith", 28, "2023-02-20")]

flat = Flat("123 Main St", "Alice Johnson", flatmates[0], flatmates)
flat.contract()

[print(i.full_name()) for i in flat.lessors]

bill = Bill("2025-11",flat,{"rent":1000, "electricity":100, "water":50})
bill.add_expense({"internet":60})

print(bill.equal_split())

flatmates[0].add_leave_days("2025-11-26", "2025-12-10")
print(flatmates[0].full_name(), flatmates[0].leaves)
print(flatmates[0].days_in_flat("2025-12-01","2025-12-31"))
print(bill.days_in_flat_split())

report = Report("flatmates_report.pdf")
report.generate(bill)