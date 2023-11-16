import sys
from os.path import dirname, abspath

import PyQt6
sys.path.append(dirname(dirname(abspath(__file__))))

from Code.GestioneRicevuta.View.vista_inserisci_ricevuta import VistaInserisciRicevuta



from Code.GestioneRicevuta.Model.ricevuta import Ricevuta
from Code.GestioneRicevuta.Model.gestore_ricevuta import GestoreRicevuta
from PyQt6.QtCore import pyqtSignal
class ContVistaInserisciRicevuta():

    def __init__(self, gestore:GestoreRicevuta):
        self.view = VistaInserisciRicevuta()
        self.model = Ricevuta()
        self.gestore = gestore

    def conferma_ricevuta(self):
        nome_acquirente = self.view.ins_nome.text()
        pass
    def mostra_tavolo_selezionato(self):
        pass

    def stampa_ricevuta(self):
        pass






