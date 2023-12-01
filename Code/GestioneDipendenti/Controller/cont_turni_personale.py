from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QStackedWidget, QTableWidgetItem

from Code.GestioneDipendenti.Controller.cont_gestione_turni import ContGestioneTurni
from Code.GestioneDipendenti.Model.gestore_dipendenti import GestoreDipendenti
from Code.GestioneDipendenti.View.vista_turni_personale import VistaTurniPersonale


class ContTurniPersonale(object):
    def __init__(self, model: GestoreDipendenti, stacked: QStackedWidget):
        self.stacked = stacked
        self.view = VistaTurniPersonale()
        stacked.addWidget(self.view)
        self.model = model
        self.update_tabella()
        # self.view.pulsante.clicked.connect(self.go_back)

    def update_tabella(self):
        cont_gestione_turni = ContGestioneTurni(self.model, self.stacked)
        tab1 = cont_gestione_turni.view.tabella
        for row in range(tab1.rowCount()):
            for col in range(tab1.columnCount()):
                item = tab1.item(row, col)
                if item is not None:
                    new_item = QTableWidgetItem(item.text())
                    self.view.tabella.setItem(row, col, new_item)
