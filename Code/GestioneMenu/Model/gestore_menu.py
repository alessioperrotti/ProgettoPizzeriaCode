from Code.GestioneMenu.Model.prodotto import Prodotto
from PyQt6.QtCore import pyqtSignal

class GestoreMenu(object):

    def __init__(self):
        self.lista_prodotti = []

    def aggiungi_prodotto(self, prodotto):
        self.lista_prodotti.append(prodotto)

    def estrai_per_codice(self, codice):

        elemento_cercato = None
        for x in self.lista_prodotti:
            if int(x.codice) == int(codice):
                elemento_cercato = x
        return elemento_cercato

    def elimina_prodotto(self, codice):

        elemento_da_eliminare = self.estrai_per_codice(codice)
        self.lista_prodotti.remove(elemento_da_eliminare)

