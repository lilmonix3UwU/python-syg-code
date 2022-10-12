from pickletools import float8


fuck = 1
while fuck == 1:
    minlpus1 = input("skal du gange, dividere, minusse eller plusse???")
    num1 = float(input("tal 1:    "))
    num2 = float(input("tal 2:    "))
    resultat = 0


    if(minlpus1 == "-"):
        resultat = num1 - num2
       
    if(minlpus1 == "+"):
        resultat = num1 + num2
        
    if(minlpus1 == "/"):
        resultat = num1 / num2
        
    if(minlpus1 == "*"):
        resultat = num1 * num2
    print(resultat)

       
    


