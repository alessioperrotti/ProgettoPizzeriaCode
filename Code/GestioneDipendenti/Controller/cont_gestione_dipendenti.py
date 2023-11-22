import sys
from PyQt6.QtWidgets import QApplication, QTableWidgetItem, QVBoxLayout, QMessageBox

from Code.GestioneDipendenti.Controller.cont_inserisci_dipendente import ContInserisciDipendente
from Code.GestioneDipendenti.Controller.cont_mostra_dipendente import ContMostraDipendente
from Code.GestioneDipendenti.Model.gestore_dipendenti import GestoreDipendenti
from Code.GestioneDipendenti.View.vista_gestione_dipendenti import VistaGestioneDipendenti
from Code.GestioneDipendenti.View.vista_inserisci_dipendente import VistaInserisciDipendente
from Code.GestioneDipendenti.View.vista_visualizza_dipendente import VistaVisualizzaDipendente


class ContGestioneDipendenti(object):
    def __init__(self, model: GestoreDipendenti, view: VistaGestioneDipendenti):
        self.view = view
        self.model = model
        self.update_tabella()
        self.dipendente_selezionato = None
        self.view.pulsante_aggiungi.clicked.connect(self.go_to_inserimento)
        self.view.pulsante_mostra.clicked.connect(self.go_to_mostrainfo)

    def riga_selezionata(self):
        selected_items = self.view.tab.selectedItems()
        abilita_pulsante = len(selected_items) > 0
        for item in selected_items:
            if item.column() == 1:
                self.dipendente_selezionato = int(item.text())
        self.view.pulsante_mostra.setEnabled(abilita_pulsante)

    def go_to_mostrainfo(self):
        dialog_mostrainfo = VistaVisualizzaDipendente()
        controller_mostrainfo = ContMostraDipendente(dialog_mostrainfo, self.model)
        dipendente_temp = self.model.estrai_cuoco_nome(self.dipendente_selezionato)  #estrae col nome ottenuto dalla tabella
        controller_mostrainfo.riempi_labels(dipendente_temp)
        dialog_mostrainfo.exec()

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
            self.view.tab.setRowCount(i + 1)
            self.view.tab.setItem(i, 0, QTableWidgetItem(x.nome))
            self.view.tab.setItem(i, 1, QTableWidgetItem(x.ruolo))
            i += 1

        for x in cuochi:
            self.view.tab.setRowCount(i + 1)
            self.view.tab.setItem(i, 0, QTableWidgetItem(x.nome))
            self.view.tab.setItem(i, 1, QTableWidgetItem(x.ruolo))
            i += 1

