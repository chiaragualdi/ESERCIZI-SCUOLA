#Calcola la media degli stipendi dei dipendenti di un'azienda, acquisiti con una ripetizione fino a quando si inserisce il valore -1 per segnalare la fine dell'input dei dati.

lista_stipendi = []
count = True
persona = 0
rip = 0
somma = 0
while count == True:
    persona += 1
    rip += 1
    print("Inserisci lo stipendio della persona", persona)
    stipendi_pers = int(input())
    lista_stipendi.append(stipendi_pers)
    x = input("Se vuoi fermarti inserisci -1, altrimenti inserisci 1: ")
    if x == -1:
            count = False
    else:
            pass
for i in lista_stipendi:
    somma += i
l = len(lista_stipendi)
print(lista_stipendi)
mediastipendi = somma/l
print(mediastipendi)
