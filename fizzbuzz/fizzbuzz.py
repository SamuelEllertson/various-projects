from collections import OrderedDict 

def main():
    for i in range(20):
        print(fizzbuzz2(i))

def fizzbuzz(n):

    #Add custom condition functions here
    def divisible(n, x):
        return lambda: n % x == 0
    
    #add conditions here
    conditions = [
        ("fizz", divisible(n, 3)),
        ("buzz", divisible(n, 5))
    ]

    #business logic, no modifications necessary
    workingList = []
    for key, condition in conditions:
        if condition():
            workingList.append(key)

    return "".join(workingList) or n

def fizzbuzz2(n):
    conditions = OrderedDict()

    #add conditions here
    conditions["fizz"] = 3
    conditions["buzz"] = 5

    #business logic, no modifications necessary
    workingList = []
    for string, value in conditions.items():
        if n % value == 0:
            workingList.append(string)

    return "".join(workingList) or n

if __name__ == '__main__':
    main()