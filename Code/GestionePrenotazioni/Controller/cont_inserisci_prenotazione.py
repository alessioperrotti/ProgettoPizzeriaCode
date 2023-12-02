from PyQt6.QtWidgets import QMessageBox

from Code.GestionePrenotazioni.View.vista_inserisci_prenotazione import VistaInserisciPrenotazione
from Code.GestionePrenotazioni.Model.prenotazione import Prenotazione
from PyQt6.QtCore import QDate

class OutOfDate(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class ContInserisciPrenotazione(object):

    def __init__(self, model, view: VistaInserisciPrenotazione):
        self.view = view
        self.model = model
        self.view.pulsante_conferma.clicked.connect(self.conferma_inserimento)

    def conferma_inserimento(self):
        try:
            nome = self.view.campo_nome.text().title()
            n_persone = self.view.spinbox_persone.value()
            #controllo numero massimo
            tavolo = self.view.combobox_tavolo.currentText()
            #controllo tavolo gia utilizzato(non deve comparire)
            orario = self.view.combobox_orario.currentText()
            #controllo orario gia utilizzato(non deve comparire)
            codice = self.model.genera_codice()
            data = self.view.calendario.selectedDate()
            if data <= QDate.currentDate():
                raise OutOfDate("Inserisci una data valida")

        except ValueError:
            if not all([
                self.view.campo_nome.text(),#non funziona PD
                self.view.spinbox_persone.value(),
                self.view.combobox_orario.currentText(),
                self.view.combobox_tavolo.currentText(),
                self.view.calendario.selectedDate(),
            ]):
                errore_msg = "Controllare che tutti i campi siano riempiti."
            else:
                if not self.view.campo_nome.text().isalpha() or not self.view.campo_nome.text().isalpha():#non funziona PD
                    errore_msg = "Il nome e il cognome possono contenere solo lettere."
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

        else:
            nuova_prenotazione = Prenotazione(codice, nome, tavolo, n_persone, orario)
            nuova_prenotazione.data = data
            # nuova_prenotazione.orario_fine = bohh
            self.model.aggiungi_prenotazione(nuova_prenotazione)

            self.view.close()

    def riempi_labels(self):
        self.view.combobox_orario.addItems(self.model.orari_disponibili)
        self.view.combobox_tavolo.addItems(self.model.tavoli_disponibili)


