from PyQt6.QtCore import Qt, QDate
from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem

from Code.GestionePrenotazioni.Model.gestore_prenotazioni import GestorePrenotazioni
from Code.GestionePrenotazioni.Model.prenotazione import Prenotazione
from Code.GestionePrenotazioni.View.vista_modifica_prenotazione import VistaModificaPrenotazione


class AlertBox(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class ContModificaPrenotazione(object):

    def __init__(self, view: VistaModificaPrenotazione, model: GestorePrenotazioni, pre_da_modificare: Prenotazione):

        self.view = view
        self.model = model
        self.pre_da_modificare = pre_da_modificare
        self.new_data_selezionata = None
        self.new_orario_selezionato = None
        self.view.pulsante_conferma.clicked.connect(self.conferma_modifica)
        self.view.calendario.selectionChanged.connect(self.riempi_tabella)
        self.riempi_labels(pre_da_modificare)
        self.view.combobox_orario.currentIndexChanged.connect(self.riempi_labels_tavolo)
        self.view.calendario.selectionChanged.connect(self.riempi_labels_tavolo)

    def riempi_labels(self, prenotazione: Prenotazione):

        self.view.campo_nome.setText(str(prenotazione.nome_cliente))
        self.view.spinbox_persone.setValue(int(prenotazione.n_persone))

        self.view.combobox_orario.addItems(self.model.orari_disponibili)

    def riempi_labels_tavolo(self):
        self.new_orario_selezionato = self.view.combobox_orario.currentText()
        tavoli_gia_selezionati = set()

        for prenotazione in self.model.lista_prenotazioni:
            if prenotazione.data == self.new_data_selezionata and prenotazione.orario == self.new_orario_selezionato:
                tavoli_gia_selezionati.add(prenotazione.tavolo_assegnato.numero)

        self.view.combobox_tavolo.clear()

        for tavolo in self.model.lista_tavoli:
            if tavolo.numero not in tavoli_gia_selezionati:
                self.view.combobox_tavolo.addItem(str(tavolo.numero))

    def riempi_tabella(self):
        self.view.tabella.setRowCount(0)
        for orario in self.model.orari_disponibili:
            self.aggiungi_riga(orario)

    def aggiungi_riga(self, orario):
        self.new_data_selezionata = self.view.calendario.selectedDate()
        row_position = self.view.tabella.rowCount()
        self.view.tabella.insertRow(row_position)

        item = QTableWidgetItem(str(orario))
        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        self.view.tabella.setItem(row_position, 0, item)

        statistiche = self.model.ricerca_data_orario(self.new_data_selezionata, orario)
        self.view.tabella.setItem(row_position, 1, QTableWidgetItem(str(statistiche[0])))
        self.view.tabella.setItem(row_position, 2, QTableWidgetItem(str(80 - statistiche[1])))

        self.view.combobox_orario.setEnabled(True)
        self.view.combobox_tavolo.setEnabled(True)
        self.view.spinbox_persone.setEnabled(True)

    def conferma_modifica(self):
        try:
            new_persone = self.view.spinbox_persone.value()
            if new_persone <= 0:
                raise AlertBox("Inserisci un numero di persone valido")
            n_tavolo = self.view.combobox_tavolo.currentText()
            new_tavolo = self.model.ricerca_tavolo(n_tavolo)
            if new_persone > new_tavolo.posti_disponibili:
                raise AlertBox("Scegli un tavolo più grande")

            new_orario = self.view.combobox_orario.currentText()
            self.new_data_selezionata = self.view.calendario.selectedDate()
            if self.new_data_selezionata < QDate.currentDate():
                raise AlertBox("Inserisci una data valida")

            for row in range(self.view.tabella.rowCount()):
                orario_tab = self.view.tabella.item(row, 0).text()
                if self.new_orario_selezionato == orario_tab:
                    posti_disponibili = self.view.tabella.item(row, 2).text()
                    if int(posti_disponibili) - int(new_persone) < 0:
                        raise AlertBox("Non ci sono posti disponibili")

        except AlertBox as ab:
            error_box = QMessageBox()
            error_box.setIcon(QMessageBox.Icon.Critical)
            error_box.setWindowTitle("Errore di Inserimento")
            error_box.setText(ab.message)
            error_box.exec()

        else:
            self.model.modifica_prenotazioni(self.pre_da_modificare.codice, new_tavolo,
                                             new_persone, new_orario, self.new_data_selezionata)
            self.view.close()
