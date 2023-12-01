from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QStackedWidget, QTableWidgetItem

from Code.GestioneDipendenti.Model.gestore_dipendenti import GestoreDipendenti
from Code.GestioneDipendenti.View.vista_home_cameriere import VistaHomeCameriere


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
        #pulsante back da HomeCameriere
        
    def click_turni(self):
        pass

    def click_prenotazioni(self):
        pass

    def click_piantina(self):
        pass