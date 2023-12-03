
import pickle
import sys
from datetime import datetime

from PyQt6.QtCore import pyqtSignal, pyqtSlot
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtWidgets import QApplication, QWidget, QStackedWidget, QPushButton, QVBoxLayout

from Code.GestioneDipendenti.Model.gestore_dipendenti import GestoreDipendenti
from Code.GestioneMagazzino.Model.gestore_magazzino import GestoreMagazzino
from Code.GestioneMenu.Model.prodotto import Prodotto
from Code.GestioneOrdiniTavolo.Model.gestore_ordini_tavolo import GestoreOrdiniTavolo
from Code.GestioneOrdiniTavolo.Model.ordine_tavolo import OrdineTavolo
from Code.GestioneOrdiniTavolo.Model.tavolo import Tavolo
from Code.GestionePrenotazioni.Model.gestore_prenotazioni import GestorePrenotazioni
from Code.GestioneRicevuta.Controller.cont_vista_gestione_ricevute import ContVistaGestioneRicevute
from Code.GestioneRicevuta.Controller.cont_vista_inserisci_ricevuta import ContVistaInserisciRicevuta
from Code.GestioneRicevuta.Model.gestore_ricevuta import GestoreRicevuta
from Code.GestioneRicevuta.Model.ricevuta import Ricevuta
from Code.GestioneMenu.Model.gestore_menu import GestoreMenu
from Code.GestioneSistema.Controller.cont_vista_login import ContVistaLogin


class SegnaleRidimensiona():
    def __init__(self):
        self.seg = pyqtSignal()


class MainWindow(QWidget):
    def __init__(self, app):
        super(MainWindow, self).__init__()

        self.stacked = QStackedWidget()
        self.init_ui()

       # centro la finestra  #va aggiunto un 22 alla larghezza e altezza rispetto alla view
        self.setFixedSize(994+22, 637+22)

        self.show()
        print(self.size())

    def cambio_view(self):

        if self.stacked.currentWidget() == self.cont_vista_login.cont_vista_login_dipendente.cont_admin.view:
            self.setFixedSize(756+22, 637+22)
            self.layout().update()
            self.close()
            self.show()

        elif self.stacked.currentWidget() == self.cont_vista_login.cont_vista_login_dipendente.cont_admin.cont_vista_turni.view:
            self.setFixedSize(994 + 22, 637 + 22)
            self.layout().update()
            self.close()
            self.show()

        elif self.stacked.currentWidget() == self.cont_vista_login.cont_vista_login_dipendente.cont_admin.cont_vista_statistiche.view:
            self.setFixedSize(994 + 22, 637 + 22)
            self.layout().update()
            self.close()
            self.show()
    def init_ui(self):
        self.gestore_ric = GestoreRicevuta()
        self.gestore_dip = GestoreDipendenti()
        self.gestore_mag = GestoreMagazzino()
        self.gestore_ord = GestoreOrdiniTavolo()
        self.gestore_men = GestoreMenu()
        self.gestore_pre = GestorePrenotazioni()

        self.cont_vista_login = ContVistaLogin(self.stacked, self.gestore_ric, self.gestore_dip, self.gestore_mag, self.gestore_ord, self.gestore_men,self.gestore_pre)
        self.stacked.addWidget(self.cont_vista_login.view)
        self.stacked.setCurrentWidget(self.cont_vista_login.view)

        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked)

        self.stacked.currentChanged.connect(self.cambio_view)

        

if __name__ == '__main__':

    app = QApplication(sys.argv)
    mainWindow = MainWindow(app)

    sys.exit(app.exec())
