file = open("Lorem.txt", "r")
text_file = file.read()
file.close()


class Text(object):

    def __init__(self, value):
        self.text = value
        self.text_split = value.split("\n")

    def create_list_of_sentences(self):
        list_of_sentences = []
        for sentence in self.text_split:
            list_of_sentences.append(Sentence(sentence))

    def count_amount_of_sentences(self):
        return len(self.text_split)


class Sentence(object):

    def __init__(self, value):
        self.sentence = value
        self.split_sentence = self.sentence.split(" ")

    def create_list_of_words(self):
        list_of_words = []
        for word in self.split_sentence:
            list_of_words.append(Token(word))
        return list_of_words

    def count_amount_of_words(self):
        return len(self.split_sentence)

    def count_amount_of_chars(self):
        sum_of_chars = 0
        for word in self.create_list_of_words():
            sum_of_chars += word.count_amount_of_chars()
        return sum_of_chars

    def __str__(self)
        str = "innehåller" + "{}" +"ord/skiljetecken" + "(" +
              "{}" + "tecken"  + ")"
        return str.format(self.count_amount_of_words(),
                          self.count_amount_of_chars())

class Token(object):

    def __init__(self, value):
        self.word = value

    def count_amount_of_tokens(self):
        return len(self.word)
