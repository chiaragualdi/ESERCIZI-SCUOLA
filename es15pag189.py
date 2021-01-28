#Dato un elenco di nazioni contenuto in una lista e uno delle rispettive capitali in una seconda lista,
#visualizza la capitale di una nazione della quale viene fornito da tastiera il nome,
#segnalando con un messaggio di errore il caso in cui la nazione rihiesta non sia compresa nell'elenco.

listanaz = ["Spagna", "Francia", "Portogallo","Germania", "Italia", "Belgio", "Svizzera", "Olanda","Danimarca", "Austria"]
listacap = ["Madrid", "Parigi", "Lisbona", "Berlino", "Roma", "Bruxelles", "Berna", "Amsterdam", "Copenaghen", "Vienna"]
while True:
    nazione = input("Digitare il nome di una nazione per avere la rispettiva capitale: ")
    nazione = nazione.capitalize()
    if nazione in listanaz:
        i = listanaz.index(nazione)
        print(listacap[i])
        print("Per smettere di controllare le nazioni premere stop, per continuare digitare qualsiasi altro tasto: ")
        ripetitore = input()
        if ripetitore == "stop":
            break
    else:
        print(nazione, "Non è nell'elenco delle nazioni registrate. Per smettere di controllare le nazioni premere stop, per ricominciare inserire qualsiasi altro tasto: ")
        ripetitore2 = input()
        if ripetitore2 == "stop":
            break
