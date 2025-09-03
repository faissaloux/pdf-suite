import fitz
import os

class pdfToImage:
    def run(self, pdf_path: str, output_folder: str):
        """
        Extracts all images from a PDF and saves them to a specified folder.
        """
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        pdfFile = fitz.open(pdf_path)
        for page_index in range(len(pdfFile)):
            page = pdfFile[page_index]
            image_list = page.get_images(full=True)

            for img_index, img in enumerate(image_list):
                xref = img[0]
                base_image = pdfFile.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]

                image_filename = os.path.join(output_folder, f"page{page_index + 1}_img{img_index + 1}.{image_ext}")
                with open(image_filename, "wb") as f:
                    f.write(image_bytes)
                print(f"Extracted: {image_filename}")

        pdfFile.close()
