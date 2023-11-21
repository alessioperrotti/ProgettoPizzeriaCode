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
        self.update_tabella()
        self.view.pulsante_aggiungi.clicked.connect(self.go_to_inserimento)

    def go_to_inserimento(self):
        vista_inserisci = VistaInserisciDipendente()
        cont_inserisci = ContInserisciDipendente(self.model, vista_inserisci)
        cont_inserisci.view.exec()

        self.update_tabella()

    def update_tabella(self):
        camerieri = self.model.lista_camerieri
        cuochi = self.model.lista_cuochi

        i = 0

        for x in camerieri:

            self.view.tab.setItem(i, 0, QTableWidgetItem(x.nome))
            self.view.tab.setItem(i, 1, QTableWidgetItem(x.ruolo))
            i += 1

        for x in cuochi:
            print(x.nome)
            self.view.tab.setItem(i, 0, QTableWidgetItem(x.nome))
            self.view.tab.setItem(i, 1, QTableWidgetItem(x.ruolo))
            i += 1

