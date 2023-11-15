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
    tabella.setFixedSize(larghezza, altezza)
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


class TestVideo(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.show()

    def init_ui(self):
        self.setWindowTitle("Gestionale Pizzeria")
        title = QLabel("Gestione Dipendenti")
        title.setFont(label_font_tit)

        layout = QVBoxLayout()
        layout_orizzontale = QHBoxLayout()
        layout_pulsanti = QVBoxLayout()

        pulsante_mostra = QPushButton("Mostra info\ndipendente")
        pulsante_mostra.setFixedSize(147, 49)
        pulsante_modifica = QPushButton("Modifica\ndipendente")
        pulsante_modifica.setFixedSize(147, 49)
        pulsante_aggiungi = QPushButton("Aggiungi\nnuovo dipendente")
        pulsante_aggiungi.setFixedSize(147, 49)
        pulsante_elimina = QPushButton("Elimina\ndipendente")
        pulsante_elimina.setFixedSize(147, 49)

        # Pulsante Back
        pulsante_back = crea_pulsante_back(35,"png/back.png")

        # Tabella
        tab = crea_tabella(18, 2, 481, 404)
        tab.setHorizontalHeaderLabels(["NOME", "RUOLO"])
        tab.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        tab.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

        layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignTop)

        layout_orizzontale.addWidget(tab, alignment=Qt.AlignmentFlag.AlignLeft)
        layout_orizzontale.addLayout(layout_pulsanti)

        # Sistemo i Pulsanti
        layout_pulsanti.addStretch()
        layout_pulsanti.addWidget(pulsante_mostra, alignment=Qt.AlignmentFlag.AlignCenter)
        layout_pulsanti.addSpacing(10)
        layout_pulsanti.addWidget(pulsante_modifica, alignment=Qt.AlignmentFlag.AlignCenter)
        layout_pulsanti.addSpacing(10)
        layout_pulsanti.addWidget(pulsante_aggiungi, alignment=Qt.AlignmentFlag.AlignCenter)
        layout_pulsanti.addSpacing(10)
        layout_pulsanti.addWidget(pulsante_elimina, alignment=Qt.AlignmentFlag.AlignCenter)
        layout_pulsanti.addStretch()

        layout.addLayout(layout_orizzontale)
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
""")
window = TestVideo()
window.show()
sys.exit(app.exec())
