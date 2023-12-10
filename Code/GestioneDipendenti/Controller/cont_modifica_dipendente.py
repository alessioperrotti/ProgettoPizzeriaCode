from datetime import datetime

from PyQt6.QtWidgets import QMessageBox

from Code.GestioneDipendenti.Model.cameriere import Cameriere
from Code.GestioneDipendenti.Model.cuoco import Cuoco
from Code.GestioneDipendenti.Model.gestore_dipendenti import GestoreDipendenti
from Code.GestioneDipendenti.View.vista_modifica_dipendente import VistaModificaDipendente

class PassTooShort(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class ContModificaDipendente(object):
    def __init__(self, model, view: VistaModificaDipendente):
        self.view = view
        self.model = model
        self.cuoco = None
        self.cameriere = None
        self.view.pulsante.clicked.connect(self.confirm_close)

    def riempi_labels_cuoco(self, cuoco: Cuoco):
        self.view.label_nome.setText(cuoco.nome)
        self.view.label_cognome.setText(cuoco.cognome)
        self.view.label_ruolo.setText(cuoco.ruolo)
        self.view.edit_email.setPlaceholderText(cuoco.email)
        self.view.edit_stipendio.setPlaceholderText(str(cuoco.stipendio))
        self.view.edit_username.setPlaceholderText(cuoco.username)
        self.view.edit_password.setPlaceholderText(cuoco.password)

    def riempi_labels_cameriere(self, cameriere: Cameriere):
        self.view.label_nome.setText(cameriere.nome)
        self.view.label_cognome.setText(cameriere.cognome)
        self.view.label_ruolo.setText(cameriere.ruolo)
        self.view.edit_email.setPlaceholderText(cameriere.email)
        self.view.edit_stipendio.setPlaceholderText(str(cameriere.stipendio))
        self.view.edit_username.setPlaceholderText(cameriere.username)
        self.view.edit_password.setPlaceholderText(cameriere.password)

    def confirm_close(self):

        try:
            new_email = str(self.view.edit_email.text())
            new_stipendio = round(float(self.view.edit_stipendio.text()),2)
            new_data_nascita = self.view.calendario.selectedDate()
            new_username = str(self.view.edit_username.text())
            new_password = str(self.view.edit_password.text())
            if len(new_password) < 6:
                raise PassTooShort("La password deve essere lunga almeno 6 caratteri.")

        except ValueError:
            if not all([
                self.view.edit_email.text(),
                self.view.edit_stipendio.text(),
                self.view.calendario.selectedDate(),
                self.view.edit_username.text(),
                self.view.edit_password.text()
            ]):
                errore_msg = "Controllare che tutti i campi siano riempiti."
            else:
                errore_msg = "Controllare che i dati siano inseriti correttamente."

            error_box = QMessageBox()
            error_box.setIcon(QMessageBox.Icon.Critical)
            error_box.setWindowTitle("Errore di Inserimento")
            error_box.setText(errore_msg)
            error_box.exec()

        except PassTooShort as pts:
            error_box = QMessageBox()
            error_box.setIcon(QMessageBox.Icon.Critical)
            error_box.setWindowTitle("Errore di Inserimento")
            error_box.setText(pts.message)
            error_box.exec()

        else:
            if self.view.label_ruolo.text() == "Cuoco":
                self.model.modifica_cuoco(self.cuoco.cognome, new_email, new_stipendio, new_data_nascita,
                                          new_username, new_password)
            if self.view.label_ruolo.text() == "Cameriere":
                self.model.modifica_cameriere(self.cameriere.cognome, new_email, new_stipendio, new_data_nascita,
                                              new_username, new_password)
            self.view.close()
