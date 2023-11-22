from Code.GestioneSistema.Controller.cont_vista_login_dipendente import ContVistaLoginDipendente
from Code.GestioneSistema.View.vista_login import VistaLogin


class ContVistaLogin():
    def __init__(self, stacked):
        self.cont_vista_login_dipendente = ContVistaLoginDipendente()
        self.view = VistaLogin()
        self.stacked = stacked
        self.view.pulsante_admin.clicked.connect(self.apri_login_dipendente)
        self.stacked.addWidget(self.cont_vista_login_dipendente.view)


    def apri_login_dipendente(self):
        self.stacked.setCurrentWidget(self.cont_vista_login_dipendente.view)
