from random import randint

total_games = 0
total_wins = 0

num_cases = 26
num_doors = 3

num_trials = 5000


def play_round_dond(switch, ignore_fails, recurse):
    global total_wins
    global total_games
    
    cases = [False] * (num_cases - 1)
    cases.append(True)
    my_case = cases.pop(randint(0, num_cases - 1))
    
    while(len(cases) > 1):
        cases.pop(randint(0, len(cases) - 1))

    other_case = cases.pop()

    if(my_case != True and other_case != True and ignore_fails):
        if(recurse):
            return play_round_dond(switch, ignore_fails, recurse)
        else:
            return
            

    if(switch):
        my_case, other_case = other_case, my_case
    
    if(my_case == True):
        total_wins += 1

    total_games += 1


def play_round_monty(switch, smart):
    global total_wins
    global total_games

    doors = [False] * num_doors
    doors[randint(0,num_doors - 1)] = True

    my_door = doors.pop(randint(0, num_doors - 1))

    while(len(doors) > 1):
        index = randint(0, len(doors) - 1)
        if(doors[index] and smart):
            continue
        doors.pop(index)

    other_door = doors.pop()

    if(not smart and my_door is False and other_door is False):
        return

    if(switch):
        my_door, other_door = other_door, my_door

    if(my_door == True):
        total_wins += 1

    total_games += 1

for x in range(num_trials):
    play_round_dond(True, True, True)
    #play_round_monty(True, False)


print(str(total_wins / total_games * 100))
