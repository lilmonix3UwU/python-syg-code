import random


working = 1

print(random)

while(working == 1):
    us = input("vil du ha et tilfældigt tal?  ja / nej:  ")
    if us == "ja":
        randomnumber = random.randrange(1, 6)
        print(randomnumber)

