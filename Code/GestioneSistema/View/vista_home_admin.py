#!/usr/bin/python
import os
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout, QApplication, QSizePolicy, QHBoxLayout,
                             QGridLayout, QTableWidget, QHeaderView)

label_font = QFont("Roboto", 24)
label_font_tit = QFont("Roboto", 32, weight=50)
label_font_piccolo = QFont("Roboto", 14)


def crea_pulsante(nome, directory):
    pulsante = QPushButton()
    label = QLabel(nome)
    label.setFont(label_font_piccolo)
    label.setStyleSheet("""QLabel{color: "white";}""")
    layout = QHBoxLayout()
    layout.addStretch()
    layout.addWidget(crea_immagine(directory, 50))
    layout.addWidget(label)
    layout.addStretch()
    pulsante.setLayout(layout)
    pulsante.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
    # pulsante.setStyleSheet("""
    #     QPushButton {
    #         color : "white"
    #         background-color: #ff776d;
    #         border-radius: 6px;
    #         }
    #    """)
    pulsante.setFixedSize(230, 100)
    return pulsante


def crea_immagine(directory, dimensione):
    label_foto = QLabel()

    cartella_principale = os.path.dirname(os.path.realpath(__file__))
    dir = os.path.abspath(os.path.join(cartella_principale, directory))


    pixmap = QPixmap(dir)
    scaled_pixmap = pixmap.scaled(dimensione, dimensione, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
    label_foto.setPixmap(scaled_pixmap)
    return label_foto



class VistaHomeAdmin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.setStyleSheet("""
            QPushButton{
                background-color: "#ff776d";
                color: "white";
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

    def initUi(self):
        # definizione oggetti
        label = QLabel("ACCESSO: Admin")
        label.setFont(label_font_tit)

        self.puls_stats = crea_pulsante("Statistiche", "png_icone/stats.png")
        self.puls_mag = crea_pulsante("Magazzino", "png_icone/magazzino.png")
        self.puls_dip = crea_pulsante("Dipendenti", "png_icone/dipendenti.png")
        self.puls_tur = crea_pulsante("Turni", "png_icone/turni.png")
        self.puls_men = crea_pulsante("Modifica Menu", "png_icone/menu.png")
        self.puls_pre = crea_pulsante("Prenotazioni", "png_icone/prenotazioni.png")
        self.puls_ric = crea_pulsante("Ricevute", "png_icone/ricevute.png")


       # back = crea_immagine("png/back.png", 35)

        # definizione layout
        layout = QVBoxLayout()
        griglia = QGridLayout()
        layout_centrale = QHBoxLayout()
        layout_orizzontale = QHBoxLayout()

        # inserimento oggetti nei layout
        layout_centrale.addStretch()
        layout_centrale.addLayout(griglia)
        layout_centrale.addStretch()


        griglia.addWidget(self.puls_stats, 1, 1)
        griglia.addWidget(self.puls_mag, 1, 2)
        griglia.addWidget(self.puls_dip, 2, 1)
        griglia.addWidget(self.puls_tur, 2, 2)
        griglia.addWidget(self.puls_men, 3, 1)
        griglia.addWidget(self.puls_pre, 3, 2)
        griglia.addWidget(self.puls_ric, 4, 1, 1, 2, alignment=Qt.AlignmentFlag.AlignCenter)


        layout.addSpacing(10)
        layout.addWidget(label)
        layout.addStretch()
        layout.addLayout(layout_centrale)
        layout.addSpacing(10)
   
        layout.addSpacing(10)

        layout_orizzontale.addSpacing(20)
        layout_orizzontale.addLayout(layout)
        layout_orizzontale.addSpacing(20)

        self.setFixedSize(756, 637)
        self.setContentsMargins(0,0,0,50)
        self.setLayout(layout_orizzontale)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VistaHomeAdmin()
    window.show()
    sys.exit(app.exec())
