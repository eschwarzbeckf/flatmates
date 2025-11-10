from flatmate import Flatmate
from fpdf import FPDF
from bill import Bill

class Report:
    def __init__(self,filename):
        self.filename = filename
        self.orientation = 'P'
        self.unit = 'mm'
        self.format = 'A4'

    def generate(self,bill:Bill) -> None:
        pdf = FPDF(self.orientation, self.unit, self.format)
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        # Set title
        pdf.cell(w=100, h=20, txt="Flatmates Report")
        pdf.cell(w=150, h=20, txt=f"{bill.period.strftime('%B %Y')}", ln=1)

        pdf.cell(w=100, h=10, txt=f"Expense",border=1)
        pdf.cell(w=50, h=10, txt=f"Amount", ln=1,border=1)
        for expense,value in bill.expenses[bill.period.year][bill.period.month]['expenses'].items():
            pdf.cell(w=100, h=10, txt=f"{expense}",border=1)
            pdf.cell(w=50, h=10, txt=f"$ {value}", ln=1,border=1)
        
        pdf.ln(4)
        pdf.cell(w=100, h=10, txt=f"total", align='R')
        pdf.cell(w=50,h=10, txt=f"$ {bill.total_bill()}")

        pdf.ln(20)
        pdf.cell(w=100, h=10, txt="Suggested Total per Flatmate",ln=2)

        pdf.cell(w=100, h=10, txt=f"Flatmate",border=1)
        pdf.cell(w=50, h=10, txt=f"Amount to Pay", ln=1,border=1)
        split = bill.days_in_flat_split()
        for flatmate, pay in split['flatmates'].items():
            pdf.cell(w=100, h=10, txt=f'{flatmate}',border=1)
            pdf.cell(w=50, h=10, txt=f"$ {pay['amount_to_pay']}", ln=1,border=1)
        pdf.output(self.filename)