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
        self.update_tabella()
        self.view.tab_cuoco.itemSelectionChanged.connect(self.riga_selezionata_cuoco)
        self.view.tab_cameriere.itemSelectionChanged.connect(self.riga_selezionata_cameriere)
        self.view.p_agg_cuoco.clicked.connect(self.click_aggiungi_cuoco)
        self.view.p_agg_cameriere.clicked.connect(self.click_aggiungi_cameriere)
        self.view.pulsante.clicked.connect(self.click_conferma)
        self.view.pulsante_rimuovi.clicked.connect(self.click_rimuovi)

    def riga_selezionata_cuoco(self):
        selected_items = self.view.tab_cuoco.selectedItems()
        abilita_pulsante = len(selected_items) > 0
        for item in selected_items:
            if item.column() == 0:
                nome_cognome = str(item.text())
                self.cognome_selezionato = nome_cognome.split()[1]  # Estraggo solo il cognome
            elif item.column() == 1:
                self.turno_selezionato = str(item.text())

        self.view.pulsante_rimuovi.setEnabled(abilita_pulsante)

    def riga_selezionata_cameriere(self):
        selected_items = self.view.tab_cameriere.selectedItems()
        abilita_pulsante = len(selected_items) > 0
        for item in selected_items:
            if item.column() == 0:
                nome_cognome = str(item.text())
                self.cognome_selezionato = nome_cognome.split()[1]  # Estraggo solo il cognome
            elif item.column() == 1:
                self.turno_selezionato = str(item.text())

        self.view.pulsante_rimuovi.setEnabled(abilita_pulsante)

    def riempi_labels(self, giorno):
        self.view.giorno_title.setText(str(giorno))
        # Riempi la combobox dei cuochi con gli elementi dalla lista
        for cuoco in self.model.lista_cuochi:
            # print("x")
            self.view.cuoco.addItem(cuoco.cognome)

        # Riempi la combobox dei camerieri con gli elementi dalla lista
        for cameriere in self.model.lista_camerieri:
            # print("y")
            self.view.cameriere.addItem(cameriere.cognome)

    def click_aggiungi_cuoco(self):
        self.cognome_selezionato = self.view.cuoco.currentText()
        self.turno_selezionato = self.view.turno_cuoco.currentText()
        self.dip_selezionato = self.model.estrai_cuoco_cognome(self.cognome_selezionato)

        self.update_tabella()

    def click_aggiungi_cameriere(self):
        self.cognome_selezionato = self.view.cameriere.currentText()
        self.turno_selezionato = self.view.turno_cameriere.currentText()
        self.dip_selezionato = self.model.estrai_cameriere_cognome(self.cognome_selezionato)

        self.update_tabella()

    def click_rimuovi(self):#quando clicco rimuovi prima che il tizio ha un turno crasha,giustamente
        giorno = self.view.giorno_title.text()

        if self.view.tab_cuoco.selectedItems():
            self.model.rimuovi_turno_cuoco(self.cognome_selezionato, giorno)

            righe_selezionate = self.view.tab_cuoco.selectedItems()
            if righe_selezionate:
                riga_da_eliminare = righe_selezionate[0].row()
                self.view.tab_cuoco.removeRow(riga_da_eliminare)

            self.cognome_selezionato = None
            self.view.tab_cuoco.clearSelection()
            print("C")

        if self.view.tab_cameriere.selectedItems():
            self.model.rimuovi_turno_cameriere(self.cognome_selezionato, giorno)

            righe_selezionate = self.view.tab_cameriere.selectedItems()
            if righe_selezionate:
                riga_da_eliminare = righe_selezionate[0].row()
                self.view.tab_cameriere.removeRow(riga_da_eliminare)

            self.cognome_selezionato = None
            self.view.tab_cameriere.clearSelection()
            print("S")

    def click_conferma(self):
        giorno = self.view.giorno_title.text()

        for row in range(self.view.tab_cuoco.rowCount()):
            nome_cognome = self.view.tab_cuoco.item(row, 0).text()
            cognome = nome_cognome.split()[1]
            turno = self.view.tab_cuoco.item(row, 1).text()

            cuoco = self.model.estrai_cuoco_cognome(cognome)

            self.model.aggiungi_turno_cuoco(cuoco, turno, giorno)

        for row in range(self.view.tab_cameriere.rowCount()):
            nome_cognome = self.view.tab_cameriere.item(row, 0).text()
            cognome = nome_cognome.split()[1]
            turno = self.view.tab_cameriere.item(row, 1).text()

            cameriere = self.model.estrai_cameriere_cognome(cognome)

            self.model.aggiungi_turno_cameriere(cameriere, turno, giorno)

        self.view.close()

    # def update_tabella(self):
    #
    #     for dipendente in self.model.lista_cuochi + self.model.lista_camerieri:
    #         if dipendente in self.model.lista_cuochi:
    #             tabella = self.view.tab_cuoco
    #             tabella.setItem()
    #         elif dipendente in self.model.lista_camerieri:
    #             tabella = self.view.tab_cameriere
    #
    #     if self.dip_selezionato in self.model.lista_cuochi:
    #         row_position = self.view.tab_cuoco.rowCount()
    #         self.view.tab_cuoco.insertRow(row_position)
    #         self.view.tab_cuoco.setItem(row_position, 0,
    #                                     QTableWidgetItem(
    #                                         self.dip_selezionato.nome + " " + self.dip_selezionato.cognome))
    #         self.view.tab_cuoco.setItem(row_position, 1, QTableWidgetItem(self.turno_selezionato))
    #
    #     if self.dip_selezionato in self.model.lista_camerieri:
    #         row_position = self.view.tab_cameriere.rowCount()
    #         self.view.tab_cameriere.insertRow(row_position)
    #         self.view.tab_cameriere.setItem(row_position, 0,
    #                                         QTableWidgetItem(
    #                                             self.dip_selezionato.nome + " " + self.dip_selezionato.cognome))
    #         self.view.tab_cameriere.setItem(row_position, 1, QTableWidgetItem(self.turno_selezionato))

    def aggiungi_riga_tabella(self, dipendente, turno, tabella):
        row_position = tabella.rowCount()
        tabella.insertRow(row_position)
        tabella.setItem(row_position, 0, QTableWidgetItem(f"{dipendente.nome} {dipendente.cognome}"))
        tabella.setItem(row_position, 1, QTableWidgetItem(turno))

    def update_tabella(self):
        giorno = self.view.giorno_title.text()
        indice_giorno = self.model.converti_giorno_indice(giorno)

        for dipendente in self.model.lista_cuochi + self.model.lista_camerieri:
            if dipendente in self.model.lista_cuochi:
                tabella = self.view.tab_cuoco
                if dipendente.turno[indice_giorno] is not None:
                    self.aggiungi_riga_tabella(dipendente,dipendente.turno[indice_giorno],tabella)
            elif dipendente in self.model.lista_camerieri:
                tabella = self.view.tab_cameriere
                if dipendente.turno[indice_giorno] is not None:
                    self.aggiungi_riga_tabella(dipendente,dipendente.turno[indice_giorno],tabella)

        if self.dip_selezionato in self.model.lista_cuochi:
            self.aggiungi_riga_tabella(self.dip_selezionato, self.turno_selezionato, self.view.tab_cuoco)

        if self.dip_selezionato in self.model.lista_camerieri:
            self.aggiungi_riga_tabella(self.dip_selezionato, self.turno_selezionato, self.view.tab_cameriere)

