import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QStackedWidget


class Model:
    def __init__(self):
        self.data = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

class VistaGestioneRicevute(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.pulsante_mostrainfo = Pulsante("Mostra Info\nRicevuta")
        self.pulsante_inserisci = Pulsante("Inserisci\nRicevuta")
        self.pulsante_elimina = Pulsante("Elimina\nRicevuta")


    def initUi(self):
        # definizione oggetti
        label = QLabel("Gestione Ricevute")
        label.setFont(label_font)
        tabella = Tabella(3, 480, 400)
        tabella.setHorizontalHeaderLabels(["Acquirente", "Numero", "Data"])
        tabella.setFont(label_font_piccolo)

        self.pulsante_mostrainfo.setFont(label_font_piccolo)
        self.pulsante_inserisci.setFont(label_font_piccolo)
        self.pulsante_elimina.setFont(label_font_piccolo)
        png_back = QLabel()
        pixmap = QPixmap("png/back.png")
        scaled_pixmap = pixmap.scaled(35, 35, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
        png_back.setPixmap(scaled_pixmap)

        # definizione layout
        layout = QVBoxLayout()
        layout_tabella_pulsanti = QHBoxLayout()
        layout_pulsanti = QVBoxLayout()

        # inserimento oggetti nel layout
        layout_pulsanti.addSpacerItem(QSpacerItem(1, 130))
        layout_pulsanti.addWidget(self.pulsante_mostrainfo)
        layout_pulsanti.addWidget(self.pulsante_inserisci)
        layout_pulsanti.addWidget(self.pulsante_elimina)
        layout_pulsanti.addSpacerItem(QSpacerItem(1, 130))

        layout_tabella_pulsanti.addSpacerItem(QSpacerItem(30, 30))
        layout_tabella_pulsanti.addWidget(tabella)
        layout_tabella_pulsanti.addSpacerItem(QSpacerItem(40, 40))
        layout_tabella_pulsanti.addLayout(layout_pulsanti)
        layout_tabella_pulsanti.addSpacerItem(QSpacerItem(30, 30))

        layout.addSpacerItem(QSpacerItem(30, 30))
        layout.addWidget(label)
        # layout.addSpacerItem(QSpacerItem(20,20))
        layout.addLayout(layout_tabella_pulsanti)
        layout.addStretch()
        layout.addWidget(png_back, alignment=Qt.AlignmentFlag.AlignLeft)

        self.setFixedSize(756, 637)
        self.setLayout(layout)
        self.show()

class View1(QWidget):
    def __init__(self, controller):
        super().__init__()

        self.controller = controller

        layout = QVBoxLayout()
        self.label = QLabel("Schermata 1")
        layout.addWidget(self.label)

        button = QPushButton("Vai a Schermata 2")
        button.clicked.connect(self.controller.switch_to_view2)
        layout.addWidget(button)

        self.setLayout(layout)


class Controller1:
    def __init__(self, stacked_widget):
        self.model = Model()
        self.view = View1(self)
        self.stacked_widget = stacked_widget

    def switch_to_view2(self):
        self.stacked_widget.setCurrentIndex(1)


class View2(QWidget):
    def __init__(self, controller):
        super().__init__()

        self.controller = controller

        layout = QVBoxLayout()
        self.label = QLabel("Schermata 2")
        layout.addWidget(self.label)

        button = QPushButton("Vai a Schermata 1")
        button.clicked.connect(self.controller.switch_to_view1)
        layout.addWidget(button)

        self.setLayout(layout)


class Controller2:
    def __init__(self, stacked_widget):
        self.model = Model()
        self.view = View2(self)
        self.stacked_widget = stacked_widget

    def switch_to_view1(self):
        self.stacked_widget.setCurrentIndex(0)


class MainApp(QApplication):
    def __init__(self, sys_argv):
        super(MainApp, self).__init__(sys_argv)

        self.stacked_widget = QStackedWidget()

        self.controller1 = Controller1(self.stacked_widget)
        self.controller2 = Controller2(self.stacked_widget)

        self.stacked_widget.addWidget(self.controller1.view)
        self.stacked_widget.addWidget(self.controller2.view)

        self.stacked_widget.show()


if __name__ == '__main__':
    app = MainApp(sys.argv)
    sys.exit(app.exec_())
