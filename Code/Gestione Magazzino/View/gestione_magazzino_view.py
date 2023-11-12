import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

font_tit = QFont("Roboto", 32, weight=400)
font_label = QFont("Roboto", 13, weight=350)
font_piccolo = QFont("Roboto", 14)

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
    header.setFont(font_piccolo)
    header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
    for i in range(1, n_colonne):
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
    tabella.setFixedWidth(larghezza)
    tabella.setFixedHeight(altezza)

    return tabella

class VistaGestioneMagazzino(QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()
        self.show()


    def initUI(self):

        main_layout = QVBoxLayout(self)
        hbox = QHBoxLayout()

        label_titolo = QLabel("Gestione Magazzino")
        label_titolo.setFont(font_tit)
        label_titolo.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        vbox_pulsanti = QVBoxLayout()
        vbox_tabella = QHBoxLayout()

        pulsante_mostrainfo = QPushButton("Mostra Info\nMateria Prima")
        pulsante_modifica = QPushButton("Modifica\nMateria Prima")
        pulsante_inserisci = QPushButton("Inserisci\nMateria Prima")
        pulsante_elimina = QPushButton("Elimina\nMateria Prima")

        pulsanti = [pulsante_mostrainfo,
                    pulsante_inserisci,
                    pulsante_modifica,
                    pulsante_elimina]

        vbox_pulsanti.addSpacerItem(QSpacerItem(217, 217))

        for x in pulsanti:
            x.setFont(font_label)
            x.setFixedSize(147,49)
            vbox_pulsanti.addWidget(x, alignment=Qt.AlignmentFlag.AlignHCenter)
            x.setStyleSheet("color: white; background-color: #ff776d; border: 0px solid black; border-radius: 6px; padding: 10px")

        vbox_pulsanti.addSpacerItem(QSpacerItem(217, 217))

        data_grid = Tabella(3, 481, 404)
        data_grid.setHorizontalHeaderLabels(["MATERIA PRIMA", "CODICE", "DISPONIBILITA"])
        data_grid.setFont(font_piccolo)
        vbox_tabella.addWidget(data_grid, alignment=Qt.AlignmentFlag.AlignLeft)
        #vbox_tabella.addSpacerItem(QSpacerItem(200,200))

        main_layout.addWidget(label_titolo, alignment=Qt.AlignmentFlag.AlignTop)
        hbox.addLayout(vbox_tabella)
        hbox.addLayout(vbox_pulsanti)
        main_layout.addLayout(hbox)
        self.setFixedSize(756,637)
        self.setLayout(main_layout)



def main():
    app = QApplication(sys.argv)
    ex = VistaGestioneMagazzino()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()