from Code.GestioneMenu.Model.gestore_menu import GestoreMenu
from Code.GestioneMenu.Model.prodotto import Prodotto
from Code.GestioneMenu.View.modifica_prodotto_view import VistaModificaProdotto
from Code.GestioneMagazzino.Model.gestore_magazzino import GestoreMagazzino
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtCore import Qt

class ContModificaProdotto(object):

    def __init__(self, view: VistaModificaProdotto, model: GestoreMenu, prodotto_da_modificare: Prodotto):
        self.view = view
        self.model = model
        self.magazzino = GestoreMagazzino()
        self.prodotto_da_modificare = prodotto_da_modificare
        self.riempi_labels(prodotto_da_modificare)

    def riempi_labels(self, prodotto: Prodotto):

        self.view.label_nome_val.setText(str(prodotto.nome))
        self.view.label_codice_val.setText(str(prodotto.codice))
        self.view.campo_prezzo.setPlaceholderText(str(prodotto.prezzo_al_pubblico))
        self.view.combo_tipologia.setCurrentText(prodotto.tipologia)
        ingredienti = prodotto.ingredienti
        for x in ingredienti:
            righe = self.view.data_grid.rowCount()
            self.view.data_grid.setRowCount(righe+1)
            item1 = QTableWidgetItem(str(x[0]))
            self.view.data_grid.setItem(righe, 0, item1)
            item1.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            item2 = QTableWidgetItem(str(x[1]))
            self.view.data_grid.setItem(righe, 1, item2)
            item2.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
