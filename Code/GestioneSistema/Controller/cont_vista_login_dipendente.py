from PyQt6.QtWidgets import QMessageBox, QStackedWidget

from Code.GestioneDipendenti.Controller.cont_home_cameriere import ContHomeCameriere
from Code.GestioneDipendenti.Controller.cont_home_cuoco import ContHomeCuoco
from Code.GestioneDipendenti.Model.gestore_dipendenti import GestoreDipendenti
from Code.GestioneMagazzino.Model.gestore_magazzino import GestoreMagazzino
from Code.GestioneMenu.Model.gestore_menu import GestoreMenu
from Code.GestioneOrdiniTavolo.Model.gestore_ordini_tavolo import GestoreOrdiniTavolo
from Code.GestionePrenotazioni.Model.gestore_prenotazioni import GestorePrenotazioni
from Code.GestioneRicevuta.Model.gestore_ricevuta import GestoreRicevuta
from Code.GestioneSistema.Controller.cont_vista_home_admin import ContVistaHomeAdmin
from Code.GestioneSistema.View.vista_login_dipendente import VistaLoginDipendente


class ContVistaLoginDipendente():

    def __init__(self, stacked:QStackedWidget, gestore_ric:GestoreRicevuta, gestore_dip:GestoreDipendenti,
                 gestore_mag:GestoreMagazzino, gestore_ord:GestoreOrdiniTavolo, gestore_menu: GestoreMenu, gestore_pre: GestorePrenotazioni):
        self.gestore_dip = gestore_dip
        self.view = VistaLoginDipendente()
        self.view.pulsante.clicked.connect(self.login)
        self.cont_admin = ContVistaHomeAdmin(stacked, gestore_ric, gestore_dip, gestore_mag, gestore_ord, gestore_menu,gestore_pre)
        self.stacked = stacked
        stacked.addWidget(self.view)

        self.cont_cameriere = ContHomeCameriere(gestore_dip, stacked)
        self.cont_cuoco = ContHomeCuoco(gestore_dip, stacked)
        # credenziali admin
        self.user_admin = "admin"
        self.pass_admin = "admin"

        self.cont_cuoco.view.pulsante_back.clicked.connect(lambda : self.stacked.setCurrentWidget(self.view))
        self.cont_cameriere.view.pulsante_back.clicked.connect(lambda : self.stacked.setCurrentWidget(self.view))



    def login(self):
        #prendo i dati inseriti dall'utente
        self.username = self.view.user_line.text()
        self.password = self.view.pass_line.text()
        #svuoto i campi di inserimento
        self.view.user_line.setText("")
        self.view.pass_line.setText("")

        if (self.username == self.user_admin and self.password == self.pass_admin):
            self.apri_finestra_admin()
        else:
            accesso, ruolo = self.gestore_dip.accesso_dipendente(self.username, self.password)
            if(accesso == True):
                    if ruolo == "Cameriere":
                        self.apri_finestra_cameriere()
                    if ruolo == "Cuoco":
                        self.apri_finestra_cuoco()
            else:
                self.mostra_errore()


    def apri_finestra_admin(self):
        self.stacked.setCurrentWidget(self.cont_admin.view)
        pass

    def apri_finestra_cameriere(self):
        self.stacked.setCurrentWidget(self.cont_cameriere.view)
        pass

    def apri_finestra_cuoco(self):
        self.stacked.setCurrentWidget(self.cont_cuoco.view)
        pass

    def mostra_errore(self):
        error_box = QMessageBox()
        error_box.setIcon(QMessageBox.Icon.Critical)
        error_box.setWindowTitle("Errore")
        error_box.setText("Credenziali errate!")
        error_box.exec()










