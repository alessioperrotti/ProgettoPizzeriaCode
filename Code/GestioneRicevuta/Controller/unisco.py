import sys
from PyQt6.QtWidgets import QApplication, QWidget, QStackedWidget, QPushButton, QVBoxLayout
from Code.GestioneRicevuta.Controller.cont_vista_gestione_ricevute import ContVistaGestioneRicevute
from Code.GestioneRicevuta.Controller.cont_vista_inserisci_ricevuta import ContVistaInserisciRicevuta
from Code.GestioneRicevuta.Model.gestore_ricevuta import GestoreRicevuta
from Code.GestioneRicevuta.Model.ricevuta import Ricevuta


class MainWindow(QWidget):
    def __init__(self, app):
        super(MainWindow, self).__init__()
        self.stacked = QStackedWidget()
        self.init_ui()
        self.show()


    def init_ui(self):
        gestore_ric = GestoreRicevuta()
        ric1 = Ricevuta(1,3,None,"Andrea",3,"esempio1")
        ric2 = Ricevuta(1,3,None,"Alessio",3,"esempio1")

        gestore_ric.aggiungi_ricevuta(1,3,None,"Andrea",15,"esempio1")
        gestore_ric.aggiungi_ricevuta(1,3,None,"Ale",12,"esempio1")

        self.cont_inserisci_ric = ContVistaInserisciRicevuta(gestore_ric)
        self.cont_gestione_ric = ContVistaGestioneRicevute(gestore_ric, self.stacked, self.cont_inserisci_ric)
        self.stacked.addWidget(self.cont_gestione_ric.view)
        self.stacked.setCurrentWidget(self.cont_gestione_ric.view)

        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow(app)

    sys.exit(app.exec())
