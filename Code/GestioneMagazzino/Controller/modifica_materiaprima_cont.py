from Code.GestioneMagazzino.View.modifica_materiaprima_view import VistaModificaMateriaPrima
from Code.GestioneMagazzino.Model.gestore_magazzino import GestoreMagazzino
from Code.GestioneMagazzino.Model.materia_prima import MateriaPrima
class ContModificaMateriaPrima(object):

    def __init__(self, view: VistaModificaMateriaPrima, model: GestoreMagazzino):

        self.view = view
        self.model = model
        self.view.pulsante_conferma.clicked.connect(self.conferma_modifica)

    def conferma_modifica(self):

        costo_al_kg = self.view.campo_costoAlKg.text()
        qta_disponibile = self.view.campo_qtaDisp.text()
        data_scadenza = self.view.campo_dataScadenza.selectedDate()
        qta_limite = self.view.campo_qtaLimite.text()
        qta_ordine_STD = self.view.campo_qtaOrdineSTD.text()

        nuova_materia_prima = MateriaPrima(costo_al_kg, qta_disponibile,
                                           qta_limite, qta_ordine_STD, data_scadenza)

        self.model.modifica_materiaprima(nuova_materia_prima)

        self.view.close()
