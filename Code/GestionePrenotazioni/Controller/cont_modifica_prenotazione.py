from PyQt6.QtWidgets import QMessageBox

from Code.GestionePrenotazioni.Model.gestore_prenotazioni import GestorePrenotazioni
from Code.GestionePrenotazioni.Model.prenotazione import Prenotazione
from Code.GestionePrenotazioni.View.vista_modifica_prenotazione import VistaModificaPrenotazione


class ContModificaPrenotazione(object):

    def __init__(self, view: VistaModificaPrenotazione, model: GestorePrenotazioni, pre_da_modificare: Prenotazione):

        self.view = view
        self.model = model
        self.pre_da_modificare = pre_da_modificare
        self.view.pulsante_conferma.clicked.connect(self.conferma_modifica)
        self.riempi_labels(pre_da_modificare)

    def riempi_labels(self, prenotazione: Prenotazione):

        self.view.campo_nome.setText(str(prenotazione.nome_cliente))
        self.view.spinbox_persone.setValue(int(prenotazione.n_persone))

        self.view.combobox_orario.addItems(self.model.orari_disponibili)
        self.view.combobox_tavolo.addItems(self.model.tavoli_disponibili)

    def conferma_modifica(self):
        global errore_msg
        try:
            new_tavolo = self.view.combobox_tavolo.currentText()
            new_persone = self.view.spinbox_persone.value()
            new_orario = self.view.combobox_orario.currentText()
            new_data = self.view.calendario.selectedDate()

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

        else:
            self.model.modifica_prenotazioni(self.pre_da_modificare.codice, new_tavolo,
                                             new_persone, new_orario, new_data)
            self.view.close()
