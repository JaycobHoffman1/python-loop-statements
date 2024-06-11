# Task 1: Loop Condition Exploration
print('Task 1: Loop Condition Exploration')

iteration_count = []
while 1 == 1:
    if len(iteration_count) < 5:
        print('This is an iteration of the while loop.')
    else:
        break
    iteration_count.append(0)


# Task 2: Conditional Exit
print('Task 2: Conditional Exit')

i = 0
while i < 5:
    print('This is an iteration of the while loop.')
    i += 1