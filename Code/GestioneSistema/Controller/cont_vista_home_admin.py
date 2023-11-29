from PyQt6.QtWidgets import QStackedWidget

from Code.GestioneDipendenti.Controller.cont_gestione_turni import ContGestioneTurni
from Code.GestioneDipendenti.Model.gestore_dipendenti import GestoreDipendenti
from Code.GestioneMagazzino.Controller.gestione_magazzino_cont import ContGestioneMagazzino
from Code.GestioneMagazzino.Model.gestore_magazzino import GestoreMagazzino
from Code.GestioneMagazzino.View.gestione_magazzino_view import VistaGestioneMagazzino
from Code.GestioneOrdiniTavolo.Model.gestore_ordini_tavolo import GestoreOrdiniTavolo
from Code.GestioneRicevuta.Controller.cont_vista_gestione_ricevute import ContVistaGestioneRicevute
from Code.GestioneRicevuta.Model.gestore_ricevuta import GestoreRicevuta
from Code.GestioneMenu.View.gestione_menu_view import VistaGestioneMenu
from Code.GestioneMenu.Controller.gestione_menu_cont import ContGestioneMenu
from Code.GestioneMenu.Model.gestore_menu import GestoreMenu
from Code.GestioneDipendenti.Controller.cont_gestione_dipendenti import ContGestioneDipendenti
from Code.GestioneDipendenti.Model.gestore_dipendenti import GestoreDipendenti
from Code.GestioneDipendenti.View.vista_gestione_dipendenti import VistaGestioneDipendenti
from Code.GestioneSistema.View.vista_home_admin import VistaHomeAdmin


class ContVistaHomeAdmin():

    def __init__(self,stacked:QStackedWidget, gestore_ric:GestoreRicevuta, gestore_dip:GestoreDipendenti,
                 gestore_mag:GestoreMagazzino, gestore_ord:GestoreOrdiniTavolo, gestore_menu:GestoreMenu):
        self.gestore_ric = gestore_ric
        self.gestore_ord = gestore_ord
        self.gestore_menu = gestore_menu
        self.lista_tav = self.gestore_ord.lista_tavoli


        self.view = VistaHomeAdmin()
        self.stacked = stacked
        self.cont_ric = ContVistaGestioneRicevute(gestore_ric, gestore_ord, gestore_ord.lista_tavoli, self.stacked)

        stacked.addWidget(self.view)
        gestore_dip = GestoreDipendenti()
        self.cont_vista_dipendenti = ContGestioneDipendenti(gestore_dip,stacked)
        self.cont_vista_turni = ContGestioneTurni(gestore_dip,stacked)
        self.cont_vista_magazzino= ContGestioneMagazzino(gestore_mag,VistaGestioneMagazzino(), stacked)
        self.cont_vista_menu = ContGestioneMenu(VistaGestioneMenu(),gestore_menu, stacked)


        # collegamento pulsanti
        self.view.puls_dip.clicked.connect(self.apri_gestione_dipendenti)
        self.view.puls_ric.clicked.connect(self.apri_gestione_ricevute)
        self.view.puls_mag.clicked.connect(self.apri_gestione_magazzino)
        self.view.puls_men.clicked.connect(self.apri_gestione_menu)
        self.view.puls_tur.clicked.connect(self.apri_gestione_turni)
        self.cont_ric.view.pulsante_back.clicked.connect(lambda : self.stacked.setCurrentWidget(self.view))
        self.cont_vista_dipendenti.view.pulsante_back.clicked.connect(lambda: self.stacked.setCurrentWidget(self.view))
        self.cont_vista_turni.view.pulsante_back.clicked.connect(lambda: self.stacked.setCurrentWidget(self.view))
        self.cont_vista_menu.view.pulsante_back.clicked.connect(lambda: self.stacked.setCurrentWidget(self.view))
        self.cont_vista_magazzino.view.pulsante_back.clicked.connect(lambda: self.stacked.setCurrentWidget(self.view))

    def apri_gestione_dipendenti(self):
        self.stacked.setCurrentWidget(self.cont_vista_dipendenti.view)

    def apri_gestione_turni(self):
        self.stacked.setCurrentWidget(self.cont_vista_turni.view)


    def apri_gestione_ricevute(self):
        self.stacked.setCurrentWidget(self.cont_ric.view)

    def apri_gestione_magazzino(self):
        self.stacked.setCurrentWidget(self.cont_vista_magazzino.view)

    def apri_gestione_menu(self):
        self.stacked.setCurrentWidget(self.cont_vista_menu.view)

