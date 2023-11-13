import PyQt6
from ..View.VistaGestioneRicevute import VistaGestioneRicevute
from ..Model.Ricevuta import Ricevuta
from PyQt6.QtCore import pyqtSignal
class ControllerVistaGestioneRicevute():

    def __init__(self, gestore):
        self.view = VistaGestioneRicevute()
        self.gestore = gestore
        self.view.pulsante_mostrainfo.clicked.connect(self.mostra_info_ricevuta())
        self.view.pulsante_inserisci.clicked.connect(self.inserisci_ricevuta())
        self.view.pulsante_elimina.clicked.connect(self.elimina_ricevuta())


    def mostra_info_ricevuta(self):
        pass

    def inserisci_ricevuta(self):
        pass

    def elimina_ricevuta(self):
        pass



