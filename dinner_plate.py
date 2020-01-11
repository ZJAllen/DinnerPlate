'''
Stage 1: Add template to PDF as "Watermark"
    -> send copy of original to "Original" folder
    -> send new file to the "Converted" folder
Stage 2: Fill out form
Stage 3: Detect when a file is added to the root folder
'''

import os
import shutil
from file_path import root_path, template, original_path, converted_path
from PyPDF2 import PdfFileWriter, PdfFileReader


def add_template(input_pdf, output, watermark):
    watermark_obj = PdfFileReader(watermark)
    watermark_page = watermark_obj.getPage(0)

    pdf_reader = PdfFileReader(input_pdf)
    pdf_writer = PdfFileWriter()

    # Watermark all the pages
    for page in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page)
        page.mergePage(watermark_page)
        pdf_writer.addPage(page)

    with open(output, 'wb') as out:
        pdf_writer.write(out)


def move_file(original, destination):
    shutil.move(original, destination)


if __name__ == '__main__':
    for f_name in os.listdir(root_path):
        if f_name.endswith('.pdf'):
            add_template(
                input_pdf=f"{root_path}/{f_name}",
                output=f"{converted_path}/{f_name}",
                watermark=template)
            move_file(f"{root_path}/{f_name}", original_path)
