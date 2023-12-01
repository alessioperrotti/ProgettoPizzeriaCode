from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QStackedWidget, QTableWidgetItem

from Code.GestioneDipendenti.Controller.cont_turni_personale import ContTurniPersonale
from Code.GestioneDipendenti.Model.gestore_dipendenti import GestoreDipendenti
from Code.GestioneDipendenti.View.vista_home_cameriere import VistaHomeCameriere
from Code.GestioneDipendenti.View.vista_turni_personale import VistaTurniPersonale
from Code.GestioneDipendenti.View.vista_visualizza_prenotazioni import VistaVisualizzaPrenotazioni


class ContHomeCameriere(object):
    def __init__(self, model: GestoreDipendenti, stacked: QStackedWidget):
        self.stacked = stacked
        self.view = VistaHomeCameriere()
        stacked.addWidget(self.view)
        self.model = model
        # self.view.pulsante.clicked.connect(self.go_back)
        self.view.p_turni.clicked.connect(self.click_turni)
        self.view.p_prenotazioni.clicked.connect(self.click_prenotazioni)
        self.view.p_piantina.clicked.connect(self.click_piantina)
        # pulsante back da HomeCameriere

    def click_turni(self):
        cont_turni = ContTurniPersonale(self.model, self.stacked)
        cont_turni.view = VistaTurniPersonale()
        cont_turni.view.exec()

    def click_prenotazioni(self):
        pass
        # dialog_prenotazioni = VistaVisualizzaPrenotazioni()
        # cont_prenotazioni = ContVisualizzaPrenotazioni(self.model,)
        # cont_prenotazioni.view = VistaTurniPersonale()
        # cont_prenotazioni.view.exec()

    def click_piantina(self):
        pass
