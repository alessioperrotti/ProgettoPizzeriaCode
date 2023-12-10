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
    #pulsante.setStyleSheet("background-color: #ff776d; border: 2px solid black; border-radius: 10px; padding: 10px")
    return pulsante


class VistaLogin(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

        self.setStyleSheet("""
           QPushButton{
               background-color: "#ff776d";
               color: "white";
               text-align: center;
               border-radius: 6px;
               font-size: 24px
           }
           QPushButton:hover{
               background-color: "red";
               font-size: 24px;
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
        # Definizione oggetti

        self.label = QLabel("Benvenuti!")
        self.label.setFont(label_font_tit)
        spazio_verticale = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        spazio_tra_pulsanti = QSpacerItem(20, 20)
        self.pulsante_admin = crea_pulsante("Accedi al sistema")
        self.pulsante_admin.setFixedSize(360, 80)
        self.pulsante_cliente = crea_pulsante("Accedi come cliente")
        self.pulsante_cliente.setFixedSize(360, 80)

        # Definizione Layout
        layout = QVBoxLayout()
        # Inserimento Item nel Layout
        layout.addItem(spazio_verticale)
        layout.addWidget(self.label, alignment=Qt.AlignmentFlag.AlignCenter)

        layout.addSpacerItem(spazio_tra_pulsanti)
        layout.addWidget(self.pulsante_admin, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addSpacerItem(spazio_tra_pulsanti)
        layout.addWidget(self.pulsante_cliente, alignment=Qt.AlignmentFlag.AlignCenter)
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
