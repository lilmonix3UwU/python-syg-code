import random


working = 1


while(working == 1):
    randomnumber = random.randrange(1, 6)
    

    us = int(input("gæt et tilfældigt tal mellem 1 og 6:   "))
   
    if us == randomnumber:
        print ("tillykke du gætede rigtid ")
       
    if us != randomnumber:
        print ("fårk deg då topte")
