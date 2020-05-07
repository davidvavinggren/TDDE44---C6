import time
import argparse
from med import minimum_edit_distance
import sys

class SpellingWarning(object):

    def __init__(self, text):
        self.text = text

    def text_modifier(self):
        text_to_modify = open(self.text, encoding = "utf-8")
        list_to_modify = text_to_midify.strip("\n").split(" ")
        return list_to_modify

    def __str__(self):
        return str(self.text_modifier())


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
    lexicon_name = sys.argv[1]
    lexicon = Lexicon(lexicon_name)
    lexicon.load_freq_data(lexicon_name)
    #print(word_freq)
    spelling_warning = SpellingWarning("kort1.txt")
    print(spelling_warning)

main()
