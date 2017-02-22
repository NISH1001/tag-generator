#!/usr/bin/env python3

from pprint import pprint

from tokenizer import Tokenizer

class Document:
    def __init__(self, id):
        self.id = id
        self.terms = []
        self.frequency_map = {}
        self.text = ""

    def add_text(self, text):
        self.text += " " + text
        self.text = self.text.strip()

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                self.add_text(line)

    def generate_frequency_map(self):
        for term in self.terms:
            try:
                count = self.frequency_map[term]
            except KeyError:
                count = 0
            self.frequency_map[term] = count + 1

    def extract_terms(self, tokenizer):
        self.terms = tokenizer.tokenize(self.text)

    def display(self):
        self.__str__()

    def __str__(self):
        return str(pprint(vars(self)))

def main():
    tokenizer = Tokenizer()

    doc = Document(1)
    #doc.add_text("hello i am paradox")
    doc.load_from_file("documents/test.txt")
    doc.extract_terms(tokenizer)
    doc.generate_frequency_map()
    doc.display()

if __name__ == "__main__":
    main()

