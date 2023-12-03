from PyQt6.QtCore import Qt, QDate
from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem

from Code.GestionePrenotazioni.Model.gestore_prenotazioni import GestorePrenotazioni
from Code.GestionePrenotazioni.Model.prenotazione import Prenotazione
from Code.GestionePrenotazioni.View.vista_modifica_prenotazione import VistaModificaPrenotazione

class OutOfDate(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class ContModificaPrenotazione(object):

    def __init__(self, view: VistaModificaPrenotazione, model: GestorePrenotazioni, pre_da_modificare: Prenotazione):

        self.view = view
        self.model = model
        self.pre_da_modificare = pre_da_modificare
        self.new_data_selezionata = None
        self.view.pulsante_conferma.clicked.connect(self.conferma_modifica)
        self.view.calendario.selectionChanged.connect(self.riempi_tabella)
        self.riempi_labels(pre_da_modificare)

    def riempi_labels(self, prenotazione: Prenotazione):

        self.view.campo_nome.setText(str(prenotazione.nome_cliente))
        self.view.spinbox_persone.setValue(int(prenotazione.n_persone))

        self.view.combobox_orario.addItems(self.model.orari_disponibili)
        self.view.combobox_tavolo.addItems(self.model.tavoli_disponibili)

    def riempi_tabella(self):
        self.view.tabella.setRowCount(0)
        for orario in self.model.orari_disponibili:
            self.aggiungi_riga(orario)

    def aggiungi_riga(self, orario):
        self.data_selezionata = self.view.calendario.selectedDate()
        row_position = self.view.tabella.rowCount()
        self.view.tabella.insertRow(row_position)

        item = QTableWidgetItem(str(orario))
        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        self.view.tabella.setItem(row_position, 0, item)

        statistiche = self.model.ricerca_data_orario(self.data_selezionata, orario)
        self.view.tabella.setItem(row_position, 1, QTableWidgetItem(str(statistiche[0])))
        self.view.tabella.setItem(row_position, 2, QTableWidgetItem(str(78 - statistiche[1])))

        self.view.combobox_orario.setEnabled(True)
        self.view.combobox_tavolo.setEnabled(True)
        self.view.spinbox_persone.setEnabled(True)

    def conferma_modifica(self):
        global errore_msg
        try:
            new_tavolo = self.view.combobox_tavolo.currentText()
            new_persone = self.view.spinbox_persone.value()
            new_orario = self.view.combobox_orario.currentText()
            self.new_data_selezionata = self.view.calendario.selectedDate()
            if self.new_data_selezionata <= QDate.currentDate():
                raise OutOfDate("Inserisci una data valida")

        except ValueError:
            if not all([
                self.view.combobox_tavolo.currentText(),
                self.view.spinbox_persone.value(),
                self.view.calendario.selectedDate(),
                self.view.combobox_orario.currentText()
            ]):
                errore_msg = "Controllare che tutti i campi siano riempiti."

            error_box = QMessageBox()
            error_box.setIcon(QMessageBox.Icon.Critical)
            error_box.setWindowTitle("Errore di Inserimento")
            error_box.setText(errore_msg)
            error_box.exec()

        except OutOfDate as od:
            error_box = QMessageBox()
            error_box.setIcon(QMessageBox.Icon.Critical)
            error_box.setWindowTitle("Errore di Inserimento")
            error_box.setText(od.message)
            error_box.exec()

        else:
            self.model.modifica_prenotazioni(self.pre_da_modificare.codice, new_tavolo,
                                             new_persone, new_orario, self.new_data_selezionata)
            self.view.close()
