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
        lista_camerieri = self.model.lista_camerieri
        lista_cuochi = self.model.lista_cuochi

        # for row in range(self.view.tabella.rowCount()):
        # for col in range(self.view.tabella.columnCount()):
        #     item = QTableWidgetItem("vuoto")
        #     self.view.tabella.setItem(0, col, item)
        #     item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

        for cuoco in lista_cuochi:
            for i in range(len(cuoco.turno)):
                item_vuoto = QTableWidgetItem("vuoto")
                item_vuoto.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                item_nome = QTableWidgetItem(cuoco.nome + " " + cuoco.cognome)
                item_nome.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                print("indice_giorno = " + str(i) + " " + str(cuoco.nome) + " turno:" + str(cuoco.turno[i]))

                if cuoco.turno[i] == "Pranzo":
                    self.view.tabella.setItem(0, i, item_nome)
                elif cuoco.turno[i] == "Cena":
                    self.view.tabella.setItem(1, i, item_nome)
                elif cuoco.turno[i] == "Pranzo & Cena":
                    self.view.tabella.setItem(0, i, item_nome)
                    self.view.tabella.setItem(1, i, item_nome)
                elif cuoco.turno[i] is None:
                    self.view.tabella.setItem(0, i, item_vuoto)
                    self.view.tabella.setItem(1, i, item_vuoto)

        for cameriere in lista_camerieri:
            for i in range(len(cameriere.turno)):
                item_vuoto = QTableWidgetItem("vuoto")
                item_vuoto.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                item_nome = QTableWidgetItem(cameriere.nome + " " + cameriere.cognome)
                item_nome.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                print("indice_giorno = " + str(i) + " " + str(cameriere.nome) + " turno:" + str(cameriere.turno[i]))

                if cameriere.turno[i] == "Pranzo":
                    self.view.tabella.setItem(0, i, item_nome)
                elif cameriere.turno[i] == "Cena":
                    self.view.tabella.setItem(1, i, item_nome)
                elif cameriere.turno[i] == "Pranzo & Cena":
                    self.view.tabella.setItem(0, i, item_nome)
                    self.view.tabella.setItem(1, i, item_nome)
                elif cameriere.turno[i] is None:
                    self.view.tabella.setItem(0, i, item_vuoto)
                    self.view.tabella.setItem(1, i, item_vuoto)


        # itero cuochi nella lista cuochi
        # il cuoco ha una lista di turni
        # itero nella lista di turni
        # il turno all'indice i devo inserirlo sulla colonna i della tabella
        # se il turno è "pranzo" lo metto sulla prima riga, altrimenti 2 altrimenti entrambe
