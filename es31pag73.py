#Fornisci la rappresentazione in binario di un numero decimale.
#Confronta il risultato con il valore ottenuto dalla funzione predefinita del linguaggio per convertire un numero decimale in binario.

print("Inserisci il valore del numero che vuoi trasformare:")
numero=int(input())
numerobinario=[]
while True:
    quoziente=numero/2
    resto=numero%2
    if resto==1:
        numerobinario.append(1)
    else:
        numerobinario.append(0)
    numero=quoziente
    if quoziente==0:
        break
numerobinario.reverse()
print(numerobinario)
