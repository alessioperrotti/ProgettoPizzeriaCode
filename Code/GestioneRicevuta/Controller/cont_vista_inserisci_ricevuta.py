import sys
from os.path import dirname, abspath

import PyQt6
from PyQt6.QtWidgets import QApplication

sys.path.append(dirname(dirname(abspath(__file__))))

from Code.GestioneRicevuta.View.vista_inserisci_ricevuta import VistaInserisciRicevuta



from Code.GestioneRicevuta.Model.ricevuta import Ricevuta
from Code.GestioneRicevuta.Model.gestore_ricevuta import GestoreRicevuta
from PyQt6.QtCore import pyqtSignal
class ContVistaInserisciRicevuta():

    def __init__(self, gestore:GestoreRicevuta):
        self.view = VistaInserisciRicevuta()
        self.gestore = gestore
        self.view.pulsante_conferma.clicked.connect(self.conferma_ricevuta)

    def conferma_ricevuta(self):
        nome_acquirente = self.view.ins_nome.text()

        self.view.close()

        pass
    def mostra_tavolo_selezionato(self):
        pass

    def stampa_ricevuta(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gestore = GestoreRicevuta()
    cont = ContVistaInserisciRicevuta(gestore)
    cont.view.show()
    sys.exit(app.exec())



