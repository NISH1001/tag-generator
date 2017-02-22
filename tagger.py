#!/usr/bin/env python3

from pprint import pprint

from document import Document
from tokenizer import Tokenizer

class Tagger:
    def __init__(self):
        self.documents = {}

    def add_document(self, document):
        self.documents[document.id] = document

    def display(self):
        for id in self.documents:
            self.documents[id].display()

    def __str__(self):
        return str(pprint(vars(self)))


def main():
    tokenizer = Tokenizer()

    doc = Document(1)
    doc.load_from_file("documents/test.txt")
    doc.extract_terms(tokenizer)
    doc.generate_frequency_map()

    tagger = Tagger()
    tagger.add_document(doc)
    tagger.display()

if __name__ == "__main__":
    main()

