import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt, pyqtSignal

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
    tabella.setFixedWidth(larghezza)
    tabella.setFixedHeight(altezza)

    return tabella

class VistaGestioneMagazzino(QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()
        #self.show()


    def initUI(self):

        main_layout = QVBoxLayout(self)
        hbox = QHBoxLayout()

        label_titolo = QLabel("Gestione Magazzino")
        label_titolo.setFont(font_tit)
        label_titolo.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        vbox_pulsanti = QVBoxLayout()
        vbox_tabella = QVBoxLayout()

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

        vbox_pulsanti.addSpacerItem(QSpacerItem(217, 217))

        self.data_grid = Tabella(3, 481, 404)
        self.data_grid.setRowCount(10)
        self.data_grid.setColumnWidth(0, 211)
        self.data_grid.setColumnWidth(1, 124)
        self.data_grid.setColumnWidth(2, 145)
        self.data_grid.setHorizontalHeaderLabels(["MATERIA PRIMA", "CODICE", "DISPONIBILITA"])
        self.data_grid.setFont(font_piccolo)
        self.data_grid.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Cerca per nome")
        self.search_bar.setFixedSize(336,29)
        self.search_bar.setStyleSheet("QLineEdit { border: 2px solid black; }")
        self.search_bar.textChanged.connect(self.filtra_elementi)
        vbox_tabella.addSpacerItem(QSpacerItem(20, 20))
        vbox_tabella.addWidget(self.search_bar, alignment=Qt.AlignmentFlag.AlignLeft)
        vbox_tabella.addWidget(self.data_grid, alignment=Qt.AlignmentFlag.AlignLeft)
        vbox_tabella.addSpacerItem(QSpacerItem(60,60))

        main_layout.addWidget(label_titolo, alignment=Qt.AlignmentFlag.AlignTop)
        hbox.addLayout(vbox_tabella)
        hbox.addLayout(vbox_pulsanti)
        main_layout.addLayout(hbox)
        self.setFixedSize(756,637)
        self.setLayout(main_layout)


    def update_tabella(self, codice, nome, qta_disponibile):

        row_position = self.data_grid.rowCount()
        self.data_grid.insertRow(row_position)
        self.data_grid.setItem(row_position, 0, QTableWidgetItem(str(codice)))
        self.data_grid.setItem(row_position, 1, QTableWidgetItem(nome))
        self.data_grid.setItem(row_position, 2, QTableWidgetItem(str(qta_disponibile)))


    def enter_event(self, pulsante):
        pulsante.setStyleSheet('background color: #e3645a; ')

    def filtra_elementi(self):

        ricerca = self.search_bar.text().lower()
        for row in range(self.data_grid.rowCount()):
                row_hidden = all(ricerca not in self.data_grid.item(row, 1).text().lower())
                self.data_grid.setRowHidden(row, row_hidden)




app = QApplication(sys.argv)
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
window = VistaGestioneMagazzino()
window.show()
sys.exit(app.exec())
