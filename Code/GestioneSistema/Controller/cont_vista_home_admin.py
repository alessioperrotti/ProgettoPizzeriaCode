from PyQt6.QtWidgets import QStackedWidget


from Code.GestioneDipendenti.Model.gestore_dipendenti import GestoreDipendenti
from Code.GestioneMagazzino.Model.gestore_magazzino import GestoreMagazzino
from Code.GestioneOrdiniTavolo.Model.gestore_ordini_tavolo import GestoreOrdiniTavolo
from Code.GestioneRicevuta.Controller.cont_vista_gestione_ricevute import ContVistaGestioneRicevute
from Code.GestioneRicevuta.Model.gestore_ricevuta import GestoreRicevuta

from Code.GestioneDipendenti.Controller.cont_gestione_dipendenti import ContGestioneDipendenti
from Code.GestioneDipendenti.Model.gestore_dipendenti import GestoreDipendenti
from Code.GestioneDipendenti.View.vista_gestione_dipendenti import VistaGestioneDipendenti
from Code.GestioneSistema.View.vista_home_admin import VistaHomeAdmin


class ContVistaHomeAdmin():

    def __init__(self,stacked:QStackedWidget, gestore_ric:GestoreRicevuta, gestore_dip:GestoreDipendenti, gestore_mag:GestoreMagazzino, gestore_ord:GestoreOrdiniTavolo):
        self.gestore_ric = gestore_ric
        self.gestore_ord = gestore_ord
        self.lista_tav = self.gestore_ord.lista_tavoli


        self.view = VistaHomeAdmin()
        self.stacked = stacked
        self.cont_ric = ContVistaGestioneRicevute(gestore_ric, gestore_ord, gestore_ord.lista_tavoli, self.stacked)

        stacked.addWidget(self.view)
        gestore_dip = GestoreDipendenti()
        self.cont_vista_dipendenti = ContGestioneDipendenti(gestore_dip,stacked)
        # collegamento pulsanti
        self.view.puls_dip.clicked.connect(self.go_to_dipendenti)
        self.view.puls_ric.clicked.connect(self.apri_gestione_ricevute)
        self.cont_ric.view.pulsante_back.clicked.connect(lambda : self.stacked.setCurrentWidget(self.view))


    def go_to_dipendenti(self):
        self.stacked.setCurrentWidget(self.cont_vista_dipendenti.view)


    def apri_gestione_ricevute(self):
        print("c")
        self.stacked.setCurrentWidget(self.cont_ric.view)

