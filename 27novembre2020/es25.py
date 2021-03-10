candidato1=input("Inserisci il nome del primo candidato: ")
voti1=int(input("Inserisci i voti che ha ottenuto: "))
candidato2=input("Inserisci il nome del secondo candidato: ")
voti2=int(input("Inserisci i voti che ha ottenuto: "))
lista1 = [candidato1, candidato2]
lista2 = [voti1, voti2]
lista1.sort()
lista2.sort()
lista2.reverse()
print(lista1)
print(lista2)