import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QStackedWidget, QWidget, QVBoxLayout
from Code.GestionePrenotazioni.Controller.cont_gestione_prenotazioni import ContGestionePrenotazioni
from Code.GestionePrenotazioni.View.vista_gestione_prenotazioni import VistaGestionePrenotazioni
from Code.GestionePrenotazioni.Model.gestore_prenotazioni import GestorePrenotazioni


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.stacked = QStackedWidget()
        self.init_ui()
        self.show()

    def init_ui(self):
        gestore_prenotazioni = GestorePrenotazioni()
        self.cont_gestione_prenotazioni = ContGestionePrenotazioni(gestore_prenotazioni, VistaGestionePrenotazioni())
        self.stacked.addWidget(self.cont_gestione_prenotazioni.view)
        self.stacked.setCurrentWidget(self.cont_gestione_prenotazioni.view)

        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked)


app = QApplication(sys.argv)
mainWindow = MainWindow()
sys.exit(app.exec())
