import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout, QApplication, QSizePolicy, QHBoxLayout,
                             QGridLayout, QTableWidget, QHeaderView, QSpacerItem, QLineEdit, QTableWidgetItem,
                             QScrollBar, QScrollArea)

label_font = QFont("Roboto", 24)
label_font_tit = QFont("Roboto", 32, weight=50)
label_font_piccolo = QFont("Roboto", 10)
header_font = QFont("Roboto", 10)


def crea_immagine(directory, dimensione):
    label_foto = QLabel()
    pixmap = QPixmap(directory)
    scaled_pixmap = pixmap.scaled(dimensione, dimensione, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
    label_foto.setPixmap(scaled_pixmap)
    return label_foto


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

        pulsante_modifica = QPushButton("Modifica")
        pulsante_modifica.setFixedSize(147, 49)
        pulsante_aggiungi = QPushButton("Aggiungi")
        pulsante_aggiungi.setFixedSize(147, 49)
        pulsante_elimina = QPushButton("Elimina")
        pulsante_elimina.setFixedSize(147, 49)
        back = crea_immagine("png/back.png", 35)

        tab = QTableWidget()
        tab.setRowCount(18)
        tab.setColumnCount(2)
        tab.setHorizontalHeaderLabels(["NOME", "RUOLO"])
        tab.setFixedSize(481, 404)

        layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignTop)

        layout_orizzontale.addWidget(tab, alignment=Qt.AlignmentFlag.AlignLeft)
        layout_orizzontale.addLayout(layout_pulsanti)
        # Sistemo i Pulsanti
        layout_pulsanti.addStretch()
        layout_pulsanti.addWidget(pulsante_modifica, alignment=Qt.AlignmentFlag.AlignCenter)
        layout_pulsanti.addSpacing(10)
        layout_pulsanti.addWidget(pulsante_aggiungi, alignment=Qt.AlignmentFlag.AlignCenter)
        layout_pulsanti.addSpacing(10)
        layout_pulsanti.addWidget(pulsante_elimina, alignment=Qt.AlignmentFlag.AlignCenter)
        layout_pulsanti.addStretch()

        layout.addLayout(layout_orizzontale)
        layout.addWidget(back)

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
