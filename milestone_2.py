import random


guess = input('Enter a single letter: ')

if len(guess) == 1 and guess.isalpha():
    print('Good guess!')
else:
    print('Oops! That is not a valid input.')



word_list = ['banana', 'strawberry', 'apple', 'papaya', 'grape']

print(word_list)

for i in range(100):
    word = random.choice(word_list)
    print(word)
