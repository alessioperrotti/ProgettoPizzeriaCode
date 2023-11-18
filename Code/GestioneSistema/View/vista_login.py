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
    pulsante.setFont(label_font)
    pulsante.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
    pulsante.setStyleSheet("background-color: #ff776d; border: 2px solid black; border-radius: 10px; padding: 10px")
    return pulsante


class VistaLogin(QWidget):
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
        """)

    def initUI(self):
        # Definizione oggetti

        label = QLabel("Benvenuti!")
        label.setFont(label_font_tit)
        spazio_verticale = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        spazio_tra_pulsanti = QSpacerItem(20, 20)
        pulsante1 = crea_pulsante("Accedi al sistema")
        pulsante1.setFixedSize(360, 80)
        pulsante2 = crea_pulsante("Accedi come cliente")
        pulsante2.setFixedSize(360, 80)

        # Definizione Layout
        layout = QVBoxLayout()
        # Inserimento Item nel Layout
        layout.addItem(spazio_verticale)
        layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)

        layout.addSpacerItem(spazio_tra_pulsanti)
        layout.addWidget(pulsante1, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addSpacerItem(spazio_tra_pulsanti)
        layout.addWidget(pulsante2, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addItem(spazio_verticale)

        self.setFixedSize(994, 637)
        self.setLayout(layout)


def main():
    app = QApplication(sys.argv)
    ex = VistaLogin()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
