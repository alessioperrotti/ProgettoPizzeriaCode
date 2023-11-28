import pickle

from Code.GestioneDipendenti.Model.cameriere import Cameriere
from Code.GestioneDipendenti.Model.cuoco import Cuoco


class GestoreDipendenti():
    def __init__(self):
        self.lista_cuochi = []
        self.lista_camerieri = []
        self.nome_file = "lista_dipendenti.pickle"
        try:
            self.carica_da_file(self.nome_file)
        except FileNotFoundError:
            print("dati dipendenti non trovati")

    def aggiungi_cuoco(self, cuoco):
        self.lista_cuochi.append(cuoco)
        self.salva_dati(self.nome_file)
        self.carica_da_file(self.nome_file)

    def aggiungi_turno_cuoco(self, cuoco,turno):
        cuoco.turno = turno
        self.salva_dati(self.nome_file)
        self.carica_da_file(self.nome_file)

    def rimuovi_turno_cuoco(self,cognome):
        cuoco_selezionato = self.estrai_cuoco_cognome(cognome)
        cuoco_selezionato.turno = None
        self.salva_dati(self.nome_file)
        self.carica_da_file(self.nome_file)

    def estrai_cuoco_cognome(self, cognome):
        for cuoco in self.lista_cuochi:
            if cognome == cuoco.cognome:
                print("trovato")
                return cuoco

    def estrai_cuoco_username(self, username):
        for cuoco in self.lista_cuochi:
            if username == cuoco.username:
                print("trovato")
                return cuoco

    def elimina_cuoco(self, cognome):
        cuoco_da_eliminare = self.estrai_cuoco_cognome(cognome)
        self.lista_cuochi.remove(cuoco_da_eliminare)
        self.salva_dati(self.nome_file)
        self.carica_da_file(self.nome_file)

    def modifica_cuoco(self, cognome_ricerca, new_email, new_stipendio,
                       new_data_nascita, new_username, new_password):
        cuoco: Cuoco = self.estrai_cuoco_cognome(cognome_ricerca)
        for x in self.lista_cuochi:
            print("c")
            if cuoco.cognome == x.cognome:
                x.email = new_email
                x.stipendio = new_stipendio
                x.data_nascita = new_data_nascita
                x.username = new_username
                x.password = new_password

        self.salva_dati(self.nome_file)
        self.carica_da_file(self.nome_file)

    #########################################################################
    def aggiungi_cameriere(self, cameriere):
        self.lista_camerieri.append(cameriere)
        self.salva_dati(self.nome_file)
        self.carica_da_file(self.nome_file)

    def aggiungi_turno_cameriere(self, cameriere ,turno):
        cameriere.turno = turno
        self.salva_dati(self.nome_file)
        self.carica_da_file(self.nome_file)

    def rimuovi_turno_cameriere(self,cognome):
        cameriere_selezionato = self.estrai_cameriere_cognome(cognome)
        cameriere_selezionato.turno = None
        self.salva_dati(self.nome_file)
        self.carica_da_file(self.nome_file)

    def estrai_cameriere_cognome(self, cognome):
        for cameriere in self.lista_camerieri:
            if cognome == cameriere.cognome:
                return cameriere

    def estrai_cameriere_username(self, username):
        for cameriere in self.lista_camerieri:
            if username == cameriere.username:
                print("trovato")
                return cameriere

    def elimina_cameriere(self, cognome):
        cameriere_da_eliminare = self.estrai_cameriere_cognome(cognome)
        self.lista_camerieri.remove(cameriere_da_eliminare)
        self.salva_dati(self.nome_file)
        self.carica_da_file(self.nome_file)

    def modifica_cameriere(self, cognome_ricerca, new_email, new_stipendio,
                           new_data_nascita, new_username, new_password):
        cameriere: Cameriere = self.estrai_cameriere_cognome(cognome_ricerca)
        for x in self.lista_camerieri:
            if cameriere.cognome == x.cognome:
                x.email = new_email
                x.stipendio = new_stipendio
                x.data_nascita = new_data_nascita
                x.username = new_username
                x.password = new_password

        self.salva_dati(self.nome_file)
        self.carica_da_file(self.nome_file)

    #################################################################################
    # def save_data_cuochi(self, nome_file):
    #     with open(nome_file, 'wb') as file:
    #         pickle.dump(self.lista_cuochi,file, pickle.HIGHEST_PROTOCOL)
    #
    #
    # def save_data_camerieri(self, nome_file):
    #     with open(nome_file, 'wb') as file:
    #         pickle.dump(self.lista_camerieri,file, pickle.HIGHEST_PROTOCOL)

    def salva_dati(self, nome_file):
        with open(nome_file, 'wb') as file:
            pickle.dump({'cuochi': self.lista_cuochi, 'camerieri': self.lista_camerieri}, file)

    def carica_da_file(self, nome_file):
        with open(nome_file, 'rb') as file:
            data = pickle.load(file)
            self.lista_cuochi = data['cuochi']
            self.lista_camerieri = data['camerieri']


