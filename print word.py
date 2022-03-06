""" Function to print a word with a given number of capitals using .upper()
"""


def print_word(word, number):
    word1 = word[0:number]
    word2 = word[number:len(word)]
    print(f"{word1.upper()}{word2}")


# Main
word_ = input("Enter word here: ")
number_ = int(input("Enter number of capitals here: "))
print_word(word_, number_)
