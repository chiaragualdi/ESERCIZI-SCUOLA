'''
I voti assegnati a 30 studenti sono memorizzati in un dizionario avente per chiavi le matricole e per valori i voti corrispondenti.
Elencare i voti in ordine crescente e successivamente visualizzare quali voti diversi sono stati assegnati riducendo a uno i voti uguaali.
'''

def crea_dizionario(d):
    for i in range(0, 30):
        matricola=input("Inserire il nome della matricola: ")
        voto=input("Inserire il voto: ")
        d[matricola]=voto

check=input("Digita 1 per inserire i nomi delle matricole con i rispettivi voti oppure 2 per utilizzare il dizionario preimpostato: ")
if check=="1":
    d={}
    crea_dizionario(d)
    print(d)
elif check=="2":
    d={
        "Carlo":9,
        "Benito":6,
        "Luigi":7,
        "Luca":10,
        "Mario":5,
        "Tommaso":8,
        "Daniele":9,
        "Giovanni":6,
        "Marco":8,
        "Francesco":5,
        "Alessio":7,
        "Federico":6,
        "Michele":4,
        "Paolo":6,
        "Matteo":7,
        "Andrea":9,
        "Giuseppe":8,
        "Davide":6,
        "Gabriele":9,
        "Piero":5,
        "Lorenzo":6,
        "Gianpaolo":6,
        "Alessandro":7,
        "Simone":7,
        "Stefano":8,
        "Samuele":4,
        "Edoardo":5,
        "Cristian":9,
        "Enrico":8,
        "Vittorio":9
        }
else:
    print("Il valore inserito non rientra tra le due possibilità date.")
matricole=list(d.keys())
voti=list(d.values())
voti_ordinati=voti[:]
voti_ordinati.sort()
voti_diversi=[]
for i in range(min(voti), max(voti)):
    if i in voti:
        voti_diversi.append(i)
print(voti_ordinati)
print(voti_diversi)

'''
I voti assegnati a 30 studenti sono memorizzati in un dizionario avente per chiavi le matricole e per valori i voti corrispondenti.
Elencare i numeri di matricola degli studenti che hanno ottenuto una votazione superiore alla media di tutte le votazioni.
'''
media=round(sum(voti)/len(voti), 1)
matricole_sopra_media=[]
for e in range(len(voti)):
    if voti[e]>media:
        matricole_sopra_media.append(matricole[e])
print(matricole_sopra_media)
