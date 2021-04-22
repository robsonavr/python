from fpdf import FPDF


name = 'Robson Adriano'
pdf = FPDF('P', 'mm', 'A4')
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(40, 10, f'Hello World!\nMy name is {name}')
pdf.output('tuto1.pdf', 'F')