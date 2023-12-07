from PyQt6.QtWidgets import QStackedWidget

from Code.GestioneDipendenti.Controller.cont_piantina import ContPiantina
from Code.GestioneDipendenti.Controller.cont_turni_personale import ContTurniPersonale
from Code.GestioneDipendenti.Model.gestore_dipendenti import GestoreDipendenti
from Code.GestioneSistema.View.vista_home_cameriere import VistaHomeCameriere
from Code.GestionePrenotazioni.Controller.cont_visualizza_prenotazioni import ContVisualizzaPrenotazioni
from Code.GestionePrenotazioni.Model.gestore_prenotazioni import GestorePrenotazioni


class ContHomeCameriere(object):
    def __init__(self, model, stacked: QStackedWidget):
        self.stacked = stacked
        self.view = VistaHomeCameriere()
        stacked.addWidget(self.view)
        self.model = model

        self.cont_turni = ContTurniPersonale(GestoreDipendenti(), stacked)
        self.cont_prenotazioni = ContVisualizzaPrenotazioni(GestorePrenotazioni(), stacked)
        self.cont_piantina = ContPiantina(GestorePrenotazioni(), stacked)

        self.view.p_turni.clicked.connect(self.click_turni)
        self.view.p_prenotazioni.clicked.connect(self.click_prenotazioni)
        self.view.p_piantina.clicked.connect(self.click_piantina)
        self.cont_piantina.view.pulsante_back.clicked.connect(lambda: self.stacked.setCurrentWidget(self.view))
        self.cont_prenotazioni.view.pulsante_back.clicked.connect(lambda: self.stacked.setCurrentWidget(self.view))
        self.cont_turni.view.pulsante_back.clicked.connect(lambda: self.stacked.setCurrentWidget(self.view))

    # def click_turni(self):
    #     cont_turni = ContTurniPersonale(GestoreDipendenti())
    #     cont_turni.view = VistaTurniPersonale()
    #     cont_turni.update_tabella()
    #     cont_turni.view.exec()

    def click_turni(self):
        self.stacked.setCurrentWidget(self.cont_turni.view)

    def click_prenotazioni(self):
        self.stacked.setCurrentWidget(self.cont_prenotazioni.view)

    def click_piantina(self):
        self.stacked.setCurrentWidget(self.cont_piantina.view)
        self.cont_piantina.update_tabella()

    # def click_prenotazioni(self):
    #     cont_prenotazioni = ContVisualizzaPrenotazioni(GestorePrenotazioni())
    #     cont_prenotazioni.view = VistaVisualizzaPrenotazioni()
    #     cont_prenotazioni.update_tabella()
    #     cont_prenotazioni.view.search_edit.textChanged.connect(cont_prenotazioni.filtra_elementi)
    #     cont_prenotazioni.view.exec()
    #
    # def click_piantina(self):
    #     cont_piantina = ContPiantina(GestorePrenotazioni(),VistaPiantina())
    #     cont_piantina.view.exec()
