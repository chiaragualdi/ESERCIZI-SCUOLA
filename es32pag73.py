#Implementa l'algoritmo per il calcolo della soluzione di un'equazione di primo grado ax+b=0.
#Il processo risolutivo dipende dai valori assunti dai coefficienti a e b secondo la tabella che segue.
a=float(input("Inserire il valore di a "))
b=float(input("Inserire il valore di b "))
if a==0:
    if b==0:
        print("L'equazione è indeterminata")
    else:
        print("L'equazione è impossibile")
elif b==0:
    print("Il risultato è x = 0")
else:
    result=(b/a)*-1
    print("Il risultato è x =", result)
