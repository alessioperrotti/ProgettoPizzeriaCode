import sys

import PyQt6
from PyQt6.QtWidgets import QStackedWidget, QTableWidgetItem
from PyQt6.QtWidgets import QApplication

from Code.GestioneOrdiniTavolo.Model.gestore_ordini_tavolo import GestoreOrdiniTavolo
from Code.GestioneOrdiniTavolo.Model.tavolo import Tavolo
from Code.GestioneRicevuta.Controller.cont_vista_inserisci_ricevuta import ContVistaInserisciRicevuta
from Code.GestioneRicevuta.Model.gestore_ricevuta import GestoreRicevuta
from Code.GestioneRicevuta.View.vista_gestione_ricevute import VistaGestioneRicevute
from Code.GestioneRicevuta.Controller.cont_vista_mostra_tavolo_selezionato import ContVistaMostraTavoloSelezionato
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

    def __init__(self, gestore_ric:GestoreRicevuta, gestore_ord:GestoreOrdiniTavolo,lista_tav:list[Tavolo], stacked_widget:QStackedWidget):
        self.ricevuta_temp = Ricevuta()
        self.gestore_ord = gestore_ord
        self.lista_tav = lista_tav
        self.view = VistaGestioneRicevute()
        self.gestore_ric = gestore_ric
        self.stacked_widget = stacked_widget
        self.aggiorna_tabella()
        self.cont_inserisci = ContVistaInserisciRicevuta(self.gestore_ric, self.gestore_ord,self.ricevuta_temp, self.lista_tav)






        self.view.pulsante_inserisci.clicked.connect(self.inserisci_ricevuta)




    def inserisci_ricevuta(self):
        self.cont_inserisci.aggiorna_tabella()
        self.cont_inserisci.view.exec()
        self.aggiorna_tabella()


    def aggiorna_tabella(self):
        lista_ric = self.gestore_ric.lista_ricevute
        i=0
        for ricevuta in lista_ric:
            self.view.tab.setItem(i,0, QTableWidgetItem(ricevuta.nomeAcquirente)) #acquirente
            self.view.tab.setItem(i, 1, QTableWidgetItem(str(ricevuta.numero)))
            self.view.tab.setItem(i, 2, QTableWidgetItem(str(ricevuta.data)))
            i += 1

if __name__ == '__main__':

    #app = QApplication(sys.argv)
    stacked = QStackedWidget()
    gestore_ric = GestoreRicevuta()
    cont_inserisci_ric = ContVistaInserisciRicevuta(gestore_ric)
    cont_gestione_ric = ContVistaGestioneRicevute(gestore_ric, stacked, cont_inserisci_ric)
    cont_gestione_ric.view.show()
    #sys.exit(app.exec())

