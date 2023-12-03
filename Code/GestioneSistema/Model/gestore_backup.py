import pickle

from Code.GestioneDipendenti.Model.gestore_dipendenti import GestoreDipendenti
from Code.GestioneMagazzino.Model.gestore_magazzino import GestoreMagazzino
from Code.GestioneMenu.Model.gestore_menu import GestoreMenu
from Code.GestioneOrdiniTavolo.Model.gestore_ordini_tavolo import GestoreOrdiniTavolo
from Code.GestionePrenotazioni.Model.gestore_prenotazioni import GestorePrenotazioni
from Code.GestioneRicevuta.Model.gestore_ricevuta import GestoreRicevuta


class GestoreBackup():
    def __init__(self, nome_file, orario_backup, gestore_pre: GestorePrenotazioni,gestore_dip: GestoreDipendenti,
                 gestore_ric: GestoreRicevuta, gestore_mag: GestoreMagazzino, gestore_ord: GestoreOrdiniTavolo,
                 gestore_menu: GestoreMenu):
        self.nome_file = nome_file
        self.orario_backup = orario_backup
        self.gestore_dip = gestore_dip
        self.gestore_ric = gestore_ric
        self.gestore_menu = gestore_menu
        self.gestore_mag = gestore_mag
        self.gestore_ord = gestore_ord
        self.gestore_pre = gestore_pre


    def effettua_backup(self):
        with open(self.nome_file, 'wb') as file:
            pickle.dump({
                'dipendenti': self.get_info_dipendenti,
                'ricevute': self.get_info_ricevute,
                'prodotti': self.get_info_prodotti,
                'ordini_tavolo': self.get_info_ordini_tavolo,
                'prenotazioni': self.get_info_prenotazioni,
                'materie_prime': self.get_info_materie_prime
                }, file)

        pass

    def get_info_dipendenti(self):

        lista_dipendenti = self.gestore_dip.lista_camerieri.copy()
        lista_dipendenti.extend(self.gestore_dip.lista_cuochi)
        return lista_dipendenti
    def get_info_ricevute(self):
        lista_ricevute = self.gestore_ric.lista_ricevute.copy()
        return lista_ricevute
    def get_info_prodotti(self):
        lista_prodotti = self.gestore_menu.lista_prodotti.copy()
        return lista_prodotti
    def get_info_ordini_tavolo(self):
        lista_ordini = self.gestore_ord.lista_ordini.copy()
        return lista_ordini
    def get_info_prenotazioni(self):
        lista_prenotazioni = self.gestore_pre.lista_prenotazioni.copy()
        return lista_prenotazioni

    def get_info_materie_prime(self):
        lista_materie_prime = self.gestore_mag.lista_materieprime.copy()
        return lista_materie_prime

