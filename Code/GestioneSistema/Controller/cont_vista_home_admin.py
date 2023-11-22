from PyQt6.QtWidgets import QStackedWidget

from Code.GestioneSistema.View.vista_home_admin import VistaHomeAdmin


class ContVistaHomeAdmin():
    def __init__(self,stacked:QStackedWidget):
        self.view = VistaHomeAdmin()
        stacked.addWidget(self.view)

