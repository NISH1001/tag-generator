#!/usr/bin/env python3

import re

class TokenProcessor:
    def __init__(self):
        # list of delimiter
        self.stopwords_fname = "data/stopwords.txt"
        self.splitter = [',', "’", '.', '/', '?', ' ', '(', ')', '"', '*', ':', '-']
        self.load_stopwords(self.stopwords_fname)

    def load_stopwords(self, filename):
        with open(filename, 'r') as f:
            self.stopwords = f.read().split('\n')

    def tokenize(self, text):
        """
            This method splits the incoming text into tokens(terms)
        """
        text = self.reduce_tokens_to_space(text).strip().lower()
        return re.split(r"\s+", text)

    def remove_stopwords(self, tokens):
        return [ token for token in tokens if token not in self.stopwords ]

    def remove_shortwords(self, tokens):
        return [ token for token in tokens if len(token) > 3]

    def reduce_tokens_to_space(self, text):
        regex = r"[{}]+".format(''.join(self.splitter))
        return re.sub(regex, " ", text)

    def display(self):
        print("splitter : {}".format(self.splitter))

def main():
    token_processor = TokenProcessor()
    tokens = token_processor.tokenize("hello i am paradox. be awesome stay    awesome.")
    tokens = token_processor.remove_stopwords(tokens)
    # tokens = token_processor.remove_shortwords(tokens)
    print(tokens)

if __name__ == "__main__":
    main()

