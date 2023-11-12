
from materia_prima import MateriaPrima
class GestoreMagazzino(object):

    def __init__(self):

        self.lista_materieprime = []


    def aggiungi_materiaprima(self, codice, nome, costo_al_kg, qta_disponibile, qta_limite, qta_ordine_STD, data_scadenza):

        nuova_materiaprima = MateriaPrima(codice, nome, costo_al_kg, qta_disponibile, qta_limite, qta_ordine_STD, data_scadenza)
        self.lista_materieprime.append(nuova_materiaprima)

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

