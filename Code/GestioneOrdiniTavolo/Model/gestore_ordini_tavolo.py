from Code.GestioneOrdiniTavolo.Model.tavolo import Tavolo
from Code.GestioneOrdiniTavolo.Model.ordine_tavolo import OrdineTavolo
import pickle

class GestoreOrdiniTavolo(object):

    def __init__(self):

        self.lista_tavoli: list[Tavolo] = []
        self.setup_tavoli()
        self.lista_ordini: list[OrdineTavolo] = []
        self.ultimo_codice_ordine = 0
        self.file_ordini_path = "lista_ordini.pickle"
        self.file_tavoli_path = "lista_tavoli.pickle"
        self.carica_da_file()

    def setup_tavoli(self):


        tavolo1 = Tavolo(1, 8)
        tavolo2 = Tavolo(2, 8)
        tavolo3 = Tavolo(3, 8)
        tavolo4 = Tavolo(4, 8)
        tavolo5 = Tavolo(5, 6)
        tavolo6 = Tavolo(6, 6)
        tavolo7 = Tavolo(7, 6)
        tavolo8 = Tavolo(8, 6)
        tavolo9 = Tavolo(9, 4)
        tavolo10 = Tavolo(10, 4)
        tavolo11 = Tavolo(11, 4)
        tavolo12 = Tavolo(12, 4)
        tavolo13 = Tavolo(13, 2)
        tavolo14 = Tavolo(14, 2)
        tavolo15 = Tavolo(15, 2)
        tavolo16 = Tavolo(16, 2)


        self.lista_tavoli.append(tavolo1)
        self.lista_tavoli.append(tavolo2)
        self.lista_tavoli.append(tavolo3)
        self.lista_tavoli.append(tavolo4)
        self.lista_tavoli.append(tavolo5)
        self.lista_tavoli.append(tavolo6)
        self.lista_tavoli.append(tavolo7)
        self.lista_tavoli.append(tavolo8)
        self.lista_tavoli.append(tavolo9)
        self.lista_tavoli.append(tavolo10)
        self.lista_tavoli.append(tavolo11)
        self.lista_tavoli.append(tavolo12)
        self.lista_tavoli.append(tavolo13)
        self.lista_tavoli.append(tavolo14)
        self.lista_tavoli.append(tavolo15)
        self.lista_tavoli.append(tavolo16)



    def genera_id(self):

        self.ultimo_codice_ordine += 1
        self.salva_ordini_su_file()
        return self.ultimo_codice_ordine

    def aggiungi_ordine(self, ordine: OrdineTavolo):

        ordine.codice = self.genera_id()
        self.lista_ordini.append(ordine)
        self.salva_ordini_su_file()
        self.carica_da_file()

    # probabilmente da togliere
    def conferma_ordine(self, ordine: OrdineTavolo):

        for x in self.lista_ordini:
            if int(x.codice) == int(ordine.codice):
                x.confermato = True



    def salva_ordini_su_file(self):

        dati = {

            'cod': self.ultimo_codice_ordine,
            'ordini': self.lista_ordini,
        }

        try:
            with open(self.file_ordini_path, 'wb') as file:
                pickle.dump(dati, file, pickle.HIGHEST_PROTOCOL)
            file.close()
        except FileNotFoundError as e:
            print(e)

    def salva_tavoli_su_file(self):

        try:
            with open(self.file_tavoli_path, 'wb') as file:
                pickle.dump(self.lista_tavoli, file, pickle.HIGHEST_PROTOCOL)
            file.close()
        except FileNotFoundError as e:
            print(e)

    def carica_da_file(self):

        try:
            with open(self.file_ordini_path, 'rb') as file1:
                dati = pickle.load(file1)

            file1.close()
            self.ultimo_codice_ordine = dati['cod']
            self.lista_ordini = dati['ordini']

            with open(self.file_tavoli_path, 'rb') as file2:
                self.lista_tavoli = pickle.load(file2)
                file2.close()

        except FileNotFoundError as e:
            print(e)
        except EOFError as e:
            print(e)

    def estrai_ordine_per_codice(self, codice):

        elemento_cercato = None
        for x in self.lista_ordini:
            if int(x.codice) == int(codice):
                elemento_cercato = x
        return elemento_cercato

    def get_info_ordinitavolo(self):
        pass


    def cerca_ordini_per_tavolo_da_pagare(self, numero_tavolo):

        lista_ordini_cercata = []
        for x in self.lista_ordini:
            if x.tavolo.numero == numero_tavolo and x.pagato == False:
                lista_ordini_cercata.append(x)

        return lista_ordini_cercata

    def get_info_ordini_tavolo(self):
        lista_ordini = self.lista_ordini.copy()
        return lista_ordini
