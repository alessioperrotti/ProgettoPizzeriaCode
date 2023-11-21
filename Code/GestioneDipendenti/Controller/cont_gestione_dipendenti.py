import sys
from PyQt6.QtWidgets import QApplication, QTableWidgetItem, QVBoxLayout, QMessageBox

from Code.GestioneDipendenti.Controller.cont_inserisci_dipendente import ContInserisciDipendente
from Code.GestioneDipendenti.Model.gestore_dipendenti import GestoreDipendenti
from Code.GestioneDipendenti.View.vista_gestione_dipendenti import VistaGestioneDipendenti
from Code.GestioneDipendenti.View.vista_inserisci_dipendente import VistaInserisciDipendente


class ContGestioneDipendenti(object):
    def __init__(self, model: GestoreDipendenti, view: VistaGestioneDipendenti):
        self.view = view
        self.model = model
        self.matprima_selezionata = None
        self.view.pulsante_aggiungi.clicked.connect(self.go_to_inserimento)

    def go_to_inserimento(self):
        self.vista_inserisci = VistaInserisciDipendente()
        cont_inserisci = ContInserisciDipendente(self.model,self.vista_inserisci)
        cont_inserisci.view.show()

