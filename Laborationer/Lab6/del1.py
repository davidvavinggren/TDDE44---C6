"""TDDE44, Labb 6, Del 1."""


class Text(object):
    """Klassen Text."""

    def __init__(self, value):
        """Initiera instansen och ta in texten i fråga."""
        self.text = value
        self.text_split = value.split("\n")
        self.sentence = self.create_list_of_sentences()

    def create_list_of_sentences(self):
        """Dela upp texten i meningar och placera meningarna i en lista."""
        list_of_sentences = []
        # addera meningarna till en lista
        for sentence in self.text_split:
            list_of_sentences.append(Sentence(sentence))
        return list_of_sentences

    def count_amount_of_sentences(self):
        """Beräkna antalet meningar."""
        return len(self.text_split)

    def count_amount_of_words_tot(self):
        """Beräkna antalet ord i texten."""
        sum_of_words = 0
        # För varje mening; addera summan av ord till en totalsumma
        for sentence in self.sentence:
            sum_of_words += sentence.count_amount_of_words()
        return sum_of_words

    def count_amount_of_chars_tot(self):
        """Beräkna antalet tecken i texten."""
        sum_of_chars = 0
        # För varje mening; addera summan tecken till en totalsumma
        for sentence in self.sentence:
            sum_of_chars += sentence.count_amount_of_chars()
        return sum_of_chars

    def __str__(self):
        """Printa enligt anvisning."""
        index = 1
        str1 = ("Texten innehåller {} meningar," +
                "{} ord/skiljetecken, {} tecken.\n")
        str2 = "Mening {} "
        str_to_return = ""
        # loopa genom meningarna och använd deras räknemetoder
        for sentence in self.sentence:
            str_to_return += (str2.format(str(index)) + sentence.__str__() +
                              "\n")
            index += 1
        return str1.format(self.count_amount_of_sentences(),
                           self.count_amount_of_words_tot(),
                           self.count_amount_of_chars_tot()) + str_to_return


class Sentence(object):
    """Klassen Sentence."""

    def __init__(self, value):
        """Initiera sentence, ta med mening och skapa en lista med ord."""
        self.sentence = value
        self.split_sentence = self.sentence.split(" ")
        self.words = self.create_list_of_words()

    def create_list_of_words(self):
        """Gör en lista med tokenobjekt och returna den."""
        list_of_words = []
        # loopa genom listan med ord
        for word in self.split_sentence:
            list_of_words.append(Token(word))
        return list_of_words

    def count_amount_of_words(self):
        """Räkna ihop alla ord i meningen."""
        return len(self.split_sentence)

    def count_amount_of_chars(self):
        """Räkna ihop summan av alla tecken i ordlistan."""
        sum_of_chars = 0
        # loopa genom alla ord i listan
        for word in self.words:
            sum_of_chars += word.count_amount_of_chars()
        return sum_of_chars

    def __str__(self):
        """Printa enligt nedan, använd räknemetoderna."""
        str = "innehåller {} ord/skiljetecken ({} tecken)"
        return str.format(self.count_amount_of_words(),
                          self.count_amount_of_chars())


class Token(object):
    """Klassen token."""

    def __init__(self, value):
        """Initiera och ta in ett ord."""
        self.word = value

    def count_amount_of_chars(self):
        """Räkna hur många tecken ett ord har."""
        return len(self.word)


def Main():
    """Huvudfunktion där allt körs."""
    file = open("Lorem.txt", "r")
    text_file = file.read()
    file.close()
    text = Text(text_file)
    if __name__ == "__main__":
        print(text)


Main()
"""Kalla på Huvudfunktion där allt körs."""
