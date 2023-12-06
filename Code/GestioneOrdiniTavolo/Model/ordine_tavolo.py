from _datetime import datetime
from Code.GestioneMenu.Model.prodotto import Prodotto
from Code.GestioneOrdiniTavolo.Model.tavolo import Tavolo


class OrdineTavolo(object):

    def __init__(self, tavolo: Tavolo):

        self.codice = None
        self.lista_prodotti = []
        self.orario = datetime.now().time()
        self.prezzo_totale = 0
        self.tavolo = tavolo
        self.pagato = False
        self.pronto = False
        #self.confermato = False

    def aggiungi_prodotto(self, prodotto: Prodotto):

        self.lista_prodotti.append(prodotto)
        self.prezzo_totale += prodotto.prezzo_al_pubblico

    def rimuovi_prodotto(self, prodotto: Prodotto):

        self.lista_prodotti.remove(prodotto)
        self.prezzo_totale -= prodotto.prezzo_al_pubblico
