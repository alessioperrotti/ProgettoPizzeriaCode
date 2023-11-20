from Code.GestionePrenotazioni.Model.prenotazione import Prenotazione


class GestorePrenotazioni():

    def __init__(self):
        self.lista_prenotazioni = []

    def aggiungi_prenotazione(self, prenotazione):
        self.lista_prenotazioni.append(prenotazione)

    def ricerca_prenotazione_nome(self, nome_cliente):
        list = []
        for prenotazione in self.lista_prenotazioni:
            if nome_cliente == prenotazione.nomeAcquirente:
                list.append(prenotazione)

    def ricerca_prenotazione_codice(self, codice):
        for prenotazione in self.lista_prenotazioni:
            if codice == prenotazione.numero:
                return prenotazione

    def elimina_prenotazione(self, nome_cliente):
        prenotazione_da_eliminare = self.ricerca_prenotazione_nome(nome_cliente)
        self.lista_prenotazioni.remove(prenotazione_da_eliminare)
