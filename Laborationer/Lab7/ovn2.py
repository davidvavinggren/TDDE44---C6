from time import time


def load_freq_data(filepath):
    """Läs in och returnera frekvensdata från filen med sökvägen filepath.

    Returnerar en lista där varje element i listan är en lista med två element
    med följande struktur: [ord, frekvens]
    """
    file = open(filepath)
    freq_data = []
    for line in file:
        freq_data.append(line.rstrip().split("\t"))
    file.close()
    return freq_data


def average_len_of_matches(substring, freq_data):
    """Returnera en lista med ord från freq_data som innehåller substring."""
    matches = []
    for word_freq in freq_data:
        if substring in word_freq[0]:
            matches.append(len(word_freq[0]))
    return sum(matches) / len(matches)


def run():
    substrings = ["guld", "funktion", "python", "program", "programmering",
                  "start", "avbryt", "begränsa", "stor", "ord", "ing"]

    freq_data = load_freq_data("webbnyheter2013_stats.tsv")

    start_time = time()
    for substring in substrings:
        avg_len = average_len_of_matches(substring, freq_data)
        print("Genomsnittslängden på ord som innehåller '{}' är {} tecken."
              .format(substring, avg_len))
    run_time = time() - start_time
    print("Körtid: {} sekunder.\n".format(run_time))


if __name__ == "__main__":
    run()
