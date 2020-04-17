
class Text(object):

    def __init__(self, value):
        self.text = value
        self.text_split = value.split("\n")

    def create_list_of_sentences(self):
        list_of_sentences = []
        for sentence in self.text_split:
            list_of_sentences.append(Sentence(sentence))
        return list_of_sentences

    def count_amount_of_sentences(self):
        return len(self.text_split)

    def count_amount_of_words_tot(self):
        sum_of_words = 0
        for sentence in self.create_list_of_sentences():
            sum_of_words += sentence.count_amount_of_words()
        return sum_of_words

    def count_amount_of_tokens_tot(self):
        sum_of_tokens = 0
        for sentence in self.create_list_of_sentences():
            sum_of_tokens += sentence.count_amount_of_tokens()
        return sum_of_tokens

    def __str__(self):
        index = 1
        str1 = "Texten innehåller {} meningar, {} ord/skiljetecken, {} tecken. \n"
        str2 = "Mening {} "
        string_to_return = ""
        for sentence in self.create_list_of_sentences():
            string_to_return += str2.format(str(index)) + sentence.__str__() + "\n"
            index +=1
        return str1.format(self.count_amount_of_sentences(),
                           self.count_amount_of_words_tot(),
                           self.count_amount_of_tokens_tot()) + string_to_return


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

    def count_amount_of_tokens(self):
        sum_of_tokens = 0
        for word in self.create_list_of_words():
            sum_of_tokens += word.count_amount_of_tokens()
        return sum_of_tokens

    def __str__(self):
        str = "innehåller {} ord/skiljetecken ({} tecken)"
        return str.format(self.count_amount_of_words(),
                          self.count_amount_of_tokens())

class Token(object):

    def __init__(self, value):
        self.word = value

    def count_amount_of_tokens(self):
        return len(self.word)

def Main():
    file = open("Lorem.txt", "r")
    text_file = file.read()
    file.close()
    text = Text(text_file)
    if __name__ == "__main__":
        print(text)

Main ()
