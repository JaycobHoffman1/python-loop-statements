import random as r

# Task 1: Your Mood Tracker
print('Task 1: Your Mood Tracker')

moods = ['happy', 'sad', 'energetic', 'calm']
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
times_of_day = ['morning', 'afternoon', 'evening']

for day in days_of_week:
    for time in times_of_day:
        print(f'On {day} {time}, you were feeling {r.choice(moods)}.')