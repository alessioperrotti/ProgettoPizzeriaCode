from Code.GestioneMagazzino.View.inserisci_materiaprima_view import VistaInserisciMateriaPrima
from Code.GestioneMagazzino.View.gestione_magazzino_view import VistaGestioneMagazzino
from Code.GestioneMagazzino.View.materia_prima_view import VistaMateriaPrima
from Code.GestioneMagazzino.Controller.inserisci_materiaprima_cont import ContInserisciMateriaPrima
from Code.GestioneMagazzino.Controller.modifica_materiaprima_cont import ContModificaMateriaPrima
from Code.GestioneMagazzino.Model.gestore_magazzino import GestoreMagazzino
from Code.GestioneMagazzino.View.modifica_materiaprima_view import VistaModificaMateriaPrima
from PyQt6.QtWidgets import QTableWidgetItem
from PyQt6.QtCore import Qt
from Code.GestioneMagazzino.Controller.materia_prima_cont import ContMateriaPrima

class ContGestioneMagazzino(object):

    def __init__(self, model: GestoreMagazzino, view: VistaGestioneMagazzino):

        self.view = view
        self.model = model
        self.update_tabella()
        self.matprima_selezionata = None
        self.view.pulsante_inserisci.clicked.connect(self.open_inserimento)
        self.view.search_bar.textChanged.connect(self.filtra_elementi)
        self.view.pulsante_mostrainfo.clicked.connect(self.open_mostrainfo)
        self.view.data_grid.itemSelectionChanged.connect(self.riga_selezionata)
        self.view.pulsante_elimina.clicked.connect(self.elimina_elemento)
        self.view.pulsante_modifica.clicked.connect(self.open_modifica)

    def open_inserimento(self):

        dialog_inserimento = VistaInserisciMateriaPrima()
        controller_inserimento = ContInserisciMateriaPrima(self.model, dialog_inserimento)
        controller_inserimento.view.exec()
        self.update_tabella()


    def riga_selezionata(self):

        selected_items = self.view.data_grid.selectedItems()
        abilita_pulsante = len(selected_items) > 0
        for item in selected_items:
            if item.column() == 1:
                self.matprima_selezionata = int(item.text())
        self.view.pulsante_mostrainfo.setEnabled(abilita_pulsante)
        self.view.pulsante_modifica.setEnabled(abilita_pulsante)

    def open_mostrainfo(self):
        dialog_mostrainfo = VistaMateriaPrima()
        controller_mostrainfo = ContMateriaPrima(dialog_mostrainfo, self.model)
        matprima_temp = self.model.estrai_per_codice(self.matprima_selezionata)  #estrae col codice ottenuto dalla tabella
        controller_mostrainfo.riempi_labels(matprima_temp)
        dialog_mostrainfo.exec()

    def update_tabella(self):

        elementi = self.model.lista_materieprime
        self.view.data_grid.setRowCount(len(elementi))
        i = 0
        for x in elementi:
            item1 = QTableWidgetItem(str(x.nome))
            self.view.data_grid.setItem(i, 0, item1)
            item1.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            stringa_a_4_cifre = "{:04d}".format(int(x.codice))
            item2 = QTableWidgetItem(stringa_a_4_cifre)
            self.view.data_grid.setItem(i, 1, item2)
            item2.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            item3 = QTableWidgetItem(str(x.qta_disponibile))
            self.view.data_grid.setItem(i, 2, item3)
            item3.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            i += 1


    def elimina_elemento(self):

        self.model.elimina_materiaprima(self.matprima_selezionata)
        self.update_tabella()
        self.matprima_selezionata = None
        self.view.data_grid.clearSelection()

    def open_modifica(self):
        dialog_modifica = VistaModificaMateriaPrima()
        matprima_temp = self.model.estrai_per_codice(self.matprima_selezionata)
        controller_modifica = ContModificaMateriaPrima(dialog_modifica, self.model, matprima_temp)
        controller_modifica.view.exec()
        self.update_tabella()


    def filtra_elementi(self):

        testo_ricerca = self.view.search_bar.text().lower()
        for row in range(self.view.data_grid.rowCount()):
            nome_materiaprima = self.view.data_grid.item(row, 0).text().lower()
            self.view.data_grid.setRowHidden(row, testo_ricerca not in nome_materiaprima)