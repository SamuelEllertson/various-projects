'''finds a numeric soution to the problem: Given a deck of cards, what position is most likely to contain the final ace?'''

from random import sample
from collections import Counter

def get_ace_position():
    return max(sample(range(1,53), 4))

def main():
    trials = 100000
    count = Counter(get_ace_position() for _ in range(trials))
    
    position, wins = count.most_common()[0]

    print(f"{position=}")
    print(f"{trials=}")
    print(f"{wins=}")
    print(f"percentage: {wins / trials * 100}")

if __name__ == '__main__':
    main()