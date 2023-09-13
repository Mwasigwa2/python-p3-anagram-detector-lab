class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        return [candidate for candidate in word_list if candidate != self.word and sorted(candidate) == sorted(self.word)]
