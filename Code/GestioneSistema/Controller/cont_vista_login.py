from Code.GestioneDipendenti.Model.gestore_dipendenti import GestoreDipendenti
from Code.GestioneMagazzino.Model.gestore_magazzino import GestoreMagazzino
from Code.GestioneMenu.Model.gestore_menu import GestoreMenu
from Code.GestioneOrdiniTavolo.Model.gestore_ordini_tavolo import GestoreOrdiniTavolo
from Code.GestionePrenotazioni.Model.gestore_prenotazioni import GestorePrenotazioni
from Code.GestioneRicevuta.Model.gestore_ricevuta import GestoreRicevuta
from Code.GestioneSistema.Controller.cont_vista_inserisci_tavolo import ContVistaInserisciTavolo
from Code.GestioneSistema.Controller.cont_vista_login_dipendente import ContVistaLoginDipendente
from Code.GestioneSistema.View.vista_login import VistaLogin


class ContVistaLogin():
    def __init__(self, stacked , gestore_ric:GestoreRicevuta, gestore_dip:GestoreDipendenti, gestore_mag:GestoreMagazzino,
                 gestore_ord:GestoreOrdiniTavolo, gestore_menu: GestoreMenu,gestore_pre: GestorePrenotazioni):

        self.cont_vista_login_dipendente = ContVistaLoginDipendente(stacked, gestore_ric, gestore_dip, gestore_mag, gestore_ord, gestore_menu,gestore_pre)
        self.cont_vista_tavolo = ContVistaInserisciTavolo(stacked, gestore_ric, gestore_dip, gestore_mag, gestore_ord)
        self.view = VistaLogin()
        self.stacked = stacked
        self.view.pulsante_cliente.clicked.connect(self.apri_inserisci_tavolo)
        self.view.pulsante_admin.clicked.connect(self.apri_login_dipendente)
        self.cont_vista_login_dipendente.view.pulsante_back.clicked.connect(lambda: self.stacked.setCurrentWidget(self.view))
        self.cont_vista_tavolo.view.pulsante_back.clicked.connect(lambda: self.stacked.setCurrentWidget(self.view))

    def apri_inserisci_tavolo(self):
        self.stacked.setCurrentWidget(self.cont_vista_tavolo.view)

    def apri_login_dipendente(self):
        self.stacked.setCurrentWidget(self.cont_vista_login_dipendente.view)



