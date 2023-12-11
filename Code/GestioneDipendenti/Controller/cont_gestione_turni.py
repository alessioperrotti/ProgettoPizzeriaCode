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

        self.view.pulsante.setEnabled(abilita_pulsante)

    def go_to_modifica(self):
        dialog_modifica = VistaModificaTurno()
        cont_modifica = ContModificaTurno(self.model, dialog_modifica)
        cont_modifica.riempi_labels(self.giorno_selezionato)
        cont_modifica.view.exec()
        self.update_tabella()

    def update_tabella(self):
        self.view.tabella.clearContents()

        #stampa di verifica
        # for cuoco in self.model.lista_cuochi:
        #     for i in range(len(cuoco.turno)):
        #         print("indice_giorno = " + str(i) + " " + str(cuoco.nome) + " turno:" + str(cuoco.turno[i])+"\n")
        #
        # for cameriere in self.model.lista_camerieri:
        #     for i in range(len(cameriere.turno)):
        #         print("indice_giorno = " + str(i) + " " + str(cameriere.nome) + " turno:" + str(cameriere.turno[i])+"\n")

        for cuoco in self.model.lista_cuochi:
            for i in range(len(cuoco.turno)):
                item_nome = QTableWidgetItem(cuoco.nome + " " + cuoco.cognome)
                item_nome.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

                if cuoco.turno[i] == "Pranzo":
                    current_item = self.view.tabella.item(0, i)
                    if current_item is not None:
                        current_item.setText(f"{current_item.text()}\n{item_nome.text()}")
                    else:
                        self.view.tabella.setItem(0, i, item_nome)
                elif cuoco.turno[i] == "Cena":
                    current_item = self.view.tabella.item(1, i)
                    if current_item is not None:
                        current_item.setText(f"{current_item.text()}\n{item_nome.text()}")
                    else:
                        self.view.tabella.setItem(1, i, item_nome)
                elif cuoco.turno[i] == "Pranzo & Cena":
                    # Handling "Pranzo & Cena" in both rows
                    current_item_pranzo = self.view.tabella.item(0, i)
                    current_item_cena = self.view.tabella.item(1, i)

                    if current_item_pranzo is not None:
                        current_item_pranzo.setText(f"{current_item_pranzo.text()}\n{item_nome.text()}")
                    else:
                        self.view.tabella.setItem(0, i, item_nome)

                    if current_item_cena is not None:
                        current_item_cena.setText(f"{current_item_cena.text()}\n{item_nome.text()}")
                    else:
                        current_item_nome_cena = QTableWidgetItem(item_nome.text())
                        current_item_nome_cena.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.view.tabella.setItem(1, i, current_item_nome_cena)

        for cameriere in self.model.lista_camerieri:
            for i in range(len(cameriere.turno)):
                item_nome = QTableWidgetItem(cameriere.nome + " " + cameriere.cognome)
                item_nome.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

                if cameriere.turno[i] == "Pranzo":
                    current_item = self.view.tabella.item(0, i)
                    if current_item is not None:
                        current_item.setText(f"{current_item.text()}\n{item_nome.text()}")
                    else:
                        self.view.tabella.setItem(0, i, item_nome)
                elif cameriere.turno[i] == "Cena":
                    current_item = self.view.tabella.item(1, i)
                    if current_item is not None:
                        current_item.setText(f"{current_item.text()}\n{item_nome.text()}")
                    else:
                        self.view.tabella.setItem(1, i, item_nome)
                elif cameriere.turno[i] == "Pranzo & Cena":
                    # Handling "Pranzo & Cena" in both rows
                    current_item_pranzo = self.view.tabella.item(0, i)
                    current_item_cena = self.view.tabella.item(1, i)

                    if current_item_pranzo is not None:
                        current_item_pranzo.setText(f"{current_item_pranzo.text()}\n{item_nome.text()}")
                    else:
                        self.view.tabella.setItem(0, i, item_nome)

                    if current_item_cena is not None:
                        current_item_cena.setText(f"{current_item_cena.text()}\n{item_nome.text()}")
                    else:
                        current_item_nome_cena = QTableWidgetItem(item_nome.text())
                        current_item_nome_cena.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                        self.view.tabella.setItem(1, i, current_item_nome_cena)



