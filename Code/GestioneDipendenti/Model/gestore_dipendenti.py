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

    def aggiungi_turno_cuoco(self, cuoco, turno, giorno):
        indice_giorno = self.converti_giorno_indice(giorno)
        #cuoco.turno.insert(indice_giorno, turno)
        cuoco.turno[indice_giorno] = turno
        self.salva_dati(self.nome_file)
        self.carica_da_file(self.nome_file)

    def rimuovi_turno_cuoco(self, cognome, giorno):
        cuoco_selezionato = self.estrai_cuoco_cognome(cognome)
        indice_giorno = self.converti_giorno_indice(giorno)
        cuoco_selezionato.turno[indice_giorno] = None
        self.salva_dati(self.nome_file)
        self.carica_da_file(self.nome_file)

    def estrai_cuoco_cognome(self, cognome):
        for cuoco in self.lista_cuochi:
            if cognome == cuoco.cognome:
                return cuoco

    def estrai_cuoco_username(self, username):
        for cuoco in self.lista_cuochi:
            if username == cuoco.username:
                return cuoco

    def elimina_cuoco(self, cognome):
        cuoco_da_eliminare = self.estrai_cuoco_cognome(cognome)
        self.lista_cuochi.remove(cuoco_da_eliminare)
        self.salva_dati(self.nome_file)
        self.carica_da_file(self.nome_file)

    def modifica_cuoco(self, cognome_ricerca, new_email, new_stipendio,
                       new_data_nascita, new_username, new_password):
        cuoco = self.estrai_cuoco_cognome(cognome_ricerca)
        for x in self.lista_cuochi:
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

    def aggiungi_turno_cameriere(self, cameriere, turno, giorno):
        indice_giorno = self.converti_giorno_indice(giorno)
        #cameriere.turno.insert(indice_giorno, turno)
        cameriere.turno[indice_giorno] = turno
        self.salva_dati(self.nome_file)
        self.carica_da_file(self.nome_file)

    def rimuovi_turno_cameriere(self, cognome, giorno):
        cameriere_selezionato = self.estrai_cameriere_cognome(cognome)
        indice_giorno = self.converti_giorno_indice(giorno)
        cameriere_selezionato.turno[indice_giorno] = None
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

    def get_info_dipendenti(self):

        lista_dipendenti = self.lista_camerieri.copy()
        lista_dipendenti.extend(self.lista_cuochi)
        return lista_dipendenti
    #################################################################################
    def salva_dati(self, nome_file):
        with open(nome_file, 'wb') as file:
            pickle.dump({'cuochi': self.lista_cuochi, 'camerieri': self.lista_camerieri}, file)

    def carica_da_file(self, nome_file):
        with open(nome_file, 'rb') as file:
            data = pickle.load(file)
            self.lista_cuochi = data['cuochi']
            self.lista_camerieri = data['camerieri']

    def converti_giorno_indice(self, giorno):
        giorni_settimana = {"lunedi": 0, "martedi": 1, "mercoledi": 2, "venerdi": 3, "sabato": 4, "domenica": 5}
        giorno = giorno.lower()

        if giorno in giorni_settimana:
            return giorni_settimana[giorno]
        else:
            raise ValueError("Giorno non valido: {}".format(giorno))

    ####################################################################################

    def accesso_dipendente(self, username, password):
        accesso = False
        lista_utilizzatori = self.lista_cuochi.copy()
        lista_utilizzatori.extend(self.lista_camerieri)
        for utilizzatore in lista_utilizzatori:
            if (username == utilizzatore.username and password == utilizzatore.password):
                accesso = True
                return accesso, utilizzatore.ruolo

        return accesso, None

