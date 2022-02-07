"""

Script to perform a Wikipedia search using the provided keyword.
It returns urls of “n” related Wikipedia pages and extracts one paragraph from each such page.

"""

import argparse
 
parser = argparse.ArgumentParser()
 
parser.add_argument("-k", "--keyword", help = "String argument to define the query string")
parser.add_argument("-n", "--num_urls", help = "Integer argument for number of wikipedia pages to extract from", type = int)
parser.add_argument("-o", "--output", help = "Output json-file name")
 
args = parser.parse_args()

import wikipedia
searches = wikipedia.search(args.keyword, results = args.num_urls)

from tqdm import tqdm

results = []  
for i in tqdm(range(args.num_urls), desc="Loading..."):
    results.append({"url" : wikipedia.page(searches[i], auto_suggest=False).url, "paragraph" : wikipedia.summary(searches[i], sentences=2, auto_suggest=False)})

import json

json_output = json.dumps(results, indent=2)

with open(args.output, "w") as outfile:
    outfile.write(json_output)

"""
** NOTE **
In this case, we only require a few lines from the page, so we can use the helper wikipedia.summary.json
To extract the complete information from a page, here are 2 methods.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

## Method 1 :

text = wikipedia.page(searches[i], auto_suggest=False).content
text = text.replace('==', '')
text = text.replace('\n', '')
print(text)

## Method 2

source = urlopen(wikipedia.page(searches[i], auto_suggest=False).url).read()
soup = BeautifulSoup(source,'lxml')

paras = []
for paragraph in soup.find_all('p'):
    paras.append(str(paragraph.text))
    
text = re.sub(r"\[.*?\]+", '', text) # Remove footnote superscripts
text = text.replace('\n', '')
print(text)
"""
