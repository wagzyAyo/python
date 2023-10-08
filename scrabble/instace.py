from answers import words_answers
SCORE = 0


class Scrabble():
    guess = set()  # Make sure each word is only stored once
    incorrect_guess = set()  # store incorrect guess

    def __init__(self, word):
        self.word = word
        self.word_list = list(word)
        print(f"Unscrable this word {self.word_list}")
        print(Scrabble.guess)

    def answer(self, ans):
        global SCORE

        if ans in Scrabble.guess:
            print("Word already guessed")

        elif set(ans) <= set(self.word_list):
            print("Correct!")
            Scrabble.guess.add(ans)
            print(f"Your score is {self.score(ans)}")
        else:
            print("word does not match the given letters")
            Scrabble.incorrect_guess.add(ans)

    def score(self, answer):
        global SCORE
        score_point = len(answer)
        SCORE += score_point
        return SCORE
