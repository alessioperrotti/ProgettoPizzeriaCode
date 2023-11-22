from Code.GestioneOrdiniTavolo.Model.ordine_tavolo import OrdineTavolo

class GestoreOrdiniTavolo(object):

    def __init__(self):

        self.lista_tavoli = []
        # self.numero = numero
        # self.posti_disponibili = posti_disponibili
        # self.stato = stato
        # #aggiungo dei tavoli
        #self.lista_tavoli.append(Tavolo(1, 4, "libero"))

        self.lista_ordini = []


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
