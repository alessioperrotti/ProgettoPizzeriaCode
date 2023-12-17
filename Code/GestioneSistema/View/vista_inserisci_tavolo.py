#!/usr/bin/python
import os
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap, QIcon
from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout, QApplication, QSpacerItem,
                             QSizePolicy, QFrame, QHBoxLayout, QLineEdit)

label_font = QFont("Roboto", 24)
label_font_tit = QFont("Roboto", 40, weight=50)
label_font_piccolo = QFont("Roboto", 14)

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
                background-color: rgba(0,0,0,0);
            }
            QPushButton:hover{
                background-color: "lightgray";
            }
            """)
    return pulsante_back


def crea_pulsante(directory):
    pulsante = QPushButton()
    layout = QHBoxLayout()
    layout.addStretch()
    layout.addWidget(crea_immagine(directory, 35))
    layout.addStretch()
    pulsante.setLayout(layout)
    pulsante.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
    pulsante.setMaximumWidth(80)


    return pulsante

def crea_immagine(directory, dimensione):
    label_foto = QLabel()
    cartella_principale = os.path.dirname(os.path.realpath(__file__))
    dir = os.path.abspath(os.path.join(cartella_principale, directory))

    pixmap = QPixmap(dir)

    scaled_pixmap = pixmap.scaled(dimensione, dimensione, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
    label_foto.setPixmap(scaled_pixmap)
    return label_foto


class VistaInserisciTavolo(QWidget):
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
        """)

    def init_ui(self):
        # Definizione oggetti
        frame = QFrame()
        frame.setFixedSize(350, 250)
        frame.setStyleSheet(".QFrame {border: 2px solid black; border-radius: 10px; padding: 40 30 40 30 px;background-color: #dddddd}")
        self.label1 = QLabel("INSERISCI IL NUMERO")
        self.label1.setFont(label_font_piccolo)
        self.label2 = QLabel("DEL TAVOLO")
        self.label2.setFont(label_font_piccolo)

        self.campo = QLineEdit()
        self.campo.setStyleSheet("Border: 1px solid black; border-radius: 2px")
        self.campo.setFont(label_font)
        self.campo.setFixedWidth(115)


        self.pulsante = crea_pulsante("png/check.png")


        self.pulsante_back = crea_pulsante_back(35, "png/back.png")



        # Definizione Layout
        layout_princ = QVBoxLayout()
        layout = QVBoxLayout()
        layout_orizz= QHBoxLayout()

        # Inserimento Item nel Layout
        layout_orizz.addWidget(self.campo)
        layout_orizz.addWidget(self.pulsante)

        layout.addWidget(self.label1, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label2,alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addSpacing(10)

        layout.addLayout(layout_orizz)

        frame.setLayout(layout)
        layout_princ.addSpacing(20)
        layout_princ.addStretch()
        layout_princ.addWidget(frame, alignment=Qt.AlignmentFlag.AlignCenter)
        layout_princ.addStretch()
        layout_princ.addWidget(self.pulsante_back, alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignBottom)
        layout_princ.addSpacing(20)
        layout_princ.setContentsMargins(20,20,20,10)

        self.setFixedSize(994, 637)
        self.setLayout(layout_princ)


def main():
    app = QApplication(sys.argv)
    ex = VistaInserisciTavolo()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
