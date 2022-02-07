**Task 2**

The file `Data Engineer Task - Data Engineer Task.csv` contains the list of urls. 
The scripts included are as follows :
1. `download.py`
   * Downloads all the pdfs to the system path specified in _PATH_
   * For links where the pdf url is not given directly, it scrapes the HTML to find all pdf links. 
2. `conversion.py` 
   * The script takes an argument _method_ belonging to the set {tesseract, pdfminer, pdfplumber} for PDF text extraction, default being tesseract.
   * Tesseract provides the best results, followed by pdfminer.
   * For our experiments, we use the default models provided by tesseract in tessdata. Since all the inputs are in Marathi, we set lang = 'mar'.
   * For other Indic languages including Bengali, Gujarati, Hindi, Kannada, Malayalam, Meetei Meyak, Oriya, Punjabi, Santali, Tamil and Telugu, the Indic OCR package (https://indic-ocr.github.io/tessdata/) provides some models which can be tested.
3. `pdf_extract.py` 
   * This script combines `download.py` and `conversion.py` and saves the final results to a json file `pdf_extract.json`.
4. `testrun.py`.
   * Utility script to create the json file if the text extracted from the PDFs are stored in text files.

**NOTE**

Since _tesseract_ showed an estimated time of 7:30 hours (pdfminer took 35 mins), I have attached the results using _pdfminer_ in `pdf_extract.json`. 
All the induvidual outputs using _pdfminer_ can be found [here](https://github.com/this-is-ac/wiki/tree/main/Task%202/pdfminer_outputs).
But _tesseract_ performs much better than _pdfminer_ which is illustrated by [pdfminer 47](https://github.com/this-is-ac/wiki/blob/main/Task%202/pdfminer_outputs/000047.txt) and [tesseract  47](https://github.com/this-is-ac/wiki/blob/main/Task%202/tesseract_outputs/000047.txt).
As we can see, _pdfminer_ wasn't able to detect any text.

With regards to reading order, since we convert the pdf to images for tesseract, I had an idea of cropping the centre of the image and run the OCR algorithm on it. If text exists, it is not in two column format and we can run the OCR on the whole page. If there is no text, we split the page into two parts vertically, and run the OCR seperately. Although it works for two column, it will fail if the text has more columns or a page is a combination of both.
To resolve this, we require the layout information, which can be extracted using a library `pdfminer6`, which I haven't tried yet.
