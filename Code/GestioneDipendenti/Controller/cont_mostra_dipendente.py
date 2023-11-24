from Code.GestioneDipendenti.Model.cameriere import Cameriere
from Code.GestioneDipendenti.Model.cuoco import Cuoco
from Code.GestioneDipendenti.Model.gestore_dipendenti import GestoreDipendenti
from Code.GestioneDipendenti.View.vista_visualizza_dipendente import VistaVisualizzaDipendente


class ContMostraDipendente(object):
    def __init__(self, view: VistaVisualizzaDipendente, model: GestoreDipendenti):
        self.view = view
        self.model = model

    def riempi_labels_cuoco(self, cuoco: Cuoco):
        #cuoco.get_info_cuoco()
        self.view.campo_nome.setText(cuoco.nome)
        self.view.campo_cognome.setText(cuoco.cognome)
        self.view.campo_ruolo.setText(cuoco.ruolo)
        self.view.campo_email.setText(cuoco.email)
        self.view.campo_stipendio.setText(str(cuoco.stipendio))
        self.view.campo_data_nascita.setText(cuoco.data_nascita.toString("dd-MM-yyyy"))
        self.view.campo_data_ingaggio.setText(str(cuoco.data_ingaggio))
        self.view.campo_username.setText(cuoco.username)
        self.view.campo_password.setText(cuoco.password)

    def riempi_labels_cameriere(self, cameriere: Cameriere):
        #cameriere.get_info_cameriere()
        self.view.campo_nome.setText(cameriere.nome)
        self.view.campo_cognome.setText(cameriere.cognome)
        self.view.campo_ruolo.setText(cameriere.ruolo)
        self.view.campo_email.setText(cameriere.email)
        self.view.campo_stipendio.setText(str(cameriere.stipendio))
        self.view.campo_data_nascita.setText(cameriere.data_nascita.toString("dd-MM-yyyy"))
        self.view.campo_data_ingaggio.setText(str(cameriere.data_ingaggio))
        self.view.campo_username.setText(cameriere.username)
        self.view.campo_password.setText(cameriere.password)
