from Code.GestioneMenu.View.inserisci_prodotto_view import VistaInserisciProdotto
from Code.GestioneMenu.Model.prodotto import Prodotto
from Code.GestioneMagazzino.Controller.inserisci_materiaprima_cont import UsedCode
from Code.GestioneMagazzino.Model.gestore_magazzino import GestoreMagazzino
from Code.GestioneMenu.Model.gestore_menu import GestoreMenu
from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem
from PyQt6.QtCore import Qt


class NoIngredienti(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class ContInserisciProdotto(object):

    def __init__(self, view: VistaInserisciProdotto, model: GestoreMenu):

        self.view = view
        self.model = model
        self.magazzino = GestoreMagazzino()
        self.matprima_selezionata = None
        self.lista_ingredienti = []
        self.view.pulsante_conferma.clicked.connect(self.conferma_inserimento)
        self.view.pulsante_aggiungi.clicked.connect(self.aggiungi_alla_tabella_ingredienti)
        self.view.data_grid.itemSelectionChanged.connect(self.riga_selezionata)
        self.view.pulsante_rimuovi.setEnabled(self.matprima_selezionata is not None)

    def conferma_inserimento(self):

        try:
            nome = self.view.campo_nome.text().title()
            codice = self.view.campo_codice.text()
            if self.model.estrai_per_codice(codice) is not None:
                raise UsedCode("Il codice inserito risulta già utilizzato.")
            prezzo = round(float(self.view.campo_prezzo.text()))
            tipo = self.view.combo_tipologia.currentText().lower()

            if self.view.data_grid.rowCount() == 0:
                raise NoIngredienti("Controllare di aver inserito gli ingredienti.")
            else:
                ingredienti = []
                for i in range(self.view.data_grid.rowCount()):
                    nome_ingrediente = self.view.data_grid.item(i, 0)
                    quantita = self.view.data_grid.item(i, 1)
                    matprima = self.magazzino.estrai_per_nome(nome_ingrediente)
                    ingrediente = (matprima, quantita)
                    ingredienti.append(ingrediente)

                nuovo_prodotto = Prodotto(nome, codice, prezzo, tipo, ingredienti)

        except ValueError:
            if not all([
                self.view.campo_codice.text(),
                self.view.campo_nome.text(),
                self.view.campo_prezzo.text(),
                self.view.combo_tipologia.currentText().lower(),
            ]):
                errore_msg = "Controllare che tutti i campi siano riempiti."
            else:
                errore_msg = "Controllare che i dati siano inseriti correttamente."

            error_box = QMessageBox()
            error_box.setIcon(QMessageBox.Icon.Critical)
            error_box.setWindowTitle("Errore di Inserimento")
            error_box.setText(errore_msg)
            error_box.exec()

        except UsedCode as uc:
            error_box = QMessageBox()
            error_box.setIcon(QMessageBox.Icon.Critical)
            error_box.setWindowTitle("Errore di Inserimento")
            error_box.setText(uc.message)
            error_box.exec()

        except NoIngredienti as ni:
            error_box = QMessageBox()
            error_box.setIcon(QMessageBox.Icon.Critical)
            error_box.setWindowTitle("Errore di Inserimento")
            error_box.setText(ni.message)
            error_box.exec()

        else:
            self.model.aggiungi_prodotto(nuovo_prodotto)
            self.view.close()


    def aggiungi_alla_tabella_ingredienti(self):

        nome_ingrediente = self.view.combo_ingrediente.currentText().title()
        try:
            quantita = round(float(self.view.campo_quantita.text()), 3)
        except ValueError:
            if not all([self.view.combo_ingrediente.currentText().lower(),
                        round(float(self.view.campo_quantita.text()), 3)]):
                errore_msg = "Riempire tutti i campi dell'ingrediente."
            else:
                errore_msg = "Controllare la quantità inserita."
            error_box = QMessageBox()
            error_box.setIcon(QMessageBox.Icon.Critical)
            error_box.setWindowTitle("Errore di Inserimento")
            error_box.setText(errore_msg)
            error_box.exec()
        else:
            righe = self.view.data_grid.rowCount()
            self.view.data_grid.setRowCount(righe+1)
            item1 = QTableWidgetItem(nome_ingrediente)
            item2 = QTableWidgetItem(str(quantita))
            self.view.data_grid.setItem(righe, 0, item1)
            item1.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.view.data_grid.setItem(righe, 1, item2)
            item2.setTextAlignment(Qt.AlignmentFlag.AlignCenter)


    def riga_selezionata(self):

        selected_items = self.view.data_grid.selectedItems()
        abilita_pulsante = len(selected_items) > 0
        for item in selected_items:
            if item.column() == 1:
                self.matprima_selezionata = int(item.text())
        self.view.pulsante_rimuovi.setEnabled(abilita_pulsante)


    def riempi_combo(self):

        for x in self.magazzino.lista_materieprime:
            self.view.combo_ingrediente.addItem(x.nome)

    def elimina_dalla_tabella_ingredienti(self):

        riga_da_eliminare = self.view.data_grid.currentRow()
        if riga_da_eliminare >= 0:
            self.view.data_grid.removeRow(riga_da_eliminare)