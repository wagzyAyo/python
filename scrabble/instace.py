

class Scrabble():
    guess = []

    def __init__(self, word):
        self.word = word
        print(f"Unscrable this word {self.word}")
        ans = input("your guess word ? ")
        self.score = 0

    def answer(self, ans):
        if ans == self.word:
            if ans not in Scrabble.guess:
                print("Correct!")
                self.score(answer=ans)
                Scrabble.guess.append(ans)
            else:
                print("Word already guessed")

    def score(self, answer):
        score = len(answer)
        self.score += score
        print(self.score)
