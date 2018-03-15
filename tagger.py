#!/usr/bin/env python3

import operator
from pprint import pprint

from document import Document
from tfidf import TFIDF
from textprocessor import TokenProcessor

class Tagger:
    def __init__(self):
        self.documents = {}
        self.tfidf = TFIDF()

    def add_document(self, document):
        self.documents[document.id] = document

    def display(self):
        for id in self.documents:
            self.documents[id].display()

    def get_terms_weighted_by_tfidf(self, document):
        documents = [ self.documents[key] for key in self.documents ]
        tfidf_list = self.tfidf.calculate_tfidf_document(documents, document)
        weighted_terms = {}
        for d in tfidf_list:
            term = d["term"]
            tf = d["tf"]
            idf = d["idf"]
            weighted_terms[term] = tf * idf
        return weighted_terms

    def get_tags_using_weighted_terms(self, weighted_terms, size=5):
        sorted_terms = sorted(weighted_terms.items(), key = operator.itemgetter(1), reverse=True)
        length = len(weighted_terms)
        size = length if size > length else size
        tags = []
        for i in range(size):
            tags.append(sorted_terms[i][0])
        return tags


    def __str__(self):
        return str(pprint(vars(self)))

def test():
    textprocessor = textprocessor()

    doc1 = Document(1)
    doc1.load_from_file("documents/test.txt")
    doc1.extract_terms(textprocessor)
    doc1.generate_frequency_map()

    doc2 = Document(2)
    doc2.load_from_file("documents/test2.txt")
    doc2.extract_terms(textprocessor)
    doc2.generate_frequency_map()

    tagger = Tagger()
    tagger.add_document(doc1)
    tagger.add_document(doc2)
    #tagger.display()
    weighted_terms = tagger.get_terms_weighted_by_tfidf(doc1)
    tags = tagger.get_tags_using_weighted_terms(weighted_terms)
    print(tags)

def test_article():
    textprocessor = TokenProcessor()

    doc1 = Document(1)
    doc1.load_from_file("documents/in_the_core")
    doc1.extract_terms(textprocessor)
    doc1.generate_frequency_map()

    doc2 = Document(2)
    doc2.load_from_file("documents/i_saw_a_dream")
    doc2.extract_terms(textprocessor)
    doc2.generate_frequency_map()

    doc3 = Document(3)
    doc3.load_from_file("documents/smile")
    doc3.extract_terms(textprocessor)
    doc3.generate_frequency_map()

    doc4 = Document(4)
    doc4.load_from_file("documents/the_mask")
    doc4.extract_terms(textprocessor)
    doc4.generate_frequency_map()

    doc5 = Document(5)
    doc5.load_from_file("documents/sound-of-life")
    doc5.extract_terms(textprocessor)
    doc5.generate_frequency_map()

    tagger = Tagger()
    tagger.add_document(doc1)
    tagger.add_document(doc2)
    tagger.add_document(doc3)
    tagger.add_document(doc4)
    tagger.add_document(doc5)

    weighted_terms = tagger.get_terms_weighted_by_tfidf(doc5)
    tags = tagger.get_tags_using_weighted_terms(weighted_terms)
    print(tags)


def main():
    test_article()

if __name__ == "__main__":
    main()
