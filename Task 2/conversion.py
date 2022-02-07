from PIL import Image
import pytesseract
import sys
from pdf2image import convert_from_path
import os
import shutil
import pdfplumber
from tqdm import tqdm
import argparse
from pdfminer3.layout import LAParams, LTTextBox
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfinterp import PDFResourceManager
from pdfminer3.pdfinterp import PDFPageInterpreter
from pdfminer3.converter import PDFPageAggregator
from pdfminer3.converter import TextConverter
import io
 
parser = argparse.ArgumentParser()
 
parser.add_argument("-m", "--method", help = "Method for text extraction : tesseract, pdfminer or pdfplumber", nargs='?', const = "tesseract")
 
args = parser.parse_args()


PATH = "C:\\Users\\HP\\Downloads\\AI4Bharat\\files\\"

TEMP = "C:\\Users\\HP\\Downloads\\AI4Bharat\\temp\\"

DEST = "C:\\Users\\HP\\Downloads\\AI4Bharat\\outputs\\"

if not os.path.exists(DEST):
    os.makedirs(DEST)

files = os.listdir(PATH)

for i, filepath in enumerate(tqdm([files[-1]])):
    
    if args.method == "tesseract":
        if not os.path.exists(TEMP):
            os.makedirs(TEMP)

        pages = convert_from_path(PATH + filepath)
        image_counter = 1
        for page in pages:
            filename = "page_"+str(image_counter)+".jpg"
            page.save(TEMP + filename, 'JPEG')
            image_counter = image_counter + 1

        filelimit = image_counter-1
        outfile = filepath[:-4] + ".txt"
        f = open(DEST + outfile, "a", encoding='utf8')

        for i in range(1, filelimit + 1):
            filename = "page_"+str(i)+".jpg"
            text = str(((pytesseract.image_to_string(Image.open(TEMP + filename), lang = 'mar'))))
            text = text.replace('-\n', '')	
            f.write(text)
        f.close()
        shutil.rmtree(TEMP)
    
    elif args.method == "pdfminer":
        resource_manager = PDFResourceManager()
        fake_file_handle = io.StringIO()
        converter = TextConverter(resource_manager, fake_file_handle, laparams=LAParams())
        page_interpreter = PDFPageInterpreter(resource_manager, converter)

        with open(PATH + filepath, 'rb') as fh:
            for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
                page_interpreter.process_page(page)
            text = fake_file_handle.getvalue()

        converter.close()
        fake_file_handle.close()
        
        outfile = filepath[:-4] + ".txt"
        f = open(DEST + outfile, "a", encoding='utf8')
        f.write(text)
        f.close()
    
    else:
        outfile = filepath[:-4] + ".txt"
        f = open(DEST + outfile, "a", encoding='utf8')
        with pdfplumber.open(PATH + filepath) as pdf:
            for page in range(len(pdf.pages)):
                f.write(pdf.pages[page].extract_text())
        f.close()