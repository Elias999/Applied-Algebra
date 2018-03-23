#! /usr/bin/python3

def ekp(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm

n = int(input("Δώστε φυσικό"))
kyklos_1 = int(n/2)
kyklos_2 = n - kyklos_1
while 1:
    print("Τάξη",ekp(kyklos_1,kyklos_2))
    if kyklos_1 ==  1 or kyklos_2 == 1:
        print ("Οχι αλλες τάξεις")
        break
    kyklos_1 +=1
    kyklos_2 -=1
