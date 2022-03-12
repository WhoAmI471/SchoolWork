class BasicWord():

    def __init__(self, word, subwords):
        self.word = word
        self.sub_words = subwords


    def has_subword(self, cand):
        return cand.lower() in self.sub_words


    def count_subwords(self):
        return f'{len(self.sub_words)}'


    def __repr__(self):
        return f'{self.word} содержит {len(self.sub_words)} слов'