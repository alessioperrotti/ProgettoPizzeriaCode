#!/usr/bin/python

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout, QApplication, QSpacerItem,
                             QSizePolicy, QFrame, QHBoxLayout, QLineEdit)

label_font = QFont("Roboto", 24)
label_font_tit = QFont("Roboto", 40, weight=50)
label_font_piccolo = QFont("Roboto", 14)


def crea_pulsante(directory):
    pulsante = QPushButton()
    layout = QHBoxLayout()
    layout.addStretch()
    layout.addWidget(crea_immagine(directory, 35))
    layout.addStretch()
    pulsante.setLayout(layout)
    pulsante.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
    pulsante.setMaximumWidth(80)


    pulsante.setStyleSheet(
        ".QPushButton {background-color: #ff1605; border: 2px solid black; border-radius: 10px; padding: 3px}")
    return pulsante

def crea_immagine(directory, dimensione):
    label_foto = QLabel()
    pixmap = QPixmap(directory)
    scaled_pixmap = pixmap.scaled(dimensione, dimensione, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
    label_foto.setPixmap(scaled_pixmap)
    return label_foto


class VistaInserisciTavolo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Definizione oggetti
        frame = QFrame()
        frame.setFixedSize(350, 250)
        frame.setStyleSheet(".QFrame {border: 2px solid black; border-radius: 10px; padding: 40 30 40 30 px;background-color: #fcafa9}")
        label1 = QLabel("INSERISCI IL NUMERO")
        label1.setFont(label_font_piccolo)
        label2 = QLabel("DEL TAVOLO")
        label2.setFont(label_font_piccolo)

        campo = QLineEdit()
        campo.setStyleSheet("Border: 1px solid black; border-radius: 2px")
        campo.setFont(label_font)
        campo.setFixedWidth(115)


        pulsante = crea_pulsante("png/check.png")






        # Definizione Layout
        layout_princ = QVBoxLayout()
        layout = QVBoxLayout()
        layout_orizz= QHBoxLayout()

        # Inserimento Item nel Layout
        layout_orizz.addWidget(campo)
        layout_orizz.addWidget(pulsante)

        layout.addWidget(label1, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label2,alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addSpacing(10)

        layout.addLayout(layout_orizz)

        frame.setLayout(layout)

        layout_princ.addWidget(frame, alignment=Qt.AlignmentFlag.AlignCenter)


        self.setFixedSize(994, 637)
        self.setLayout(layout_princ)


def main():
    app = QApplication(sys.argv)
    ex = VistaInserisciTavolo()
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
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
