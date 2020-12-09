str=input("Inserisci la parola: ")
l=len(str)
posizione=l-1
indice=0
while indice<posizione:
    if str[indice]==str[posizione]:
        indice=indice+1
        posizione=posizione-1
        print("La parola inserita è un palidromo.")
        break
    else:
        print("La parola inserita non è un palidromo.")
        break