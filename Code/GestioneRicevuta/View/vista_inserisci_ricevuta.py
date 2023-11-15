#!/usr/bin/python

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout, QApplication, QSpacerItem,
                             QSizePolicy, QHBoxLayout, QFrame, QLineEdit, QTableWidget, QHeaderView, QAbstractItemView)

label_font = QFont("Roboto", 24)
label_font_tit = QFont("Roboto", 32, weight=50)
label_font_piccolo = QFont("Roboto", 10)
header_font = QFont("Roboto", 10)
header_font.setBold(True)


def Pulsante(nome):
    pulsante = QPushButton(nome)
    pulsante.setFont(label_font)
    pulsante.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
   # pulsante.setStyleSheet("background-color: #ff776d; border: 2px solid black; border-radius: 10px; padding: 10px")
    return pulsante

def crea_tabella(righe, colonne, larghezza, altezza):
    tabella = QTableWidget()
    tabella.setRowCount(righe)
    tabella.setColumnCount(colonne)
    header = tabella.horizontalHeader()
    # header.setFont(header_font)
    header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    tabella.verticalHeader().setVisible(False)
    tabella.setFixedSize(larghezza, altezza)
    tabella.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
    tabella.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

    return tabella



class VistaInserisciRicevuta(QWidget):
    def __init__(self):
        super().__init__()
        self.ricerca = None
        self.tabella = None
        self.pulsante1 = None
        self.initUi()

    def initUi(self):
        # Definizione oggetti

        label_titolo = QLabel("<b>Inserimento nuova ricevuta</b>")
        label_titolo.setFont(label_font)
        label_titolo.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        frame1 = QFrame()
        frame1.setFrameShape(QFrame.Shape.HLine)

        self.ricerca = QLineEdit()
        self.ricerca.setPlaceholderText("Cerca numero tavolo")
        self.ricerca.setFont(label_font_piccolo)
        self.ricerca.setFixedWidth(340)
        self.ricerca.setStyleSheet("border: 1px solid black; padding: 3px")

        self.tabella = crea_tabella(8,2, 340, 115)
        self.tabella.setHorizontalHeaderLabels(["TAVOLO", "NUMERO ORDINI"])

        self.tabella.setFont(label_font_piccolo)

        self.pulsante1 = Pulsante("Mostra Tavolo selezionato")
        self.pulsante1.setFont(label_font_piccolo)
        self.pulsante1.setFixedHeight(70)

        label_nome = QLabel("Nome acquirente")
        label_nome.setFont(label_font_piccolo)

        ins_nome = QLineEdit()
        ins_nome.setFont(label_font_piccolo)
        ins_nome.setFixedWidth(340)
        ins_nome.setStyleSheet("border: 1px solid black; padding: 3px")

        self.pulsante2 = Pulsante("Conferma inserimento")
        pulsante3 = Pulsante("Stampa Ricevuta")
        self.pulsante2.setFont(label_font_piccolo)
        pulsante3.setFont(label_font_piccolo)
        self.pulsante2.setFixedHeight(70)
        pulsante3.setFixedHeight(70)

        # Definizione layout
        layout = QVBoxLayout()
        layout_tabella_e_tavolo = QHBoxLayout()
        layout_tasti = QHBoxLayout()

        # Inserimento oggetti nei layout

        layout_tabella_e_tavolo.addWidget(self.tabella)
        layout_tabella_e_tavolo.addSpacerItem(QSpacerItem(30, 30))
        layout_tabella_e_tavolo.addWidget(self.pulsante1)
        layout_tabella_e_tavolo.addSpacerItem(QSpacerItem(30, 30))

        layout_tasti.addSpacerItem(QSpacerItem(140, 1))
        layout_tasti.addWidget(self.pulsante2)
        layout_tasti.addWidget(pulsante3)
        layout_tasti.addSpacerItem(QSpacerItem(140, 1))

        layout.addWidget(label_titolo, alignment=Qt.AlignmentFlag.AlignTop)
        layout.addWidget(frame1, alignment=Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.ricerca, alignment=Qt.AlignmentFlag.AlignTop)
        layout.addSpacing(10)
        layout.addLayout(layout_tabella_e_tavolo)
        layout.addSpacerItem(QSpacerItem(1, 1, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding))
        layout.addWidget(label_nome)
        layout.addSpacing(10)
        layout.addWidget(ins_nome)
        layout.addSpacing(20)
        layout.addLayout(layout_tasti)
        layout.addSpacing(20)

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
            QHeaderView:section {
                    font-weight: bold;
                background-color: lightgray;
            }
            QHeaderView:active {
                background-color: gray;
            }
        """)
        self.setFixedSize(690, 474)
        self.setLayout(layout)
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = VistaInserisciRicevuta()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
