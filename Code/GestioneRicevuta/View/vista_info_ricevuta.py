#!/usr/bin/python

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout, QApplication, QSpacerItem,
                             QSizePolicy, QHBoxLayout, QFrame, QLineEdit, QTableWidget, QHeaderView, QAbstractItemView,
                             QDialog, QGridLayout)

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



class VistaInserisciRicevuta(QDialog):
    def __init__(self):
        super().__init__()
        self.ricerca = None
        self.tabella = None
        self.pulsante_mostra = None
        self.initUi()

    def initUi(self):
        # Definizione oggetti

        label_titolo = QLabel("<b>Scheda dati ricevuta</b>")
        label_titolo.setFont(label_font)
        label_titolo.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        frame1 = QFrame()
        frame1.setFrameShape(QFrame.Shape.HLine)

        lab_num = QLabel("Numero:")
        lab_nom = QLabel("Nome acquirente:")
        lab_amm = QLabel("Ammontare lordo:")
        lab_data = QLabel("Data di emissione:")
        lab_ora = QLabel("Orario di emissione:")
        lab_lis = QLabel("Lista Prodotti:")

        self.lab_num_s = QLabel()
        self.lab_nom_s = QLabel()
        self.lab_amm_s = QLabel()
        self.lab_data_s = QLabel()
        self.lab_ora_s = QLabel()

        l1 = QHBoxLayout()
        l2 = QHBoxLayout()
        l3 = QHBoxLayout()
        l4 = QHBoxLayout()
        l5 = QHBoxLayout()


        l1.addWidget(lab_num)
        l1.addWidget(self.lab_num_s)
        l2.addWidget(lab_nom)
        l2.addWidget(self.lab_nom_s)
        l3.addWidget(lab_amm)
        l3.addWidget(self.lab_amm_s)
        l4.addWidget(lab_data)
        l4.addWidget(self.lab_data_s)
        l5.addWidget(lab_ora)
        l5.addWidget(self.lab_ora_s)



        lay = QVBoxLayout()

        layout = QGridLayout()
        layout.addLayout(l1,0,0)
        layout.addLayout(l2,1,0)
        layout.addLayout(l3,2,0)
        layout.addLayout(l4,0,1)
        layout.addLayout(l5,1,1)
        layout.addWidget(frame1, 3,0,2,1)


        lay.addWidget(label_titolo)
        #lay.addWidget(frame1)
        lay.addLayout(layout)
        lay.addWidget(lab_lis)

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
        self.setFixedSize(904, 626)
        layout.setContentsMargins(30, 20, 10, 20)
        self.setLayout(lay)



def main():
    app = QApplication(sys.argv)
    ex = VistaInserisciRicevuta()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
