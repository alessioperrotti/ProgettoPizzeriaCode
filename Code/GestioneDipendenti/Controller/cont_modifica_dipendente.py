from datetime import datetime

from Code.GestioneDipendenti.Model.cameriere import Cameriere
from Code.GestioneDipendenti.Model.cuoco import Cuoco
from Code.GestioneDipendenti.Model.gestore_dipendenti import GestoreDipendenti
from Code.GestioneDipendenti.View.vista_modifica_dipendente import VistaModificaDipendente


class ContModificaDipendente(object):
    def __init__(self, model: GestoreDipendenti, view: VistaModificaDipendente):
        self.view = view
        self.model = model
        self.cuoco = None
        self.cameriere = None
        self.view.pulsante.clicked.connect(self.confirm_close)

    def riempi_labels_cuoco(self, cuoco: Cuoco):
        self.view.label_nome.setText(cuoco.nome)
        self.view.label_cognome.setText(cuoco.cognome)
        self.view.label_ruolo.setText(cuoco.ruolo)

    def riempi_labels_cameriere(self, cameriere: Cameriere):
        self.view.label_nome.setText(cameriere.nome)
        self.view.label_cognome.setText(cameriere.cognome)
        self.view.label_ruolo.setText(cameriere.ruolo)

    def confirm_close(self):  # CONTROOOLLLO

        new_email = self.view.edit_email.text()
        new_stipendio = self.view.edit_stipendio.text()
        new_data_nascita = self.view.calendario.selectedDate()
        new_username = self.view.edit_username.text()
        new_password = self.view.edit_password.text()

        if self.view.label_ruolo == "Cuoco":
            self.model.modifica_cuoco(self.cuoco.nome, new_email, new_stipendio, new_data_nascita,
                                      new_username, new_password)
        if self.view.label_ruolo == "Cameriere":
            self.model.modifica_cameriere(self.cameriere.nome, new_email, new_stipendio, new_data_nascita,
                                          new_username, new_password)
        self.view.close()
