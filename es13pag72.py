#Verifica se un numero è pari o dispari.
print("Quando vuoi interrompere il programma inserisci stop.")
while True:
    n=int(input("Inserisci il numero: "))
    if n=="stop":
        False
    else:
        if n%2==0:
            print(n, "è un numero pari.")
        else:
            print(n, "è un numero dispari.")
    
