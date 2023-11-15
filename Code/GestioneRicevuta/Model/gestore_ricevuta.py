from ricevuta import Ricevuta

class GestoreRicevuta():

    def __init__(self):
        self.lista_ricevute = []

    def aggiungi_ricevuta(self,ammontareLordo, data, listaProdotti, nomeAcquirente, numero, ora):
        self.lista_ricevute.append(Ricevuta(ammontareLordo, data, listaProdotti, nomeAcquirente, numero, ora))

    def ricerca_ricevuta_nome(self, nomeAcquirente):
        list = []
        for ricevuta in self.lista_ricevute:
            if nomeAcquirente == ricevuta.nomeAcquirente:
                list.append(ricevuta)


    def ricerca_ricevuta_numero(self, numero):
        for ricevuta in self.lista_ricevute:
            if numero == ricevuta.numero:
                return ricevuta


    def elimina_ricevuta(self, numero):
        ricevuta_da_eliminare = self.ricerca_ricevuta_numero(numero)
        self.lista_ricevute.remove(ricevuta_da_eliminare)




