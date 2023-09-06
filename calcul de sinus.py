# ce programme permet de faire la division de sin(x) et x .
print("ce programme permet de faire la division de sin(x) et x")
from math import sin
n = int(input("entrer un nombre pour debuter l'intervalle des nombres :"))
x = int(input("entrer un nombre pour cloturer l'intervalle des nombres:"))
for i in range(-n, x+1):

    try:
        print("la division de ce calcul en remplaçant dans la fonction x par",i," est:",sin(i)/i)
    except:
        print("Nous ne pouvons pas faire la division  d'un nombre par 0")
