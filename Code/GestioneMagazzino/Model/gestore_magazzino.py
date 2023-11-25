
import os
import pickle
from Code.GestioneMagazzino.Model.materia_prima import MateriaPrima
from PyQt6.QtCore import pyqtSignal
from datetime import date


class GestoreMagazzino(object):

    elemento_inserito = pyqtSignal(int, str, float, float, float, float, date)

    def __init__(self):

        self.lista_materieprime = []
        self.file_pickle_path = 'Code/GestioneMagazzino/Data/lista_materieprime.pickle'
        self.carica_da_file()


    def aggiungi_materiaprima(self, materiaprima):

        self.lista_materieprime.append(materiaprima)


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

    def estrai_per_codice(self, codice):

        elemento_cercato = None
        for x in self.lista_materieprime:
            if int(x.codice) == int(codice):
                elemento_cercato = x
        return elemento_cercato

    def estrai_per_nome(self, nome):

        elemento_cercato = None
        for x in self.lista_materieprime:
            if str(x.nome) == str(nome):
                elemento_cercato = x
        return elemento_cercato

    def salva_su_file(self):

        if os.path.exists(self.file_pickle_path):
            with open(self.file_pickle_path, 'wb') as file:
                pickle.dump(self.lista_materieprime, file)
            file.close()

    def carica_da_file(self):

        if os.path.exists(self.file_pickle_path):
            with open(self.file_pickle_path, 'rb') as file:
                self.lista_materieprime = pickle.load(file)


    def elimina_materiaprima(self, codice):

        elemento_da_eliminare = self.estrai_per_codice(codice)
        self.lista_materieprime.remove(elemento_da_eliminare)

    def decrementa_disponibilita(self, codice, decremento):

        for x in self.lista_materieprime:
            if x.codice == codice:
                x.qta_disponibile -= decremento

    def incrementa_disponibilita(self, codice, incremento):

        for x in self.lista_materieprime:
            if x.codice == codice:
                x.qta_disponibile += incremento

    def get_info_materieprime(self):
        pass

