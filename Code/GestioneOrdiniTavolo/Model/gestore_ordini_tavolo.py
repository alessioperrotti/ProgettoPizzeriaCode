from Code.GestioneOrdiniTavolo.Model.ordine_tavolo import OrdineTavolo
from Code.GestioneOrdiniTavolo.Model.tavolo import Tavolo
from Code.GestioneOrdiniTavolo.Model.ordine_tavolo import OrdineTavolo

class GestoreOrdiniTavolo(object):

    def __init__(self):

        self.lista_tavoli = []
        self.lista_ordini = []
        self.ultimo_codice_ordine = 0

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
