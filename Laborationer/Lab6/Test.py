from del1 import Text, Sentence, Token

file = open("Lorem.txt", "r")
text_file = file.read()
file.close()

text = Text(text_file)

if __name__ == "__main__":
    print(text)
