from Code.GestioneMagazzino.Model.materia_prima import MateriaPrima


class Prodotto(object):

    def __init__(self, nome, codice, prezzo_al_pubblico, tipologia, ingredienti):

        self.nome = nome
        self.codice = codice
        self.prezzo_al_pubblico = prezzo_al_pubblico
        self.tipologia = tipologia
        self.ingredienti = ingredienti          # lista di tuple (MateriaPrima, quantità: int)
        self.costo_unitario = self.calcola_costo_unitario()

    def calcola_costo_unitario(self):

        costo = 0
        for ingrediente in self.ingredienti:
            costokg_matprima = ingrediente[0].costo_al_kg
            costo_materiaprima = round(costokg_matprima * ingrediente[1], 2)
            costo += costo_materiaprima
        return costo
