from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class VistaMenu(QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()
        self.setStyleSheet("""
                    QPushButton{
                        background-color: "#ff776d";
                        color: "white";
                        text-align: center;
                        border-radius: 6px;
                        font-family:Roboto;
                    }
                    QPushButton:hover{
                        background-color: "red";
                        font-size: 13px;
                    }
                    QTableWidget {
                        background-color: white;
                        alternate-background-color: white;
                        selection-background-color: darkcyan;
                        border: 2px solid grey;
                    }
                    QHeaderView:section {
                        background-color: lightgray;
                        font-weight: bold;
                    }
                    QHeaderView:active {
                        background-color: gray;
                    }
                """)


    def initUI(self):

        main_layout = QHBoxLayout(self)
        vbox_sinistra = QVBoxLayout()
        vbox_centrale = QVBoxLayout()
        vbox_destra = QVBoxLayout()

        self.pulsante_antipasti = QPushButton("Antipasti")
        self.pulsante_pizze = QPushButton("Pizze")
        self.pulsante_softdrinks = QPushButton("Soft Drinks")
        self.pulsante_birre = QPushButton("Birre")

        pulsanti_filtro = [self.pulsante_antipasti, self.pulsante_pizze,
                           self.pulsante_softdrinks, self.pulsante_birre]
        for x in pulsanti_filtro:
            x.setStyleSheet("""
                        QPushButton{
                            background-color: "white";
                            color: "black";
                            text-align: center;
                            border-radius: 6px;
                            border-color: "white"
                            font-family:Roboto;
                        }
                        
                        QPushButton:hover{
                            background-color: "D3D3D3";
                        }
                    """)
            x.setFont(QFont("Roboto", 24))
            x.setFixedSize(155, 52)
            vbox_sinistra.addWidget(x, alignment=Qt.AlignmentFlag.AlignVCenter)

        frame1 = QFrame()
        frame1.setFrameShape(QFrame.Shape.VLine)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        contenitore = QWidget()
        contenitore.setFixedSize(576, 637)
        contenitore.setLayout(vbox_centrale)
        contenitore.setContentsMargins(20, 10, 20, 0)
        label_antipasti = QLabel("<b>Antipasti</b>")
        label_pizze = QLabel("<b>Pizze</b>")
        label_softdrinks = QLabel("<b>Soft Drinks</b>")
        label_birre = QLabel("<b>Birre</b>")

        labels_categorie = [label_antipasti, label_pizze,
                         label_softdrinks,label_birre]

        for x in labels_categorie:
            x.setFixedSize(370, 37)
            x.setFont(QFont("Roboto", 28))

        self.grid_antipasti = QGridLayout()
        self.grid_pizze = QGridLayout()
        self.grid_softdrinks = QGridLayout()
        self.grid_birre = QGridLayout()

        vbox_centrale.addWidget(label_antipasti)
        vbox_centrale.addLayout(self.grid_antipasti)
        vbox_centrale.addWidget(label_pizze)
        vbox_centrale.addLayout(self.grid_pizze)
        vbox_centrale.addWidget(label_softdrinks)
        vbox_centrale.addLayout(self.grid_softdrinks)
        vbox_centrale.addWidget(label_birre)
        vbox_centrale.addLayout(self.grid_birre)

        self.scroll_area.setWidget(contenitore)

        

        self.pulsante_confermaordine = QPushButton("Conferma Ordine")
        self.pulsante_visualizzaconto = QPushButton("Visualizza Conto")
        self.pulsante_terminaservizio = QPushButton("Termina Servizio")

        pulsanti_dx = [self.pulsante_confermaordine, self.pulsante_visualizzaconto, self.pulsante_terminaservizio]

        for x in pulsanti_dx:
            x.setFixedSize(194, 48)
            vbox_destra.addWidget(x)

