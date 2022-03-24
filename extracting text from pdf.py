from PyPDF2 import PdfFileReader
from pathlib import Path

pdf_path = (
    Path.cwd()
    /"EXAMPLE.pdf"
)

pdf = PdfFileReader(str(pdf_path))
print(pdf.getNumPages())
print(pdf.documentInfo)
print(pdf.documentInfo.title)

first_page = pdf.getPage(0)

print(type(first_page))

print(first_page.extractText())

for page in pdf.pages:
    print(page.extractText())

from pathlib import Path
from PyPDF2 import PdfFileReader

pdf_path = (
    Path.cwd()
    / "EXAMPLE.pdf"
)

pdf_reader = PdfFileReader(str(pdf_path))
output_file_path = Path.cwd() / "EXAMPLE.txt"

with output_file_path.open(mode="w") as output_file:
    title = pdf_reader.documentInfo.title
    num_pages = pdf_reader.getNumPages()
    output_file.write(f"{title}\\nNumber of pages: {num_pages}\\n\\n")

    for page in pdf_reader.pages:
        text = page.extractText()
        output_file.write(text)