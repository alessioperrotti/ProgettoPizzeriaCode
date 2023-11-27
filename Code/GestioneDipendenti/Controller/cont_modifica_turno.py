from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTableWidgetItem

from Code.GestioneDipendenti.Model.cameriere import Cameriere
from Code.GestioneDipendenti.Model.cuoco import Cuoco
from Code.GestioneDipendenti.Model.gestore_dipendenti import GestoreDipendenti
from Code.GestioneDipendenti.View.vista_modifica_turno import VistaModificaTurno


class ContModificaTurno(object):
    def __init__(self, model: GestoreDipendenti, view: VistaModificaTurno):
        self.view = view
        self.model = model
        self.view.p_agg_cuoco.clicked.connect(self.click_aggiungi_cuoco)
        # self.view.p_agg_cameriere.clicked.connect(self.click_aggiungi)

    def riempi_labels(self, giorno):
        self.view.giorno_title.setText(str(giorno))
        # Riempi la combobox dei cuochi con gli elementi dalla lista
        for cuoco in self.model.lista_cuochi:
            print("x")
            self.view.cuoco.addItem(cuoco.cognome)

        # Riempi la combobox dei camerieri con gli elementi dalla lista
        for cameriere in self.model.lista_camerieri:
            print("y")
            self.view.cameriere.addItem(cameriere.cognome)

    def click_aggiungi_cuoco(self):
        cuoco_temp = self.model.estrai_cuoco_cognome(self.view.cuoco.currentText())
        cuoco_temp.turno = self.view.turno_cuoco.currentText()
        print(cuoco_temp.turno)
        self.update_tabella()
    def update_tabella(self):
        camerieri = self.model.lista_camerieri
        cuochi = self.model.lista_cuochi

        i = 0
        # for x in camerieri:
        #     item_nome = QTableWidgetItem(x.nome + " " + x.cognome)
        #     item_nome.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        #     self.view.tab_cuoco.setItem(i, 0, item_nome)
        #
        #     item_turno = QTableWidgetItem(x.turno)
        #     item_turno.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        #     self.view.tab_cuoco.setItem(i, 1, item_turno)
        #     i += 1

        for x in cuochi:
            item_nome = QTableWidgetItem(x.nome + " " + x.cognome)
            item_nome.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.view.tab_cameriere.setItem(i, 0, item_nome)

            item_turno = QTableWidgetItem(x.turno)
            item_turno.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.view.tab_cameriere.setItem(i, 1, item_turno)
            i += 1
