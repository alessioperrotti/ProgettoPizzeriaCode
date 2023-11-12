#!/usr/bin/python

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout, QApplication, QSpacerItem,
                             QSizePolicy)

label_font = QFont("Roboto", 24)
label_font_tit = QFont("Roboto", 40, weight=50)
label_font_piccolo = QFont("Roboto", 14)


def crea_pulsante(nome):
    pulsante = QPushButton(nome)
    pulsante.setFont(label_font_piccolo)
    pulsante.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)
    pulsante.setStyleSheet("background-color: #ff776d; border: 1px solid black;  padding: 10px")
    return pulsante


class VistaMessaggioErroreLogin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Definizione oggetti
        label1 = QLabel("<b>Errore</b>")
        label1.setFont(label_font_piccolo)
        label2 = QLabel("Credenziali errate.")
        label2.setFont(label_font_piccolo)
        label3 = QLabel("Riprova!")
        label3.setFont(label_font_piccolo)

        pulsante = crea_pulsante("OK")


        # Definizione Layout
        layout = QVBoxLayout()

        # Inserimento Item nel Layout
        layout.addWidget(label1, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label2,alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label3,alignment=Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(pulsante)


        self.setFixedSize(323, 147)
        self.setLayout(layout)

        self.show()


def main():
    app = QApplication(sys.argv)
    ex = VistaMessaggioErroreLogin()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
