from words import Words
from instace import Scrabble
import random

scrabbled_words = []

for word in Words:
    scrabbled_words.append(word)

game_on = True
guess = 0

while game_on:
    word_to_guess = random.choice(scrabbled_words)

    while guess <= 5:
        scrabble = Scrabble(word_to_guess)
        guess += 1
    game = input('want to continue? Y or N ')
    if game == "N":
        game_on = False
