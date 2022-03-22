import img2pdf
from PIL import Image
import os

img_path = 'C:/Users/BRIJESH/Downloads/RESULT.png'

pdf_path = 'C:/Users/BRIJESH/Documents/RESULT.pdf'

image = Image.open(img_path)

pdf_bytes = img2pdf.convert(image.filename)

file = open(pdf_path, "wb")

file.write(pdf_bytes)

image.close()

file.close()

print("SUCCESSFULLY MADE PDF FILE.")
