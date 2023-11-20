from  Code.GestionePrenotazioni.View.vista_inserisci_prenotazione import VistaInserisciPrenotazione
from Code.GestionePrenotazioni.Model.prenotazione import Prenotazione
from PyQt6.QtCore import QDate
class ContInserisciPrenotazione(object):

    def __init__(self, model, view: VistaInserisciPrenotazione):

        self.view = view
        self.model = model

        self.view.pulsante_conferma.clicked.connect(self.conferma_inserimento)
        #self.view.campo_dataScadenza.dateChanged.connect(self.data_cambiata)

    def conferma_inserimento(self):
        nome = self.view.campo_nome.text()

        nuova_prenotazione = Prenotazione(nome)

        self.model.aggiungi_prenotazione(nuova_prenotazione)

        self.view.close()


    def data_cambiata(self, data):
        self.model.data_scadenza = data