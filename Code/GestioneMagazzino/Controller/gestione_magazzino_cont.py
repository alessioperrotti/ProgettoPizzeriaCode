from ..View.gestione_magazzino_view import VistaGestioneMagazzino
from ..View.inserisci_materiaprima_view import VistaInserisciMateriaPrima


class ContGestioneMagazzino(object):

    def __init__(self, model):

        self.view = VistaGestioneMagazzino()
        self.model = model


    def open_inserimento(self):

        dialog_inserimento = VistaInserisciMateriaPrima()
        dialog_inserimento.exec_()

    def update_tabella(self, codice, nome, qta_disponibile):

        self.model.elemento_inserito.connect(self.view.update_tabella())