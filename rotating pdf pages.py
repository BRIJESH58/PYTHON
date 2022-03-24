from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_path = (
    Path.cwd() 
	/ "EXAMPLE.pdf"
)

pdf_reader = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()

for n in range(pdf_reader.getNumPages()):
    page = pdf_reader.getPage(n)
    if n % 2 == 0:
        page.rotateClockwise(90)
    pdf_writer.addPage(page)

with Path("EXAMPLE_ROTATED.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)

pdf_reader = PdfFileReader(str(pdf_path))

print(pdf_reader.getPage(0))

page = pdf_reader.getPage(0)
print(page["/Rotate"])

page = pdf_reader.getPage(1)
print(page["/Rotate"])

page = pdf_reader.getPage(0)
print(page["/Rotate"])

page.rotateClockwise(90)
print(page["/Rotate"])

pdf_reader = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()

for page in pdf_reader.pages:
    if page["/Rotate"] == -90:
        page.rotateClockwise(90)
    pdf_writer.addPage(page)

with Path("EXAMPLE_ROTATED.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)