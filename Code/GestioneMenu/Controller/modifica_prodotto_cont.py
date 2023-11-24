from Code.GestioneMenu.Model.gestore_menu import GestoreMenu
from Code.GestioneMenu.Model.prodotto import Prodotto
from Code.GestioneMenu.View.modifica_prodotto_view import VistaModificaProdotto

class ContModificaProdotto(object):

    def __init__(self, view: VistaModificaProdotto, model: GestoreMenu, prodotto_da_modificare: Prodotto):
        self.view = view
        self.model = model
        self.prodotto_da_modificare = prodotto_da_modificare