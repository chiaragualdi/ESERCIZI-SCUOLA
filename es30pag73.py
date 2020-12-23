#Fornisci la rappresentazione in decimale di un numero binario.
#Confronta il risultato con il valore ottenuto dalla funzione predefinita del linguaggio per convertire un numero binario in decimale.

lunghezza=int(input("Inserisci il numero di cifre da cui è composto il numero binario: "))
somma=0
for i in range(lunghezza):
    cifra=int(input("elenca le cifre a partire da destra: "))
    valore=(cifra*cifra)
    somma=somma+valore
print(somma)
