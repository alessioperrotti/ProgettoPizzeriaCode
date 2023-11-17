from ..View.inserisci_materiaprima_view import VistaInserisciMateriaPrima


class ContGestioneMagazzino(object):

    def __init__(self, model, view):

        self.view = view
        self.model = model
        print("Connessione del segnale inizializzata")
        self.view.pulsante_inserisci.clicked.connect(self.open_inserimento)

    def open_inserimento(self):
        print("Funzione open_inserimento chiamata")
        dialog_inserimento = VistaInserisciMateriaPrima()
        dialog_inserimento.show()

    def update_tabella(self, codice, nome, qta_disponibile):

        self.model.elemento_inserito.connect(self.view.update_tabella())