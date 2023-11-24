from PyQt6.QtWidgets import QStackedWidget, QMessageBox

from Code.GestioneDipendenti.Model.gestore_dipendenti import GestoreDipendenti
from Code.GestioneMagazzino.Model.gestore_magazzino import GestoreMagazzino
from Code.GestioneOrdiniTavolo.Model.gestore_ordini_tavolo import GestoreOrdiniTavolo
from Code.GestioneRicevuta.Model.gestore_ricevuta import GestoreRicevuta
from Code.GestioneSistema.View.vista_inserisci_tavolo import VistaInserisciTavolo


class GestoreTavolo:
    pass


class ContVistaInserisciTavolo():
    def __init__(self,stacked:QStackedWidget, gestore_ric:GestoreRicevuta, gestore_dip:GestoreDipendenti,
                 gestore_mag:GestoreMagazzino,gestore_ord:GestoreOrdiniTavolo):
        self.stacked = stacked

        self.view = VistaInserisciTavolo()
        stacked.addWidget(self.view)
        self.gestore_ord = gestore_ord
        self.view.pulsante.clicked.connect(self.inserisci_tavolo)
        self.tavolo = None

    def inserisci_tavolo(self):
        n_tavolo = self.view.campo.text()
        self.view.campo.setText("")
        for tavolo in self.gestore_ord.lista_tavoli:
            if str(tavolo.numero) == n_tavolo:
                self.tavolo = tavolo
                #e qui si imposta nello stacked il cont_vista_menu.view
                return

        error_box = QMessageBox()
        error_box.setIcon(QMessageBox.Icon.Critical)
        error_box.setWindowTitle("Errore")
        error_box.setText("Tavolo non esistente")
        error_box.exec()
