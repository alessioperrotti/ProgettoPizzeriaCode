from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem

from Code.GestionePrenotazioni.View.vista_inserisci_prenotazione import VistaInserisciPrenotazione
from Code.GestionePrenotazioni.Model.prenotazione import Prenotazione
from PyQt6.QtCore import QDate, Qt


class AlertBox(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class ContInserisciPrenotazione(object):

    def __init__(self, model, view: VistaInserisciPrenotazione):
        self.view = view
        self.model = model
        self.data_selezionata = None
        self.orario_selezionato = None
        self.view.pulsante_conferma.clicked.connect(self.conferma_inserimento)
        self.view.calendario.selectionChanged.connect(self.riempi_tabella)
        self.view.combobox_orario.currentIndexChanged.connect(self.riempi_labels_tavolo)
        self.view.calendario.selectionChanged.connect(self.riempi_labels_tavolo)

    def conferma_inserimento(self):
        try:
            nome = self.view.campo_nome.text().title()
            if nome == "":
                raise AlertBox("Il campo nome è obbligatorio")
            if not nome.isalpha():
                raise AlertBox("Il nome può contenere solo caratteri")
            n_persone = self.view.spinbox_persone.value()
            if n_persone <= 0:
                raise AlertBox("Inserisci un numero di persone valido")
            n_tavolo = self.view.combobox_tavolo.currentText()
            tavolo = self.model.ricerca_tavolo(n_tavolo)
            if n_persone > tavolo.posti_disponibili:
                raise AlertBox("Scegli un tavolo più grande")

            self.orario_selezionato = self.view.combobox_orario.currentText()
            codice = self.model.genera_codice()

            self.data_selezionata = self.view.calendario.selectedDate()
            if self.data_selezionata < QDate.currentDate():
                raise AlertBox("Inserisci una data valida")

            for row in range(self.view.tabella.rowCount()):
                orario_tab = self.view.tabella.item(row, 0).text()
                if self.orario_selezionato == orario_tab:
                    posti_disponibili = self.view.tabella.item(row, 2).text()
                    if int(posti_disponibili) - int(n_persone) < 0:
                        raise AlertBox("Non ci sono posti disponibili")

        except AlertBox as ab:
            error_box = QMessageBox()
            error_box.setIcon(QMessageBox.Icon.Critical)
            error_box.setWindowTitle("Errore di Inserimento")
            error_box.setText(ab.message)
            error_box.exec()

        else:
            nuova_prenotazione = Prenotazione(codice, nome, tavolo, n_persone, self.orario_selezionato)
            nuova_prenotazione.data = self.data_selezionata
            self.model.aggiungi_prenotazione(nuova_prenotazione)

            self.view.close()

    def riempi_labels_orario(self):
        self.view.combobox_orario.addItems(self.model.orari_disponibili)

    def riempi_labels_tavolo(self):
        self.orario_selezionato = self.view.combobox_orario.currentText()
        tavoli_gia_selezionati = set()

        for prenotazione in self.model.lista_prenotazioni:
            if prenotazione.data == self.data_selezionata and prenotazione.orario == self.orario_selezionato:
                tavoli_gia_selezionati.add(prenotazione.tavolo_assegnato.numero)

        self.view.combobox_tavolo.clear()

        for tavolo in self.model.lista_tavoli:
            if tavolo.numero not in tavoli_gia_selezionati:
                self.view.combobox_tavolo.addItem(str(tavolo.numero))

    def rimuovi_tavolo_selezionato(self, numero_tavolo):
        tav_da_rimuovere = self.view.combobox_tavolo.findText(str(numero_tavolo))
        if tav_da_rimuovere != -1:
            self.view.combobox_tavolo.removeItem(tav_da_rimuovere)

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
        self.view.tabella.setItem(row_position, 2, QTableWidgetItem(str(80 - statistiche[1])))

        self.view.combobox_orario.setEnabled(True)
        self.view.combobox_tavolo.setEnabled(True)
        self.view.spinbox_persone.setEnabled(True)
