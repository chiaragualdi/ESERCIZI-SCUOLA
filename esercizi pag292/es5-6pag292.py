'''
Elenca proprietà e metodi della classe Prodotto.
Definisci il metodo assegna_prezzo della classe prodotto.
'''

class Prodotto:
    def __init__(self, nome, tipo, scadenza="Nessuna scadenza", prezzo=0, note="X"):
        self.nome = nome
        self.tipo = tipo
        self.scadenza = scadenza
        self.prezzo = prezzo
        self.note = note
    
    def assegna_prezzo(self, prezzo):
        self.prezzo = prezzo
    def info(self):
        print("Nome:", self.name)
        print("Tipo:", self.tipo)
        print("Prezzo:", self.prezzo)
        print("Scadenza:", self.scadenza)
        print("Note:", self.notes)

p1 = Prodotto("MacBook Air", "computer", prezzo = 2000, note = "versione 10.14.6")
p1.info()

p2 = Prodotto("Yogurt", "Latticino", "15 marzo 2021")
p2.assegna_prezzo(2.50)
p2.info()