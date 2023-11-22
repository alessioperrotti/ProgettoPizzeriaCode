from Code.GestioneMagazzino.View.modifica_materiaprima_view import VistaModificaMateriaPrima
from Code.GestioneMagazzino.Model.gestore_magazzino import GestoreMagazzino
from Code.GestioneMagazzino.Model.materia_prima import MateriaPrima
class ContModificaMateriaPrima(object):

    def __init__(self, view: VistaModificaMateriaPrima, model: GestoreMagazzino):

        self.view = view
        self.model = model
        self.view.pulsante_conferma.clicked.connect(self.conferma_modifica)

    def riempi_labels(self, materiaprima: MateriaPrima):

        self.view.label_codice2.setText(str(materiaprima.codice))
        self.view.label_nome2.setText(str(materiaprima.nome))

    def conferma_modifica(self):

        new_costo_al_kg = self.view.campo_costoAlKg.text()
        new_qta_disponibile = self.view.campo_qtaDisp.text()
        new_data_scadenza = self.view.campo_dataScadenza.selectedDate()
        new_qta_limite = self.view.campo_qtaLimite.text()
        new_qta_ordine_STD = self.view.campo_qtaOrdineSTD.text()

        self.model.modifica_materiaprima(new_costo_al_kg, new_qta_disponibile, new_qta_limite,
                                         new_qta_ordine_STD, new_data_scadenza)

        self.view.close()
