from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QStackedWidget, QTableWidgetItem

from Code.GestioneDipendenti.Controller.cont_turni_personale import ContTurniPersonale
from Code.GestioneDipendenti.Model.gestore_dipendenti import GestoreDipendenti
from Code.GestioneDipendenti.View.vista_home_cuoco import VistaHomeCuoco
from Code.GestioneDipendenti.View.vista_turni_personale import VistaTurniPersonale


class ContHomeCuoco(object):
    def __init__(self, model: GestoreDipendenti, stacked: QStackedWidget):
        self.stacked = stacked
        self.view = VistaHomeCuoco()
        stacked.addWidget(self.view)
        self.model = model
        # self.view.pulsante.clicked.connect(self.go_back)
        self.view.p_turni.clicked.connect(self.click_turni)
        self.view.p_comande.clicked.connect(self.click_comande)
        #pulsante back da TurniCuoco
    def click_turni(self):
        cont_turni = ContTurniPersonale(self.model, self.stacked)
        cont_turni.view = VistaTurniPersonale()
        cont_turni.view.exec()

    def click_comande(self):
        pass