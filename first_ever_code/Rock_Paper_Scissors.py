import random


def ask():
    choice = raw_input("Rock, Paper, or Scissors?: ").lower()
    if choice == "rock" or choice == "r":
        return 1
    elif choice == "paper" or choice == "p":
        return 2
    elif choice == "scissors" or choice == "s":
        return 3
    else:
        print "Invalid Input"
        ask()


def test(intchoice, comp):
    if intchoice == comp:
        print "Tie"
        return "Tie"
    elif (intchoice == 1 and comp == 2) or (intchoice == 2 and comp == 3) or (intchoice == 3 and comp == 1):
        print "Computer wins!"
        return "CP"
    elif (intchoice == 1 and comp == 3) or (intchoice == 2 and comp == 1) or (intchoice == 3 and comp == 2):
        print "You Win!"
        return "PL"
    else:
        print "PROBLEM"


def computer():
    comp = random.randint(1, 3)
    return comp


def play(rounds):
    stats = []
    for item in range(rounds):
        my_choice = ask()
        computer_choice = computer()
        stats.append(test(my_choice, computer_choice))
    return stats


def pre_round():
    return int(raw_input("How many Rounds?: "))


def statistics(stats):
    ties = 0
    computer_wins = 0
    player_wins = 0
    for item in stats:
        if item == "Tie":
            ties += 1
        elif item == "CP":
            computer_wins += 1
        elif item == "PL":
            player_wins += 1
    print "Ties: %i" % ties
    print "Loses: %i" % computer_wins
    print "Wins: %i" % player_wins


rounds = pre_round()
stats = play(rounds)
statistics(stats)
