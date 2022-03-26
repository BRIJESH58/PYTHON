from reportlab.pdfgen.canvas import Canvas

canvas = Canvas("hello.pdf")
canvas.drawString(72, 72, "Hello, World")
canvas.save()

from reportlab.lib.units import inch, cm  # noqa

print(cm)
print(inch)

canvas = Canvas("hello.pdf", pagesize=(8.5 * inch, 11 * inch))

from reportlab.lib.pagesizes import LETTER  # noqa

canvas = Canvas("hello.pdf", pagesize=LETTER)
print(LETTER)

canvas = Canvas("font-example.pdf", pagesize=LETTER)
canvas.setFont("Times-Roman", 18)
canvas.drawString(1 * inch, 10 * inch, "Times New Roman (18 pt)")
canvas.save()

from reportlab.lib.colors import blue
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas

canvas = Canvas("font-colors.pdf", pagesize=LETTER)

canvas.setFont("Times-Roman", 12)

canvas.setFillColor(blue)
canvas.drawString(1 * inch, 10 * inch, "Blue text")

canvas.save()
