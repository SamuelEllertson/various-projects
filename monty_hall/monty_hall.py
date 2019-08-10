from random import randint

def main():
    n = 10000
    count = 0
    wins = 0

    for i in range(n):
        choice = getVal()
        car = getVal()

        opened = getVal(choice, car)

        if opened == car:
            continue

        count += 1

        if choice != car:
            wins += 1

    print(f"probability is: {wins / count:.3f}")

def getVal(choice=None, car=None):
    if choice is None:
        return randint(1,3)

    while True:
        temp = randint(1,3)

        if temp == choice or temp == car:
            continue

        return temp

if __name__ == '__main__':
    main()
