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
        self.cognome_selezionato = None
        self.turno_selezionato = None
        self.dip_selezionato = None
        self.view.p_agg_cuoco.clicked.connect(self.click_aggiungi_cuoco)
        self.view.p_agg_cameriere.clicked.connect(self.click_aggiungi_cameriere)
        self.view.pulsante.clicked.connect(self.click_conferma)

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
        self.cognome_selezionato = self.view.cuoco.currentText()
        self.turno_selezionato = self.view.turno_cuoco.currentText()
        cuoco_selezionato = self.model.estrai_cuoco_cognome(self.cognome_selezionato)

        # if cuoco_selezionato:
        #     cuoco_selezionato.turno = self.turno_selezionato
        #     print(cuoco_selezionato.turno)

        self.update_tabella(cuoco_selezionato)

    def click_aggiungi_cameriere(self):
        self.cognome_selezionato = self.view.cameriere.currentText()
        self.turno_selezionato = self.view.turno_cameriere.currentText()
        cameriere_selezionato = self.model.estrai_cameriere_cognome(self.cognome_selezionato)

        if cameriere_selezionato:
            cameriere_selezionato.turno = self.turno_selezionato
            print(cameriere_selezionato.turno)

        self.update_tabella(cameriere_selezionato)

    def click_conferma(self):
        for row in range(self.view.tab_cuoco.rowCount()):
            nome_cognome = self.view.tab_cuoco.item(row,0).text()
            cognome = nome_cognome.split()[1]
            turno = self.view.tab_cuoco.item(row,1).text()

            cuoco = self.model.estrai_cuoco_cognome(cognome)

            self.model.aggiungi_turno_cuoco(cuoco,turno)

        for row in range(self.view.tab_cameriere.rowCount()):
            nome_cognome = self.view.tab_cameriere.item(row, 0).text()
            cognome = nome_cognome.split()[1]
            turno = self.view.tab_cameriere.item(row, 1).text()

            cameriere = self.model.estrai_cameriere_cognome(cognome)

            self.model.aggiungi_turno_cameriere(cameriere, turno)

        self.view.close()


    def update_tabella(self, dip_selezionato):
        self.dip_selezionato = dip_selezionato

        if self.dip_selezionato in self.model.lista_cuochi:
            row_position = self.view.tab_cuoco.rowCount()
            self.view.tab_cuoco.insertRow(row_position)

            self.view.tab_cuoco.setItem(row_position, 0, QTableWidgetItem(
                self.dip_selezionato.nome + " " + self.dip_selezionato.cognome))
            self.view.tab_cuoco.setItem(row_position, 1, QTableWidgetItem(self.turno_selezionato))
            self.view.tab_cuoco.setCellWidget(row_position, 2, self.view.p_rim_cuoco)

        if self.dip_selezionato in self.model.lista_camerieri:
            row_position = self.view.tab_cameriere.rowCount()
            self.view.tab_cameriere.insertRow(row_position)

            self.view.tab_cameriere.setItem(row_position, 0,
                                            QTableWidgetItem(
                                                self.dip_selezionato.nome + " " + self.dip_selezionato.cognome))
            self.view.tab_cameriere.setItem(row_position, 1, QTableWidgetItem(self.turno_selezionato))
            self.view.tab_cameriere.setCellWidget(row_position, 2, self.view.p_rim_cameriere)
