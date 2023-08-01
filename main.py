import math

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

operator = int(input("Vælg en funktion: \n1 - plus\n2 - minus\n3 - gange\n4 - divider\n"))
tal1 = float(input("Vælg første tal: "))
tal2 = float(input("Vælg andet tal: "))

print("Resultat:")
if(operator == 1):
    print(add(tal1,tal2))
elif(operator == 2):
    print(subtract(tal1,tal2))
elif(operator == 3):
    print(multiply(tal1,tal2))
elif(operator == 4):
    print(divide(tal1,tal2))
else:
    print("Ugyldig valg")