import sys

from PyQt6.QtWidgets import QWidget, QStackedWidget, QVBoxLayout, QApplication

from Code.GestioneDipendenti.Controller.cont_gestione_dipendenti import ContGestioneDipendenti
from Code.GestioneDipendenti.Controller.cont_gestione_turni import ContGestioneTurni
from Code.GestioneDipendenti.Model.gestore_dipendenti import GestoreDipendenti


class MainTurni(QWidget):
    def __init__(self):
        super(MainTurni, self).__init__()
        self.cont_gestione_dip = None
        self.stacked = QStackedWidget()
        self.init_ui()
        self.show()

    def init_ui(self):
        gestore_dip = GestoreDipendenti()
        self.cont_gestione_dip = ContGestioneTurni(gestore_dip,self.stacked)
        self.stacked.addWidget(self.cont_gestione_dip.view)
        self.stacked.setCurrentWidget(self.cont_gestione_dip.view)

        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked)


app = QApplication(sys.argv)
mainWindow = MainTurni()
sys.exit(app.exec())
