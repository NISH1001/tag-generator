#!/usr/bin/env python3

from document import Document
from tokenizer import Tokenizer

class TFIDF:
    def __init__(self):
        pass

    def calculate_term_frequency(self, document, term):
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


def main():
    tokenizer = Tokenizer()

    doc = Document(1)
    #doc.add_text("hello i am paradox")
    doc.load_from_file("documents/test.txt")
    doc.extract_terms(tokenizer)
    doc.generate_frequency_map()

    tfidf = TFIDF()
    tf = tfidf.calculate_term_frequency(doc, "paradox")
    print(tf)

if __name__ == "__main__":
    main()

