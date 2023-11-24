from Code.GestioneMenu.Model.gestore_menu import GestoreMenu
from Code.GestioneMenu.View.gestione_menu_view import VistaGestioneMenu
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtCore import Qt

class ContGestioneMenu(object):

    def __init__(self, view: VistaGestioneMenu, model: GestoreMenu):

        self.view = view
        self.model = model
        self.update_tabella()

    def update_tabella(self):

        elementi = self.model.lista_prodotti()
        self.view.data_grid.setRowCount(len(elementi))
        i = 0
        for x in elementi:
            item1 = QTableWidgetItem(str(x.nome))
            self.view.data_grid.setItem(i, 0, item1)
            item1.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            item2 = QTableWidgetItem(str(x.prezzo))
            self.view.data_grid.setItem(i, 1, item2)
            item2.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            item3 = QTableWidgetItem(str(x.tipologia))
            self.view.data_grid.setItem(i, 2, item3)
            item3.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            i += 1