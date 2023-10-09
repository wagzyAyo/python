from answers import words_answers
import random
SCORE = 0


class Scrabble():
    guess = set()  # Make sure each word is only stored once

    def __init__(self, word):
        self.word = word
        self.word_list = list(self.word)
        print(f"Unscrable this word {self.word_list}")
        print(Scrabble.guess)

    def answer(self, ans):
        global SCORE

        if ans in Scrabble.guess:
            print("Word already guessed")

        elif set(ans) <= set(self.word_list) and ans in words_answers[self.word]:

            print("Correct!")
            print(f"You score {self.score(ans)}pts for your {ans} word")
            Scrabble.guess.add(ans)
            print(f"Your total score is {SCORE}")
        else:
            print("word does not match the given letters")

    def score(self, answer):
        """This method calculate users score
        and return user score points for each corrected guess"""
        global SCORE
        score_point = len(answer)
        SCORE += score_point
        return score_point
