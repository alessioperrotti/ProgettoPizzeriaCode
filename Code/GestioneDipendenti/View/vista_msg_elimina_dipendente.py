
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout, QApplication, QSpacerItem,
                             QSizePolicy, QHBoxLayout)

label_font = QFont("Roboto", 24)
label_font_tit = QFont("Roboto", 40, weight=50)
label_font_piccolo = QFont("Roboto", 13)


def crea_pulsante(nome):
    pulsante = QPushButton(nome)
    pulsante.setFont(label_font_piccolo)
    pulsante.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)
    pulsante.setStyleSheet("""
        QPushButton{
            color: white;
            background-color: #ff776d;
            border-radius: 6px;
        }
        QPushButton:hover{
            background-color: "red"
        }
    """)
    return pulsante


class VistaMsgEliminaDipendente(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Definizione oggetti
        label1 = QLabel("<b>Attenzione</b>")
        label1.setFont(label_font_piccolo)
        label2 = QLabel("Sei sicuro di voler eliminare\nil dipendente selezionato?")
        label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label2.setFont(label_font_piccolo)

        pulsante1 = crea_pulsante("Annulla")
        pulsante2 = crea_pulsante("Sono sicuro")


        # Definizione Layout
        layout = QVBoxLayout()
        layout_orizzontale = QHBoxLayout()

        # Inserimento Item nel Layout
        layout.addWidget(label1, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label2,alignment=Qt.AlignmentFlag.AlignCenter)

        layout.addSpacing(10)
        layout.addLayout(layout_orizzontale)
        layout_orizzontale.addWidget(pulsante1)
        layout_orizzontale.addWidget(pulsante2)

        self.setFixedSize(323, 147)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    vista = VistaMsgEliminaDipendente()
    vista.show()
    sys.exit(app.exec())