from PyPDF2 import PdfFileWriter

pdf_writer = PdfFileWriter()

page = pdf_writer.addBlankPage(width=72, height=72)

print(type(page))

from pathlib import Path

with Path("BLANK.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)

from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_path = (
    Path.cwd()
    / "EXAMPLE.pdf"
)
input_pdf = PdfFileReader(str(pdf_path))

first_page = input_pdf.getPage(0)

pdf_writer = PdfFileWriter()
pdf_writer.addPage(first_page)

with Path("FIRST_PAGE.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)

from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path

pdf_path = (
    Path.cwd()
    / "EXAMPLE.pdf"
)
input_pdf = PdfFileReader(str(pdf_path))

pdf_writer = PdfFileWriter()
for n in range(1, 1):
    page = input_pdf.getPage(n)
    pdf_writer.addPage(page)

print(pdf_writer.getNumPages())

pdf_writer = PdfFileWriter()

for page in input_pdf.pages[1:3]:
    pdf_writer.addPage(page)

with Path("EXAMPLE2.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)
