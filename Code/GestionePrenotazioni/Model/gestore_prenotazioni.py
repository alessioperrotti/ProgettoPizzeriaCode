import pickle

from Code.GestionePrenotazioni.Model.prenotazione import Prenotazione


class GestorePrenotazioni():
    def __init__(self):
        self.lista_prenotazioni = []
        self.orari_disponibili = ["12:30", "13:00", "13:30", "14:00", "14:30", "15:00"]
        self.tavoli_disponibili = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        self.ultimo_codice_prenotazione = 0
        self.nome_file = "lista_prenotazioni.pickle"
        try:
            self.carica_da_file(self.nome_file)
        except FileNotFoundError:
            print("dati dipendenti non trovati")

    def aggiungi_prenotazione(self, prenotazione):
        self.lista_prenotazioni.append(prenotazione)
        self.salva_dati(self.nome_file)
        self.carica_da_file(self.nome_file)

    def modifica_prenotazioni(self, codice_ricerca, new_tavolo, new_persone,
                              new_orario, new_data):

        pren_da_modificare: Prenotazione = self.ricerca_prenotazione_codice(codice_ricerca)
        for x in self.lista_prenotazioni:
            if int(pren_da_modificare.codice) == int(x.codice):
                x.tavolo_assegnato = new_tavolo
                x.n_persone = new_persone
                x.orario = new_orario
                x.data = new_data

    def elimina_prenotazione(self, codice):
        prenotazione_da_eliminare = self.ricerca_prenotazione_codice(codice)
        self.lista_prenotazioni.remove(prenotazione_da_eliminare)
        self.salva_dati(self.nome_file)
        self.carica_da_file(self.nome_file)

    def ricerca_prenotazione_codice(self, codice):
        for prenotazione in self.lista_prenotazioni:
            if codice == prenotazione.codice:
                return prenotazione

    def genera_codice(self):
        self.ultimo_codice_prenotazione += 1
        return self.ultimo_codice_prenotazione

    #############################################################

    def salva_dati(self, nome_file):
        dati = {
            'cod': self.ultimo_codice_prenotazione,
            'lista': self.lista_prenotazioni
        }
        with open(nome_file, 'wb') as file:
            pickle.dump(dati, file)
        file.close()

    def carica_da_file(self, nome_file):
        with open(nome_file, 'rb') as file:
            dati = pickle.load(file)
        file.close()
        self.ultimo_codice_prenotazione = dati['cod']
        self.lista_prenotazioni = dati['lista']
