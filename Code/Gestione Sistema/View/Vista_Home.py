#!/usr/bin/python

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QLCDNumber, QSlider, QLabel, QPushButton, QVBoxLayout, QApplication, QSpacerItem,
                             QSizePolicy, QHBoxLayout, QFrame, QLineEdit, QGridLayout, QTableWidget, QTableWidgetItem,
                             QHeaderView)
from PyQt6.QtGui import QFont, QPixmap

label_font = QFont("Roboto", 24)
label_font_tit = QFont("Roboto", 32, weight=50)
label_font_piccolo = QFont("Roboto", 14)

def Pulsante(nome, directory):
    pulsante = QPushButton()
    label = QLabel(nome)
    label.setFont(label_font_piccolo)
    layout = QHBoxLayout()
    layout.addStretch()
    layout.addWidget(Immagine(directory, 50))
    layout.addWidget(label)
    layout.addStretch()
    pulsante.setLayout(layout)
    pulsante.setSizePolicy(QSizePolicy.Policy.Minimum,QSizePolicy.Policy.Minimum)
    pulsante.setStyleSheet(".QPushButton {background-color: #ff776d; border: 2px solid black; border-radius: 10px; padding: 10px}")
    pulsante.setFixedSize(230,100)
    return pulsante

def Immagine(directory, dimensione):
    label_foto = QLabel()
    pixmap = QPixmap(directory)
    scaled_pixmap = pixmap.scaled(dimensione, dimensione, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
    label_foto.setPixmap(scaled_pixmap)
    return label_foto


def Tabella(nColonne, larghezza, altezza):
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

    tabella.setColumnCount(nColonne)

    header = tabella.horizontalHeader()
    header.setFont(label_font_piccolo)
    header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
    for i in range(1, nColonne):
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
    tabella.setFixedWidth(larghezza)
    tabella.setFixedHeight(altezza)

    return tabella




class Vista_Home_Admin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        #definizione oggetti
        label = QLabel("ACCESSO: Admin")
        label.setFont(label_font_tit)
        pulsante1=Pulsante("Statistiche", "png/stats.png");
        pulsante2=Pulsante("Magazzino",  "png/magazzino.png");
        pulsante3=Pulsante("Dipendenti", "png/dipendenti.png");
        pulsante4=Pulsante("Turni", "png/turni.png");
        pulsante5=Pulsante("Modifica Menu", "png/stats.png");
        pulsante6=Pulsante("Prenotazioni", "png/stats.png");
        pulsante7=Pulsante("Ricevute", "png/stats.png");

        back = Immagine("png/back.png",35)

        #definizione layout
        layout = QVBoxLayout()
        griglia = QGridLayout()
        layout_centrale = QHBoxLayout()
        layout_orizzontale = QHBoxLayout()

        #inserimento oggetti nei layout
        layout_centrale.addStretch()
        layout_centrale.addLayout(griglia)
        layout_centrale.addStretch()

        griglia.addWidget(pulsante1, 1,1)
        griglia.addWidget(pulsante2, 1,2)
        griglia.addWidget(pulsante3, 2,1)
        griglia.addWidget(pulsante4, 2,2)
        griglia.addWidget(pulsante5, 3,1)
        griglia.addWidget(pulsante6, 3,2)
        griglia.addWidget(pulsante7, 4,1,1,2, alignment=Qt.AlignmentFlag.AlignCenter)

        layout.addSpacing(10)
        layout.addWidget(label)
        layout.addStretch()
        layout.addLayout(layout_centrale)
        layout.addSpacing(10)
        layout.addWidget(back)
        layout.addSpacing(10)

        layout_orizzontale.addSpacing(20)
        layout_orizzontale.addLayout(layout)
        layout_orizzontale.addSpacing(20)


        self.setFixedSize(994, 637)
        self.setLayout(layout_orizzontale)
        self.show()









def main():
    app = QApplication(sys.argv)
    ex = Vista_Home_Admin()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()


