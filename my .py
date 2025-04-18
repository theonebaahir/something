import string

def has_symbol_or_number(word):
    for char in word:
        if char in string.digits or char in string.punctuation:
            return True
    return False

# Example usage
word = input("Enter a word: ")

if has_symbol_or_number(word):
    print("The word contains a symbol or a number.")
else:
    print("The word does not contain any symbol or number.")
