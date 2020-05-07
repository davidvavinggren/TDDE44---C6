import time
import argparse
from med import minimum_edit_distance
import sys

class SpellingWarning(object):
    pass

class Report(object):
    pass

class WordFreq(object):

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

def main():
    lexicon_name = sys.argv[1]
    word_freq = WordFreq(lexicon_name)
    word_freq.load_freq_data(lexicon_name)
    print(word_freq)

main()
