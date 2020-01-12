## Text Interpreter

The Text Interpreter tool can read text data (images, PDFs, plain text, etc.), extract keywords, and define the keywords. It is useful to synthesize information from long articles or skim textbook pages when you're running short on time. 

Developed 10/26/2019 for the Code Ada hackathon.

### Frontend/Backend

1. Python
 - pytesseract for Optical Character Recognition
 - spaCy for Keyword extraction (remove stopwords, POS tagging)
2. SerpAPI to obtain json of word/definition/questions/links for each keyword 
3. Flask, HTML/Css

#### Contributors
Shresta Bangaru and Elena Zheng
