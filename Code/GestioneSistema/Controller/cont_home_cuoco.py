from PyQt6.QtWidgets import QStackedWidget

from Code.GestioneDipendenti.Controller.cont_turni_personale import ContTurniPersonale
from Code.GestioneDipendenti.Model.gestore_dipendenti import GestoreDipendenti
from Code.GestioneSistema.View.vista_home_cuoco import VistaHomeCuoco


class ContHomeCuoco(object):
    def __init__(self, model: GestoreDipendenti, stacked: QStackedWidget):
        self.stacked = stacked
        self.view = VistaHomeCuoco()
        stacked.addWidget(self.view)
        self.model = model

        self.cont_turni = ContTurniPersonale(GestoreDipendenti(),stacked)

        self.view.p_turni.clicked.connect(self.click_turni)
        self.view.p_comande.clicked.connect(self.click_comande)
        self.cont_turni.view.pulsante_back.clicked.connect(lambda: self.stacked.setCurrentWidget(self.view))

    # def click_turni(self):
    #     cont_turni = ContTurniPersonale(self.model)
    #     cont_turni.view = VistaTurniPersonale()
    #     cont_turni.update_tabella()
    #     cont_turni.view.exec()

    def click_turni(self):
        self.stacked.setCurrentWidget(self.cont_turni.view)

    def click_comande(self):
        pass