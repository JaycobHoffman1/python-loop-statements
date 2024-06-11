import random as r

# Task 1: Your Mood Today
print('Task 1: Your Mood Today')

moods = ['happy', 'sad', 'energetic', 'calm']
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for i in range(len(days_of_week)):
    print(f'On {days_of_week[i]}, you were feeling {r.choice(moods)}.')