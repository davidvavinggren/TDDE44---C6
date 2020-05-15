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

    def suggest(self):
        i = -1
        amount_of_suggestions = 0
        edit_distances = []
        suggestion_list = []
        for word in self.lexicon:
            if len(word[0]) == len(self.word):
                edit_distances.append(minimum_edit_distance(self.word, word[0]))
        #På vilken plats är minsta edit distance?
        for element in edit_distances:
            i += 1
            if element == min(edit_distances) and amount_of_suggestions < 3:
                suggestion_list.append(self.lexicon[i])
                suggestion_list.append(self.word)
                amount_of_suggestions += 1
        return suggestion_list

    def __str__(self):
        return str()


class Report(object):

    def __init__(self, text, lexicon):
        self.file = open(text, "r", encoding = "utf-8")
        self.text = self.file.readlines()
        self.file.close()
        self.spelling_warnings = []
        self.lexicon = lexicon

    def text_modifier(self, text):
        string_to_modify = str(text).replace("\n", " ").lower()
        list_to_modify = re.sub("[\W_]+", " ", string_to_modify).split(" ")
        list_to_modify.remove("")
        return list_to_modify

    def is_in_lexicon(self, word, list_length):
        i = 0
        while i < list_length:
            if word in self.lexicon[i]:
                return True
            elif i == len(self.lexicon):
                return False
            i += 1

    def comparer(self):
        row_number = 0
        for row in self.text:
            row_number += 1
            row = self.text_modifier(row)
            #print(row)
            for word in row:
                if word == "":
                    break
                if not self.is_in_lexicon(word, len(self.lexicon)):
                    self.spelling_warnings.append(SpellingWarning(self.lexicon, word, row_number))
        print("¤ Found {} unknown words.".format(len(self.spelling_warnings)))
        return self.spelling_warnings

    def save(self):
        txt_file = open(self.lexicon.filepath, "w+")
        txt_file.write("¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤")
        for spelling_warning in self.spelling_warnings:
            txt_file.write("[Line {}] {}: {}".format(self.spelling_warning.row_number, self.spelling_warning.word, self.spelling_warning.suggest()))
        txt_file.close()

    def __str__(self):
        pass


class Lexicon(object):

    def __init__(self, filepath, list_length):
        self.filepath = filepath
        self.list_length = list_length

    def load_freq_data(self):
        """Läs in och returnera frekvensdata från filen med sökvägen filepath.

        Returnerar en lista där varje element i listan är en lista med två element
        med följande struktur: [ord, frekvens]
        """

        print("¤ Reading {} and looking for unknown words...".format(self.filepath))
        file = open(self.filepath, encoding='utf-8')
        freq_data = []
        i = 0
        for line in file:
            if i < self.list_length:
                freq_data.append(line.rstrip().split("\t"))
            i += 1
        file.close()
        return freq_data

    def __str__(self):
        return str(self.lexicon[0:1000])


def main():
    start_time = time()
    lexicon_name = sys.argv[1]
    text = sys.argv[2]
    list_length = int(sys.argv[3])
    lexicon = Lexicon(lexicon_name, list_length)
    sorted_lexicon = lexicon.load_freq_data()
    report = Report(text, sorted_lexicon)
    spelling_warnings = report.comparer()
    print("¤ Looking for suggestions for these unknown words:")
    for spelling_warning in spelling_warnings:
        print(spelling_warning, end = " ")
        spelling_warning.suggest()
    #report = report.save()
    #print(report)
    run_time = time() - start_time
    print("\n" + "Runtime: " + str(run_time))


main()
