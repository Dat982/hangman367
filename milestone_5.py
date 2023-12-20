import random

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_' for letter in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = list()
    def check_guess(self, guess):
        f_guess = guess.lower()
        if f_guess in self.word:
            self.num_letters -=1 
            print(f'Good guess! {guess} is in the word.')
            for i, x in enumerate(self.word):
                if x == f_guess:
                    self.word_guessed.pop(i)
                    self.word_guessed.insert(i,f_guess)
        else:
            self.num_lives -= 1
            print(f'Sorry, {f_guess} is not in the word.')
            print(f'You have {self.num_lives} lives left')
    def ask_for_input(self):
        # while True:
        guess = input('Enter a single letter: ')
        if len(guess) != 1:
            print('Invalid letter. Please, enter a single alphabetical character.')
        elif guess in self.list_of_guesses:
            print('You already tried guessing the letter')
        else:
            self.check_guess(guess)
            self.list_of_guesses.append(guess)


def play_game(word_list, num_lives = 5):
    game = Hangman(word_list = word_list, num_lives = num_lives)
    while True:
        if game.num_lives == 0:
            print('You lost')
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        elif game.num_letters == 0:
            print('Congratulations. You won the game!')
            break

if __name__ == '__main__':
    play_game(word_list = ['banana', 'strawberry', 'apple', 'papaya', 'grape'])
