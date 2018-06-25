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

    def process_text(self, text):
        text = text.encode('ascii', errors='ignore').decode()
        text = text.lower()
        text = re.sub(r'http\S+', ' ', text)
        text = re.sub(r'#+', ' ', text )
        text = re.sub(r'@[A-Za-z0-9]+', ' ', text)
        text = re.sub(r"([A-Za-z]+)'s", r"\1 is", text)
        #text = re.sub(r"\'s", " ", text)
        text = re.sub(r"\'ve", " have ", text)
        text = re.sub(r"won't", "will not ", text)
        text = re.sub(r"isn't", "is not ", text)
        text = re.sub(r"can't", "can not ", text)
        text = re.sub(r"n't", " not ", text)
        text = re.sub(r"i'm", "i am ", text)
        text = re.sub(r"\'re", " are ", text)
        text = re.sub(r"\'d", " would ", text)
        text = re.sub(r"\'ll", " will ", text)
        text = re.sub('\W', ' ', text)
        text = re.sub(r'\d+', ' ', text)
        text = re.sub('\s+', ' ', text)
        text = text.strip()
        return text

    def tokenize(self, text):
        """
            This method splits the incoming text into tokens(terms)
        """
        # text = self.reduce_tokens_to_space(text).strip().lower()
        text = self.process_text(text)
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

