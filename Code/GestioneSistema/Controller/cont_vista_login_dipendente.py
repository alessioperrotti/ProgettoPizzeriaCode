from Code.GestioneDipendenti.Model.gestore_dipendenti import GestoreDipendenti
from Code.GestioneSistema.View.vista_login_dipendente import VistaLoginDipendente


class ContVistaLoginDipendente():

    #credenziali admin
    self.user_admin = "admin"
    self.pass_admin = "admin"
    def __init__(self, gestore_dip:GestoreDipendenti)
        self.gestore_dip = gestore_dip
        self.view = VistaLoginDipendente()
        self.view.pulsante.clicked.connect(self.login)

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
            self.apri_finestra_admin
        else:
            for utilizzatore in lista_utilizzatori:
                if (self.username == utilizzatore.username and self.password == utilizzatore.password):
                    self.apri_finestra_dipendente(utilizzatore)
                    break
            else:
                self.mostra_errore()    





