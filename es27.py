#I dati relativi al numero dei veicoli transitati in entrata a un casello autostradale sono inseriti, giorno per giorno, con una ripetizione che termina quando si inserisce 0 come segnalazione della fine dell'input dei dati.
#Comunica il totale dei veicoli transitati nel periodo considerato.

lista_veicoli = []
count = True
ngiorni = 0
rip = 0
somma = 0
while count == True:
    ngiorni += 1
    rip += 1
    print("Quanti veicoli sono entrati il giorno", ng,"? ")
    veicoli = int(input())
    lista_veicoli.append(veicoli)

    if rip == 3:
        q = int(input("Vuoi uscire? Per uscire scrivi 0, se no premi 1 : "))
        rip = 0
        if q == 0:
            count = False
        else:
            pass
for i in lista_veicoli:
    somma += i
print("In", ngiorni,"giorni, sono transitati", somma, "veicoli.")
