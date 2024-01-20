import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while "-" in word  or ' ' in word:
        word  = random.choice(words)

    return word.upper()

def hangman():
    word  = get_valid_word(words)
    word_letters = set(word) 
    alphabet  = set(string.ascii_uppercase)
    used_letters = set()

    while len(word_letters) > 0:

        print("\nYou have used these letters: ", ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]

        print('\nCurrent word: ', ' '.join(word_list))

        user_letter = input('\nGuess a letter: ').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print("\n*** You already guessed that letter ***")

        else:
            print('Invalid')

    print("\n\n---- ",word," ----")

hangman()

