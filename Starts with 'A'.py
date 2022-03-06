def starts_with_a(word):
    if word[0] == "A":
        return True
    else:
        return False


# main
word_to_check = input("Enter word: ").upper()
print(starts_with_a(word_to_check))
