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
                'dipendenti': self.gestore_dip.get_info_dipendenti,
                'ricevute': self.gestore_ric.get_info_ricevute,
                'prodotti': self.gestore_menu.get_info_prodotti,
                'ordini_tavolo': self.gestore_ord.get_info_ordini_tavolo,
                'prenotazioni': self.gestore_pre.get_info_prenotazioni,
                'materie_prime': self.gestore_mag.get_info_materie_prime
                }, file)

        pass









