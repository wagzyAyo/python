from words import Words
from instace import Scrabble
import random

scrabbled_words = []

for word in Words:
    scrabbled_words.append(word)

game_on = True
guess = 0

while game_on:
    def game(opt):
        word_to_guess = random.choice(scrabbled_words)

        while opt <= 4:
            scrabble = Scrabble(word_to_guess)
            guess_ans = input("your guess word ? ")
            scrabble.answer(guess_ans)
            opt += 1
    game_cont = input('want to continue? Y or N ')
    if game_cont == "Y":
        game(guess)
    if game_cont == "N":
        game_on = False
