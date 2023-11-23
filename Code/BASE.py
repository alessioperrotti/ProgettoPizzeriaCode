import sys

from PyQt6.QtCore import pyqtSignal, pyqtSlot
from PyQt6.QtWidgets import QApplication, QWidget, QStackedWidget, QPushButton, QVBoxLayout

from Code.GestioneDipendenti.Model.gestore_dipendenti import GestoreDipendenti
from Code.GestioneMagazzino.Model.gestore_magazzino import GestoreMagazzino
from Code.GestioneMenu.Model.prodotto import Prodotto
from Code.GestioneOrdiniTavolo.Model.gestore_ordini_tavolo import GestoreOrdiniTavolo
from Code.GestioneOrdiniTavolo.Model.ordine_tavolo import OrdineTavolo
from Code.GestioneOrdiniTavolo.Model.tavolo import Tavolo
from Code.GestioneRicevuta.Controller.cont_vista_gestione_ricevute import ContVistaGestioneRicevute
from Code.GestioneRicevuta.Controller.cont_vista_inserisci_ricevuta import ContVistaInserisciRicevuta
from Code.GestioneRicevuta.Model.gestore_ricevuta import GestoreRicevuta
from Code.GestioneRicevuta.Model.ricevuta import Ricevuta
from Code.GestioneSistema.Controller.cont_vista_login import ContVistaLogin

class SegnaleRidimensiona():
    def __init__(self):
        self.seg = pyqtSignal()
class MainWindow(QWidget):


    def __init__(self, app):
        super(MainWindow, self).__init__()

        self.stacked = QStackedWidget()
        self.init_ui()


        self.setFixedSize(956, 637)


        self.show()

    def ridimensiona(self):

        if self.stacked.currentWidget() == self.cont_vista_login.cont_vista_login_dipendente.cont_admin.view:
            self.setFixedSize(756, 637)
            self.layout().update()
            self.close()
            self.show()


        print("ciao")

    def init_ui(self):
        gestore_ric = GestoreRicevuta()
        gestore_dip = GestoreDipendenti()
        gestore_mag = GestoreMagazzino()
        gestore_ord = GestoreOrdiniTavolo()

        self.cont_vista_login = ContVistaLogin(self.stacked, gestore_ric, gestore_dip, gestore_mag, gestore_ord)
        self.stacked.addWidget(self.cont_vista_login.view)
        self.stacked.setCurrentWidget(self.cont_vista_login.view)

        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked)

        self.stacked.currentChanged.connect(self.ridimensiona)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow(app)

    sys.exit(app.exec())
