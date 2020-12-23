#Dato un elenco di studenti partecipanti a una gara sportiva di lancio del peso (nome studente, lancio).
#Visualizza il valore del lancio del vincitore (valore massimo).

listanomi=[]
listalanci=[]
print("Per fermare il programma inserire stop")
while True:
    print("Inserisci il nome dello studente: ")
    nome=input()
    if nome=="stop":
        break
    else:
        listanomi.append(nome)
        lancio=int(input("Inserisci il valore in metri del lancio: "))
        listalanci.append(lancio)
massimo=max(listalanci)
print(massimo)
