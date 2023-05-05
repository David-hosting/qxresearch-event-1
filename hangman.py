import random
from os import system

WORDS =  ["hangman","banana","tomato","python","minecraft","potato","android"]
choosed_word = list(random.choice(WORDS))
MAX_TRIES = 6 #print(MAX_TRIES)
used_letters = []
wrong_letters = []
template = ["_" for i in range(len(choosed_word))]
HANGMAN_ASCII_ART = """ welcome to:
    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \\
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/
"""

ERR = ""
SYMBOLS = '!@#$%^&*()/*-+?\"\"\'\'><.,;:'



while True:

    system("cls")
    print(HANGMAN_ASCII_ART)
    print("Wrong used letters:", wrong_letters)

    if "".join(template) == "".join(choosed_word):
        print('Congrats, you won!')
        input("Press Enter to exit")
        break
    if MAX_TRIES == 0:
        print("You lost, the word was: {}".format("".join(choosed_word)))
        print("last ERR:", ERR)
        input("Press Enter to exit ")
        break

    print(f'You have {MAX_TRIES} lives left')
    print("".join(template))
    print(ERR)
    
    letter = input("guess a letter: ")
    if letter == "".join(choosed_word):
        system("cls")
        print(HANGMAN_ASCII_ART)
        print("Wrong used letters:", wrong_letters)
        print(f'You have {MAX_TRIES} lives left')
        print(letter)
        print(ERR)
        break
    if letter.lower() in used_letters:
        ERR = "You already tried this letter!"
        continue
    if len(letter) != 1:
        ERR = "length must me one!"
        continue
    if letter.isdigit() == True:
        ERR = "Answer cannot be a number! Please write a letter."
        continue
    if letter in SYMBOLS:
        ERR = "Answer cannot be a symbol! Please write a letter."
    else:

        if letter.lower() in choosed_word:
            used_letters.append(letter)
            for i in range(len(choosed_word)):
                if choosed_word[i] == letter.lower():
                    template[i] = letter.lower()

        else:
            MAX_TRIES -= 1
            used_letters.append(letter.lower())
            wrong_letters.append(letter.lower())
