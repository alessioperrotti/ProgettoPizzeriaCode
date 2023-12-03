from PyQt6.QtWidgets import QMessageBox, QTableWidgetItem

from Code.GestionePrenotazioni.View.vista_inserisci_prenotazione import VistaInserisciPrenotazione
from Code.GestionePrenotazioni.Model.prenotazione import Prenotazione
from PyQt6.QtCore import QDate, Qt


class OutOfDate(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class OutOfSpace(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class ChangeTable(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class ContInserisciPrenotazione(object):

    def __init__(self, model, view: VistaInserisciPrenotazione):
        self.view = view
        self.model = model
        self.data_selezionata = None
        self.view.pulsante_conferma.clicked.connect(self.conferma_inserimento)
        self.view.calendario.selectionChanged.connect(self.riempi_tabella)

    def conferma_inserimento(self):
        try:
            nome = self.view.campo_nome.text().title()

            n_persone = self.view.spinbox_persone.value()
            tavolo = self.view.combobox_tavolo.currentText()
            # for t in self.model.lista_tavoli:
            #     if t.numero == tavolo:
            #         if n_persone > t.posti_disponibili:
            #             raise ChangeTable("Scegli un tavolo più grande")

            orario = self.view.combobox_orario.currentText()
            codice = self.model.genera_codice()

            self.data_selezionata = self.view.calendario.selectedDate()
            if self.data_selezionata <= QDate.currentDate():
                raise OutOfDate("Inserisci una data valida")

            for row in range(self.view.tabella.rowCount()):
                orario_tab = self.view.tabella.item(row, 0).text()
                if orario == orario_tab:
                    posti_disponibili = self.view.tabella.item(row, 2).text()
                    if int(posti_disponibili) - int(n_persone) < 0:
                        raise OutOfSpace("Non ci sono posti disponibili")

        except ValueError:
            if not all([
                self.view.campo_nome.text(),  # non funziona PD
                self.view.spinbox_persone.value(),
                self.view.combobox_orario.currentText(),
                self.view.combobox_tavolo.currentText(),
                self.view.calendario.selectedDate(),
            ]):
                errore_msg = "Controllare che tutti i campi siano riempiti."
            else:
                if not self.view.campo_nome.text():  # non funziona PD!
                    errore_msg = "Il campo nome è obbligatorio."
                elif not self.view.campo_nome.text().isalpha():
                    errore_msg = "Il nome può contenere solo lettere."
                else:
                    errore_msg = "Controllare che i dati siano inseriti correttamente."

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

        except OutOfSpace as os:
            error_box = QMessageBox()
            error_box.setIcon(QMessageBox.Icon.Critical)
            error_box.setWindowTitle("Errore di Inserimento")
            error_box.setText(os.message)
            error_box.exec()

        except ChangeTable as ct:
            error_box = QMessageBox()
            error_box.setIcon(QMessageBox.Icon.Critical)
            error_box.setWindowTitle("Errore di Inserimento")
            error_box.setText(ct.message)
            error_box.exec()

        else:
            nuova_prenotazione = Prenotazione(codice, nome, tavolo, n_persone, orario)
            nuova_prenotazione.data = self.data_selezionata
            # nuova_prenotazione.orario_fine = bohh
            self.model.aggiungi_prenotazione(nuova_prenotazione)

            self.view.close()

#devono riempirsi quando clicco sulla data
    def riempi_labels(self):
        self.view.combobox_orario.addItems(self.model.orari_disponibili)
        self.view.combobox_tavolo.addItems(self.model.tavoli_disponibili)
        # for tavolo in self.model.lista_tavoli:
        #     self.view.combobox_tavolo.addItem(str(tavolo.numero))

    def riempi_labels2(self,data,orario):
        self.view.combobox_orario.addItems(self.model.orari_disponibili)

        tavoli_gia_selezionati = set()
        for prenotazione in self.model.lista_prenotazioni:
            if prenotazione.data == data and prenotazione.orario == orario:
                tavoli_gia_selezionati.add(prenotazione.tavolo_assegnato)
                for tavolo in self.model.lista_tavoli:
                    if tavolo.numero not in tavoli_gia_selezionati and tavolo.stato != "prenotato":
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
        self.view.tabella.setItem(row_position, 2, QTableWidgetItem(str(78 - statistiche[1])))

        self.view.combobox_orario.setEnabled(True)
        self.view.combobox_tavolo.setEnabled(True)
        self.view.spinbox_persone.setEnabled(True)

#se lo stato del tavolo è prenotato
#rimuovo