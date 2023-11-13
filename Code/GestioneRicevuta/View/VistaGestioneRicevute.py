#!/usr/bin/python

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout, QApplication, QSpacerItem,
                             QSizePolicy, QHBoxLayout, QTableWidget, QHeaderView)

label_font = QFont("Roboto", 24)
label_font_tit = QFont("Roboto", 40, weight=50)
label_font_piccolo = QFont("Roboto", 14)


def Pulsante(nome):
    pulsante = QPushButton(nome)
    pulsante.setFont(label_font)
    pulsante.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
    pulsante.setStyleSheet("background-color: #ff776d; border: 2px solid black; border-radius: 10px; padding: 10px")
    return pulsante


def Tabella(n_colonne, larghezza, altezza):
    tabella = QTableWidget()
    tabella.setStyleSheet("""
               QTableWidget {
                   background-color: white;
                   alternate-background-color: white;
                   selection-background-color: darkcyan;
                   border: 2px solid black;
                   border-radius: 5px;
               }

               QTableWidget::item {
                   padding: 5px;
                   border: 1px solid black;
               } 
               QHeaderView::section {
                   background-color: lightgray;
               }
           """)

    tabella.setColumnCount(n_colonne)

    header = tabella.horizontalHeader()
    header.setFont(label_font_piccolo)
    header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
    for i in range(1, n_colonne):
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
    tabella.setFixedWidth(larghezza)
    tabella.setFixedHeight(altezza)

    return tabella


class VistaGestioneRicevute(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.pulsante_mostrainfo = Pulsante("Mostra Info\nRicevuta")
        self.pulsante_inserisci = Pulsante("Inserisci\nRicevuta")
        self.pulsante_elimina = Pulsante("Elimina\nRicevuta")


    def initUi(self):
        # definizione oggetti
        label = QLabel("Gestione Ricevute")
        label.setFont(label_font)
        tabella = Tabella(3, 480, 400)
        tabella.setHorizontalHeaderLabels(["Acquirente", "Numero", "Data"])
        tabella.setFont(label_font_piccolo)

        self.pulsante_mostrainfo.setFont(label_font_piccolo)
        self.pulsante_inserisci.setFont(label_font_piccolo)
        self.pulsante_elimina.setFont(label_font_piccolo)
        png_back = QLabel()
        pixmap = QPixmap("png/back.png")
        scaled_pixmap = pixmap.scaled(35, 35, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
        png_back.setPixmap(scaled_pixmap)

        # definizione layout
        layout = QVBoxLayout()
        layout_tabella_pulsanti = QHBoxLayout()
        layout_pulsanti = QVBoxLayout()

        # inserimento oggetti nel layout
        layout_pulsanti.addSpacerItem(QSpacerItem(1, 130))
        layout_pulsanti.addWidget(self.pulsante_mostrainfo)
        layout_pulsanti.addWidget(self.pulsante_inserisci)
        layout_pulsanti.addWidget(self.pulsante_elimina)
        layout_pulsanti.addSpacerItem(QSpacerItem(1, 130))

        layout_tabella_pulsanti.addSpacerItem(QSpacerItem(30, 30))
        layout_tabella_pulsanti.addWidget(tabella)
        layout_tabella_pulsanti.addSpacerItem(QSpacerItem(40, 40))
        layout_tabella_pulsanti.addLayout(layout_pulsanti)
        layout_tabella_pulsanti.addSpacerItem(QSpacerItem(30, 30))

        layout.addSpacerItem(QSpacerItem(30, 30))
        layout.addWidget(label)
        # layout.addSpacerItem(QSpacerItem(20,20))
        layout.addLayout(layout_tabella_pulsanti)
        layout.addStretch()
        layout.addWidget(png_back, alignment=Qt.AlignmentFlag.AlignLeft)

        self.setFixedSize(756, 637)
        self.setLayout(layout)
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = VistaGestioneRicevute()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
