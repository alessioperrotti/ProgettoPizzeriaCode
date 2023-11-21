#!/usr/bin/python

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout, QApplication, QSpacerItem,
                             QSizePolicy, QHBoxLayout, QFrame, QLineEdit, QTableWidget, QHeaderView, QAbstractItemView,
                             QDialog, QGridLayout)

label_font = QFont("Roboto", 24)
label_font_tit = QFont("Roboto", 20, weight=50)
label_font_piccolo = QFont("Roboto", 12)
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
    def settaFont(self,font:QFont, *args):
        for arg in args:
            arg.setFont(font)



    def initUi(self):
        # Definizione oggetti

        label_titolo = QLabel("<b>Scheda dati ricevuta</b>")
        label_titolo.setFont(label_font)


        frame1 = QFrame()
        frame1.setFrameShape(QFrame.Shape.HLine)


        frame2 = QFrame()
        frame2.setFrameShape(QFrame.Shape.HLine)
        frame2.setFrameShadow(QFrame.Shadow.Plain)




        frame3 = QFrame()
        frame3.setStyleSheet("border: 1px solid black; border-radius: 5px; padding: 10px")
        frame3.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        lab_num = QLabel("<b>Numero:</b>")
        lab_nom = QLabel("<b>Nome acquirente:</b>")
        lab_amm = QLabel("<b>Ammontare lordo:</b>")
        lab_data = QLabel("<b>Data di emissione:</b>")
        lab_ora = QLabel("<b>Orario di emissione:</b>")
        lab_lis = QLabel("<b>Lista Prodotti:</b>")
        self.settaFont(label_font_piccolo, lab_num, lab_ora, lab_lis, lab_data, lab_amm, lab_nom)
        self.lab_num_s = QLabel()
        self.lab_nom_s = QLabel()
        self.lab_amm_s = QLabel()
        self.lab_data_s = QLabel()
        self.lab_ora_s = QLabel()
        self.settaFont(label_font_piccolo, self.lab_num_s,self.lab_nom_s,self.lab_amm_s ,self.lab_data_s,self.lab_ora_s )
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
        layout.setContentsMargins(20, 20, 20, 20)

        layout2 = QVBoxLayout()
        layout2.addWidget(lab_lis)
        layout2.addWidget(frame3)
        layout2.setContentsMargins(20, 20, 20, 20)

        lay.addWidget(label_titolo)
        lay.addWidget(frame1)
        lay.addLayout(layout)
        lay.addSpacing(5)
        lay.addWidget(frame2)


        lay.addLayout(layout2)





        self.setStyleSheet("""
          
            
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
