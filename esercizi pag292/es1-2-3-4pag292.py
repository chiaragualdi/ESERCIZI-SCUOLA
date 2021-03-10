'''
es1. Crea una classe Atleta per rappresentare le informazioni su un giocatore.
     La classe deve contenere un attributo booleano chiamato visitaMedica.
es2. Aggiungi alla classe Atleta un metodo per assegnare all'atleta il nome della squadra dove gioca.
es3. Aggiungi alla classe Atleta un metodo chiamato effettua_visita che ponga l'attributo visitaMedica uguale a True.
es4. Aggiungi alla classe Atleta un metodo per visualizzare i dati del giocatore.
'''

class Atleta:
    def __init__(self, nome, cognome, età, squadra="mancante", visita_medica=False):
        self.nome = nome
        self.cognome = cognome
        self.età = età
        self.squadra = squadra
        self.visita_medica = visita_medica

    def info(self):
        print("Nome:" , self.nome)
        print("Cognome:" , self.cognome)
        print("Età:" , self.età)
        print("Squadra:" , self.squadra)
        print("Visita medica:" , self.visita_medica)
        
    def add_squadra(self, nome_squadra):
        self.squadra = nome_squadra

    def effettua_visita(self):
        self.visita_medica=True

atleta = Atleta("Kylian", "Mbappè", 22)
atleta.info()
atleta.add_squadra("Paris Saint-German Football Club")
atleta.effettua_visita()
atleta.info()
