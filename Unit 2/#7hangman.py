#Group Challenge: HANGMAN PROBLEM

words = ['one', 'five', 'three']

import random

word_index = random.randint(0,len(words)-1) #random.choice
word = words[word_index]

answer = []

for char in word:
    answer += '_'
print(answer)

guess = input('please guess: ')
if guess in word:
    letter_position = word.index(guess,0,len(word)-1)
    print(letter_position)
    guess = input('correct! please continue: ')
else:
    guess = input('guess again: ')


print(answer)