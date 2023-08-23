import random
# Punto 1

Numbers = []
numbersNeg = []

for i in range (1,11):
    aux = random.randint(0,10)
    Numbers.append(aux)
    i = str(i)
    aux2 = "-" + i
    numbersNeg.append(aux2)

for i in numbersNeg: 
    print(i)

#punto 2

M1 = [[8.5, 14.8, -6.45], [12.515,7.1,4.02], [-11.45,3.79,21.55]]

#punto 3


#punto 4
lista1 = []

for i in range (1,101):
    if i % 3 ==0: 
        i = "m3"
    lista1.append(i)
    