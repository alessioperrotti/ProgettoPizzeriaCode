import sys
from PyQt6.QtWidgets import QApplication, QTableWidgetItem, QVBoxLayout, QMessageBox

from Code.GestioneDipendenti.Model.cameriere import Cameriere
from Code.GestioneDipendenti.Model.cuoco import Cuoco
from Code.GestioneDipendenti.Model.gestore_dipendenti import GestoreDipendenti
from Code.GestioneDipendenti.View.vista_gestione_dipendenti import VistaGestioneDipendenti
from Code.GestioneDipendenti.View.vista_inserisci_dipendente import VistaInserisciDipendente
from datetime import datetime


class ContInserisciDipendente(object):
    def __init__(self, model, view: VistaInserisciDipendente):
        self.view = view
        self.model = model
        self.view.pulsante.clicked.connect(self.confirm_close)

    def confirm_close(self):
        nome = self.view.edit_nome.text()
        cognome = self.view.edit_cognome.text()
        ruolo = self.view.edit_ruolo.currentText()
        email = self.view.edit_email.text()
        stipendio = self.view.edit_stipendio.text()
        data_nascita = self.view.calendario.selectedDate()
        username = self.view.edit_username.text()
        password = self.view.edit_password.text()

        current_date = datetime.now().date()

        if ruolo == "Cuoco":
            new_cuoco = Cuoco(nome,cognome,email,stipendio,username,password)
            new_cuoco.data_nascita = data_nascita
            new_cuoco.data_ingaggio = current_date
            self.model.aggiungi_cuoco(nome,cognome,email,stipendio,username,password)
        if ruolo == "Cameriere":
            new_cameriere = Cameriere(nome,cognome,email,stipendio,username,password)
            new_cameriere.data_nascita = data_nascita
            new_cameriere.data_ingaggio = current_date

        self.view.close()
