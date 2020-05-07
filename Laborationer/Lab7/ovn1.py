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


def word_in_data(word, freq_data):
    """Returnera True om word finns i freq_data, annars returnera False."""
    for word_freq in freq_data:
        if word_freq[0] == word:
            return True
    return False


def find_words_in_file(words, filepath):
    """Skriv ut om orden i words finns i filen med sökvägen filepath."""
    for word in words:
        freq_data = load_freq_data(filepath)
        print("{}: {}".format(word, word_in_data(word, freq_data)))


def run():
    words = ["python", "långsam", "snabb", "komplexitet"]
    start_time = time()
    find_words_in_file(words, "webbnyheter2013_stats.tsv")
    run_time = time() - start_time
    print("Körtid: {} sekunder.\n".format(run_time))


if __name__ == "__main__":
    run()
