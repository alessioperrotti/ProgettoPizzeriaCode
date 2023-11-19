
class OrdineTavolo(object):

    def __init__(self, codice, orario, prezzo_totale, tavolo):

        self.codice = codice
        self.lista_prodotti = []
        self.orario = orario
        self.prezzo_totale = prezzo_totale
        self.tavolo = tavolo
        self.pagato = False

    def aggiungi_prodotto(self, prodotto):

        self.lista_prodotti.append(prodotto)