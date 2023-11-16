import PyQt6
from PyQt5.QtWidgets import QStackedWidget

from Code.GestioneRicevuta.Controller.cont_vista_inserisci_ricevuta import ContVistaInserisciRicevuta
from Code.GestioneRicevuta.View.vista_gestione_ricevute import VistaGestioneRicevute
from Code.GestioneRicevuta.Model.ricevuta import Ricevuta
from PyQt6.QtCore import pyqtSignal
class ContVistaGestioneRicevute():
##vista0
    def __init__(self, gestore, stacked_widget:QStackedWidget, cont1:ContVistaInserisciRicevuta):
        self.cont_inserisci = cont1
        self.view = VistaGestioneRicevute()
        self.gestore = gestore
        self.stacked_widget = stacked_widget
        self.view.pulsante_mostra.clicked.connect(self.mostra_info_ricevuta())
        self.view.pulsante_inserisci.clicked.connect(self.inserisci_ricevuta())
        self.view.pulsante_elimina.clicked.connect(self.elimina_ricevuta())


    def mostra_info_ricevuta(self):

        pass

    def inserisci_ricevuta(self):
        #self.stacked_widget.setCurrentWidget(self.cont_inserisci)
        self.cont_inserisci.view()
        self.cont_inserisci.view.show()
        self.view.setDisabled()
        pass

    def elimina_ricevuta(self):
        pass

if __name__ == '__main__':
    print("c")
