# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")
#Class longestword inherits wordgame
class LongestWord(WordGame):

    def __init__(self, rounds: int):
        super().__init__(rounds)


#method round_winner overides round_winner in wordgame class  
    def round_winner(self, player1_word: str, player2_word: str):

       if len(player1_word) > len(player2_word):

            return 1

       elif len(player2_word) > len(player1_word):

            return  2

    

class MostVowels(WordGame):

    def __init__(self, rounds: int):

        super().__init__(rounds)

#method round_winner overides round_winner in wordgame class 
    def round_winner(self, player1_word: str, player2_word: str):

        vowels = "aeiou"
        player1_vowels = 0
        player2_vowels = 0

        for char in player1_word:

            if char in vowels:
                player1_vowels += 1


        for char in player2_word:

            if char in vowels:
                player2_vowels += 1

        
        if player1_vowels > player2_vowels:

            return 1

        elif player2_vowels > player1_vowels:

            return 2
    

class RockPaperScissors(WordGame):

    def __init__(self, rounds: int):
        super().__init__(rounds)

    
    def round_winner(self, player1_word: str, player2_word: str):
        
        words = {"rock":0, "paper": 1, "scissors": 2}

        if player1_word not in words and player2_word not in words:
            return 0

        if player1_word not in words:
            return 2

        if player2_word not in words:
            return 1

        difference = words[player1_word] - words[player2_word]

        if difference == 0:
            return 0
        elif difference == 1 or difference == -2:
            return 1
        
        return 2
              

if __name__ == "__main__":

    p = RockPaperScissors(3)
    p.play()
