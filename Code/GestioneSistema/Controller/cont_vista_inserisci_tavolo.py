from PyQt6.QtWidgets import QStackedWidget, QMessageBox

from Code.GestioneDipendenti.Model.gestore_dipendenti import GestoreDipendenti
from Code.GestioneMagazzino.Model.gestore_magazzino import GestoreMagazzino
from Code.GestioneOrdiniTavolo.Controller.menu_cont import ContMenu
from Code.GestioneOrdiniTavolo.Model.gestore_ordini_tavolo import GestoreOrdiniTavolo
from Code.GestioneOrdiniTavolo.View.menu_view import VistaMenu
from Code.GestioneRicevuta.Model.gestore_ricevuta import GestoreRicevuta
from Code.GestioneSistema.View.vista_inserisci_tavolo import VistaInserisciTavolo


class GestoreTavolo:
    pass


class ContVistaInserisciTavolo():
    def __init__(self,stacked:QStackedWidget, gestore_ric:GestoreRicevuta, gestore_dip:GestoreDipendenti,
                 gestore_mag:GestoreMagazzino,gestore_ord:GestoreOrdiniTavolo):
        self.stacked = stacked

        self.view = VistaInserisciTavolo()
        self.cont_menu = ContMenu(VistaMenu(),gestore_ord,None, stacked)
        stacked.addWidget(self.view)
        self.gestore_ord = gestore_ord
        self.view.pulsante.clicked.connect(self.inserisci_tavolo)
        self.tavolo = None

    def inserisci_tavolo(self):
        n_tavolo = self.view.campo.text()
        self.view.campo.setText("")
        tavolo_trovato = False
        for tavolo in self.gestore_ord.lista_tavoli:
            if str(tavolo.numero) == n_tavolo:
                self.tavolo = tavolo
                self.cont_menu.tavolo = tavolo
                tavolo_trovato = True
                self.stacked.setCurrentWidget(self.cont_menu.view)
                #e qui si imposta nello stacked il cont_vista_menu.view
                return
        if not tavolo_trovato:
            error_box = QMessageBox()
            error_box.setIcon(QMessageBox.Icon.Critical)
            error_box.setWindowTitle("Errore")
            error_box.setText("Tavolo non esistente")
            error_box.exec()

