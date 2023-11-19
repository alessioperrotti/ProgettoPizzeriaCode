import sys
from PyQt6.QtWidgets import QApplication, QTableWidgetItem, QVBoxLayout

from Code.GestioneMenu.Model.prodotto import Prodotto
from Code.GestioneOrdiniTavolo.Model.gestore_ordini_tavolo import GestoreOrdiniTavolo
from Code.GestioneOrdiniTavolo.Model.ordine_tavolo import OrdineTavolo
from Code.GestioneOrdiniTavolo.Model.tavolo import Tavolo
from Code.GestioneRicevuta.View.vista_inserisci_ricevuta import VistaInserisciRicevuta
from Code.GestioneRicevuta.Controller.cont_vista_mostra_tavolo_selezionato import ContVistaMostraTavoloSelezionato



from Code.GestioneRicevuta.Model.ricevuta import Ricevuta
from Code.GestioneRicevuta.Model.gestore_ricevuta import GestoreRicevuta
from PyQt6.QtCore import pyqtSignal
class ContVistaInserisciRicevuta():

    def __init__(self, gestore_ric:GestoreRicevuta, gestore_ord:GestoreOrdiniTavolo, ricevuta_temp:Ricevuta, lista_tav:list[Tavolo]):
        self.lista_tavoli = lista_tav
        self.view = VistaInserisciRicevuta()
        self.gestore_ric = gestore_ric
        self.gestore_ord = gestore_ord
        self.view.pulsante_conferma.clicked.connect(self.conferma_ricevuta)
        self.tavolo_selezionato = None
        lista = []
        self.controller_mostra = ContVistaMostraTavoloSelezionato(self.gestore_ric, ricevuta_temp)
        self.view.pulsante_mostra.clicked.connect(self.mostra_tavolo_selezionato)
        self.view.tabella.itemSelectionChanged.connect(self.imposta_linea_selezionata)


    def imposta_linea_selezionata(self):
        item_selezionati = self.view.tabella.selectedItems()
        for item in item_selezionati:
            if item.column() == 0:
                self.tavolo_selezionato = int(item.text())
                break


    def conferma_ricevuta(self):
        nome_acquirente = self.view.ins_nome.text()

        self.view.close()

        pass
    def mostra_tavolo_selezionato(self):


        list = self.gestore_ord.cerca_ordini_per_tavolo(self.tavolo_selezionato)

        self.controller_mostra.ordini = list
        self.controller_mostra.aggiorna_lista()
        self.controller_mostra.view.exec()


    def aggiorna_tabella(self):
        i=0
        for tavolo in self.lista_tavoli:

            num_ord = len(self.gestore_ord.cerca_ordini_per_tavolo(tavolo.numero))

            if num_ord!=0:
                self.view.tabella.setItem(i, 0, QTableWidgetItem(str(tavolo.numero)))
                self.view.tabella.setItem(i, 1, QTableWidgetItem(str(num_ord)))
                i+=1



if __name__ == '__main__':
    app = QApplication(sys.argv)
    gestore = GestoreRicevuta()
    cont = ContVistaInserisciRicevuta(gestore)
    cont.view.show()
    sys.exit(app.exec())



