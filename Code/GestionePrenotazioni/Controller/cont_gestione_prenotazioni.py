from PyQt6.QtWidgets import QTableWidgetItem, QStackedWidget

from Code.GestionePrenotazioni.Controller.cont_inserisci_prenotazione import ContInserisciPrenotazione
from Code.GestionePrenotazioni.Model.gestore_prenotazioni import GestorePrenotazioni
from Code.GestionePrenotazioni.View.vista_gestione_prenotazioni import VistaGestionePrenotazioni
from Code.GestionePrenotazioni.View.vista_inserisci_prenotazione import VistaInserisciPrenotazione


class ContGestionePrenotazioni(object):

    def __init__(self, model: GestorePrenotazioni,stacked : QStackedWidget):
        self.view = VistaGestionePrenotazioni()
        self.model = model
        self.update_tabella()
        self.view.pulsante_inserisci.clicked.connect(self.click_inserisci)

    def riga_selezionata(self):
        pass

    def click_inserisci(self):
        dialog_inserisci = VistaInserisciPrenotazione()
        cont_inserisci = ContInserisciPrenotazione(self.model,dialog_inserisci)
        cont_inserisci.view.exec()

    def click_mostra(self):
        pass

    def click_elimina(self):
        pass

    def update_tabella(self):
        pass

