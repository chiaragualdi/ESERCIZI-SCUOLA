#Alla fine della giornata di elezioni per il ballottaggio tra due candidati, si acquisiscono i voti ottenuti dai due candidati.
Scrivi il programma che calcoli le percentuali ottenute da ciascun candidato e comunichi il nome del vincitore.
x=int(input("Inserisci il numero divoti ottenuti dal primo candidato"))
y=int(input("Inserisci il numero di voti ottenuti dal secondo candidato"))
tot=int(x+y)
xperc=int(x*100/tot)
yperc=int(y*100/tot)
if xperc>yperc:
    print("Il vincitore è il primo candidato")
else:
    print("Il vincitore è il secondo candidato")