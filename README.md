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

## References
https://en.wikipedia.org/wiki/Tf%E2%80%93idf

http://www.tfidf.com/
