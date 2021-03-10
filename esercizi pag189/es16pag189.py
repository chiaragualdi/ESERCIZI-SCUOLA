#Risolvi il problema precedente partendo da due liste che generano un dizionario con la nazione come chiave e la capitale come valore.
# Successivamente interroga il dizionario per visualizzare la capitale di una nazione.

def crea_dizionario(listanaz, listacap, diz={}):
    for i in range(len(listanaz)):
        diz[listanaz[i]] = listacap[i]
    return diz

def main():
    listanaz = ["Spagna", "Francia", "Portogallo","Germania", "Italia", "Belgio", "Svizzera", "Olanda","Danimarca", "Austria"]
    listacap = ["Madrid", "Parigi", "Lisbona", "Berlino", "Roma", "Bruxelles", "Berna", "Amsterdam", "Copenaghen", "Vienna"]
    d = crea_dizionario(listanaz, listacap)
    while True:
        print("Inserisci il nome di una nazione per avere il nome della rispettiva capitale: ")
        nazione = input()
        nazione = nazione.capitalize()
        if nazione not in d:
            print("La nazione non è presente dell'elenco. Premere stop per chiudere, altrimenti premere qualsiasi altro tasto per reinserire la nazione: ")
            check = input()
            if check == "stop":
                break
        else:
            capitale = d.get(nazione)
            print("La capitale è:", capitale, "Premere stop per chiudere, altrimenti premere qualsiasi altro tasto per reinserire la nazione:")
            check = input()
            if check == "stop":
                break
main()