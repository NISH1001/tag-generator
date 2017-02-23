#!/usr/bin/env python3

from pprint import pprint

from document import Document
from tfidf import TFIDF
from tokenizer import Tokenizer

class Tagger:
    def __init__(self):
        self.documents = {}
        self.tfidf = TFIDF()

    def add_document(self, document):
        self.documents[document.id] = document

    def display(self):
        for id in self.documents:
            self.documents[id].display()

    def tag_document(self, document):
        documents = [ self.documents[key] for key in self.documents ]
        tfidf_list = self.tfidf.calculate_tfidf_document(documents, document)
        weighted_terms = {}
        for d in tfidf_list:
            term = d["term"]
            tf = d["tf"]
            idf = d["idf"]
            weighted_terms[term] = tf * idf
        return weighted_terms

    def __str__(self):
        return str(pprint(vars(self)))


def main():
    tokenizer = Tokenizer()

    doc1 = Document(1)
    doc1.load_from_file("documents/test.txt")
    doc1.extract_terms(tokenizer)
    doc1.generate_frequency_map()

    doc2 = Document(2)
    doc2.load_from_file("documents/test2.txt")
    doc2.extract_terms(tokenizer)
    doc2.generate_frequency_map()

    tagger = Tagger()
    tagger.add_document(doc1)
    tagger.add_document(doc2)
    #tagger.display()
    weighted_terms = tagger.tag_document(doc1)
    print(weighted_terms)

if __name__ == "__main__":
    main()
