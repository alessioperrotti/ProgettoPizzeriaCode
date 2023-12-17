import os
import sys

from PyQt6.QtWidgets import QApplication, QTableWidgetItem, QMessageBox
from Code.GestioneOrdiniTavolo.Model.gestore_ordini_tavolo import GestoreOrdiniTavolo
from Code.GestioneOrdiniTavolo.Model.tavolo import Tavolo
from Code.GestioneRicevuta.Controller.cont_vista_mostra_tavolo_selezionato import ContVistaMostraTavoloSelezionato
from Code.GestioneRicevuta.Model.gestore_ricevuta import GestoreRicevuta
from Code.GestioneRicevuta.Model.ricevuta import Ricevuta
from Code.GestioneRicevuta.View.vista_inserisci_ricevuta import VistaInserisciRicevuta


class ContVistaInserisciRicevuta:
    cartella_controller = os.path.dirname(os.path.realpath(__file__))
    cartella_base = os.path.abspath(os.path.join(cartella_controller, os.pardir))
    cartella_data = os.path.join(cartella_base, 'Data')

    def __init__(self, gestore_ric: GestoreRicevuta, gestore_ord: GestoreOrdiniTavolo, lista_tav: list[Tavolo]):

        self.lista_tavoli = lista_tav
        self.view = VistaInserisciRicevuta()
        self.ricevuta_temp = Ricevuta()
        self.gestore_ric = gestore_ric
        self.gestore_ord = gestore_ord
        self.view.pulsante_conferma.clicked.connect(self.conferma_ricevuta)
        self.tavolo_selezionato = None

        self.controller_mostra = ContVistaMostraTavoloSelezionato(self.gestore_ric, self.ricevuta_temp)
        self.view.pulsante_mostra.clicked.connect(self.mostra_tavolo_selezionato)
        self.view.tabella.itemSelectionChanged.connect(self.imposta_linea_selezionata)
        self.view.pulsante_mostra.setEnabled(self.tavolo_selezionato is not None)
        self.view.ricerca.textChanged.connect(self.filtra_tabella)

    def imposta_linea_selezionata(self):
        item_selezionati = self.view.tabella.selectedItems()
        for item in item_selezionati:
            if item.column() == 0:
                self.tavolo_selezionato = int(item.text())
                break
        self.view.pulsante_mostra.setEnabled(self.tavolo_selezionato is not None)

    def conferma_ricevuta(self):

        nome_acquirente = self.view.ins_nome.text()
        self.ricevuta_temp.nomeAcquirente = nome_acquirente
        if self.ricevuta_temp.nomeAcquirente == "":
            self.ricevuta_temp.nomeAcquirente = "Anonimo"

        if self.controller_mostra.ordini == []:
            error_box = QMessageBox()
            error_box.setIcon(QMessageBox.Icon.Critical)
            error_box.setWindowTitle("Errore")
            error_box.setText("Selezionare almeno un ordine per poter confermare la ricevuta")
            error_box.exec()


        else:

            num = self.gestore_ric.aggiungi_ricevuta(self.ricevuta_temp.ammontareLordo, self.ricevuta_temp.data,
                                                     self.ricevuta_temp.listaProdotti,
                                                     self.ricevuta_temp.nomeAcquirente, self.ricevuta_temp.ora,
                                                     self.ricevuta_temp.tavolo)
            self.gestore_ric.ricerca_ricevuta_numero(num)

            for ordine in self.controller_mostra.ordini:
                ordine.pagato = True

            self.gestore_ord.salva_ordini_su_file()

            self.view.close()
            self.view.ins_nome.clear()
            self.view.ricerca.clear()
            self.ricevuta_temp = Ricevuta()
            self.controller_mostra.ordini = []

    def mostra_tavolo_selezionato(self):

        list = self.gestore_ord.cerca_ordini_per_tavolo_da_pagare(self.tavolo_selezionato)
        self.controller_mostra.ric = self.ricevuta_temp
        self.controller_mostra.ordini = list
        self.controller_mostra.aggiorna_lista()
        self.controller_mostra.view.exec()
        self.view.tabella.clearSelection()
        self.tavolo_selezionato = None
        self.view.pulsante_mostra.setEnabled(self.tavolo_selezionato is not None)
        self.ricevuta_temp = self.controller_mostra.ric

    def aggiorna_tabella(self):

        i = 0
        for tavolo in self.lista_tavoli:

            num_ord = len(self.gestore_ord.cerca_ordini_per_tavolo_da_pagare(tavolo.numero))

            if num_ord != 0:
                self.view.tabella.setItem(i, 0, QTableWidgetItem(str(tavolo.numero)))
                self.view.tabella.setItem(i, 1, QTableWidgetItem(str(num_ord)))
                i += 1

        self.view.tabella.setRowCount(i)

    def filtra_tabella(self):
        testo_ricerca = self.view.ricerca.text().lower()

        for riga in range(self.view.tabella.rowCount()):
            n_tavolo = self.view.tabella.item(riga, 0).text().lower()
            self.view.tabella.setRowHidden(riga, testo_ricerca not in n_tavolo)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gestore = GestoreRicevuta()
    cont = ContVistaInserisciRicevuta(gestore)
    cont.view.show()
    sys.exit(app.exec())
