"""
Utility script to download pdf files from a CSV file.

"""

import pandas as pd

data = pd.read_csv("Data Engineer Task - Data Engineer Task.csv", header=None)

websites = data.iloc[:, 0]

from urllib.request import urlretrieve
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import re
import os
import urllib
from urllib.parse import urljoin

PATH = "C:\\Users\\HP\\Downloads\\AI4Bharat\\files\\"

for i, url in enumerate(websites):
    if url[-4:] == '.pdf':
        response = requests.get(url)
        with open(PATH + str(i).zfill(6) + ".pdf", 'wb') as f:
            f.write(response.content)
    else:
        response = requests.get(url)
        soup= BeautifulSoup(response.text, "html.parser")  
        unique = set()
        for link in soup.select("a[href$='.pdf']"):
            unique.add(link['href'])
        for downloadable in unique:
            filename = str(i).zfill(6) + ".pdf"
            with open(PATH + filename, 'wb') as f:
                f.write(requests.get(urljoin(url,downloadable)).content)