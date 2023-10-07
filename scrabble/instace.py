

class Scrabble():
    guess = set()  # Make sure each word is only stored once
    score = 0

    def __init__(self, word):
        self.word = word
        print(f"Unscrable this word {self.word}")
        guess_ans = input("your guess word ? ")
        self.answer(guess_ans)
        print(Scrabble.score)

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
        Scrabble.score += score
        print(self.score)
