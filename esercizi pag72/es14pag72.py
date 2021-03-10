#Crea un programma che scriva la differenza di due numeri a e b se il prodotto è maggiore di 10,
# oppure la loro somma se il prodotto è minore o uguale a 10.
a=int(input("Inserisci il valore di a: "))
b=int(input("Inserisci il valore di b: "))
prodotto=a*b
if prodotto>10:
    differenza=a-b
    print("La loro differenza è", differenza)
else:
    somma=a+b
    print("La loro somma è", somma)
