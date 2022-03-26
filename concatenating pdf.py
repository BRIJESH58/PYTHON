from PyPDF2 import PdfFileMerger

pdf_merger = PdfFileMerger()

from pathlib import Path  # noqa

reports_dir = (
    Path.cwd()
    / "FOLDER NAME"
)

for path in reports_dir.glob("*.pdf"):
    print(path.name)

expense_reports = list(reports_dir.glob("*.pdf"))
expense_reports.sort()

for path in expense_reports:
    print(path.name)

for path in expense_reports:
    pdf_merger.append(str(path))

with Path("EXAMPLE.pdf").open(mode="wb") as output_file:
    pdf_merger.write(output_file)