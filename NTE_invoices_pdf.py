from fpdf import FPDF
from datetime import date

#variables

total = 0
total_dates = 0
date_count = 0
cost = 26.73
GS_bonus = 5 
YM_bonus = 11
SCM_bonus = 8
BP_bonus = 7
date = date.today() 

GS_dates = input("Which dates for George Street?") 
YM_dates = input("Which dates for Yorke Mead?") 
SCM_dates = input("Which dates for St Cuthbert Mayne?")
BP_dates = input("Which dates for St Bridgewater Primary?")


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


total_dates = GS_dates + ' ' + YM_dates + ' ' + SCM_dates + ' ' + BP_dates

for i in total_dates.split(): date_count+=1 

total = date_count * cost + GS_bonus + YM_bonus + SCM_bonus + BP_bonus

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
pdf.cell(0, 100, '', ln=True, border=0)
pdf.cell(0, 10, f'George Street school: {GS_dates}      £{cost}. Bonus = £{GS_bonus}', ln=True, align ='C')
pdf.cell(0, 10, f'Yorke Mead Primary: {YM_dates}      £{cost}. Bonus = £{YM_bonus}', ln=True, align ='C')
pdf.cell(0, 10, f'St Cuthbert Mayne: {SCM_dates}      £{cost}. Bonus = £{SCM_bonus}', ln=True, align ='C')
pdf.cell(0, 10, f'Bridgewater Primary: {BP_dates}      £{cost}. Bonus = £{BP_bonus}', ln=True, align ='C')
pdf.cell(0, 60, '', ln=True, border=0)
pdf.cell(0, 10, f'Total = £{total}', ln=True, align ='R')


pdf.output(f'{invoice_num} NTE invoice.pdf')