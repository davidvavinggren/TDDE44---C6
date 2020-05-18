"""TDDE44, Labb 7."""


from time import time
import re
import argparse
from med import minimum_edit_distance
import sys


class SpellingWarning(object):
    """Klassen SpellingWarning."""

    def __init__(self, lexicon, word, row_number, list_length):
        """Initiera SpellingWarning med instatsvaribler som behövs."""
        self.lexicon = lexicon
        self.word = word
        self.row_number = row_number
        self.list_length = list_length
        self.suggestion_list = []

    def suggest(self):
        """Gå igenom ord i lexicon och jämför med de felstavade orden."""
        i = -1
        amount_of_suggestions = 0
        suggestion_string = ""
        # Jämför orden i lexikonet mot ordet i fråga.
        for word in self.lexicon[0:self.list_length]:
            #if len(word[0]) == len(self.word):
            self.suggestion_list.append([word[0],
                                        minimum_edit_distance(self.word,
                                                              word[0])])
            # Om de är lika långa, beräkna edit distance och lägg till ordet
            # tillsammans med edit distance i self.suggestion_list.
            if len(word[0]) == len(self.word):
                self.suggestion_list.append([word[0],
                                            minimum_edit_distance(self.word,
                                                                  word[0])])
        # Om det inte hittas förslag, skriv ut strängen nedan.
        if not self.get_3_suggestions():
            return "Found no suggestions with the same length."
        # Skapa sträng med suggestions utifrån self.suggestion_list.
        for word in self.get_3_suggestions():
            suggestion_string += word[0] + ", "
        return suggestion_string[:-2]

    def get_3_suggestions(self):
        """Gå igenom förslag på ord och hitta de med kortast edit distance."""
        try:
            list_in_progress = self.suggestion_list.copy()
            suggestion = []
            min_value_pos = 0
            min_value = 0
            for k in range (3):
            # Kör tre gånger för att hitta tre förslag.
            for k in range(3):
                i = -1
                min_value = self.suggestion_list[0][1]
                # Gå igenom listan med möjliga ersättare.
                for tuple in list_in_progress:
                    i += 1
                    # Tillsätt det minsta edit distancet till en variabel.
                    if tuple[1] < min_value:
                        min_value = tuple[1]
                        min_value_pos = i
                suggestion.append(list_in_progress[min_value_pos])
                list_in_progress.remove(list_in_progress[min_value_pos])
        # Skicka inget ifall det inte finns någon möjlig ersättare.
        except IndexError:
            return
        return suggestion

    def write_to_report(self):
        return "[Line {}] {}: {}".format(self.row_number,
                                         self.word,
                                         self.suggest())
        """Skriv in relevant information till rapporten."""
        return "[Line {}] {}: {}".format(self.row_number,
                                         self.word,
                                         self.suggest())

    def __str__(self):
        """Skirv ut vilket ord som undersöks."""
        return self.word


class Report(object):
    """Klassen Report."""

    def __init__(self, text, lexicon, list_length, sorted_dict):
        """Initiera Report med nedanstående instansvariabler."""
        self.file = open(text, "r", encoding = "utf-8")
        self.text_name = text
        self.text = self.file.readlines()
        self.file.close()
        self.spelling_warnings = []
        self.lexicon = lexicon_name
        self.list_length = list_length
        self.sorted_dict = sorted_dict

    def text_modifier(self, text):
        """Modifiera raden som ska rättas."""
        string_to_modify = str(text).replace("\n", " ").lower()
        list_to_modify = re.sub("[\W_]+", " ", string_to_modify).split(" ")
        list_to_modify.remove("")
        return list_to_modify

    def is_in_lexicon(self, word):
        """Kolla igenom hela lexikonet för att se om ordet är felstavat."""
        i = 0
        # Loopa över lexikonet.
        while i < len(self.sorted_dict):
            # Returnera sant om ordet finns.
            if word in self.sorted_dict.keys():
                return True
            # Returnerna falskt om ordet inte finns.
            elif i == len(self.lexicon):
                return False
            i += 1

    def comparer(self):
        """Skapa varning om ordet inte finns i lexikonet."""
        print("¤ Looking for unknown words in {}".format(self.text_name))
        row_number = 0
        # Ta varje rad och modifiera den.
        for row in self.text:
            row_number += 1
            row = self.text_modifier(row)
            #print(row)
            # Ta varje ord i den modifierade raden och anropa is_in_lexicon.
            # Skapa varning beroende på returen.
            for word in row:
                # Kolla om det är en tom sträng.
                if word == "":
                    break
                # Om det inte är en tom sträng.
                if not self.is_in_lexicon(word) and word.isalpha():
                    self.spelling_warnings.append(SpellingWarning(
                                                  self.lexicon,
                                                  word,
                                                  row_number,
                                                  self.list_length))
        print("¤ Found {} unknown words.".format(len(self.spelling_warnings)))
        return self.spelling_warnings

    def save(self, start_time):
        """Ta in spelling_warnings och skriv in förslag i rapporten."""
        self.comparer()
        txt_file = open("report_" + self.text_name, "w", encoding="utf-8")
        txt_file.write("*******************************" +
                       "*******************************" +
                       "***************************\n")
        # Låt alla spelling_warnings skriva ut sina förslag.
        for spelling_warning in self.spelling_warnings:
            txt_file.write(spelling_warning.write_to_report() + "\n")
        run_time = time() - start_time
        txt_file.write("Time to write report: " + str(run_time) + "\n")
        txt_file.write("*******************************" +
                       "*******************************" +
                       "***************************\n")
        txt_file.close()
        return txt_file

    def __str__(self):
        """Skicka vidare rapportens namn."""
        return "report_{}".format(self.text_name)


class Lexicon(object):
    """Klassen Lexicon."""

    def __init__(self, filepath):
        """Initiera klassen Lexicon och skicka med en sökväg."""
        self.filepath = filepath

    def load_freq_data(self):
        """Skapa en lista och ett dict av lexikonet."""
        print("¤ Reading lexicon {}".format(self.filepath))
        file = open(self.filepath, encoding='utf-8')
        freq_data_list = []
        freq_data_dict = {}
        # Behandla varje rad i lexikonet så att de blir element i en
        # lista/dict.
        for line in file:
            line = line.rstrip().split("\t")
            freq_data_list.append(line)
            freq_data_dict[line[0]] = line
        file.close()
        return freq_data_list, freq_data_dict

    def __str__(self):
        """Skriv ut lexikonet som en sträng när det printas."""
        return str(self.lexicon)


def main():
    """Scriptet körs enligt nedanstånde anvisningar."""
    start_time = time()
    lexicon_name = sys.argv[1]
    list_length = int(sys.argv[2])
    sorted_lexicon = sorted_data[0]
    sorted_dict = sorted_data[1]
    list_of_reports = []
    # Skapa rapport för varje "text-argument" i terminalen.
    for text in sys.argv[3:]:
        report = Report(text, sorted_lexicon, list_length, sorted_dict)
        list_of_reports.append(report)
    # Spara rapporten i en fil.
    for report in list_of_reports:
        report.save(start_time)
    print("¤ Suggestions written in reports: ")
    # Printa report.
    for report in list_of_reports:
        print(report)
    run_time = time() - start_time
    print("\n" + "Runtime: " + str(run_time))



if __name__ == "__main__":
    main()
