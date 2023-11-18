from ..View.inserisci_materiaprima_view import VistaInserisciMateriaPrima
from Code.GestioneMagazzino.View.gestione_magazzino_view import VistaGestioneMagazzino
from Code.GestioneMagazzino.Controller.inserisci_materiaprima_cont import ContInserisciMateriaPrima

class ContGestioneMagazzino(object):

    def __init__(self, model, view: VistaGestioneMagazzino):

        self.view = view
        self.model = model
        print("Connessione del segnale inizializzata")
        self.view.pulsante_inserisci.clicked.connect(self.open_inserimento)

    def open_inserimento(self):
        print("Funzione open_inserimento chiamata")
        dialog_inserimento = VistaInserisciMateriaPrima()
        controller_inserimento = ContInserisciMateriaPrima(self.model, dialog_inserimento)
        controller_inserimento.view.exec()

    def update_tabella(self, codice, nome, qta_disponibile):

        self.model.elemento_inserito.connect(self.view.update_tabella())