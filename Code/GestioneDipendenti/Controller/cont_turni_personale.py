from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QStackedWidget, QTableWidgetItem

from Code.GestioneDipendenti.Controller.cont_gestione_turni import ContGestioneTurni
from Code.GestioneDipendenti.Model.gestore_dipendenti import GestoreDipendenti
from Code.GestioneDipendenti.View.vista_turni_personale import VistaTurniPersonale


class ContTurniPersonale(object):
    def __init__(self, model: GestoreDipendenti, stacked: QStackedWidget):
        self.view = VistaTurniPersonale()
        self.model = model
        self.update_tabella()
        self.stacked = stacked
        stacked.addWidget(self.view)

    def update_tabella(self):
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
