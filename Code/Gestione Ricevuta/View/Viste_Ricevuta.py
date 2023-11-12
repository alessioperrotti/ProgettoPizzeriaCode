#!/usr/bin/python

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QLCDNumber, QSlider, QLabel, QPushButton, QVBoxLayout, QApplication, QSpacerItem,
                             QSizePolicy, QHBoxLayout, QFrame, QLineEdit, QGridLayout, QTableWidget, QTableWidgetItem,
                             QHeaderView)
from PyQt6.QtGui import QFont, QPixmap

label_font = QFont("Roboto", 24)
label_font_tit = QFont("Roboto", 40, weight=50)
label_font_piccolo = QFont("Roboto", 14)

def Pulsante(nome):
    pulsante = QPushButton(nome)
    pulsante.setFont(label_font)
    pulsante.setSizePolicy(QSizePolicy.Policy.Minimum,QSizePolicy.Policy.Minimum)
    pulsante.setStyleSheet("background-color: #ff776d; border: 2px solid black; border-radius: 10px; padding: 10px")
    return pulsante

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


class Vista_Inserisci_Ricevuta(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        #Definizione oggetti

        label_titolo = QLabel("<b>Inserimento nuova ricevuta</b>")
        label_titolo.setFont(label_font)
        label_titolo.setSizePolicy(QSizePolicy.Policy.Minimum,QSizePolicy.Policy.Minimum)

        frame1 = QFrame()
        frame1.setFrameShape(QFrame.Shape.HLine)

        ricerca = QLineEdit()
        ricerca.setPlaceholderText("Cerca numero tavolo")
        ricerca.setFont(label_font_piccolo)
        ricerca.setFixedWidth(340)
        ricerca.setStyleSheet("border: 1px solid black; padding: 3px")


        tabella = Tabella(2,340,115);
        tabella.setHorizontalHeaderLabels(["TAVOLO","NUMERO ORDINI"])
        tabella.setFont(label_font_piccolo)


        pulsante1 = Pulsante("Mostra Tavolo selezionato")
        pulsante1.setFont(label_font_piccolo)
        pulsante1.setFixedHeight(70)

        label_nome = QLabel("Nome acquirente")
        label_nome.setFont(label_font_piccolo)

        ins_nome = QLineEdit()
        ins_nome.setFont(label_font_piccolo)
        ins_nome.setFixedWidth(340)
        ins_nome.setStyleSheet("border: 1px solid black; padding: 3px")

        pulsante2 = Pulsante("Conferma inserimento")
        pulsante3 = Pulsante("Stampa Ricevuta")
        pulsante2.setFont(label_font_piccolo)
        pulsante3.setFont(label_font_piccolo)
        pulsante2.setFixedHeight(70)
        pulsante3.setFixedHeight(70)





        #Definizione layout
        layout = QVBoxLayout()
        layout_tabella_e_tavolo = QHBoxLayout()
        layout_tasti = QHBoxLayout()

        #Inserimento oggetti nei layout

        layout_tabella_e_tavolo.addWidget(tabella)
        layout_tabella_e_tavolo.addSpacerItem(QSpacerItem(30,30))
        layout_tabella_e_tavolo.addWidget(pulsante1)
        layout_tabella_e_tavolo.addSpacerItem(QSpacerItem(30,30))

        layout_tasti.addSpacerItem(QSpacerItem(140,1))
        layout_tasti.addWidget(pulsante2)
        layout_tasti.addWidget(pulsante3)
        layout_tasti.addSpacerItem(QSpacerItem(140,1))


        layout.addWidget(label_titolo, alignment=Qt.AlignmentFlag.AlignTop)
        layout.addWidget(frame1,alignment=Qt.AlignmentFlag.AlignTop)
        layout.addWidget(ricerca,alignment=Qt.AlignmentFlag.AlignTop)
        layout.addSpacing(10)
        layout.addLayout(layout_tabella_e_tavolo)
        layout.addSpacerItem(QSpacerItem(1,1,QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding))
        layout.addWidget(label_nome)
        layout.addSpacing(10)
        layout.addWidget(ins_nome)
        layout.addSpacing(20)
        layout.addLayout(layout_tasti)
        layout.addSpacing(20)




        self.setFixedSize(690, 474)
        self.setLayout(layout)
        self.show()


class Vista_Gestione_Ricevute(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        #definizione oggetti
        label = QLabel("Gestione Ricevute")
        label.setFont(label_font)
        tabella = Tabella(3, 480, 400)
        tabella.setHorizontalHeaderLabels(["Acquirente","Numero","Data"])
        tabella.setFont(label_font_piccolo)
        pulsante1 = Pulsante("Mostra Info\nRicevuta")
        pulsante2 = Pulsante("Inserisci\nRicevuta")
        pulsante3 = Pulsante("Elimina\nRicevuta")
        pulsante1.setFont(label_font_piccolo)
        pulsante2.setFont(label_font_piccolo)
        pulsante3.setFont(label_font_piccolo)
        png_back = QLabel()
        pixmap = QPixmap("png/back.png")
        scaled_pixmap = pixmap.scaled(35, 35, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
        png_back.setPixmap(scaled_pixmap)


        #definizione layout
        layout = QVBoxLayout()
        layout_tabella_pulsanti = QHBoxLayout()
        layout_pulsanti = QVBoxLayout()

        #inserimento oggetti nel layout
        layout_pulsanti.addSpacerItem(QSpacerItem(1,130))
        layout_pulsanti.addWidget(pulsante1)
        layout_pulsanti.addWidget(pulsante2)
        layout_pulsanti.addWidget(pulsante3)
        layout_pulsanti.addSpacerItem(QSpacerItem(1,130))


        layout_tabella_pulsanti.addSpacerItem(QSpacerItem(30,30))
        layout_tabella_pulsanti.addWidget(tabella)
        layout_tabella_pulsanti.addSpacerItem(QSpacerItem(40,40))
        layout_tabella_pulsanti.addLayout(layout_pulsanti)
        layout_tabella_pulsanti.addSpacerItem(QSpacerItem(30,30))



        layout.addSpacerItem(QSpacerItem(30,30))
        layout.addWidget(label)
        #layout.addSpacerItem(QSpacerItem(20,20))
        layout.addLayout(layout_tabella_pulsanti)
        layout.addStretch()
        layout.addWidget(png_back, alignment=Qt.AlignmentFlag.AlignLeft)




        self.setFixedSize(756, 637)
        self.setLayout(layout)
        self.show()





def main():
    app = QApplication(sys.argv)
    ex = Vista_Gestione_Ricevute()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()


