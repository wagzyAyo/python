
class Scrabble():
    guess = set()  # Make sure each word is only stored once

    def __init__(self, word):
        self.word = word
        print(f"Unscrable this word {self.word}")

    def answer(self, ans):

        if ans in self.word:
            if ans not in Scrabble.guess:
                print("Correct!")
                self.score(answer=ans)
                Scrabble.guess.append(ans)
            else:
                print("Word already guessed")
            print(f"Your score: {self.score(ans)}")

    def score(self, answer):
        self.score = 0
        score_point = len(answer)
        self.score += score_point
        return self.score
