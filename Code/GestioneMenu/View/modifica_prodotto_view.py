import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont, QPixmap, QIcon
from PyQt6.QtCore import Qt

font_tit = QFont("Roboto", 24, weight=50)
font_label = QFont("Roboto", 18, weight=350)

def crea_tabella(righe, colonne, larghezza, altezza):
    tabella = QTableWidget()
    tabella.setRowCount(righe)
    tabella.setColumnCount(colonne)
    header = tabella.horizontalHeader()
    header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    tabella.verticalHeader().setVisible(False)
    tabella.setFixedSize(larghezza, altezza)
    return tabella


class VistaModificaProdotto(QDialog):

    def __init__(self):

        super().__init__()
        self.initUI()
        self.setStyleSheet("""
                    QPushButton{
                        background-color: "#ff776d";
                        color: "white";
                        text-align: center;
                        border-radius: 6px;
                        font-family:Roboto;
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
                        background-color: lightgray;
                        font-weight: bold;
                    }
                    QHeaderView:active {
                        background-color: gray;
                    }
                """)


    def initUI(self):

        main_layout = QVBoxLayout(self)
        #vbox = QVBoxLayout()
        hbox_datagrid = QHBoxLayout()
        hbox_conferma = QHBoxLayout()
        upper_grid = QGridLayout()

        label_titolo = QLabel("<b>Modifica Dati Prodotto</b>")
        label_titolo.setFont(font_tit)

        linea1 = QFrame()
        linea1.setFrameShape(QFrame.Shape.HLine)
        linea2 = QFrame()
        linea2.setFrameShape(QFrame.Shape.HLine)

        label_nome = QLabel("<b>Nome prodotto:</b>")
        self.label_nome_val = QLabel()
        label_codice = QLabel("<b>Codice:</b>")
        self.label_codice_val = QLabel()
        label_prezzo = QLabel("Prezzo al pubblico:")
        self.campo_prezzo = QLineEdit()
        label_tipologia = QLabel("Tipologia:")
        self.combo_tipologia = QComboBox()
        self.combo_tipologia.addItem("Piatto")
        self.combo_tipologia.addItem("Bevanda")

        widgets1 = [label_nome, self.label_nome_val, label_codice, self.label_codice_val,
                    label_prezzo, self.campo_prezzo, label_tipologia, self.combo_tipologia]

        for x in widgets1:
            x.setFont(font_label)
            x.setFixedSize(216, 33)

        upper_grid.addWidget(label_nome, 1, 1)
        upper_grid.addWidget(self.label_nome_val, 2, 1)
        upper_grid.addWidget(label_codice, 1, 2)
        upper_grid.addWidget(self.label_codice_val, 2, 2)
        upper_grid.addWidget(label_prezzo, 4, 1)
        upper_grid.addWidget(self.campo_prezzo, 5, 1)
        upper_grid.addWidget(label_tipologia, 4, 2)
        upper_grid.addWidget(self.combo_tipologia, 5, 2)
        upper_grid.addItem(QSpacerItem(216, 40), 3, 1)
        upper_grid.addItem(QSpacerItem(216, 40), 3, 2)

        spacer_item = QSpacerItem(10, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        upper_grid.addItem(spacer_item, 0, 1)

        upper_hbox = QHBoxLayout()
        upper_hbox.addSpacerItem(QSpacerItem(16, 400))
        upper_hbox.addLayout(upper_grid)
        upper_hbox.addSpacerItem(QSpacerItem(170, 400))
        middle_grid = QGridLayout()

        label_ingrediente = QLabel("Ingrediente:")
        label_ingrediente.setFont(font_label)
        label_ingrediente.setFixedSize(200, 33)
        self.combo_ingrediente = QComboBox()
        self.combo_ingrediente.setFixedSize(216, 26)
        label_quantita = QLabel("Quantità (Kg):")
        label_quantita.setFont(font_label)
        label_quantita.setFixedSize(200, 33)
        self.campo_quantita = QLineEdit()
        self.campo_quantita.setFixedSize(121, 26)

        self.pulsante_aggiungi = QPushButton("Aggiungi Ingrediente")
        self.pulsante_aggiungi.setFixedSize(162, 32)
        #self.pulsante_aggiungi.setFont(QFont("Roboto", 15, weight=350))

        middle_grid.addWidget(label_ingrediente, 1, 1)
        middle_grid.addWidget(self.combo_ingrediente, 2, 1)
        middle_grid.addWidget(label_quantita, 1, 2)
        middle_grid.addWidget(self.campo_quantita, 2, 2)
        middle_grid.addItem(QSpacerItem(30, 40), 1, 3)
        middle_grid.addWidget(self.pulsante_aggiungi, 2, 4)

        self.data_grid = crea_tabella(0, 2, 461, 191)
        self.data_grid.setHorizontalHeaderLabels(["INGREDIENTE", "QUANTITÀ(Kg)"])
        self.data_grid.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        hbox_datagrid.addWidget(self.data_grid)

        self.pulsante_rimuovi = QPushButton("Rimuovi Ingrediente\nSelezionato")
        self.pulsante_rimuovi.setFixedSize(162, 55)
        #self.pulsante_rimuovi.setFont(QFont("Roboto", 15, weight=350))
        hbox_datagrid.addWidget(self.pulsante_rimuovi)

        self.pulsante_conferma = QPushButton("Conferma Modifica")
        self.pulsante_conferma.setFixedSize(205, 74)
        #self.pulsante_conferma.setFont(QFont("Roboto", 15, weight=350))
        hbox_conferma.addWidget(self.pulsante_conferma)

        main_layout.addWidget(label_titolo, alignment=Qt.AlignmentFlag.AlignTop)
        main_layout.addWidget(linea1, alignment=Qt.AlignmentFlag.AlignTop)
        main_layout.addLayout(upper_hbox)
        main_layout.addWidget(linea2)
        main_layout.addLayout(middle_grid)
        main_layout.addLayout(hbox_datagrid)
        main_layout.addLayout(hbox_conferma)

        self.setFixedSize(726, 712)
        self.setLayout(main_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VistaModificaProdotto()
    window.show()
    sys.exit(app.exec())

