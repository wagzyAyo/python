from words import Words
from instace import Scrabble
import random

scrabbled_words = []

for word in Words:
    scrabbled_words.append(word)

game_on = True
guess = 0


def game(opt):
    word_to_guess = random.choice(scrabbled_words)
    print("You only have 5 chances")

    while opt <= 4:
        scrabble = Scrabble(word_to_guess)
        guess_ans = input("your guess word ? ")
        scrabble.answer(guess_ans)
        opt += 1


while game_on:
    game(guess)

    game_cont = input('want to continue? Y or N ')
    if game_cont == "Y" or game_cont == "y":
        Scrabble.guess.clear()
        game(guess)
    elif game_cont == "N" or game_cont == "n":
        game_on = False
