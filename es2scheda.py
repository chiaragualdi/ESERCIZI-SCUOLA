listaA=[]
listaB=[]
ciclo=True
while ciclo==True:
    print("Scrivi le parole da aggiungere nella lista A, inserisci 1 per uscire")
    parola=input()
    if parola=="1":
        ciclo=False
    else:
        listaA.append(parola)
nparole=len(listaA)
for i in range(nparole):
    nlett=len(listaA[i])
    listaB.append(nlett)
print("Ecco il numero di lettere delle parole che hai inserito:")
print(listaB)
