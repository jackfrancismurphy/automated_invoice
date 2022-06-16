from tkinter.font import ITALIC
from fpdf import FPDF
from datetime import date

#variables

total = 0
total_dates = 0
date_count = 0

written_dates = []
total_hours = []
all_dates_written = "no"
subject = input("Which subject taught?")
rate = int(input("What was the rate?"))
#new variables

#external data variable

def get_var_value(filename="invoice_number.txt"):
    with open(filename, "a+") as f:
        f.seek(0)
        val = int(f.read() or 0) + 1
        f.seek(0)
        f.truncate()
        f.write(str(val))
        return val

invoice_num = get_var_value()

date = date.today() 

# create FPDF object
# Layout ('P','L')
# Unit ('mm', 'cm', 'in')
# format ('A3', 'A4' (default), 'A5', 'Letter', 'Legal', (100,150))
pdf = FPDF('P', 'mm', 'A4')

# Add a page
pdf.add_page()

# specify font
# fonts ('times', 'courier', 'helvetica', 'symbol', 'zpfdingbats')
# 'B' (bold), 'U' (underline), 'I' (italics), '' (regular), combination (i.e., ('BU'))
# font size
pdf.set_font('times', '', 16)
pdf.set_text_color(0,0,0)
# Add text
# w = width
# h = height
# txt = your text
# ln (0 False; 1 True - move cursor down to next line)
# border (0 False; 1 True - add border around cell)


pdf.cell(140, 10, f'Invoice {invoice_num}')
pdf.cell(40, 10, f'Date: {date}', ln=True)
pdf.set_font('times', 'I', 16)
pdf.cell(0, 10, f'Invoice generated using Python 3', ln=True, align ='L')
pdf.set_font('times', '', 16)
pdf.cell(0, 90, '', ln=True, border=0)

pdf.cell(0, 10, f'{subject} tuition.', ln=True, align ='C', border= 1)
while all_dates_written == "no":
    tute_date = input("Which dates? (e.g 27th March)")
    tute_hours = input("How many hours?")
    total_hours.append(int(tute_hours))
    pdf.cell(0, 10, f'{tute_date}      {tute_hours} hours tuition.', ln=True, align ='C')
    all_dates_written = input("all dates written? (yes/no)")



pdf.cell(0, 10, f'{sum(total_hours)} hours total', ln=True, align ='C')

total = float(sum(total_hours)*rate) 

# calculation


pdf.cell(0, 20, '', ln=True, border=0)
pdf.cell(0, 10, f'Total = £{total}', ln=True, align ='R')
pdf.cell(0, 10, '', ln=True, border=0)
pdf.cell(0, 10, 'Payable to:', ln=True, align ='R')
pdf.cell(0, 10, 'Jack Murphy', ln=True, align ='R')
pdf.cell(0, 10, '07 08 06', ln=True, align ='R')
pdf.cell(0, 10, '21469405', ln=True, align ='R')
pdf.cell(0, 10, 'Nationwide', ln=True, align ='R')

#f'{invoice_num} NTE invoice.pdf'
pdf.output(f"C:\\Users\\lilma\\OneDrive\\old Documents\\Bureaucratic\\Invoices\\invoice {invoice_num} JM.pdf")


#check invoice number 