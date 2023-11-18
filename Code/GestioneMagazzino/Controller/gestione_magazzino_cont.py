from Code.GestioneMagazzino.View.inserisci_materiaprima_view import VistaInserisciMateriaPrima
from Code.GestioneMagazzino.View.gestione_magazzino_view import VistaGestioneMagazzino
from Code.GestioneMagazzino.Controller.inserisci_materiaprima_cont import ContInserisciMateriaPrima
from Code.GestioneMagazzino.Model.gestore_magazzino import GestoreMagazzino
from PyQt6.QtWidgets import QTableWidgetItem

class ContGestioneMagazzino(object):

    def __init__(self, model: GestoreMagazzino, view: VistaGestioneMagazzino):

        self.view = view
        self.model = model
        self.update_tabella()
        self.view.pulsante_inserisci.clicked.connect(self.open_inserimento)

    def open_inserimento(self):
        dialog_inserimento = VistaInserisciMateriaPrima()
        controller_inserimento = ContInserisciMateriaPrima(self.model, dialog_inserimento)
        controller_inserimento.view.exec()
        self.update_tabella()

    def update_tabella(self):
        elementi = self.model.lista_materieprime

        i = 0
        for x in elementi:
            self.view.data_grid.setItem(i, 0, QTableWidgetItem(str(x.nome)))
            self.view.data_grid.setItem(i, 1, QTableWidgetItem(str(x.codice)))
            self.view.data_grid.setItem(i, 2, QTableWidgetItem(str(x.qta_disponibile)))
            i += 1