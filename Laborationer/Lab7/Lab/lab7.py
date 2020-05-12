from time import time
import re
import argparse
from med import minimum_edit_distance
import sys

class SpellingWarning(object):

    def __init__(self, lexicon, word, row_number):
        self.lexicon = lexicon
        self.word = word
        self.row_number = row_number

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
                    edit_distance = minimum_edit_distance(word, lex_word)
                    break

    def __str__(self):
        return str(self.word)


class Report(object):

    def __init__(self, text, lexicon_name):
        self.file = open(text, "r", encoding = "utf-8")
        self.text = self.file.readlines()
        self.file.close()
        self.spelling_warnings = []
        self.lexicon = Lexicon(lexicon_name)

    def text_modifier(self, text):
        string_to_modify = str(text).replace("\n", " ").lower()
        list_to_modify = re.sub("[\W_]\-", " ", string_to_modify).split(" ")
        return list_to_modify

    def comparer(self):
        fixed_list = []
        row_number = 0
        for row in self.text:
            row_number += 1
            row = self.text_modifier(row)
            for word in row:
                if not self.lexicon.is_in_lexicon(word, 10):
                    self.spelling_warnings.append(SpellingWarning(self.lexicon, word, row_number))
        return self.spelling_warnings

    def __str__(self):
        return str(self.text_modifier)


class Lexicon(object):

    def __init__(self, lexicon_name):
        self.lexicon = lexicon_name
        self.fixed_lexicon = self.load_freq_data(lexicon_name)

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

    def is_in_lexicon(self, word, list_length):
        i = 0
        while i < list_length:
            print(self.fixed_lexicon[i])
            if word in self.fixed_lexicon[i]:
                return True
            elif i == len(self.fixed_lexicon):
                return False
            i += 1


    def __str__(self):
        return str(self.fixed_lexicon[0:1000])


def main():
    start_time = time()
    lexicon_name = sys.argv[1]
    text = sys.argv[2]
    lexicon = Lexicon(lexicon_name)
    report = Report(text, lexicon_name)
    spelling_warnings = report.comparer()
#    for spelling_warning in spelling_warnings:
#       print(spelling_warning)
    #print(lexicon)
    run_time = time() - start_time
    print(str(run_time))


main()
