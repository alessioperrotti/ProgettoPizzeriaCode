from Code.GestioneMagazzino.View.inserisci_materiaprima_view import VistaInserisciMateriaPrima
from Code.GestioneMagazzino.Model.materia_prima import MateriaPrima
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtCore import QDate
from Code.GestioneMagazzino.Model.gestore_magazzino import GestoreMagazzino


class UsedCode(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class OutOfDate(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(message)


class ContInserisciMateriaPrima(object):

    def __init__(self, model: GestoreMagazzino, view: VistaInserisciMateriaPrima):

        self.view = view
        self.model = model

        self.view.pulsante_conferma.clicked.connect(self.conferma_inserimento)

    def conferma_inserimento(self):

        try:
            codice = self.view.campo_codice.text()
            if self.model.estrai_per_codice(codice) is not None:
                raise UsedCode("Il codice inserito risulta già utilizzato.")
            nome = self.view.campo_nome.text().title()
            costo_al_kg = round(float(self.view.campo_costoAlKg.text()), 2)
            qta_disponibile = round(float(self.view.campo_qtaDisp.text()), 3)
            data_scadenza = self.view.campo_dataScadenza.selectedDate()
            if data_scadenza <= QDate.currentDate():
                raise OutOfDate("La materia prima risulta già scaduta.")
            qta_limite = round(float(self.view.campo_qtaLimite.text()), 3)
            qta_ordine_STD = round(float(self.view.campo_qtaOrdineSTD.text()), 3)
            nuova_materia_prima = MateriaPrima(codice, nome, costo_al_kg, qta_disponibile,
                                               qta_limite, qta_ordine_STD, data_scadenza)

        except ValueError:
            if not all([
                self.view.campo_codice.text(),
                self.view.campo_nome.text(),
                self.view.campo_costoAlKg.text(),
                self.view.campo_qtaDisp.text(),
                self.view.campo_qtaLimite.text(),
                self.view.campo_qtaOrdineSTD.text(),
            ]):
                errore_msg = "Controllare che tutti i campi siano riempiti."
            else:
                errore_msg = "Controllare che i dati siano inseriti correttamente."

            error_box = QMessageBox()
            error_box.setIcon(QMessageBox.Icon.Critical)
            error_box.setWindowTitle("Errore di Inserimento")
            error_box.setText(errore_msg)
            error_box.exec()

        except UsedCode as uc:
            error_box = QMessageBox()
            error_box.setIcon(QMessageBox.Icon.Critical)
            error_box.setWindowTitle("Errore di Inserimento")
            error_box.setText(uc.message)
            error_box.exec()

        except OutOfDate as od:
            error_box = QMessageBox()
            error_box.setIcon(QMessageBox.Icon.Critical)
            error_box.setWindowTitle("Errore di Inserimento")
            error_box.setText(od.message)
            error_box.exec()

        else:
            self.model.aggiungi_materiaprima(nuova_materia_prima)
            self.view.close()

