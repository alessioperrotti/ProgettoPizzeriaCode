import PyQt6
from ..View.VistaInserisciRicevuta import VistaInserisciRicevuta
from ..Model.Ricevuta import Ricevuta
from PyQt6.QtCore import pyqtSignal
class ControllerVistaInserisciRicevuta():

    def __init__(self, ):
        self.view = VistaInserisciRicevuta()
        self.model = Ricevuta()





