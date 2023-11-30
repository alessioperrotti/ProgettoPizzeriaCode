from Code.GestioneMenu.Model.gestore_menu import GestoreMenu
from Code.GestioneMenu.View.gestione_menu_view import VistaGestioneMenu
from Code.GestioneMenu.View.inserisci_prodotto_view import VistaInserisciProdotto
from Code.GestioneMenu.Controller.inserisci_prodotto_cont import ContInserisciProdotto
from Code.GestioneMenu.View.msg_elimina_prodotto_view import VistaMsgEliminaProdotto
from Code.GestioneMenu.Controller.msg_elimina_prodotto_cont import ContMsgEliminaProdotto
from Code.GestioneMenu.View.modifica_prodotto_view import VistaModificaProdotto
from Code.GestioneMenu.Controller.modifica_prodotto_cont import ContModificaProdotto
from PyQt6.QtWidgets import QTableWidgetItem, QStackedWidget
from PyQt6.QtCore import Qt


class ContGestioneMenu(object):

    def __init__(self, view: VistaGestioneMenu, model: GestoreMenu, stacked: QStackedWidget):

        self.view = view
        self.model = model
        self.stacked = stacked
        stacked.addWidget(self.view)
        self.update_tabella()
        self.prodotto_selezionato = None
        self.view.search_bar.textChanged.connect(self.filtra_elementi)
        self.view.pulsante_inserisci.clicked.connect(self.open_inserimento)
        self.view.data_grid.itemSelectionChanged.connect(self.riga_selezionata)
        self.view.pulsante_elimina.setEnabled(self.prodotto_selezionato is not None)
        self.view.pulsante_elimina.clicked.connect(self.elimina_elemento)
        self.view.pulsante_modifica.setEnabled(self.prodotto_selezionato is not None)
        self.view.pulsante_modifica.clicked.connect(self.open_modifica)


    def update_tabella(self):

        elementi = self.model.lista_prodotti
        self.view.data_grid.setRowCount(len(elementi))
        i = 0
        for x in elementi:
            item1 = QTableWidgetItem(str(x.nome))
            self.view.data_grid.setItem(i, 0, item1)
            item1.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            item2 = QTableWidgetItem(str(x.prezzo_al_pubblico))
            self.view.data_grid.setItem(i, 1, item2)
            item2.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            item3 = QTableWidgetItem(str(x.tipologia))
            self.view.data_grid.setItem(i, 2, item3)
            item3.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            i += 1

    def open_inserimento(self):
        dialog_inserimento = VistaInserisciProdotto()
        controller_inserimento = ContInserisciProdotto(dialog_inserimento, self.model)
        controller_inserimento.view.exec()
        self.update_tabella()


    def riga_selezionata(self):

        selected_items = self.view.data_grid.selectedItems()
        abilita_pulsante = len(selected_items) > 0
        for item in selected_items:
            if item.column() == 0:
                self.prodotto_selezionato = item.text()
        self.view.pulsante_modifica.setEnabled(abilita_pulsante)
        self.view.pulsante_elimina.setEnabled(abilita_pulsante)


    def elimina_elemento(self):

        dialog_conferma_elimina = VistaMsgEliminaProdotto()
        controller_conferma = ContMsgEliminaProdotto(dialog_conferma_elimina)
        controller_conferma.view.exec()
        if controller_conferma.conferma:
            controller_conferma.view.close()
            self.model.elimina_prodotto(self.prodotto_selezionato)
            self.update_tabella()
            self.prodotto_selezionato = None
            self.view.data_grid.clearSelection()


    def open_modifica(self):
        dialog_modifica = VistaModificaProdotto()
        prodotto_temp = self.model.estrai_per_nome(self.prodotto_selezionato)
        controller_modifica = ContModificaProdotto(dialog_modifica, self.model, prodotto_temp)
        controller_modifica.view.exec()
        self.update_tabella()


    def filtra_elementi(self):

        testo_ricerca = self.view.search_bar.text().lower()
        for row in range(self.view.data_grid.rowCount()):
            nome_prodotto = self.view.data_grid.item(row, 0).text().lower()
            self.view.data_grid.setRowHidden(row, testo_ricerca not in nome_prodotto)