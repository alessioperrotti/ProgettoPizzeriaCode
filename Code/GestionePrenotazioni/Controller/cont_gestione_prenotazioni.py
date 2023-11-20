from PyQt6.QtWidgets import QTableWidgetItem

from Code.GestionePrenotazioni.Controller.cont_inserisci_prenotazione import ContInserisciPrenotazione
from Code.GestionePrenotazioni.Model.gestore_prenotazioni import GestorePrenotazioni
from Code.GestionePrenotazioni.View.vista_gestione_prenotazioni import VistaGestionePrenotazioni
from Code.GestionePrenotazioni.View.vista_inserisci_prenotazione import VistaInserisciPrenotazione


class ContGestionePrenotazioni(object):

    def __init__(self, model: GestorePrenotazioni, view: VistaGestionePrenotazioni):

        self.view = view
        self.model = model
        self.update_tabella()
        self.prenotazione_selezionata = None
        self.view.pulsante_aggiungi.clicked.connect(self.open_vista_inserimento)

    def open_vista_inserimento(self):
        vista_inserimento = VistaInserisciPrenotazione()
        vista_inserimento.show()
        controller_inserimento = ContInserisciPrenotazione(self.model, vista_inserimento)
        controller_inserimento.view.exec()
        self.update_tabella()

    def update_tabella(self):
        elementi = self.model.lista_prenotazioni

        i = 0
        for x in elementi:
            self.view.tab.setItem(i, 0, QTableWidgetItem(str(x.nome)))
            self.view.tab.setItem(i, 1, QTableWidgetItem(str(x.tavolo)))
            self.view.tab.setItem(i, 1, QTableWidgetItem(str(x.orario)))
            self.view.tab.setItem(i, 1, QTableWidgetItem(str(x.giorno)))
            self.view.tab.setItem(i, 1, QTableWidgetItem(str(x.posti)))
            self.view.tab.setItem(i, 1, QTableWidgetItem(str(x.codice)))
            i += 1