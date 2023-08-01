import math

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def power(x,y):
    return pow(x,y)

def squareRoot(x):
    return math.sqrt(x)


operator = int(input("Vælg en funktion: \n1 - plus\n2 - minus\n3 - gange\n4 - divider\n5 - power\n6 - square root\n"))
tal1 = float(input("Vælg første tal: "))
tal2 = float(input("Vælg andet tal: "))

print("Resultat:")
match operator:
    case 1:
        print(add(tal1,tal2))
    case 2:
        print(subtract(tal1,tal2))
    case 3:
        print(multiply(tal1,tal2))
    case 4:
        print(divide(tal1,tal2))
    case 5:
        print(power(tal1, tal2))
    case 6:
        print(squareRoot(tal1))
    case _:
        print("Ugyldig valg")