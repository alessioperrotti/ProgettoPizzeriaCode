from Code.GestioneMagazzino.View.inserisci_materiaprima_view import VistaInserisciMateriaPrima
from Code.GestioneMagazzino.View.gestione_magazzino_view import VistaGestioneMagazzino
from Code.GestioneMagazzino.View.materia_prima_view import VistaMateriaPrima
from Code.GestioneMagazzino.Controller.inserisci_materiaprima_cont import ContInserisciMateriaPrima
from Code.GestioneMagazzino.Model.gestore_magazzino import GestoreMagazzino
from PyQt6.QtWidgets import QTableWidgetItem
from Code.GestioneMagazzino.Controller.materia_prima_cont import ContMateriaPrima

class ContGestioneMagazzino(object):

    def __init__(self, model: GestoreMagazzino, view: VistaGestioneMagazzino):

        self.view = view
        self.model = model
        self.update_tabella()
        self.matprima_selezionata = None
        self.view.pulsante_inserisci.clicked.connect(self.open_inserimento)
        self.view.pulsante_mostrainfo.clicked.connect(self.open_mostrainfo)
        self.view.data_grid.itemSelectionChanged.connect(self.riga_selezionata)
        self.view.pulsante_mostrainfo.clicked.connect(self.open_mostrainfo)

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

    def open_mostrainfo(self):
        dialog_mostrainfo = VistaMateriaPrima()
        controller_mostrainfo = ContMateriaPrima(dialog_mostrainfo, self.model)
        matprima_temp = self.model.estrai_per_codice(self.matprima_selezionata)  #estrae col codice ottenuto dalla tabella
        controller_mostrainfo.riempi_labels(matprima_temp)
        dialog_mostrainfo.exec()

    def update_tabella(self):
        elementi = self.model.lista_materieprime

        i = 0
        for x in elementi:
            self.view.data_grid.setItem(i, 0, QTableWidgetItem(str(x.nome)))
            self.view.data_grid.setItem(i, 1, QTableWidgetItem(str(x.codice)))
            self.view.data_grid.setItem(i, 2, QTableWidgetItem(str(x.qta_disponibile)))
            i += 1