#Costruisci un dizionario ottenuto da quello dell'esercizio 16 invertendo il ruolo di chiave e valore.
#Usa il nuovo dizionario per trovare il nome della nazione, noto il nome della capitale.

nazioni_capitali={
    "Italia":"Roma",
    "Francia":"Parigi",
    "Spagna":"Madrid",
    "Germania":"Berlino",
    "Regno unito":"Londra",
    "Portogallo":"Lisbona"
}
capitali_nazioni={capitali: nazioni for nazioni, capitali in nazioni_capitali.items()}
print("Per fermare il programma inserire stop.")
while True:
    capitale=input("Inserire una capitale: ").capitalize
    if capitale=="Stop":
        break
    elif capitale in capitali_nazioni:
        print(capitale, "è presente in", capitali_nazioni[capitale])
    else:
        print("La nazione non è presente.")
