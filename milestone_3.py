import random

word_list = ['banana', 'strawberry', 'apple', 'papaya', 'grape']

word = random.choice(word_list)

def check_guess(guess):
    if guess.lower() in word:
        print(f'Good guess! {guess} is in the word. The word is {word}')
        return True
    else:
        print(f'Sorry, {guess} is not in the word. Try again.')
        return False

def ask_for_input():
    while True:
        guess = input('Enter a single letter: ')
        if len(guess) == 1 and guess.isalpha():
            print('Valid guess')
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')
    check_guess(guess)


ask_for_input()