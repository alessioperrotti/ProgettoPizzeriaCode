from Code.GestioneOrdiniTavolo.Model.ordine_tavolo import OrdineTavolo
from Code.GestioneOrdiniTavolo.Model.tavolo import Tavolo
from Code.GestioneOrdiniTavolo.Model.ordine_tavolo import OrdineTavolo

class GestoreOrdiniTavolo(object):

    def __init__(self):

        self.lista_tavoli = []
        self.lista_ordini = []
        self.ultimo_codice_ordine = 0

    def setup_tavoli(self):

        tavolo1 = Tavolo(1, 8)
        tavolo2 = Tavolo(2, 8)
        tavolo3 = Tavolo(3, 8)
        tavolo4 = Tavolo(4, 8)
        tavolo5 = Tavolo(5, 6)
        tavolo6 = Tavolo(6, 6)
        tavolo7 = Tavolo(7, 6)
        tavolo8 = Tavolo(8, 4)
        tavolo9 = Tavolo(9, 4)
        tavolo10 = Tavolo(10, 4)
        tavolo11 = Tavolo(11, 4)
        tavolo1 = Tavolo(12, 2)
        tavolo1 = Tavolo(13, 2)
        tavolo1 = Tavolo(14, 2)
        tavolo1 = Tavolo(15, 2)
        tavolo1 = Tavolo(16, 2)
        tavolo1 = Tavolo(17, 2)

    def genera_id(self):
        self.ultimo_codice_ordine += 1
        return self.ultimo_codice_ordine

    def aggiungi_ordine(self, ordine: OrdineTavolo):

        ordine.codice = self.genera_id()
        self.lista_ordini.append(ordine)

    def conferma_ordine(self, ordine):

        self.lista_ordini.append(ordine)


    def get_info_ordinitavolo(self):
        pass


    def cerca_ordini_per_tavolo_da_pagare(self, numero_tavolo):

        lista_ordini_cercata = []
        for x in self.lista_ordini:
            if x.tavolo.numero == numero_tavolo and x.pagato == False:
                lista_ordini_cercata.append(x)

        return lista_ordini_cercata
