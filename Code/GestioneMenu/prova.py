import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QStackedWidget, QWidget, QVBoxLayout
from Code.GestioneMenu.Controller.gestione_menu_cont import ContGestioneMenu
from Code.GestioneMenu.View.gestione_menu_view import VistaGestioneMenu
from Code.GestioneMenu.Model.gestore_menu import GestoreMenu

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.stacked = QStackedWidget()
        self.init_ui()
        self.show()


    def init_ui(self):
        gestore_menu = GestoreMenu()
        self.cont_gestione_menu = ContGestioneMenu(VistaGestioneMenu(), gestore_menu)
        self.stacked.addWidget(self.cont_gestione_menu.view)
        self.stacked.setCurrentWidget(self.cont_gestione_menu.view)

        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked)


app = QApplication(sys.argv)
mainWindow = MainWindow()

sys.exit(app.exec())



