from fpdf import FPDF

PDF = FPDF()

PDF.add_page()

PDF.set_font("Arial", size = 50)

PDF.cell(200, 10, txt = "HELLO STUDENTS", ln = 1, align = 'C')

PDF.cell(200, 10, txt = "HOW TO CREATE PDF FILE USING PYTHON",ln = 2, align = 'C')

PDF.output("WATERMARK1.pdf")