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

        if all(ans.count(letter) <= self.word_list.count(letter) for letter in ans):
            if ans not in Scrabble.guess and ans in words_answers[self.word]:
                print("Correct!")
                Scrabble.guess.append(ans)
                print(f"Your score is {self.score(ans)}")
            else:
                print("Word already guessed")
        else:
            print("word does not match the given letters")
            Scrabble.incorrect_guess.add(ans)

    def score(self, answer):
        global SCORE
        score_point = len(answer)
        SCORE += score_point
        return SCORE
