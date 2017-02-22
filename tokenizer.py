#!/usr/bin/env python3

import re

class Tokenizer:
    def __init__(self):
        # list of delimiter
        self.splitter = [',', '.', '/', '?', ' ']
    
    def tokenize(self, text):
        """
            This method splits the incoming text into tokens(terms)
        """
        text = self.reduce_tokens_to_space(text).strip().lower()
        return re.split(r"\s+", text)
    
    def reduce_tokens_to_space(self, text):
        regex = r"[{}]+".format(''.join(self.splitter))
        return re.sub(regex, " ", text)

    def display(self):
        print("splitter : {}".format(self.splitter))

def main():
    tokenizer = Tokenizer()
    splitted = tokenizer.tokenize("hello i am paradox. be awesome stay    awesome.")
    print(splitted)

if __name__ == "__main__":
    main()

