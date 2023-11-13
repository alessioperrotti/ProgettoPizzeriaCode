from Ricevuta import Ricevuta

class GestoreRicevuta():

    def __init__(self):
        self.lista_ricevute = []

    def aggiungiRicevuta(self,ammontareLordo, data, listaProdotti, nomeAcquirente, numero, ora):
        self.lista_ricevute.append(Ricevuta(ammontareLordo, data, listaProdotti, nomeAcquirente, numero, ora))

    def ricercaRicevuta(self):
    def eliminaRicevuta(self):
