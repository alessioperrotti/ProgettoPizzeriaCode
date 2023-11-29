import os

from PyQt6.QtGui import QPixmap, QIcon, QFont
from PyQt6.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QLabel, QPushButton, QFrame, QTableWidget, QHeaderView, \
    QHBoxLayout, QApplication
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg


class VistaStatistiche(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setStyleSheet("""
                  QPushButton{
                      background-color: "#ff776d";
                      color: "white";
                      text-align: center;
                      border-radius: 6px;
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
                      font-weight: bold;
                      background-color: lightgray;
                  }
                  QHeaderView:active {
                      background-color: gray;
                  }
              """)

    def settaFont(self, font: QFont, *args):
        for arg in args:
            arg.setFont(font)

    def crea_pulsante_back(self,dimensioni, directory):
        pulsante_back = QPushButton()
        cartella_principale = os.path.dirname(os.path.realpath(__file__))
        dir = os.path.abspath(os.path.join(cartella_principale, directory))

        img = QPixmap(dir)
        icon = img.scaledToWidth(dimensioni)
        icon = QIcon(icon)
        pulsante_back.setIcon(icon)
        pulsante_back.setIconSize(img.size())
        pulsante_back.setFixedSize(dimensioni, dimensioni)
        pulsante_back.setStyleSheet("""
                QPushButton{
                    background-color: rgba(0, 0, 0, 0);
                }
                QPushButton:hover{
                    background-color: "lightgray";
                }
                """)
        return pulsante_back

    def crea_tabella(self, righe, colonne, larghezza, altezza):
        tabella = QTableWidget()
        tabella.setRowCount(righe)
        tabella.setColumnCount(colonne)
        header = tabella.horizontalHeader()
        header_font = QFont("Roboto", 10)
        header_font.setBold(True)
        header.setFont(header_font)
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        tabella.verticalHeader().setVisible(False)
        tabella.setFixedSize(larghezza, altezza)
        return tabella

    def initUI(self):
        label = QLabel("<b>Statistiche<\b>")
        self.pulsante_back = self.crea_pulsante_back(35, "png/back.png")
        label1 = QLabel("Ricavo netto mensile medio:")
        frame1 = QFrame()
        self.ricavo_netto = QLabel("€ 0")
        label2 = QLabel("Prodotti piu venduti:",parent=frame1)
        self.tabella = self.crea_tabella(4, 4, 350, 170)

        self.settaFont(QFont("Roboto", 26), label)

        self.settaFont(QFont("Roboto", 18), label1, label2, self.ricavo_netto)
        self.grid_layout = QGridLayout()
        layout = QVBoxLayout()
        l1 = QHBoxLayout()
        l2 = QVBoxLayout()


        self.grafico2 = FigureCanvasQTAgg(fig)



        l1.addWidget(label1)
        l1.addWidget(frame1)
        l1.addStretch()
        l2.addWidget(label2)
        l2.addWidget(self.tabella)




        self.grid_layout.addLayout(l1,0,0)
        self.grid_layout.addLayout(l2,1,0)







        layout.addWidget(label)
        layout.addStretch()
        layout.addLayout(self.grid_layout)
        layout.addStretch()
        layout.addWidget(self.pulsante_back)

        layout.setContentsMargins(10,10,10,10)
        layout.setContentsMargins(40,40,40,40)

        self.setFixedSize(994, 637)
        self.setLayout(layout)


if "__main__" == __name__:
    app = QApplication([])
    window = VistaStatistiche()
    window.show()
    app.exec()

