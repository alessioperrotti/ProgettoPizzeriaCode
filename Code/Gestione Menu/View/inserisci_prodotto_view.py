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


class VistaInserisciProdotto(QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()


    def initUI(self):

        main_layout = QVBoxLayout(self)
        vbox = QVBoxLayout()
        hbox_datagrid = QHBoxLayout()
        hbox_conferma = QHBoxLayout()
        upper_grid = QGridLayout()

        label_titolo = QLabel("<b>Inserimento Nuovo Prodotto</b>")
        label_titolo.setFont(font_tit)
        #label_titolo.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        linea1 = QFrame()
        linea1.setFrameShape(QFrame.Shape.HLine)
        linea2 = QFrame()
        linea2.setFrameShape(QFrame.Shape.HLine)

        label_nome = QLabel("Nome prodotto:")
        self.campo_nome = QLineEdit()
        label_codice = QLabel("Codice:")
        self.campo_codice = QLineEdit()
        label_prezzo = QLabel("Prezzo al pubblico:")
        self.campo_prezzo = QLineEdit()
        label_tipologia = QLabel("Tipologia:")
        self.combo_tipologia = QComboBox()
        self.combo_tipologia.addItem("Piatto")
        self.combo_tipologia.addItem("Bevanda")

        widgets1 = [label_nome, self.campo_nome, label_codice, self.campo_codice,
                    label_prezzo, self.campo_prezzo, label_tipologia, self.combo_tipologia]

        for x in widgets1:
            x.setFont(font_label)
            x.setFixedSize(216, 33)

        upper_grid.addWidget(label_nome, 1, 1)
        upper_grid.addWidget(self.campo_nome, 2, 1)
        upper_grid.addWidget(label_codice, 1, 2)
        upper_grid.addWidget(self.campo_codice, 2, 2)
        upper_grid.addWidget(label_prezzo, 3, 1)
        upper_grid.addWidget(self.campo_prezzo, 4, 1)
        upper_grid.addWidget(label_tipologia, 3, 2)
        upper_grid.addWidget(self.combo_tipologia, 4, 2)

        middle_grid = QGridLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()

        label_ingrediente = QLabel("Ingrediente:")
        self.combo_ingrediente = QComboBox()
        self.combo_ingrediente.addItem("Ingrediente 1")
        self.combo_ingrediente.addItem("Ingrediente 2")
        self.combo_ingrediente.addItem("Ingrediente 3")
        label_quantita = QLabel("Quantità (Kg):")
        self.campo_quantita = QLineEdit()

        self.pulsante_aggiungi = QPushButton("Aggiungi Ingrediente")
        self.pulsante_aggiungi.setFixedSize(162, 32)
        self.pulsante_aggiungi.setFont(QFont("Roboto", 15, weight=50))

        middle_grid.addWidget(label_ingrediente, 1, 1)
        middle_grid.addWidget(self.combo_ingrediente, 2, 1)
        middle_grid.addWidget(label_quantita, 1, 2)
        middle_grid.addWidget(self.campo_quantita, 2, 2)
        middle_grid.addWidget(self.pulsante_aggiungi, 2, 3)
        vbox.addLayout(middle_grid)

        self.data_grid = crea_tabella(6, 2, 461, 191)
        self.data_grid.setHorizontalHeaderLabels(["INGREDIENTE", "QUANTITÀ(Kg)"])
        hbox_datagrid.addWidget(self.data_grid)

        self.pulsante_rimuovi = QPushButton("Rimuovi Ingrediente\nSelezionato")
        self.pulsante_rimuovi.setFixedSize(162, 55)
        self.pulsante_rimuovi.setFont(QFont("Roboto", 15, weight=300))
        hbox_datagrid.addWidget(self.pulsante_rimuovi)

        main_layout.addWidget(label_titolo, alignment=Qt.AlignmentFlag.AlignTop)
        main_layout.addWidget(linea1, alignment=Qt.AlignmentFlag.AlignTop)
        main_layout.addLayout(upper_grid)
        main_layout.addWidget(linea2)
        main_layout.addLayout(middle_grid)
        main_layout.addLayout(hbox_datagrid)

        self.setFixedSize(726, 712)
        self.setLayout(main_layout)


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
        font-size: 15px;
    }
    QTableWidget {
        background-color: white;
        alternate-background-color: white;
        selection-background-color: darkcyan;
        border: 2px solid grey;
    }
""")

window = VistaInserisciProdotto()
window.show()
sys.exit(app.exec())

