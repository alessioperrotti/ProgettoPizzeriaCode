from Code.GestioneDipendenti.Model.gestore_dipendenti import GestoreDipendenti
from Code.GestioneSistema.Controller.cont_vista_login_dipendente import ContVistaLoginDipendente
from Code.GestioneSistema.View.vista_login import VistaLogin


class ContVistaLogin():
    def __init__(self, stacked):
        gestore_dip = GestoreDipendenti()
        self.cont_vista_login_dipendente = ContVistaLoginDipendente(gestore_dip, stacked)
        self.view = VistaLogin()
        self.stacked = stacked
        self.view.pulsante_admin.clicked.connect(self.apri_login_dipendente)



    def apri_login_dipendente(self):
        self.stacked.setCurrentWidget(self.cont_vista_login_dipendente.view)
