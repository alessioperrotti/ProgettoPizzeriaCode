from  ..View.gestione_magazzino_view import VistaGestioneMagazzino

class ContGestioneMagazzino(object):

    def __init__(self, model):

        self.view = VistaGestioneMagazzino()
        self.model = model

    def update_tabella(self, codice, nome, qta_disponibile):

        self.model.elemento_inserito.connect(self.view.update_tabella())