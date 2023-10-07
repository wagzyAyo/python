SCORE = 0


class Scrabble():
    guess = []  # Make sure each word is only stored once

    def __init__(self, word):
        self.word = word
        self.word_list = list(word)
        print(f"Unscrable this word {self.word_list}")
        print(Scrabble.guess)

    def answer(self, ans):
        global SCORE

        if set(ans) <= set(self.word_list):
            if ans not in Scrabble.guess:
                print("Correct!")
                Scrabble.guess.append(ans)
                print(f"Your score is {self.score(ans)}")
            else:
                print("Word already guessed")
        else:
            print("word does not match the given letters")

        print(SCORE)

    def score(self, answer):
        global SCORE
        score_point = len(answer)
        SCORE += score_point
        return SCORE
