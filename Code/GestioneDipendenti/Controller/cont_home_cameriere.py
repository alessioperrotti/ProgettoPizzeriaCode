from PyQt6.QtWidgets import QStackedWidget

from Code.GestioneDipendenti.Controller.cont_piantina import ContPiantina
from Code.GestioneDipendenti.Controller.cont_turni_personale import ContTurniPersonale
from Code.GestioneDipendenti.Model.gestore_dipendenti import GestoreDipendenti
from Code.GestioneDipendenti.View.vista_home_cameriere import VistaHomeCameriere
from Code.GestioneDipendenti.View.vista_piantina import VistaPiantina
from Code.GestioneDipendenti.View.vista_turni_personale import VistaTurniPersonale
from Code.GestionePrenotazioni.Model.gestore_prenotazioni import GestorePrenotazioni


class ContHomeCameriere(object):
    def __init__(self, model, stacked: QStackedWidget):
        self.stacked = stacked
        self.view = VistaHomeCameriere()
        stacked.addWidget(self.view)
        self.model = model
        self.cont_turni_personale = ContTurniPersonale(self.model)

        self.view.p_turni.clicked.connect(self.click_turni)
        self.view.p_prenotazioni.clicked.connect(self.click_prenotazioni)
        self.view.p_piantina.clicked.connect(self.click_piantina)
        self.cont_turni_personale.view.pulsante_back.clicked.connect(lambda: self.stacked.setCurrentWidget(self.view))
        # pulsante back da HomeCameriere

    def click_turni(self):
        cont_turni = ContTurniPersonale(GestoreDipendenti())
        cont_turni.view = VistaTurniPersonale()
        cont_turni.view.exec()

    def click_prenotazioni(self):
        pass
        # dialog_prenotazioni = VistaVisualizzaPrenotazioni()
        # cont_prenotazioni = ContVisualizzaPrenotazioni(self.model,)
        # cont_prenotazioni.view = VistaTurniPersonale()
        # cont_prenotazioni.view.exec()

    def click_piantina(self):
        cont_piantina = ContPiantina(GestorePrenotazioni(),VistaPiantina())
        cont_piantina.view.exec()
