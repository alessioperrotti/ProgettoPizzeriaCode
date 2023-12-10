import pickle

from Code.GestioneOrdiniTavolo.Model.gestore_ordini_tavolo import GestoreOrdiniTavolo
from Code.GestionePrenotazioni.Model.prenotazione import Prenotazione


class GestorePrenotazioni():
    def __init__(self):
        self.gestore_ordini_tavolo = GestoreOrdiniTavolo()
        self.lista_prenotazioni = []
        self.orari_disponibili = ["12:30", "13:00", "13:30", "14:00", "14:30", "19:00", "19:30", "20:00", "20:30",
                                  "21:00", "21:30", "22:00", "22:30", "23:00"]

        self.lista_tavoli = self.gestore_ordini_tavolo.lista_tavoli

        self.ultimo_codice_prenotazione = 0
        self.nome_file_prenotazioni = "lista_prenotazioni.pickle"
        self.nome_file_tavoli = "lista_tavoli.pickle"
        try:
            self.carica_da_file(self.nome_file_prenotazioni, self.nome_file_tavoli)
            # self.gestore_ordini_tavolo.carica_da_file()
        except FileNotFoundError:
            print("dati prenotazioni non trovati")

    def stampa_lista_tavoli(self):
        for tavolo in self.lista_tavoli:
            print(f"Tavolo {tavolo.numero}: Stato - {tavolo.stato}")

    def aggiungi_prenotazione(self, prenotazione):
        self.lista_prenotazioni.append(prenotazione)
        prenotazione.tavolo_assegnato.cambia_stato("prenotato")
        print(prenotazione.tavolo_assegnato.stato)

        self.salva_dati(self.nome_file_prenotazioni,self.nome_file_tavoli)
        self.carica_da_file(self.nome_file_prenotazioni,self.nome_file_tavoli)

    def modifica_prenotazioni(self, codice_ricerca, new_tavolo, new_persone,
                              new_orario, new_data):

        pren_da_modificare: Prenotazione = self.ricerca_prenotazione_codice(codice_ricerca)
        pren_da_modificare.tavolo_assegnato.cambia_stato("libero")

        for x in self.lista_prenotazioni:
            if int(pren_da_modificare.codice) == int(x.codice):
                x.tavolo_assegnato = new_tavolo
                x.tavolo_assegnato.cambia_stato("prenotato")
                x.n_persone = new_persone
                x.orario = new_orario
                x.data = new_data

        self.salva_dati(self.nome_file_prenotazioni, self.nome_file_tavoli)
        self.carica_da_file(self.nome_file_prenotazioni, self.nome_file_tavoli)

    def elimina_prenotazione(self, codice):
        prenotazione_da_eliminare = self.ricerca_prenotazione_codice(codice)
        tavolo = self.ricerca_tavolo(prenotazione_da_eliminare.tavolo_assegnato.numero)
        tavolo.cambia_stato("libero")

        self.lista_prenotazioni.remove(prenotazione_da_eliminare)
        self.stampa_lista_tavoli()

        self.salva_dati(self.nome_file_prenotazioni, self.nome_file_tavoli)
        self.carica_da_file(self.nome_file_prenotazioni, self.nome_file_tavoli)

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

    def salva_dati(self, nome_file_prenotazioni, nome_file_tavoli):
        dati_prenotazioni = {
            'cod': self.ultimo_codice_prenotazione,
            'lista': self.lista_prenotazioni
        }

        dati_tavoli = {
            'tavoli': self.lista_tavoli
        }

        with open(nome_file_prenotazioni, 'wb') as file_prenotazioni:
            pickle.dump(dati_prenotazioni, file_prenotazioni)
        file_prenotazioni.close()

        with open(nome_file_tavoli, 'wb') as file_tavoli:
            pickle.dump(dati_tavoli, file_tavoli)
        file_tavoli.close()

    def carica_da_file(self, nome_file_prenotazioni, nome_file_tavoli):
        with open(nome_file_prenotazioni, 'rb') as file_prenotazioni:
            dati_prenotazioni = pickle.load(file_prenotazioni)

        with open(nome_file_tavoli, 'rb') as file_tavoli:
            dati_tavoli = pickle.load(file_tavoli)

        self.ultimo_codice_prenotazione = dati_prenotazioni['cod']
        self.lista_prenotazioni = dati_prenotazioni['lista']
        self.lista_tavoli = dati_tavoli['tavoli']

    def get_info_prenotazioni(self):
        lista_prenotazioni = self.lista_prenotazioni.copy()
        return lista_prenotazioni
