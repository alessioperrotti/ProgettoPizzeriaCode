import sys

import PyQt6
from PyQt6.QtWidgets import QStackedWidget
from PyQt6.QtWidgets import QApplication

from Code.GestioneRicevuta.Controller.cont_vista_inserisci_ricevuta import ContVistaInserisciRicevuta
from Code.GestioneRicevuta.Model.gestore_ricevuta import GestoreRicevuta
from Code.GestioneRicevuta.View.vista_gestione_ricevute import VistaGestioneRicevute
from Code.GestioneRicevuta.Model.ricevuta import Ricevuta
from PyQt6.QtCore import pyqtSignal, pyqtSlot


class ContVistaGestioneRicevute():
    ##vista0
    def mostra_info_ricevuta(self):
        pass


    def inserisci_ricevuta(self):
        self.view.pulsante_inserisci.setText("O")
        self.cont_inserisci.view.show()

        # self.view.setDisabled(True)


    def elimina_ricevuta(self):
        pass

    def __init__(self, gestore, stacked_widget:QStackedWidget, cont_inserisci_ric:ContVistaInserisciRicevuta):
        self.cont_inserisci = cont_inserisci_ric
        self.view = VistaGestioneRicevute()
        self.gestore = gestore
        self.stacked_widget = stacked_widget

      #  self.view.pulsante_mostra.clicked.connect(self.mostra_info_ricevuta())
        self.view.pulsante_inserisci.clicked.connect(self.inserisci_ricevuta)


      #  self.view.pulsante_elimina.clicked.connect(self.elimina_ricevuta())

    def inserisci_ricevuta(self):
        print("c")
        self.cont_inserisci.view.exec()


if __name__ == '__main__':

    #app = QApplication(sys.argv)
    stacked = QStackedWidget()
    gestore_ric = GestoreRicevuta()
    cont_inserisci_ric = ContVistaInserisciRicevuta(gestore_ric)
    cont_gestione_ric = ContVistaGestioneRicevute(gestore_ric, stacked, cont_inserisci_ric)
    cont_gestione_ric.view.show()
    #sys.exit(app.exec())

