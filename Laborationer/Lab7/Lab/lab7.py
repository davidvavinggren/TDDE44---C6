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
        amount_of_suggestions = 0
        edit_distances = []
        suggestion_list = []
        suggestion_string = ""
        for word in self.lexicon[0:self.list_length]:
            if len(word[0]) == len(self.word):
                edit_distances.append(minimum_edit_distance(self.word, word[0]))
        #På vilken plats är minsta edit distance?
        for element in edit_distances:
            i += 1
            if element == min(edit_distances) and amount_of_suggestions < 3:
                suggestion_list.append(self.lexicon[i])
                amount_of_suggestions += 1
        for suggestion in suggestion_list:
            suggestion_string += suggestion[0] + ", "
        return suggestion_string[:-2]

    def write_to_report(self):
        return "[Line {}] {}: {}".format(self.row_number, self.word, self.suggest())

    def __str__(self):
        return self.word


class Report(object):

    def __init__(self, text, lexicon, list_length, sorted_dict):
        self.file = open(text, "r", encoding = "utf-8")
        self.text = self.file.readlines()
        self.file.close()
        self.spelling_warnings = []
        self.lexicon = lexicon
        self.list_length = list_length
        self.sorted_dict = sorted_dict

    def text_modifier(self, text):
        string_to_modify = str(text).replace("\n", " ").lower()
        list_to_modify = re.sub("[\W_]+", " ", string_to_modify).split(" ")
        list_to_modify.remove("")
        return list_to_modify

    def is_in_lexicon(self, word):
        i = 0
        while i < len(self.sorted_dict):
            if word in self.sorted_dict.keys():
                return True
            elif i == len(self.lexicon):
                return False
            i += 1

    def comparer(self):
        row_number = 0
        for row in self.text:
            row_number += 1
            row = self.text_modifier(row)
            for word in row:
                if word == "":
                    break
                if not self.is_in_lexicon(word) and word.isalpha():
                    self.spelling_warnings.append(SpellingWarning(self.lexicon, word, row_number, self.list_length))
        print("¤ Found {} unknown words:".format(len(self.spelling_warnings)))
        return self.spelling_warnings

    def save(self):
        txt_file = open("report.txt", "w", encoding = "utf-8")
        txt_file.write("***************************************************************************\n")
        for spelling_warning in self.spelling_warnings:
            txt_file.write(spelling_warning.write_to_report() + "\n")
        txt_file.write("***************************************************************************\n")
        txt_file.close()

    def __str__(self):
        return report.save()


class Lexicon(object):

    def __init__(self, filepath):
        self.filepath = filepath

    def load_freq_data(self):
        """Läs in och returnera frekvensdata från filen med sökvägen filepath.

        Returnerar en lista där varje element i listan är en lista med två element
        med följande struktur: [ord, frekvens]
        """

        print("¤ Reading {} and looking for unknown words...".format(self.filepath))
        file = open(self.filepath, encoding='utf-8')
        freq_data_list = []
        freq_data_dict = {}
        for line in file:
            freq_data_list.append(line.rstrip().split("\t"))
            freq_data_dict[line.rstrip().split("\t")[0]] = line.rstrip().split("\t")[1]
        file.close()
        return freq_data_list, freq_data_dict

    def __str__(self):
        return str(self.lexicon)


def main():
    start_time = time()
    lexicon_name = sys.argv[1]
    list_length = int(sys.argv[2])
    text = sys.argv[3]
    lexicon = Lexicon(lexicon_name)
    sorted_data = lexicon.load_freq_data()
    sorted_lexicon = sorted_data[0]
    sorted_dict = sorted_data[1]
    report = Report(text, sorted_lexicon, list_length, sorted_dict)
    spelling_warnings = report.comparer()
    print("¤ Looking for suggestions for the unknown words:")
    for spelling_warning in spelling_warnings:
        print(spelling_warning, end = " ")
        spelling_warning.suggest()
    print(report.save())

    run_time = time() - start_time
    print("\n" + "Runtime: " + str(run_time))



if __name__ == "__main__":
    main()
