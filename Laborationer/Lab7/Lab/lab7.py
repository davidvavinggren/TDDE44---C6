from time import time
import re
import argparse
from med import minimum_edit_distance
import sys

class SpellingWarning(object):

    def __init__(self, text, lexicon):
        self.lexicon = lexicon
        self.file = open(text, "r", encoding = "utf-8")
        self.text = self.file.read()
        self.file.close()
        self.epic_text = self.text_modifier()

    def text_modifier(self):
        string_to_modify = str(self.text).replace("\n", " ").lower()
        list_to_modify = re.sub("[\W_]\-", " ", string_to_modify).split(" ")
        return list_to_modify

    def comparer(self):
        n = 0
        for word in self.epic_text:
            #n += 1
            #print(word)
            for lex_word in self.lexicon:
                if word in lex_word[0]:
                    n += 1
                    #print(word)
                    break
                elif word not in lex_word[0]:
                    #n += 1
                    print(word) #str(n))
                    edit_distance = minimum_edit_distance(word, lex_word)
                    break

    def __str__(self):
        pass
        #return str(self.text_modifier())


class Report(object):
    pass

class Lexicon(object):

    def __init__(self, lexicon):
        self.lexicon = lexicon

    def load_freq_data(self, filepath):
        """Läs in och returnera frekvensdata från filen med sökvägen filepath.

        Returnerar en lista där varje element i listan är en lista med två element
        med följande struktur: [ord, frekvens]
        """

        file = open(filepath, encoding='utf-8')
        freq_data = []
        for line in file:
            freq_data.append(line.rstrip().split("\t"))
        file.close()
        return freq_data

    def __str__(self):
        return str(self.load_freq_data(self.lexicon))


def main():
    start_time = time()
    lexicon_name = sys.argv[1]
    lexicon = Lexicon(lexicon_name)
    print(lexicon.load_freq_data(lexicon_name))
    #print(word_freq)
    #spelling_warning = SpellingWarning("kort1.txt", lexicon.load_freq_data(lexicon_name))
    #spelling_warning.comparer()
    run_time = time() - start_time
    print(str(run_time))


main()
