""" Function to print the longest word in any sequence
"""


def longest_word(string_list):
    longest = [""]
    for word in string_list:
        if len(word) > len(longest):
            longest = [word]
        elif len(word) == len(longest[0]):
            longest.append(word)

    return longest


words = []
word_ = ""
while word_ != "1":
    word_ = input("Add word to list (or 1 to end): ")
    words.append(word_)
print(f"The longest word in the sequence {words} is {longest_word(words)}")
