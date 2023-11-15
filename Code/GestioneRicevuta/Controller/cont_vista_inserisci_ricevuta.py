import PyQt6
from ..View.vista_inserisci_ricevuta import VistaInserisciRicevuta
from ..Model.ricevuta import Ricevuta
from PyQt6.QtCore import pyqtSignal
class ContVistaInserisciRicevuta():

    def __init__(self):
        self.view = VistaInserisciRicevuta()
        self.model = Ricevuta()
        self.view.






