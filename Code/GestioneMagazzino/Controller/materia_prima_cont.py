from Code.GestioneMagazzino.View.materia_prima_view import VistaMateriaPrima
from Code.GestioneMagazzino.Model.gestore_magazzino import GestoreMagazzino
from Code.GestioneMagazzino.Model.materia_prima import MateriaPrima
class ContMateriaPrima(object):

    def __init__(self, view: VistaMateriaPrima, model: GestoreMagazzino):

        self.view = view
        self.model = model


    def riempi_labels(self, materiaprima: MateriaPrima):

        self.view.label_codice2.setText(str(materiaprima.codice))
        self.view.label_codice2.setText(str(materiaprima.nome))
        self.view.label_costoAlKg2.setText(str(materiaprima.costo_al_kg))
        self.view.label_qtaDisp2.setText(str(materiaprima.qta_disponibile))
        self.view.label_qtaLimite2.setText(str(materiaprima.qta_limite))
        self.view.label_qtaOrdineSTD2.setText(str(materiaprima.qta_ordine_STD))
        self.view.label_dataScadenza2.setText(str(materiaprima.data_scadenza))