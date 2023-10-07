

class Scrabble():
    guess = set()  # Make sure each word is only stored once
    score = 0

    def __init__(self, word):
        self.word = word
        print(f"Unscrable this word {self.word}")
        print("You only have 5 chances")
        print(f"Your score: {Scrabble.score}")

    def answer(self, ans):
        if ans in self.word:
            if ans not in Scrabble.guess:
                print("Correct!")
                self.score(answer=ans)
                Scrabble.guess.append(ans)
            else:
                print("Word already guessed")

    def score(self, answer):
        score_point = len(answer)
        Scrabble.score += score_point
