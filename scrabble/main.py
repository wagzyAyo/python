from words import Words
from instace import Scrabble
import random

scrabbled_words = []

for word in Words:
    scrabbled_words.append(word)

word_to_guess = random.choice(scrabbled_words)

scrabble = Scrabble(word_to_guess)
