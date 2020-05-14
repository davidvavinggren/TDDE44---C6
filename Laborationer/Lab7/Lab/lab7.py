from time import time
import re
import argparse
from med import minimum_edit_distance
import sys

class SpellingWarning(object):

    def __init__(self, lexicon, word, row_number, list_length):
        self.lexicon = lexicon
        self.word = word
        self.row_number = row_number
        self.list_length = list_length

    def suggest(self):
        i = -1
        edit_distances = []
        suggestion_list = []
        for word in self.lexicon[0:self.list_length]:
             edit_distances.append(minimum_edit_distance(self.word, word[0]))
        #På vilken plats är minsta edit distance?
        for element in edit_distances:
            i += 1
            if element == min(edit_distances):
                suggestion_list.append(self.lexicon[i])
                suggestion_list.append(self.word)
        return suggestion_list

    def __str__(self):
        return str(self.suggest())


class Report(object):

    def __init__(self, text, lexicon_name):
        self.file = open(text, "r", encoding = "utf-8")
        self.text = self.file.readlines()
        self.file.close()
        self.spelling_warnings = []
        self.lexicon = Lexicon(lexicon_name)
        self.fixed_lexicon = self.lexicon.load_freq_data(lexicon_name)
        self.list_length = 1000

    def text_modifier(self, text):
        string_to_modify = str(text).replace("\n", " ").lower()
        list_to_modify = re.sub("[\W_]+", " ", string_to_modify).split(" ")
        list_to_modify.remove("")
        return list_to_modify

    def comparer(self):
        fixed_list = []
        row_number = 0
        for row in self.text:
            row_number += 1
            row = self.text_modifier(row)
            for word in row:
                if word == "":
                    break
                if not self.lexicon.is_in_lexicon(word, self.list_length):
                    self.spelling_warnings.append(SpellingWarning(self.fixed_lexicon, word, row_number, self.list_length))
        return self.spelling_warnings

    def __str__(self):
        pass


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
    for spelling_warning in spelling_warnings:
        spelling_warning.suggest()
    #print(str(spelling_warnings[0].suggest()))
    run_time = time() - start_time
    print(str(run_time))



main()
