#!/usr/bin/env python3

import operator
from pprint import pprint

from textprocessor import TokenProcessor

class Document:
    def __init__(self, id):
        self.id = id
        self.terms = []
        self.frequency_map = {}
        self.text = ""
        self.smoothing = False

    def add_text(self, text):
        """
            Append text
        """
        self.text += "\n" + text
        self.text = self.text.strip()

    def load_from_file(self, filename):
        """
            This is used to append text from a file
        """
        with open(filename, 'r') as f:
            for line in f:
                self.add_text(line)

    def get_total_term_count(self):
        """
            Return the total number of terms in the document
        """
        return len(self.terms)

    def get_term_count(self, term, smoothing=False):
        """
            Return the total occurence of given term in the document
        """
        count = 0
        try:
            count = self.frequency_map[term]
        except KeyError:
            count = 0
        return count


    def generate_frequency_map(self):
        """
            It is used to generate a frequency map for the document.
            Eg:
            {
                "a" : 12,
                "i" : 1
            }
        """
        for term in self.terms:
            try:
                count = self.frequency_map[term]
            except KeyError:
                count = 0
            self.frequency_map[term] = count + 1

    def extract_terms(self, tokenizer):
        """
            It is used to extract individual terms from the text.

            It uses the tokenizer passed as the parameter
        """
        self.terms = tokenizer.tokenize(self.text)
        self.terms = tokenizer.remove_stopwords(self.terms)
        self.terms = tokenizer.remove_shortwords(self.terms)

    def get_frequent_terms(self, size=5):
        """
            This method returns the map with most frequent terms in the document
            sorted in descending order by frequency.
        """
        # gives a list of tuple with (key,value)
        sorted_map = sorted(self.frequency_map.items(), key = operator.itemgetter(1), reverse=True)
        to_ret = {}
        if size > len(sorted_map):
            size = len(sorted_map)
        for i in range(size):
            pair = sorted_map[i]
            to_ret[pair[0]] = pair[1]
        return to_ret


    def display(self):
        self.__str__()

    def __str__(self):
        return str(pprint(vars(self)))

def main():
    token_processor = TokenProcessor()

    doc = Document(1)
    doc.load_from_file("documents/test.txt")
    doc.extract_terms(token_processor)
    doc.generate_frequency_map()
    print(doc.get_frequent_terms())

if __name__ == "__main__":
    main()

