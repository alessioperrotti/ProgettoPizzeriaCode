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
    # header.setFont(header_font)
    header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
    tabella.verticalHeader().setVisible(False)
    tabella.setFixedSize(larghezza, altezza)
    tabella.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
    tabella.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
    return tabella


def crea_pulsante_back(dimensioni, directory):
    pulsante_back = QPushButton()
    img = QPixmap(directory)
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


class VistaVisualizzaPrenotazioni(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.show()

    def init_ui(self):
        self.setWindowTitle("Gestionale Pizzeria")
        title = QLabel("Prenotazioni")
        title.setFont(label_font_tit)

        layout = QVBoxLayout()
        layout_orizzontale = QHBoxLayout()
        layout_pulsanti = QVBoxLayout()


        # Pulsante Back
        pulsante_back = crea_pulsante_back(35,"png/back.png")

        # Campo di ricerca
        search_label = QLabel('Cerca:')
        search_label.setFont(label_font_piccolo)
        search_edit = QLineEdit()
        search_edit.setFixedWidth(336)

        # Tabella
        tab = crea_tabella(18, 6, 685, 402)
        tab.setHorizontalHeaderLabels(["NOME CLIENTE","TAVOLO","ORARIO","GIORNO","POSTI","CODICE"])


        layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignTop)
        layout.addSpacing(20)
        layout.addWidget(search_label)
        layout.addWidget(search_edit)

        layout_orizzontale.addWidget(tab, alignment=Qt.AlignmentFlag.AlignLeft)
        layout_orizzontale.addLayout(layout_pulsanti)

        layout.addLayout(layout_orizzontale)
        layout.addStretch()
        layout.addWidget(pulsante_back)

        layout.setContentsMargins(30, 20, 10, 20)
        self.setFixedSize(756, 637)
        self.setLayout(layout)


app = QApplication(sys.argv)

app.setStyleSheet("""
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
window = VistaVisualizzaPrenotazioni()
window.show()
sys.exit(app.exec())




