#!/usr/bin/env python3

import glob

from document import Document
from textprocessor import TokenProcessor

def get_train_documents(documents_path, token_processor):
    if not token_processor:
        token_processor = TokenProcessor()
    documents = []
    filenames = glob.glob(documents_path)
    for i, filename in enumerate(filenames):
        doc = Document(i)
        doc.load_from_file(filename)
        doc.extract_terms(token_processor)
        doc.generate_frequency_map()
        documents.append(doc)
    return documents

def get_test_document(filename, token_processor):
    if not token_processor:
        token_processor = TokenProcessor()
    doc = Document(filename)
    doc.load_from_file(filename)
    doc.extract_terms(token_processor)
    doc.generate_frequency_map()
    return doc


def main():
    documents = get_train_documents("data/documents/*")
    print(documents)

if __name__ == "__main__":
    main()

