import random as r

# Task 1: Random Choice Game
print('Task 1: Random Choice Game')

colors = ['red', 'blue', 'yellow', 'purple', 'orange', 'green']
rndm_color = r.choice(colors)
user_guess = input('Guess the color I\'m thinking of: ')

print(f'You are correct! I was thinking of {rndm_color}!' if user_guess == rndm_color else 'That is incorrect.')