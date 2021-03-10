# Utilizzare una struttura a coda per memorizzare i nomi dei pazienti.
# Scrivere un programma per registrare i nomi.
# Visualizzare il nome del primo paziente della coda.

lista = []
print ("Ricordo che per interrompere il programma inserire stop.")
while True:
    paziente = input("Inserire il nome del paziente: ").capitalize()
    if paziente == "stop":
        break
    else:
        lista.append(paziente)
index = 0
while index < len(lista):
    prossimo = lista.pop(index)
    print("Deve sottoporsi all'esame ", prossimo)
index += 1
print("Non ci sono altri pazienti in coda.")