from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QStackedWidget, QTableWidgetItem

from Code.GestioneDipendenti.Controller.cont_modifica_turno import ContModificaTurno
from Code.GestioneDipendenti.Model.gestore_dipendenti import GestoreDipendenti
from Code.GestioneDipendenti.View.vista_gestione_turni_personale import VistaGestioneTurniPersonale
from Code.GestioneDipendenti.View.vista_modifica_turno import VistaModificaTurno


class ContGestioneTurni(object):
    def __init__(self, model: GestoreDipendenti, stacked: QStackedWidget):
        self.stacked = stacked
        self.view = VistaGestioneTurniPersonale()
        stacked.addWidget(self.view)
        self.model = model
        self.update_tabella()
        self.giorno_selezionato = None
        self.view.tabella.itemSelectionChanged.connect(self.colonna_selezionata)
        self.view.pulsante.clicked.connect(self.go_to_modifica)

    def colonna_selezionata(self):
        selected_items = self.view.tabella.selectedItems()
        abilita_pulsante = len(selected_items) > 0
        colonne_selezionate = []

        for item in selected_items:
            colonna_selezionata = item.column()
            colonne_selezionate.append(colonna_selezionata)
        if colonne_selezionate:
            indice_colonna_selezionata = colonne_selezionate[0]
            self.giorno_selezionato = self.view.tabella.horizontalHeaderItem(indice_colonna_selezionata).text()
            print(self.giorno_selezionato)

        self.view.pulsante.setEnabled(abilita_pulsante)

    def go_to_modifica(self):
        dialog_modifica = VistaModificaTurno()
        cont_modifica = ContModificaTurno(self.model, dialog_modifica)
        cont_modifica.riempi_labels(self.giorno_selezionato)
        cont_modifica.view.exec()
        self.update_tabella()

    def update_tabella(self):
        camerieri = self.model.lista_camerieri
        cuochi = self.model.lista_cuochi

        i = 0
        for x in camerieri:
            # self.view.tab.setItem(i, 0, QTableWidgetItem(x.nome+" "+x.cognome))
            # self.view.tab.setItem(i, 1, QTableWidgetItem(x.ruolo))
            # i += 1

            item_nome = QTableWidgetItem(x.nome + "\n" + x.cognome)
            item_nome.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.view.tabella.setItem(i, 0, item_nome)
            i += 1

        for x in cuochi:
            # self.view.tab.setItem(i, 0, QTableWidgetItem(x.nome+" "+x.cognome))
            # self.view.tab.setItem(i, 1, QTableWidgetItem(x.ruolo))
            # i += 1

            item_nome = QTableWidgetItem(x.nome + " " + x.cognome)
            item_nome.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.view.tabella.setItem(i, 0, item_nome)
            i += 1
