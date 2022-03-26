from pathlib import Path
from PyPDF2 import PdfFileMerger

report_dir = (
    Path.cwd()
    / "FOLDER NAME"
)

report_path = report_dir / "FILE1.pdf"
toc_path = report_dir / "FILE2.pdf"

pdf_merger = PdfFileMerger()
pdf_merger.append(str(report_path))

pdf_merger.merge(1, str(toc_path))

with Path("EXAMPLE.pdf").open(mode="wb") as output_file:
    pdf_merger.write(output_file)
