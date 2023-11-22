from Code.GestioneMagazzino.View.inserisci_materiaprima_view import VistaInserisciMateriaPrima
from Code.GestioneMagazzino.Model.materia_prima import MateriaPrima


class ContInserisciMateriaPrima(object):

    def __init__(self, model, view: VistaInserisciMateriaPrima):

        self.view = view
        self.model = model

        self.view.pulsante_conferma.clicked.connect(self.conferma_inserimento)

    def conferma_inserimento(self):

        codice = self.view.campo_codice.text()
        nome = self.view.campo_nome.text()
        costo_al_kg = self.view.campo_costoAlKg.text()
        qta_disponibile = self.view.campo_qtaDisp.text()
        data_scadenza = self.view.campo_dataScadenza.selectedDate()
        qta_limite = self.view.campo_qtaLimite.text()
        qta_ordine_STD = self.view.campo_qtaOrdineSTD.text()

        nuova_materia_prima = MateriaPrima(codice, nome, costo_al_kg, qta_disponibile,
                                           qta_limite, qta_ordine_STD, data_scadenza)

        self.model.aggiungi_materiaprima(nuova_materia_prima)
        self.view.close()
