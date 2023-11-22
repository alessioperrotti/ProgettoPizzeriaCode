import sys
from PyQt6.QtWidgets import QApplication, QWidget, QStackedWidget, QVBoxLayout

from Code.GestioneDipendenti.Controller.cont_gestione_dipendenti import ContGestioneDipendenti
from Code.GestioneDipendenti.Model.gestore_dipendenti import GestoreDipendenti
from Code.GestioneDipendenti.View.vista_gestione_dipendenti import VistaGestioneDipendenti


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.cont_gestione_dip = None
        self.stacked = QStackedWidget()
        self.init_ui()
        self.show()

    def init_ui(self):
        gestore_dip = GestoreDipendenti()
        self.cont_gestione_dip = ContGestioneDipendenti(gestore_dip, VistaGestioneDipendenti())
        self.stacked.addWidget(self.cont_gestione_dip.view)
        self.stacked.setCurrentWidget(self.cont_gestione_dip.view)

        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked)


app = QApplication(sys.argv)
mainWindow = MainWindow()
sys.exit(app.exec())
