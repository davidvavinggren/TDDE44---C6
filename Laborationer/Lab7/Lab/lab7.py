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
        self.suggestion_list = []

    def suggest(self):
        i = -1
        amount_of_suggestions = 0
        suggestion_string = ""
        for word in self.lexicon[0:self.list_length]:
            if len(word[0]) == len(self.word):
                self.suggestion_list.append([word[0], minimum_edit_distance(self.word, word[0])])
        if not self.get_3_suggestions():
            return "Found no suggestions with the same length."
        for word in self.get_3_suggestions():
            suggestion_string += word[0] + ", "
        return suggestion_string[:-2]

    def get_3_suggestions(self):
        try:
            list_in_progress = self.suggestion_list.copy()
            suggestion = []
            min_value_pos = 0
            min_value = 0
            for k in range (3):
                i = -1
                min_value = self.suggestion_list[0][1]
                for tuple in list_in_progress:
                    i += 1
                    if tuple[1] < min_value:
                        min_value = tuple[1]
                        min_value_pos = i
                suggestion.append(list_in_progress[min_value_pos])
                list_in_progress.remove(list_in_progress[min_value_pos])
        except IndexError:
            return
        return suggestion

    def write_to_report(self):
        return "[Line {}] {}: {}".format(self.row_number, self.word, self.suggest())

    def __str__(self):
        return self.word


class Report(object):

    def __init__(self, text, lexicon, list_length, sorted_dict):
        self.file = open(text, "r", encoding = "utf-8")
        self.text_name = text
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
        print("¤ Looking for unknown words in {}".format(self.text_name))
        row_number = 0
        for row in self.text:
            row_number += 1
            row = self.text_modifier(row)
            for word in row:
                if word == "":
                    break
                if not self.is_in_lexicon(word) and word.isalpha():
                    self.spelling_warnings.append(SpellingWarning(self.lexicon, word, row_number, self.list_length))
        print("¤ Found {} unknown words.".format(len(self.spelling_warnings)))
        return self.spelling_warnings

    def save(self, start_time):
        self.comparer()
        txt_file = open("report_" + self.text_name, "w", encoding = "utf-8")
        txt_file.write("***************************************************************************\n")
        for spelling_warning in self.spelling_warnings:
            txt_file.write(spelling_warning.write_to_report() + "\n")
        run_time = time() - start_time
        txt_file.write("Time to write report: " + str(run_time) + "\n")
        txt_file.write("***************************************************************************\n")
        txt_file.close()
        return txt_file

    def __str__(self):
        return "report_{}".format(self.text_name)


class Lexicon(object):

    def __init__(self, filepath):
        self.filepath = filepath

    def load_freq_data(self):
        """Läs in och returnera frekvensdata från filen med sökvägen filepath.

        Returnerar en lista där varje element i listan är en lista med två element
        med följande struktur: [ord, frekvens]
        """

        print("¤ Reading lexicon {}".format(self.filepath))
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
    list_of_reports = []
    for text in sys.argv[3:]:
        report = Report(text, sorted_lexicon, list_length, sorted_dict)
        list_of_reports.append(report)
    for report in list_of_reports:
        report.save(start_time)
    print("¤ Suggestions written in reports: ")
    for report in list_of_reports:
        print(report)
    run_time = time() - start_time
    print("\n" + "Runtime: " + str(run_time))



if __name__ == "__main__":
    main()
