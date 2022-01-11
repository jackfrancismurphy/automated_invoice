from fpdf import FPDF

#variables
total = 0
total_dates = 0
date_count = 0
cost = 26.73
GS_bonus = 5 
YM_bonus = 9
SCM_bonus = 8
BP_bonus = 7 

GS_dates = input("Which dates for George Street?") 
YM_dates = input("Which dates for Yorke Mead?") 
SCM_dates = input("Which dates for St Cuthbert Mayne?")
BP_dates = input("Which dates for St Bridgewater Primary?")
invoice_num = input("What number invoice is this?")

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


pdf.cell(120, 10, f'Invoice {invoice_num}')
pdf.cell(40, 10, 'Date:[coming soon]', ln=True)
pdf.cell(0, 100, '', ln=True, border=0)
pdf.cell(0, 10, f'George Street school: {GS_dates}      £{cost}. Bonus = £{GS_bonus}', ln=True, align ='C')
pdf.cell(0, 10, f'Yorke Mead Primary: {YM_dates}      £{cost}. Bonus = £{YM_bonus}', ln=True, align ='C')
pdf.cell(0, 10, f'St Cuthbert Mayne: {SCM_dates}      £{cost}. Bonus = £{SCM_bonus}', ln=True, align ='C')
pdf.cell(0, 10, f'Bridgewater Primary: {BP_dates}      £{cost}. Bonus = £{BP_bonus}', ln=True, align ='C')
pdf.cell(0, 60, '', ln=True, border=0)
pdf.cell(0, 10, f'Total = £{total}', ln=True, align ='R')


pdf.output(f'{invoice_num} NTE invoice.pdf')



#invoice number
#different schools 
#calculate table?
#have code run incase there's a different number of children 
#around 5 minutes into video 2 learn how to put a header and footer image (to make it look pretty)
#deal with date in a bit.
#Need to know how to store invoice number outside of this document