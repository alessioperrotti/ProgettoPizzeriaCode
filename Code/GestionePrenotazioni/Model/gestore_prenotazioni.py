import pickle

from Code.GestionePrenotazioni.Model.prenotazione import Prenotazione


class GestorePrenotazioni():
    def __init__(self):
        self.lista_prenotazioni = []
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

    def modifica_prenotazioni(self, codice_ricerca, new_costo_al_kg, new_qta_disponibile,
                              new_qta_limite, new_qta_ordine_STD, new_data_scadenza):

        pren_da_modificare: Prenotazione = self.ricerca_prenotazione_codice(codice_ricerca)
        for x in self.lista_prenotazioni:
            if int(pren_da_modificare.codice) == int(x.codice):
                x.costo_al_kg = new_costo_al_kg
                x.qta_disponibile = new_qta_disponibile
                x.qta_limite = new_qta_limite
                x.qta_ordine_STD = new_qta_ordine_STD
                x.data_scadenza = new_data_scadenza

    def elimina_prenotazione(self, nome_cliente):
        prenotazione_da_eliminare = self.ricerca_prenotazione_codice(nome_cliente)
        self.lista_prenotazioni.remove(prenotazione_da_eliminare)
        self.salva_dati(self.nome_file)
        self.carica_da_file(self.nome_file)

    def ricerca_prenotazione_codice(self, codice):
        for prenotazione in self.lista_prenotazioni:
            if codice == prenotazione.numero:
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
