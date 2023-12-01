from PyQt6.QtWidgets import QMessageBox, QStackedWidget

from Code.GestioneDipendenti.Controller.cont_home_cameriere import ContHomeCameriere
from Code.GestioneDipendenti.Controller.cont_home_cuoco import ContHomeCuoco
from Code.GestioneDipendenti.Model.gestore_dipendenti import GestoreDipendenti
from Code.GestioneMagazzino.Model.gestore_magazzino import GestoreMagazzino
from Code.GestioneMenu.Model.gestore_menu import GestoreMenu
from Code.GestioneOrdiniTavolo.Model.gestore_ordini_tavolo import GestoreOrdiniTavolo
from Code.GestioneRicevuta.Model.gestore_ricevuta import GestoreRicevuta
from Code.GestioneSistema.Controller.cont_vista_home_admin import ContVistaHomeAdmin
from Code.GestioneSistema.View.vista_login_dipendente import VistaLoginDipendente


class ContVistaLoginDipendente():

    def __init__(self, stacked:QStackedWidget, gestore_ric:GestoreRicevuta, gestore_dip:GestoreDipendenti,
                 gestore_mag:GestoreMagazzino, gestore_ord:GestoreOrdiniTavolo, gestore_menu: GestoreMenu):
        self.gestore_dip = gestore_dip
        self.view = VistaLoginDipendente()
        self.view.pulsante.clicked.connect(self.login)
        self.cont_admin = ContVistaHomeAdmin(stacked, gestore_ric, gestore_dip, gestore_mag, gestore_ord, gestore_menu)
        self.stacked = stacked
        stacked.addWidget(self.view)

        self.cont_cameriere = ContHomeCameriere(gestore_dip, stacked)
        self.cont_cuoco = ContHomeCuoco(gestore_dip, stacked)
        # credenziali admin
        self.user_admin = "admin"
        self.pass_admin = "admin"

    def login(self):
        #prendo i dati inseriti dall'utente
        self.username = self.view.user_line.text()
        self.password = self.view.pass_line.text()
        #svuoto i campi di inserimento
        self.view.user_line.setText("")
        self.view.pass_line.setText("")

        lista_utilizzatori=self.gestore_dip.lista_cuochi.copy()
        lista_utilizzatori.extend(self.gestore_dip.lista_camerieri)
        #print(lista_utilizzatori)
        accesso = False

        if (self.username == self.user_admin and self.password == self.pass_admin):
            self.apri_finestra_admin()
            accesso = True
        else:
            for utilizzatore in lista_utilizzatori:
                if (self.username == utilizzatore.username and self.password == utilizzatore.password):

                    accesso = True
                    if utilizzatore.ruolo == "Cameriere":
                        self.apri_finestra_cameriere()
                    if utilizzatore.ruolo == "Cuoco":
                        self.apri_finestra_cuoco()
                    break
        if accesso == False:
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










