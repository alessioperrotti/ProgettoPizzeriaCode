import sys

from View.VistaGestioneRicevute import VistaGestioneRicevute
from View.VistaInserisciRicevuta import VistaInserisciRicevuta
from PyQt6.QtWidgets import QStackedWidget, QApplication
class ControllerGestioneRicevute():
    def __init__(self, stacked_widget,sys_argv):
        self.view = VistaGestioneRicevute()
        self.stacked = stacked_widget
        self.view.pulsante_inserisci.clicked.connect(self.clicked_inserisci_ricevuta)
    def clicked_inserisci_ricevuta(self,sys_argv):
        self.stacked.setCurrentIndex(1)



class ControllerInserisciRicevuta():
    def __init__(self, stacked_widget):
        self.view = VistaInserisciRicevuta()
        self.stacked = stacked_widget
        self.view.pulsante1.clicked.connect(self.clicked_inserisci_ricevuta)


    def clicked_inserisci_ricevuta(self):
        self.stacked.setCurrentIndex(0)
        #self.view.show()
        pass


class MainApp(QApplication):
    def __init__(self,sys_argv):
        super(MainApp, self).__init__(sys_argv)
        self.stacked_widget = QStackedWidget()
        self.controller1 = ControllerGestioneRicevute(self.stacked_widget, sys_argv)
        self.controller2 = ControllerInserisciRicevuta(self.stacked_widget)
        self.stacked_widget.addWidget(self.controller1.view)
        self.stacked_widget.addWidget(self.controller2.view)
        self.stacked_widget.show()

if __name__ == '__main__':
    app = MainApp(sys.argv)
    sys.exit(app.exec())
