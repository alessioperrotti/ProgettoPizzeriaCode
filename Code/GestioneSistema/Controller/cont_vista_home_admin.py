from PyQt6.QtWidgets import QStackedWidget

from Code.GestioneDipendenti.Controller.cont_gestione_dipendenti import ContGestioneDipendenti
from Code.GestioneDipendenti.Model.gestore_dipendenti import GestoreDipendenti
from Code.GestioneDipendenti.View.vista_gestione_dipendenti import VistaGestioneDipendenti
from Code.GestioneSistema.View.vista_home_admin import VistaHomeAdmin


class ContVistaHomeAdmin():
    def __init__(self,stacked: QStackedWidget):
        self.view = VistaHomeAdmin()
        self.stacked = stacked
        stacked.addWidget(self.view)
        gestore_dip = GestoreDipendenti()
        self.cont_vista_dipendenti = ContGestioneDipendenti(gestore_dip,stacked)
        self.view.pulsante3.clicked.connect(self.go_to_dipendenti)

    def go_to_dipendenti(self):
        self.stacked.setCurrentWidget(self.cont_vista_dipendenti.view)

