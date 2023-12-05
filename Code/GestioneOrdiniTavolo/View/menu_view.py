import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont, QPixmap
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
        contenitore.setMinimumSize(576, 0)
        contenitore.setLayout(vbox_centrale)
        contenitore.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        contenitore.setContentsMargins(20, 0, 20, 0)
        self.label_antipasti = QLabel("<b>Antipasti</b>")
        self.label_pizze = QLabel("<b>Pizze</b>")
        self.label_softdrinks = QLabel("<b>Soft Drinks</b>")
        self.label_birre = QLabel("<b>Birre</b>")

        labels_categorie = [self.label_antipasti, self.label_pizze,
                         self.label_softdrinks,self.label_birre]

        for x in labels_categorie:
            x.setFixedSize(370, 37)
            x.setFont(QFont("Roboto", 28))

        self.grid_antipasti = QGridLayout()
        self.grid_antipasti.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.grid_pizze = QGridLayout()
        self.grid_pizze.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.grid_softdrinks = QGridLayout()
        self.grid_softdrinks.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.grid_birre = QGridLayout()
        self.grid_birre.setAlignment(Qt.AlignmentFlag.AlignLeft)

        vbox_centrale.addWidget(self.label_antipasti, alignment=Qt.AlignmentFlag.AlignTop)
        vbox_centrale.addLayout(self.grid_antipasti)
        vbox_centrale.addSpacerItem(QSpacerItem(576, 60))
        vbox_centrale.addWidget(self.label_pizze, alignment=Qt.AlignmentFlag.AlignTop)
        vbox_centrale.addLayout(self.grid_pizze)
        vbox_centrale.addSpacerItem(QSpacerItem(576, 60))
        vbox_centrale.addWidget(self.label_softdrinks, alignment=Qt.AlignmentFlag.AlignTop)
        vbox_centrale.addLayout(self.grid_softdrinks)
        vbox_centrale.addSpacerItem(QSpacerItem(576, 60))
        vbox_centrale.addWidget(self.label_birre, alignment=Qt.AlignmentFlag.AlignTop)
        vbox_centrale.addLayout(self.grid_birre)
        vbox_centrale.addSpacerItem(QSpacerItem(576, 60))

        self.scroll_area.setWidget(contenitore)

        label_recap = QLabel("<b>Recap Ordine</b>")
        label_recap.setFixedSize(225, 37)
        label_recap.setFont(QFont("Roboto", 28))

        vbox_destra.addWidget(label_recap)

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

    def __init__(self, nome_prodotto, percorso_immagine):
        super().__init__()
        self.nome_prodotto = nome_prodotto
        self.percorso_immagine = percorso_immagine
        self.setObjectName("BoxProdotto")
        self.initUI()
        self.pulsante_meno.clicked.connect(self.decremento)
        self.pulsante_piu.clicked.connect(self.incremento)

    def initUI(self):
        self.setFixedSize(147, 204)
        main_layout = QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        upframe = QFrame()
        upframe.setFixedSize(147, 40)
        upframe.setStyleSheet(".QFrame {border: 1px solid black; border-radius: 3px; background-color: #FFFFFF;}")
        nome_layout = QVBoxLayout(upframe)
        nome_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_nome = QLabel(self.nome_prodotto, upframe)
        self.label_nome.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_nome.setFont(QFont("Roboto", 12))
        nome_layout.addWidget(self.label_nome)
        main_layout.addWidget(upframe)


        frame_immagine = QFrame()
        frame_immagine.setStyleSheet(".QFrame {border: 1px solid black; border-radius: 0px; background-color: #FFFFFF}")
        layout_immagine = QVBoxLayout(frame_immagine)

        image_label = QLabel()
        pixmap = QPixmap(self.percorso_immagine)
        image_label.setPixmap(pixmap.scaled(75, 75, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_immagine.addWidget(image_label, Qt.AlignmentFlag.AlignCenter)
        layout_immagine.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        layout_immagine.setSpacing(0)
        main_layout.addWidget(frame_immagine)

        downframe = QFrame()
        downframe.setFixedSize(147, 40)
        downframe.setStyleSheet(".QFrame {border: 1px solid black; border-radius: 3px; background-color: #ff776d;}")
        downframe_layout = QHBoxLayout()
        self.pulsante_meno = QPushButton("-")
        self.pulsante_meno.setFixedSize(20, 20)
        self.pulsante_meno.setStyleSheet("""
                QPushButton {
                    background-color: #ff776d;
                    color: black;
                    text-align: center;
                    border-radius: 6px;
                    border-color: white;
                    font-family: Roboto;
                }
                QPushButton:hover {
                    background-color: #ff776d;
                    font-size: 20px;
                }
            """)
        self.pulsante_meno.setFont(QFont("Roboto", 20))
        self.pulsante_piu = QPushButton("+")
        self.pulsante_piu.setFixedSize(20, 20)
        self.pulsante_piu.setStyleSheet("""
                QPushButton {
                    background-color: #ff776d;
                    color: black;
                    text-align: center;
                    border-radius: 6px;
                    border-color: white;
                    font-family: Roboto;
                }
                QPushButton:hover {
                    background-color: #ff776d;
                    font-size: 20px;
                }
            """)
        self.pulsante_piu.setFont(QFont("Roboto", 20))
        self.label_quantita = QLabel("0")
        self.label_quantita.setFont(QFont("Roboto", 18))
        downframe_layout.addWidget(self.pulsante_meno)
        downframe_layout.addWidget(self.label_quantita, alignment=Qt.AlignmentFlag.AlignCenter)
        downframe_layout.addWidget(self.pulsante_piu)
        downframe.setLayout(downframe_layout)

        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(downframe)

    def incremento(self):

        qta = int(self.label_quantita.text())
        self.label_quantita.setText(str(qta+1))

    def decremento(self):

        qta = int(self.label_quantita.text())
        if qta > 0:
            self.label_quantita.setText(str(qta-1))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    #window = BoxProdotto("bla", "bla")
    window = VistaMenu()
    window.show()
    sys.exit(app.exec())

