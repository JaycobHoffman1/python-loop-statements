# Task 1: The Selective DJ
print('Task 1: The Selective DJ')

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
second_to_fourth_track = genres[1:4]

print('The second to fourth tracks are as follows:')
for track in second_to_fourth_track:
    print(track)


# Task 2: The One-Liner Band with List Comprehensions
print('Task 2: The One-Liner Band with List Comprehensions')

new_list = [f'{genre} Music' for genre in genres]

print(f'The new list is as follows: {new_list}')


# Task 3: Numerical Beats with range
print('Task 3: Numerical Beats with range')

for i in range(1, 11)[::-1]:
    print(i)
print('The beat drops now!')