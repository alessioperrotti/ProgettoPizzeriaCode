from PyQt6.QtWidgets import QMessageBox, QStackedWidget

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

        lista_utilizzatori=self.gestore_dip.lista_cuochi
        lista_utilizzatori.extend(self.gestore_dip.lista_camerieri)

        if (self.username == self.user_admin and self.password == self.pass_admin):
            self.apri_finestra_admin()
        else:
            for cameriere in self.gestore_dip.lista_camerieri:
                if (self.username == cameriere.username and self.password == cameriere.password):
                    self.apri_finestra_cameriere()
                    break
            for cuoco in self.gestore_dip.lista_cuochi:
                if (self.username == cuoco.username and self.password == cuoco.password):
                    self.apri_finestra_cuoco()
                    break
            self.mostra_errore()


    def apri_finestra_admin(self):
        self.stacked.setCurrentWidget(self.cont_admin.view)
        pass

    def apri_finestra_cameriere(self):
        pass

    def apri_finestra_cuoco(self):
        pass

    def mostra_errore(self):
        error_box = QMessageBox()
        error_box.setIcon(QMessageBox.Icon.Critical)
        error_box.setWindowTitle("Errore")
        error_box.setText("Credenziali errate!")
        error_box.exec()










