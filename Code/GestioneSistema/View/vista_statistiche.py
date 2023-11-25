import os

from PyQt6.QtGui import QPixmap, QIcon, QFont
from PyQt6.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QLabel, QPushButton, QFrame, QTableWidget, QHeaderView


class VistaStatistiche(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def crea_pulsante_back(dimensioni, directory):
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
        label = QLabel("Statistiche")
        self.pulsante_back = self.crea_pulsante_back(35, "png/back.png")
        label1 = QLabel("Ricavo netto\nmensile medio:")
        frame1 = QFrame()
        self.ricavo_netto = QLabel("€ 0")
        label2 = QLabel("Prodotti piu venduti:")
        self.tabella = self.crea_tabella(4, 4, 350, 170)


        grid_layout = QGridLayout()
        layout = QVBoxLayout()

        grid_layout.

        layout.addWidget(label)
        layout.addLayout(grid_layout)
        layout.addWidget(self.pulsante_indietro)

        layout.setContentsMargins(10,10,10,10)
        layout.setContentsMargins(20,30,20,30)

        self.setFixedSize(994, 637)
        self.setLayout(layout)
        pass

