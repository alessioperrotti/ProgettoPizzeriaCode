
class Prodotto(object):

    def __init__(self, nome, codice, prezzo_al_pubblico, tipologia):

        self.nome = nome
        self.codice = codice
        self.prezzo_al_pubblico = prezzo_al_pubblico
        self.tipologia = tipologia
        self.ingredienti = []


    def aggiungi_ingrediente(self, ingrediente):

        self.ingredienti.append(ingrediente)
