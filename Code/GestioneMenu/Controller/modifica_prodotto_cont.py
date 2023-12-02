from Code.GestioneMenu.Model.gestore_menu import GestoreMenu
from Code.GestioneMenu.Model.prodotto import Prodotto
from Code.GestioneMenu.View.modifica_prodotto_view import VistaModificaProdotto
from Code.GestioneMagazzino.Model.gestore_magazzino import GestoreMagazzino
from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox
from PyQt6.QtCore import Qt
from Code.GestioneMenu.Controller.inserisci_prodotto_cont import NoIngredienti

class ContModificaProdotto(object):

    def __init__(self, view: VistaModificaProdotto, model: GestoreMenu, prodotto_da_modificare: Prodotto):
        self.view = view
        self.model = model
        self.magazzino = GestoreMagazzino()
        self.riempi_combo()
        self.prodotto_da_modificare = prodotto_da_modificare
        self.prodotto_selezionato = None
        self.riempi_labels(prodotto_da_modificare)
        self.view.pulsante_aggiungi.clicked.connect(self.aggiungi_alla_tabella_ingredienti)
        self.view.data_grid.itemSelectionChanged.connect(self.riga_selezionata)
        self.view.pulsante_rimuovi.setEnabled(self.prodotto_selezionato is not None)
        self.view.pulsante_rimuovi.clicked.connect(self.elimina_dalla_tabella_ingredienti)
        self.view.pulsante_conferma.clicked.connect(self.conferma_modifica)

    def riempi_labels(self, prodotto: Prodotto):

        self.view.label_nome_val.setText(str(prodotto.nome))
        codice_a_4_cifre = "{:04d}".format(int(prodotto.codice))
        self.view.label_codice_val.setText(codice_a_4_cifre)
        self.view.campo_prezzo.setPlaceholderText(str(prodotto.prezzo_al_pubblico))
        self.view.combo_tipologia.setCurrentText(str(prodotto.tipologia).title())
        self.view.combo_tipologia.setEnabled(False)
        ingredienti = prodotto.ingredienti
        for x in ingredienti:
            righe = self.view.data_grid.rowCount()
            self.view.data_grid.setRowCount(righe+1)
            item1 = QTableWidgetItem(str(x[0].nome))
            self.view.data_grid.setItem(righe, 0, item1)
            item1.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            item2 = QTableWidgetItem(str(x[1]))
            self.view.data_grid.setItem(righe, 1, item2)
            item2.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

    def aggiungi_alla_tabella_ingredienti(self):

        nome_ingrediente = self.view.combo_ingrediente.currentText().title()
        try:
            quantita = round(float(self.view.campo_quantita.text()), 3)

        except ValueError:
            if not all([self.view.combo_ingrediente.currentText().lower(),
                        self.view.campo_quantita.text()]):
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

            if (self.prodotto_da_modificare.tipologia.lower() == 'soft drink'
                    or self.prodotto_da_modificare.tipologia.lower() == 'birra') and self.view.data_grid.rowCount() == 1:
                self.view.combo_ingrediente.setEnabled(False)
                self.view.campo_quantita.setEnabled(False)
                self.view.pulsante_aggiungi.setEnabled(False)

    def riga_selezionata(self):

        selected_items = self.view.data_grid.selectedItems()
        abilita_pulsante = len(selected_items) > 0
        for item in selected_items:
            if item.column() == 0:
                self.prodotto_selezionato = item.text()
        self.view.pulsante_rimuovi.setEnabled(abilita_pulsante)

    def elimina_dalla_tabella_ingredienti(self):

        riga_da_eliminare = self.view.data_grid.currentRow()
        if riga_da_eliminare >= 0:
            self.view.data_grid.removeRow(riga_da_eliminare)

        if (self.view.combo_tipologia.currentText().lower() == 'soft drink'
                or self.view.combo_tipologia.currentText().lower() == 'birra') and self.view.data_grid.rowCount() == 0:
            self.view.combo_ingrediente.setEnabled(True)
            self.view.campo_quantita.setEnabled(True)
            self.view.pulsante_aggiungi.setEnabled(True)

    def conferma_modifica(self):

        try:
            new_prezzo = round(float(self.view.campo_prezzo.text()), 2)

            if self.view.combo_tipologia.currentText().lower() == 'antipasto'\
                    or self.view.combo_tipologia.currentText().lower() == 'pizza':
                if self.view.data_grid.rowCount() == 0:
                    raise NoIngredienti("Controllare di aver inserito gli ingredienti.")
                else:
                    nuovi_ingredienti = []
                    for i in range(self.view.data_grid.rowCount()):
                        nome_ingrediente = self.view.data_grid.item(i, 0).text().lower()
                        quantita = float(self.view.data_grid.item(i, 1).text())
                        matprima = self.magazzino.estrai_per_nome(nome_ingrediente)
                        ingrediente = (matprima, quantita)
                        nuovi_ingredienti.append(ingrediente)

            else:
                if self.view.data_grid.rowCount() == 0:
                    raise NoIngredienti("Controllare di aver inserito l'ingrediente corrispondente.")
                else:
                    nuovi_ingredienti = []
                    nome_ingrediente = self.view.data_grid.item(0, 0).text().lower()
                    quantita = float(self.view.data_grid.item(0, 1).text())
                    matprima = self.magazzino.estrai_per_nome(nome_ingrediente)
                    ingrediente = (matprima, quantita)
                    nuovi_ingredienti.append(ingrediente)

        except ValueError:

            if self.view.campo_prezzo is None:
                errore_msg = "Controllare che tutti i campi siano riempiti."
            else:
                errore_msg = "Controllare che i dati siano inseriti correttamente."

            error_box = QMessageBox()
            error_box.setIcon(QMessageBox.Icon.Critical)
            error_box.setWindowTitle("Errore di Inserimento")
            error_box.setText(errore_msg)
            error_box.exec()

        except NoIngredienti as ni:
            error_box = QMessageBox()
            error_box.setIcon(QMessageBox.Icon.Critical)
            error_box.setWindowTitle("Errore di Inserimento")
            error_box.setText(ni.message)
            error_box.exec()

        else:
            self.model.modifica_prodotto(self.prodotto_da_modificare.nome, new_prezzo, nuovi_ingredienti)
            self.view.close()

    def riempi_combo(self):

        for x in self.magazzino.lista_materieprime:
            self.view.combo_ingrediente.addItem(x.nome)