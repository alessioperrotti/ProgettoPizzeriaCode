from Code.GestioneDipendenti.Model.cuoco import Cuoco
from Code.GestioneDipendenti.Model.gestore_dipendenti import GestoreDipendenti
from Code.GestioneDipendenti.View.vista_visualizza_dipendente import VistaVisualizzaDipendente


class ContMostraDipendente(object):
    def __init__(self, view: VistaVisualizzaDipendente, model: GestoreDipendenti):
        self.view = view
        self.model = model

    def riempi_labels(self, cuoco: Cuoco):
        self.view.campo_nome.setText(str(cuoco.nome))
        self.view.campo_cognome.setText(str(cuoco.cognome))
        self.view.campo_ruolo.setText(str(cuoco.ruolo))
        self.view.campo_email.setText(str(cuoco.email))
        self.view.campo_stipendio.setText(str(cuoco.stipendio))
        self.view.campo_data_nascita.setText(str(cuoco.data_nascita.toString("dd-MM-yyyy")))
        self.view.campo_data_ingaggio.setText(str(cuoco.data_ingaggio.toString("dd-MM-yyyy")))
        self.view.campo_username.setText(str(cuoco.username))
        self.view.campo_password.setText(str(cuoco.password))
