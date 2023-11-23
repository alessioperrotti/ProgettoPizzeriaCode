from Code.GestioneMagazzino.View.modifica_materiaprima_view import VistaModificaMateriaPrima
from Code.GestioneMagazzino.Model.gestore_magazzino import GestoreMagazzino
from Code.GestioneMagazzino.Model.materia_prima import MateriaPrima
from PyQt6.QtWidgets import QMessageBox


class ContModificaMateriaPrima(object):

    def __init__(self, view: VistaModificaMateriaPrima, model: GestoreMagazzino, matprima_da_modificare: MateriaPrima):

        self.view = view
        self.model = model
        self.matprima_da_modificare = matprima_da_modificare
        self.view.pulsante_conferma.clicked.connect(self.conferma_modifica)
        self.riempi_labels(matprima_da_modificare)

    def riempi_labels(self, materiaprima: MateriaPrima):

        self.view.label_codice2.setText(str(materiaprima.codice))
        self.view.label_nome2.setText(str(materiaprima.nome))

    def conferma_modifica(self):

        try:
            new_costo_al_kg = self.view.campo_costoAlKg.text()
            new_qta_disponibile = self.view.campo_qtaDisp.text()
            new_data_scadenza = self.view.campo_dataScadenza.selectedDate()
            new_qta_limite = self.view.campo_qtaLimite.text()
            new_qta_ordine_STD = self.view.campo_qtaOrdineSTD.text()

        except ValueError:
            if not all([
                new_costo_al_kg,
                new_qta_disponibile,
                new_data_scadenza,
                new_qta_limite,
                new_qta_ordine_STD
            ]):
                errore_msg = "Controllare che tutti i campi siano riempiti."
            else:
                errore_msg = "Controllare che i dati siano inseriti correttamente."

            error_box = QMessageBox()
            error_box.setIcon(QMessageBox.Icon.Critical)
            error_box.setWindowTitle("Errore di Inserimento")
            error_box.setText(errore_msg)
            error_box.exec()

        else:
            self.model.modifica_materiaprima(self.matprima_da_modificare.codice, new_costo_al_kg,
                                             new_qta_disponibile, new_qta_limite,
                                         new_qta_ordine_STD, new_data_scadenza)
            self.view.close()

