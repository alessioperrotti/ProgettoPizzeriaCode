import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap, QIcon
from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout, QApplication, QSizePolicy, QHBoxLayout,
                             QGridLayout, QTableWidget, QHeaderView, QSpacerItem, QLineEdit, QTableWidgetItem,
                             QScrollBar, QScrollArea, QAbstractItemView)

# Font
label_font = QFont("Roboto", 24)
label_font_tit = QFont("Roboto", 32, weight=50)
label_font_piccolo = QFont("Roboto", 10)
header_font = QFont("Roboto", 10)
header_font.setBold(True)


def crea_tabella(righe, colonne, larghezza, altezza):
    tabella = QTableWidget()
    tabella.setRowCount(righe)
    tabella.setColumnCount(colonne)
    header = tabella.horizontalHeader()
    header.setFont(header_font)
    header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    tabella.verticalHeader().setVisible(False)
    tabella.setFixedSize(larghezza, altezza)
    return tabella



class VistaGestioneRicevute(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()
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

    def init_ui(self):
        self.setWindowTitle("Gestionale Pizzeria")
        title = QLabel("Conto Tavolo n.")
        title.setFont(label_font_tit)

        layout = QVBoxLayout()
        layout_orizzontale = QHBoxLayout()
        layout_pulsanti = QVBoxLayout()


        self.pulsante_mostra = QPushButton("Mostra info\nricevute")
        self.pulsante_mostra.setFixedSize(147, 49)
        self.pulsante_inserisci = QPushButton("Inserisci\nricevuta")
        self.pulsante_inserisci.setFixedSize(147, 49)
        self.pulsante_elimina = QPushButton("Elimina\nricevuta")
        self.pulsante_elimina.setFixedSize(147, 49)

        #self.pulsante_inserisci.clicked.connect(lambda : self.pulsante_inserisci.setText("O"))
        # Pulsante Back


        # Tabella
        self.tab = crea_tabella(18, 3, 481, 404)
        self.tab.setHorizontalHeaderLabels(["ACQUIRENTE", "NUMERO", "DATA"])
        self.tab.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tab.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

        layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignTop)

        layout_orizzontale.addWidget(self.tab, alignment=Qt.AlignmentFlag.AlignLeft)
        layout_orizzontale.addLayout(layout_pulsanti)

        # Sistemo i Pulsanti
        layout_pulsanti.addStretch()
        layout_pulsanti.addWidget(self.pulsante_mostra, alignment=Qt.AlignmentFlag.AlignCenter)
        layout_pulsanti.addSpacing(10)
        layout_pulsanti.addWidget(self.pulsante_inserisci, alignment=Qt.AlignmentFlag.AlignCenter)
        layout_pulsanti.addSpacing(10)
        layout_pulsanti.addWidget(self.pulsante_elimina, alignment=Qt.AlignmentFlag.AlignCenter)
        layout_pulsanti.addStretch()

        layout.addLayout(layout_orizzontale)


        layout.setContentsMargins(30, 20, 10, 20)
        self.setFixedSize(756, 637)
        self.setLayout(layout)
        self.pulsante_inserisci.setFocus()






if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VistaGestioneRicevute()
    window.show()
    sys.exit(app.exec())
