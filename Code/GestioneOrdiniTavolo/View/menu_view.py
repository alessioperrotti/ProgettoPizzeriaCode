import sys
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

        vbox_sinistra.addSpacerItem(QSpacerItem(180, 165))

        for x in pulsanti_filtro:
            x.setStyleSheet("""
                QPushButton {
                    background-color: #ececec;
                    color: black;
                    text-align: center;
                    border-radius: 6px;
                    border-color: white;
                    font-family: Roboto;
                }
                QPushButton:hover {
                    background-color: #D3D3D3;
                    font-size: 24px;
                }
            """)

            x.setFont(QFont("Roboto", 24))
            x.setFixedSize(155, 52)
            vbox_sinistra.addWidget(x, alignment=Qt.AlignmentFlag.AlignVCenter)

        vbox_sinistra.addSpacerItem(QSpacerItem(180, 175))

        frame1 = QFrame()
        frame1.setFrameShape(QFrame.Shape.VLine)

        frame2 = QFrame()
        frame2.setFrameShape(QFrame.Shape.VLine)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        contenitore = QWidget()
        contenitore.setFixedSize(576, 637)
        contenitore.setLayout(vbox_centrale)
        contenitore.setContentsMargins(20, 0, 20, 0)
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

        vbox_centrale.addWidget(label_antipasti, alignment=Qt.AlignmentFlag.AlignTop)
        vbox_centrale.addLayout(self.grid_antipasti)
        vbox_centrale.addWidget(label_pizze, alignment=Qt.AlignmentFlag.AlignTop)
        vbox_centrale.addLayout(self.grid_pizze)
        vbox_centrale.addWidget(label_softdrinks, alignment=Qt.AlignmentFlag.AlignTop)
        vbox_centrale.addLayout(self.grid_softdrinks)
        vbox_centrale.addWidget(label_birre, alignment=Qt.AlignmentFlag.AlignTop)
        vbox_centrale.addLayout(self.grid_birre)

        self.scroll_area.setWidget(contenitore)

        label_recap = QLabel("<b>Recap Ordine</b>")
        label_recap.setFixedSize(225, 37)
        label_recap.setFont(QFont("Roboto", 28))

        vbox_destra.addWidget(label_recap)

        #rettangolo_recap = QWidget()
        #rettangolo_recap.setFixedSize(194, 335)
        self.lista_recap = QListWidget()
        self.lista_recap.setFixedSize(194, 335)

        vbox_destra.addWidget(self.lista_recap)

        self.pulsante_confermaordine = QPushButton("Conferma Ordine")
        self.pulsante_visualizzaconto = QPushButton("Visualizza Conto")
        self.pulsante_terminaservizio = QPushButton("Termina Servizio")

        pulsanti_dx = [self.pulsante_confermaordine, self.pulsante_visualizzaconto, self.pulsante_terminaservizio]

        for x in pulsanti_dx:
            x.setFixedSize(194, 48)
            vbox_destra.addWidget(x)


        main_layout.addLayout(vbox_sinistra)
        main_layout.addWidget(frame1)
        main_layout.addWidget(self.scroll_area)
        main_layout.addWidget(frame2)
        main_layout.addLayout(vbox_destra)

        self.setLayout(main_layout)
        self.setFixedSize(994, 637)


class BoxProdotto(QWidget):

    def __init__(self, nome_prodotto):
        super().__init__()
        self.initUI()
        self.nome_prodotto = nome_prodotto

    def initUI(self):
        self.setFixedSize(147, 190)
        main_layout = QVBoxLayout(self)
        upframe = QFrame()
        upframe.setFixedSize(145, 40)
        upframe.setStyleSheet(".QFrame {border: 1px solid black; border-radius: 3px; background-color: #ececec")
        self.label_nome = QLabel("Prodotto", upframe)
        self.label_nome.setFont(QFont("Roboto", 17))
        main_layout.addWidget(upframe)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BoxProdotto()
    window.show()
    sys.exit(app.exec())

