from PyQt6.QtWidgets import QStackedWidget, QMessageBox

from Code.GestioneDipendenti.Model.gestore_dipendenti import GestoreDipendenti
from Code.GestioneMagazzino.Model.gestore_magazzino import GestoreMagazzino
from Code.GestioneOrdiniTavolo.Controller.menu_cont import ContMenu
from Code.GestioneOrdiniTavolo.Model.gestore_ordini_tavolo import GestoreOrdiniTavolo
from Code.GestioneOrdiniTavolo.View.menu_view import VistaMenu
from Code.GestioneRicevuta.Model.gestore_ricevuta import GestoreRicevuta
from Code.GestioneSistema.View.vista_inserisci_tavolo import VistaInserisciTavolo
from Code.GestioneOrdiniTavolo.Model.tavolo import Tavolo


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

    def inserisci_tavolo(self):
        n_tavolo = int(self.view.campo.text())
        self.view.campo.setText("")
        tavolo_trovato = False
        for tavolo in self.gestore_ord.lista_tavoli:
            if int(tavolo.numero) == n_tavolo:
                self.tavolo = tavolo
                tavolo.cambia_stato("occupato")
                self.gestore_ord.salva_ordini_su_file()
                tavolo_trovato = True
                self.cont_menu = ContMenu(VistaMenu(), self.gestore_ord, self.tavolo, self.stacked)
                self.stacked.setCurrentWidget(self.cont_menu.view)
                break
        if not tavolo_trovato:
            error_box = QMessageBox()
            error_box.setIcon(QMessageBox.Icon.Critical)
            error_box.setWindowTitle("Errore")
            error_box.setText("Tavolo non esistente")
            error_box.exec()

