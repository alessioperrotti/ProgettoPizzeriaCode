import sys

import PyQt6
from PyQt6.QtWidgets import QStackedWidget, QTableWidgetItem
from PyQt6.QtWidgets import QApplication

from Code.GestioneOrdiniTavolo.Model.gestore_ordini_tavolo import GestoreOrdiniTavolo
from Code.GestioneOrdiniTavolo.Model.tavolo import Tavolo
from Code.GestioneRicevuta.Controller.cont_vista_info_ricevuta import ContVistaInfoRicevuta
from Code.GestioneRicevuta.Controller.cont_vista_inserisci_ricevuta import ContVistaInserisciRicevuta
from Code.GestioneRicevuta.Model.gestore_ricevuta import GestoreRicevuta
from Code.GestioneRicevuta.View.vista_gestione_ricevute import VistaGestioneRicevute
from Code.GestioneRicevuta.Controller.cont_vista_mostra_tavolo_selezionato import ContVistaMostraTavoloSelezionato
from Code.GestioneRicevuta.Model.ricevuta import Ricevuta
from PyQt6.QtCore import pyqtSignal, pyqtSlot

from Code.GestioneRicevuta.View.vista_info_ricevuta import VistaInfoRicevuta


class ContVistaGestioneRicevute():
    ##vista0
    def mostra_info_ricevuta(self):
        self.cont_info_ric.view = VistaInfoRicevuta()
        self.cont_info_ric.numero_selezionato = self.numero_selezionato
        self.cont_info_ric.imposta_info()
        self.cont_info_ric.view.exec()





    def inserisci_ricevuta(self):
        self.view.pulsante_inserisci.setText("O")
        self.cont_inserisci.view.show()

        # self.view.setDisabled(True)

    def imposta_linea_selezionata(self):
        item_selezionati = self.view.tab.selectedItems()
        for item in item_selezionati:
            if item.column() == 1:  # cioe prendo l'elemento della seconda colonna
                self.numero_selezionato = int(item.text())


                break


        self.view.pulsante_mostra.setEnabled(self.numero_selezionato is not None)
        self.view.pulsante_elimina.setEnabled(self.numero_selezionato is not None)
    def elimina_ricevuta(self):
        self.gestore_ric.elimina_ricevuta(self.numero_selezionato)
        self.aggiorna_tabella()
        self.numero_selezionato = None
        self.view.tab.clearSelection()

    def __init__(self, gestore_ric:GestoreRicevuta, gestore_ord:GestoreOrdiniTavolo,lista_tav:list[Tavolo], stacked_widget:QStackedWidget):
        self.numero_selezionato = None
        self.ricevuta_temp = Ricevuta()
        self.gestore_ord = gestore_ord
        self.lista_tav = lista_tav
        self.view = VistaGestioneRicevute()
        self.gestore_ric = gestore_ric
        self.stacked_widget = stacked_widget
        self.aggiorna_tabella()
        self.cont_inserisci = ContVistaInserisciRicevuta(self.gestore_ric, self.gestore_ord, self.lista_tav)
        self.cont_info_ric = ContVistaInfoRicevuta(self.gestore_ric)

        self.view.tab.itemSelectionChanged.connect(self.imposta_linea_selezionata)
        self.view.pulsante_inserisci.clicked.connect(self.inserisci_ricevuta)
        self.view.pulsante_elimina.clicked.connect(self.elimina_ricevuta)
        self.view.pulsante_mostra.clicked.connect(self.mostra_info_ricevuta)
        self.view.pulsante_mostra.setEnabled(self.numero_selezionato is not None)
        self.view.pulsante_elimina.setEnabled(self.numero_selezionato is not None)

    def inserisci_ricevuta(self):
        self.cont_inserisci.aggiorna_tabella()
        self.cont_inserisci.view.exec()
        self.aggiorna_tabella()



    def aggiorna_tabella(self):

        lista_ric = self.gestore_ric.lista_ricevute
        self.view.tab.setRowCount(len(lista_ric))
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

