from _datetime import datetime
from Code.GestioneMagazzino.Model.materia_prima import MateriaPrima

class OrdineRistorante(object):

    def __init__(self):

        self.data_richiesta = datetime.now()
        self.lista_prodotti: list[MateriaPrima] = []
        self.costo_totale = 0

    def aggiungi_all_ordine(self, matprima: MateriaPrima):
        self.lista_prodotti.append(matprima)