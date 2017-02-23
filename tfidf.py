#!/usr/bin/env python3

import math

from document import Document
from tokenizer import Tokenizer

class TFIDF:
    def __init__(self):
        self.documents = {}

    def calculate_term_frequency(self, document, term):
        """
            This method calculates the normalized frequency of the term in the
            given document
        """
        frequency_map = document.frequency_map
        total_terms = 0
        for key in frequency_map:
            total_terms += frequency_map[key]
        term_count = 0
        try:
            term_count = frequency_map[term]
        except KeyError:
            term_count = 0
        return term_count / total_terms

    def calculate_inverse_document_frequency(self, documents, term):
        """
            This method calculates the rareness of the term that may appear in multiple documents
        """
        total_documents = len(documents)
        total_document_with_term = 0
        for document in documents:
            term_count = document.get_term_count(term)
            if term_count > 0:
                total_document_with_term += 1
        idf = 0
        #print("total docs : {}, total doc with term : {}".format(total_documents, total_document_with_term))
        if total_documents > 0 and total_document_with_term > 0:
            idf = math.log( total_documents / total_document_with_term)
        return  idf

def main():
    tokenizer = Tokenizer()

    doc = Document(1)
    doc.load_from_file("documents/test.txt")
    doc.extract_terms(tokenizer)
    doc.generate_frequency_map()

    doc1 = Document(2)
    doc1.load_from_file("documents/test2.txt")
    doc1.extract_terms(tokenizer)
    doc1.generate_frequency_map()

    tfidf = TFIDF()
    tf = tfidf.calculate_term_frequency(doc, "i")
    print(tf)
    idf = tfidf.calculate_inverse_document_frequency([doc, doc1], "i")
    print(idf)

if __name__ == "__main__":
    main()

