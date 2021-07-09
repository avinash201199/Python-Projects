# Python3 program to convert image to pfd
# using img2pdf library
#first install img2pdf library  by running this code  on terminal  pip install img2pdf

# importing necessary libraries
import img2pdf
from PIL import Image
import os

# storing image path
img_path = "image.jpg"

# storing pdf path
pdf_path = "image.pdf"

# opening image
image = Image.open(img_path)

# converting into chunks using img2pdf
pdf_bytes = img2pdf.convert(image.filename)

# opening or creating pdf file
file = open(pdf_path, "wb")

# writing pdf files with chunks
file.write(pdf_bytes)

# closing image file
image.close()

# closing pdf file
file.close()

# output
print("Successfully made pdf file")
