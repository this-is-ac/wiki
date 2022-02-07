from urllib.request import urlretrieve
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import re
import os
import urllib
from urllib.parse import urljoin
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

import pandas as pd

data = pd.read_csv("Data Engineer Task - Data Engineer Task.csv", header=None)

websites = data.iloc[:, 0]

PATH = "C:\\Users\\HP\\Downloads\\Task\\files\\"

import json

final_results = []  

def get_content(filepath):
    TEMPO = "C:\\Users\\HP\\Downloads\\AI4Bharat\\pdfminer_outputs\\"
    with open(TEMPO + filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return lines

for i, url in enumerate(websites):
    if url[-4:] == '.pdf':
        #response = requests.get(url)
        # with open(PATH + str(i).zfill(6) + ".pdf", 'wb') as f:
        #     f.write(response.content)
        final_results.append({"page-url" : url, "pdf-url" : url, "pdf-content" : get_content(str(i).zfill(6) + ".txt")})
    else:
        response = requests.get(url)
        soup= BeautifulSoup(response.text, "html.parser")  
        unique = set()
        for link in soup.select("a[href$='.pdf']"):
            unique.add(link['href'])
        for downloadable in unique:
            filename = str(i).zfill(6) + ".txt"
            # with open(PATH + filename, 'wb') as f:
            #     f.write(requests.get(urljoin(url,downloadable)).content)
            final_results.append({"page-url" : url, "pdf-url" : urljoin(url,downloadable), "pdf-content" : get_content(filename)})

json_output = json.dumps(final_results, indent=2)

with open("pdf_extract.json", "w") as outfile:
    outfile.write(json_output)
