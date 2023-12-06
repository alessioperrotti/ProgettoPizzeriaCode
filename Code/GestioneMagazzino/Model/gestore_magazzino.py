
import os
import pickle
from Code.GestioneMagazzino.Model.materia_prima import MateriaPrima
from Code.GestioneMagazzino.Model.ordine_ristorante import OrdineRistorante
from _datetime import datetime, timedelta

class GestoreMagazzino(object):

    def __init__(self):

        self.lista_materieprime: list[MateriaPrima] = []
        self.file_pickle_path = "lista_materieprime.pickle"
        self.carica_da_file()


    def aggiungi_materiaprima(self, materiaprima):

        self.lista_materieprime.append(materiaprima)
        self.salva_su_file()
        self.carica_da_file()


    def modifica_materiaprima(self, codice_ricerca, new_costo_al_kg, new_qta_disponibile,
                              new_qta_limite, new_qta_ordine_STD, new_data_scadenza):

        matprima_da_modificare: MateriaPrima = self.estrai_per_codice(codice_ricerca)

        for x in self.lista_materieprime:
            if int(matprima_da_modificare.codice) == int(x.codice):
                x.costo_al_kg = new_costo_al_kg
                x.qta_disponibile = new_qta_disponibile
                x.qta_limite = new_qta_limite
                x.qta_ordine_STD = new_qta_ordine_STD
                x.data_scadenza = new_data_scadenza

        self.salva_su_file()
        self.carica_da_file()

    def estrai_per_codice(self, codice):

        elemento_cercato = None
        for x in self.lista_materieprime:
            if int(x.codice) == int(codice):
                elemento_cercato = x
        return elemento_cercato

    def estrai_per_nome(self, nome):

        elemento_cercato = None
        for x in self.lista_materieprime:
            if str(x.nome).lower() == str(nome):
                elemento_cercato = x
        return elemento_cercato

    def salva_su_file(self):

        try:
            with open(self.file_pickle_path, 'wb') as file:
                pickle.dump(self.lista_materieprime, file, pickle.HIGHEST_PROTOCOL)
            file.close()
        except FileNotFoundError as e:
            print(e)

    def carica_da_file(self):

        try:
            with open(self.file_pickle_path, 'rb') as file:
                self.lista_materieprime = pickle.load(file)
                file.close()
        except FileNotFoundError:
            print("file non trovato")


    def elimina_materiaprima(self, codice):

        elemento_da_eliminare = self.estrai_per_codice(codice)
        self.lista_materieprime.remove(elemento_da_eliminare)
        self.salva_su_file()
        self.carica_da_file()

    def decrementa_disponibilita(self, codice, decremento):

        for x in self.lista_materieprime:
            if int(x.codice) == int(codice):
                if x.qta_disponibile >= decremento:
                    x.qta_disponibile = round((x.qta_disponibile - decremento), 3)
                    self.salva_su_file()
                    self.carica_da_file()
                    return True
                else:
                    return False

    def controlla_magazzino(self):

        self.carica_da_file()
        domani = datetime.now().date() + timedelta(days=1)
        ordine_rist = OrdineRistorante()

        for matprima in self.lista_materieprime:
            if (matprima.data_scadenza <= domani) or (matprima.qta_disponibile <= matprima.qta_limite):
                ordine_rist.aggiungi_all_ordine(matprima)
                self.incrementa_disponibilita(matprima.codice, matprima.qta_ordine_STD)

    def incrementa_disponibilita(self, codice, incremento):

        for x in self.lista_materieprime:
            if int(x.codice) == int(codice):
                x.qta_disponibile = round((x.qta_disponibile + incremento), 3)

    def get_info_materieprime(self):
        return self.lista_materieprime

