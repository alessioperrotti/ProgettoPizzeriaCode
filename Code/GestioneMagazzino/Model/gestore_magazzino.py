
from Code.GestioneMagazzino.Model.materia_prima import MateriaPrima
from PyQt6.QtCore import pyqtSignal
from datetime import date
class GestoreMagazzino(object):

    elemento_inserito = pyqtSignal(int, str, float, float, float, float, date)

    def __init__(self):

        self.lista_materieprime = []


    def aggiungi_materiaprima(self, codice, nome, costo_al_kg, qta_disponibile, qta_limite,
                              qta_ordine_STD, data_scadenza):

        nuova_materiaprima = MateriaPrima(codice, nome, costo_al_kg, qta_disponibile, qta_limite, qta_ordine_STD, data_scadenza)
        self.lista_materieprime.append(nuova_materiaprima)

        #self.elemento_inserito.emit(codice, nome, qta_disponibile)


    def modifica_materiaprima(self, codice, new_nome, new_costo_al_kg, new_qta_disponibile,
                              new_qta_limite, new_qta_ordine_STD, new_data_scadenza):

        found = False

        for x in self.lista_materieprime:
            if x.codice == codice:
                x.nome = new_nome
                x.costo_al_kg =  new_costo_al_kg
                x.qta_disponibile = new_qta_disponibile
                x.qta_limite = new_qta_limite
                x.qta_ordine_STD = new_qta_ordine_STD
                x.data_scadenza = new_data_scadenza
                found = True

        if not found:
            pass

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

