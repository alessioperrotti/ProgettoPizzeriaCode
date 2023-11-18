import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QStackedWidget, QWidget, QVBoxLayout
from Code.GestioneMagazzino.Controller.gestione_magazzino_cont import ContGestioneMagazzino
from Code.GestioneMagazzino.View.gestione_magazzino_view import VistaGestioneMagazzino
from Code.GestioneMagazzino.Model.gestore_magazzino import GestoreMagazzino

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.stacked = QStackedWidget()
        self.init_ui()
        self.show()


    def init_ui(self):
        gestore_mag = GestoreMagazzino()
        self.cont_gestione_mag = ContGestioneMagazzino(gestore_mag, VistaGestioneMagazzino())
        self.stacked.addWidget(self.cont_gestione_mag.view)
        self.stacked.setCurrentWidget(self.cont_gestione_mag.view)

        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()

    sys.exit(app.exec())



