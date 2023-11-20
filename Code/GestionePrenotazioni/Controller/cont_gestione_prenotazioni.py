from PyQt6.QtWidgets import QTableWidgetItem

from Code.GestionePrenotazioni.Controller.cont_inserisci_prenotazione import ContInserisciPrenotazione
from Code.GestionePrenotazioni.Model.gestore_prenotazioni import GestorePrenotazioni
from Code.GestionePrenotazioni.View.vista_gestione_prenotazioni import VistaGestionePrenotazioni
from Code.GestionePrenotazioni.View.vista_inserisci_prenotazione import VistaInserisciPrenotazione


class ContGestionePrenotazioni(object):

    def __init__(self, model: GestorePrenotazioni, view: VistaGestionePrenotazioni):

        self.view = view
        self.model = model
        self.view.pulsante_aggiungi.clicked.connect(self.open_vista_inserimento)

    def open_vista_inserimento(self):
        self.vista = VistaInserisciPrenotazione()
        self.vista.show()

