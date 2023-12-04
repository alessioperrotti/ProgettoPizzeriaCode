import pickle

from Code.GestioneOrdiniTavolo.Model.gestore_ordini_tavolo import GestoreOrdiniTavolo
from Code.GestionePrenotazioni.Model.prenotazione import Prenotazione


class GestorePrenotazioni():
    def __init__(self):
        gestore_ordini_tavolo = GestoreOrdiniTavolo()
        self.lista_prenotazioni = []
        self.orari_disponibili = ["12:30", "13:00", "13:30", "14:00", "14:30", "19:00", "19:30", "20:00", "20:30",
                                  "21:00", "21:30", "22:00", "22:30", "23:00"]

        self.lista_tavoli = gestore_ordini_tavolo.lista_tavoli

        self.ultimo_codice_prenotazione = 0
        self.nome_file = "lista_prenotazioni.pickle"
        try:
            self.carica_da_file(self.nome_file)
        except FileNotFoundError:
            print("dati dipendenti non trovati")

    def stampa_lista_tavoli(self):
        print(self.lista_tavoli)
        for tavolo in self.lista_tavoli:
            print("numeroT: " + str(tavolo.numero) + "posti: " + str(tavolo.posti_disponibili) + "stato: " + str(tavolo.stato))

    def aggiungi_prenotazione(self, prenotazione):
        self.lista_prenotazioni.append(prenotazione)
        prenotazione.tavolo_assegnato.stato = "prenotato"
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

        self.salva_dati(self.nome_file)
        self.carica_da_file(self.nome_file)

    def elimina_prenotazione(self, codice):
        prenotazione_da_eliminare = self.ricerca_prenotazione_codice(codice)
        prenotazione_da_eliminare.tavolo_assegnato.stato = "libero"
        self.lista_prenotazioni.remove(prenotazione_da_eliminare)

        self.salva_dati(self.nome_file)
        self.carica_da_file(self.nome_file)

    def ricerca_prenotazione_codice(self, codice):
        for prenotazione in self.lista_prenotazioni:
            if codice == prenotazione.codice:
                return prenotazione

    def ricerca_tavolo(self, n_tavolo):
        for tavolo in self.lista_tavoli:
            if int(n_tavolo) == tavolo.numero:
                print("tav trovato")
                return tavolo

    def genera_codice(self):
        self.ultimo_codice_prenotazione += 1
        return self.ultimo_codice_prenotazione

    def ricerca_data_orario(self, data, orario):
        count_prenotazioni = 0
        total_persone = 0
        for prenotazione in self.lista_prenotazioni:
            if prenotazione.data == data and prenotazione.orario == orario:
                print("trovato")
                count_prenotazioni += 1
                total_persone += prenotazione.n_persone
                # print(count_prenotazioni)
                # print(total_persone)
        return count_prenotazioni, total_persone

    #############################################################

    def salva_dati(self, nome_file):
        dati = {
            'cod': self.ultimo_codice_prenotazione,
            'lista': self.lista_prenotazioni,
            'tavoli': self.lista_tavoli
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
        self.lista_tavoli = dati['tavoli']
