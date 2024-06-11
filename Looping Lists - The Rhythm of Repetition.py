# Task 1: The for Loop DJ Set
print('Task 1: The for Loop DJ Set')

genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

counter = 1
for genre in genres:
    if genre == 'Jazz':
        print(f'Track {counter} - {genre}: A vibrant, swinging beat!')
    elif genre == 'Rock':
        print(f'Track {counter} - {genre}: A loud and exciting ride!')
    elif genre == 'Hip-hop':
        print(f'Track {counter} - {genre}: An energetic, rhythmic flow!')
    elif genre == 'Classical':
        print(f'Track {counter} - {genre}: A beautiful opera featuring a myriad of instruments!')

    counter += 1


# Task 2: The Remix Artist with while
print('Task 2: The Remix Artist with while')

counter = 0
while counter < len(genres):
    if genres[counter] == 'Jazz':
        print(f'Track {counter + 1} - {genres[counter]}: A vibrant, swinging beat!')
    elif genres[counter] == 'Rock':
        print(f'Track {counter + 1} - {genres[counter]}: A loud and exciting ride!')
    elif genres[counter] == 'Hip-hop':
        print(f'Track {counter + 1} - {genres[counter]}: An energetic, rhythmic flow!')
        break
    elif genres[counter] == 'Classical':
        print(f'Track {counter + 1} - {genres[counter]}: A beautiful opera featuring a myriad of instruments!')

    counter += 1


# Task 3: Light Show Technician Loop
print('Task 3: Light Show Technician Loop')

for i in range(len(genres)):
    if genres[i] == 'Jazz' or genres[i] == 'Classical':
        continue
    else:
        print(f'Track {i + 1} - The {genres[i][0].lower()}{genres[i][1:]} light show is ready!')