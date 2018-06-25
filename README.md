# tag-generator
A simple application to generate tags for the given text (document) using tf-idf.

----

## tf-idf
Implementation of term frequency - inverse document frequency

----------

## What is tf-idf ?
Tf-idf stands for  **term frequency - inverse document frequency** which is used in text mining and information retrieval system to evauluate how important a word is in a document.  

The importance is directly proportional to the number of times a word appears in the document but is also weighted down by the frequency of the word in the whole corpus.

## Mathematically

**term-frequency (tf)** of a term/word t is actually given by:

`tf = (number of times the term t appears in a document ) / (total number of terms in the same document)`

**inverse document frequency (idf)** mesaures how much rare a term is throughout the multiple documents.
That is, more the rareness of a term, the greater we tend to value the rareness.

`idf = natural_logarithm[ (total number of documents) / (number of documents having the term t) ]`

Here, `natural_logarithm` is the logarithmic function with base **e**.

-----------------

## Dependency
The only dependency I have used here *(Used from June 25, 2018 and onwards)* is `nltk` library for lemmatization purpose.  
```bash
pip install nltk
```

## Usage

#### First clone this repo
```bash
git clone https://github.com/NISH1001/tag-generator
```

#### Put documents (text file) inside *data/documents/* path
The tagger uses the documents available inside **data/documents/**  
So, make sure there is alteast one document inside this path.  

#### Test the tagger
Run the **tagger.py** script. [I am assuming you are using python3]
```bash
python3 tagger.py
```

This will generate default 5 tags. Additional number can be supplied for getting more tags.  
```bash
python3 tagger.py 7
```

If you want to test a custom text file, put that inside the data folder as **data/test**. 

## References
https://en.wikipedia.org/wiki/Tf%E2%80%93idf

http://www.tfidf.com/
