#La rete di vendita di un'azienda è suddivisa in 4 zone: Nord, Sud, Centro, Isole.
# Dopo aver acquisito in un array il fatturato nelle 4 zone,
# calcolare il totale del fatturato e i valori in percentuale delle vendite nelle 4 zone rispetto al totale.

fatturato = {}
fatturato["fatturato_nord"] = float(input("Inserire il fatturato della zona Nord: "))
fatturato["fatturato_sud"] = float(input("Inserire il fatturato della zona Sud: "))
fatturato["fatturato_centro"] = float(input("Inserire il fatturato della zona Centro: "))
fatturato["fatturato_isole"] = float(input("Inserire il fatturato della zona Isole: "))

totale = round(sum(fatturato.values()), 1)

percentuale_nord = fatturato["fatturato_nord"]*100/totale
percentuale_sud = fatturato["fatturato_sud"]*100/totale
percentuale_centro = fatturato["fatturato_centro"]*100/totale
percentuale_isole = fatturato["fatturato_isole"]*100/totale
print(totale)

print("Il totale è", totale)
print("Le percentuali delle varie zone rispetto al totale sono: Nord:", percentuale_nord, "%, Sud:", percentuale_sud, "%, Centro:", percentuale_centro, "%, Isole:", percentuale_isole, "%")
