**Task 1**

The script `wiki_extractor.py` performs a Wikipedia search using a keyword and returns urls of _n_ related Wikipedia pages and extracts one paragraph from each such page.
The results are stored in a json file, and in this case `out.json`. 

Since we require only 2 lines from each page, I have used the _summary_ helper to extract it. In case we require the complete information from a page, I have added the code for the same at the bottom of the script `wiki_extractor.py`.
