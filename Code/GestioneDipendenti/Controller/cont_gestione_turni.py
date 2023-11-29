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

        for row in range(self.view.tabella.rowCount()):
            for col in range(self.view.tabella.columnCount()):
                item = QTableWidgetItem("vuoto")
                self.view.tabella.setItem(row, col, item)
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

        # for x in cuochi:
        #     item_nome = QTableWidgetItem(x.nome + " " + x.cognome)
        #     item_nome.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        #
        #     if x.turno == "Pranzo":
        #         testo_attuale = self.view.tabella.item(0, i).text() if self.view.tabella.item(0,
        #                                                                                       i) is not None else ""
        #         testo_combinato = testo_attuale + "\n" + item_nome.text() if testo_attuale else item_nome.text()
        #         self.view.tabella.setItem(0, i, QTableWidgetItem(testo_combinato))
        #     elif x.turno == "Cena":
        #         self.view.tabella.setItem(1, i, item_nome)
        #     elif x.turno == "Pranzo & Cena":
        #         testo_attuale = self.view.tabella.item(0, i).text() if self.view.tabella.item(0,
        #                                                                                       i) is not None else ""
        #         testo_combinato = testo_attuale + "\n" + item_nome.text() if testo_attuale else item_nome.text()
        #         self.view.tabella.setItem(0, i, QTableWidgetItem(testo_combinato))
        #         self.view.tabella.setItem(1, i, item_nome)
        #
        #     i += 1


