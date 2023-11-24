import sys

from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QApplication, QTableWidgetItem, QVBoxLayout, QMessageBox

from Code.GestioneDipendenti.Model.cameriere import Cameriere
from Code.GestioneDipendenti.Model.cuoco import Cuoco
from Code.GestioneDipendenti.Model.gestore_dipendenti import GestoreDipendenti
from Code.GestioneDipendenti.View.vista_gestione_dipendenti import VistaGestioneDipendenti
from Code.GestioneDipendenti.View.vista_inserisci_dipendente import VistaInserisciDipendente
from datetime import datetime


class OutOfDate(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class UsedUsername(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

# class NameAlert(Exception):
#     def __init__(self, message):
#         self.message = message
#         super().__init__(message)


class ContInserisciDipendente(object):
    def __init__(self, model, view: VistaInserisciDipendente):
        self.view = view
        self.model = model
        self.view.pulsante.clicked.connect(self.confirm_close)

    def confirm_close(self):
        current_date = datetime.now().date()
        try:
            nome = self.view.edit_nome.text().title()
            cognome = self.view.edit_cognome.text().title()
            # if not nome.isalpha() or not cognome.isalpha():
            #     raise NameAlert("Il nome e il cognome possono contenere solo lettere.")
            ruolo = self.view.edit_ruolo.currentText()
            email = self.view.edit_email.text()
            stipendio = round(float(self.view.edit_stipendio.text()), 2)
            data_nascita = self.view.calendario.selectedDate()
            if data_nascita >= QDate.currentDate():
                raise OutOfDate("Il Bro deve ancora nascere")
            username = self.view.edit_username.text()
            if self.model.estrai_cuoco_username(username) is not None:
                raise UsedUsername("L'username inserito risulta già utilizzato.")
            if self.model.estrai_cameriere_username(username) is not None:
                raise UsedUsername("L'username inserito risulta già utilizzato.")
            password = self.view.edit_password.text()

        except ValueError:
            if not all([
                self.view.edit_nome.text(),
                self.view.edit_cognome.text(),
                self.view.edit_email.text(),
                self.view.edit_stipendio.text(),
                self.view.calendario.selectedDate(),
                self.view.edit_username.text(),
                self.view.edit_password.text(),
            ]):
                errore_msg = "Controllare che tutti i campi siano riempiti."
            else:
                if not self.view.edit_nome.text().isalpha() or not self.view.edit_cognome.text().isalpha():
                    errore_msg = "Il nome e il cognome possono contenere solo lettere."
                else:
                    errore_msg = "Controllare che i dati siano inseriti correttamente."

            error_box = QMessageBox()
            error_box.setIcon(QMessageBox.Icon.Critical)
            error_box.setWindowTitle("Errore di Inserimento")
            error_box.setText(errore_msg)
            error_box.exec()

        except UsedUsername as uc:
            error_box = QMessageBox()
            error_box.setIcon(QMessageBox.Icon.Critical)
            error_box.setWindowTitle("Errore di Inserimento")
            error_box.setText(uc.message)
            error_box.exec()

        except OutOfDate as od:
            error_box = QMessageBox()
            error_box.setIcon(QMessageBox.Icon.Critical)
            error_box.setWindowTitle("Errore di Inserimento")
            error_box.setText(od.message)
            error_box.exec()

        # except NameAlert as na:
        #     error_box = QMessageBox()
        #     error_box.setIcon(QMessageBox.Icon.Critical)
        #     error_box.setWindowTitle("Errore di Inserimento")
        #     error_box.setText(na.message)
        #     error_box.exec()

        else:
            if ruolo == "Cuoco":
                new_cuoco = Cuoco(nome, cognome, email, username, password, stipendio)
                new_cuoco.data_nascita = data_nascita
                new_cuoco.data_ingaggio = current_date
                self.model.aggiungi_cuoco(new_cuoco)
            else:
                new_cameriere = Cameriere(nome, cognome, email, username, password, stipendio)
                new_cameriere.data_nascita = data_nascita
                new_cameriere.data_ingaggio = current_date
                self.model.aggiungi_cameriere(new_cameriere)

            self.view.close()
