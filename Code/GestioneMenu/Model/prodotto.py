from Code.GestioneMagazzino.Model.materia_prima import MateriaPrima


class Prodotto(object):

    def __init__(self, nome, codice, prezzo_al_pubblico, tipologia, ingredienti):

        self.nome = nome
        self.codice = codice
        self.prezzo_al_pubblico = prezzo_al_pubblico
        self.tipologia = tipologia
        self.ingredienti = ingredienti          # lista di tuple (MateriaPrima, quantità: int)



