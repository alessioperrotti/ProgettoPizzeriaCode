import PyQt6
from  ..View.inserisci_materiaprima_view import VistaInserisciMateriaPrima
class ContInserisciMateriaPrima(object):

    def __init__(self, model):

        self.view = VistaInserisciMateriaPrima()
        self.model = model

        self.view.pulsante_conferma.clicked.connect(self.conferma_inserimento)


    def conferma_inserimento(self):

        codice = self.view.campo_codice.text()
        nome = self.view.campo_nome.text()
        costo_al_kg = self.view.campo_costoAlKg.text()
        qta_disponibile = self.view.campo_qtaDisp.text()
        data_scadenza = self.view.campo_dataScadenza.dateChanged.connect(self.data_cambiata)
        qta_limite = self.view.campo_qtaLimite.text()
        qta_ordine_STD = self.view.campo_qtaOrdineSTD.text()

        self.model.aggiungi_materiaprima(codice, nome, costo_al_kg, qta_disponibile, qta_limite,
                              qta_ordine_STD, data_scadenza)




    def data_cambiata(self, data_scadenza):
        self.model.data_scadenza = data_scadenza



