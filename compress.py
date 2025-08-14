from pypdf import PdfWriter

writer = PdfWriter(clone_from="output/output.pdf")

for page in writer.pages:
    for img in page.images:
        img.replace(img.image, quality=20)

with open("output/compressed/output.pdf", "wb") as f:
    writer.write(f)

# from PIL import Image

# image = Image.open("output/output.pdf")
# image.save("output/output_compressed.pdf", quality=60) # 70 is a common quality setting
