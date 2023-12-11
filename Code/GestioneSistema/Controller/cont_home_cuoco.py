from PyQt6.QtWidgets import QStackedWidget

from Code.GestioneDipendenti.Controller.cont_lista_comande import ContListaComande
from Code.GestioneDipendenti.Controller.cont_turni_personale import ContTurniPersonale
from Code.GestioneDipendenti.Model.gestore_dipendenti import GestoreDipendenti
from Code.GestioneOrdiniTavolo.Model.gestore_ordini_tavolo import GestoreOrdiniTavolo
from Code.GestioneSistema.View.vista_home_cuoco import VistaHomeCuoco


class ContHomeCuoco(object):
    def __init__(self, model: GestoreDipendenti, stacked: QStackedWidget, gestore_ord:GestoreOrdiniTavolo):
        self.stacked = stacked
        self.view = VistaHomeCuoco()
        stacked.addWidget(self.view)
        self.model = model
        self.cont_comande = ContListaComande(gestore_ord, stacked)
        self.cont_turni = ContTurniPersonale(GestoreDipendenti(),stacked)

        self.view.p_turni.clicked.connect(self.click_turni)
        self.view.p_comande.clicked.connect(self.click_comande)
        self.cont_turni.view.pulsante_back.clicked.connect(lambda: self.stacked.setCurrentWidget(self.view))
        self.cont_comande.view.pulsante_back.clicked.connect(lambda: self.stacked.setCurrentWidget(self.view))



    def click_turni(self):
        self.stacked.setCurrentWidget(self.cont_turni.view)

    def click_comande(self):
        self.cont_comande.aggiorna_lista()
        self.stacked.setCurrentWidget(self.cont_comande.view)
