from _datetime import datetime


class OrdineTavolo(object):

    def __init__(self, tavolo):

        self.codice = None
        self.lista_prodotti = []
        self.orario = datetime.now().time()
        self.prezzo_totale = 0
        self.tavolo = tavolo
        self.pagato = False
        self.completato = False

    def aggiungi_prodotto(self, prodotto):

        self.lista_prodotti.append(prodotto)
        self.prezzo_totale += prodotto.prezzo_al_pubblico