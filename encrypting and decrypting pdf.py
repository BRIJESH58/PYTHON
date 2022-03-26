from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_path = (
    Path.cwd()
    / "EXAMPLE.pdf"
)

pdf_reader = PdfFileReader(str(pdf_path))

pdf_writer = PdfFileWriter()
pdf_writer.appendPagesFromReader(pdf_reader)

pdf_writer.encrypt(user_pwd="SUPERSECRET")

output_path = Path.cwd() / "EXAMPLE_PROTECTED.pdf"
with output_path.open(mode="wb") as output_file:
    pdf_writer.write(output_file)

user_pwd = "SUPERSECRET"
owner_pwd = "REALLYSUPERSECRET"
pdf_writer.encrypt(user_pwd=user_pwd, owner_pwd=owner_pwd)

from pathlib import Path  
from PyPDF2 import PdfFileReader, PdfFileWriter  

pdf_path = Path.cwd() / "EXAMPLE_PROTECTED.pdf"

pdf_reader = PdfFileReader(str(pdf_path))

print(pdf_reader.decrypt(password="SUPERSECRET"))

print(pdf_reader.getPage(0))
