import sys

from PyQt6.QtWidgets import QWidget, QStackedWidget, QVBoxLayout, QApplication

from Code.GestioneDipendenti.Controller.cont_home_cameriere import ContHomeCameriere
from Code.GestioneDipendenti.Model.gestore_dipendenti import GestoreDipendenti


class MainTurni(QWidget):
    def __init__(self):
        super(MainTurni, self).__init__()
        self.cont_home_cam = None
        self.stacked = QStackedWidget()
        self.init_ui()
        self.show()

    def init_ui(self):
        gestore_dip = GestoreDipendenti()
        self.cont_home_cam = ContHomeCameriere(gestore_dip,self.stacked)
        self.stacked.addWidget(self.cont_home_cam.view)
        self.stacked.setCurrentWidget(self.cont_home_cam.view)

        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked)


app = QApplication(sys.argv)
mainWindow = MainTurni()
sys.exit(app.exec())