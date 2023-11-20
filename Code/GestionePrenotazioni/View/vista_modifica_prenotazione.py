import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap, QIcon
from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout, QApplication, QSizePolicy, QHBoxLayout,
                             QGridLayout, QTableWidget, QHeaderView, QSpacerItem, QLineEdit, QTableWidgetItem,
                             QScrollBar, QScrollArea, QAbstractItemView, QCheckBox, QSpinBox, QComboBox,
                             QCalendarWidget, QFrame)

# Font
label_font = QFont("Roboto", 24)
label_font_tit = QFont("Roboto", 24,weight=50)
label_font_piccolo = QFont("Roboto", 10)
header_font = QFont("Roboto", 10)
header_font.setBold(True)


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


def crea_pulsante_back(dimensioni, directory):
    pulsante_back = QPushButton()
    img = QPixmap(directory)
    icon = img.scaledToWidth(dimensioni)
    icon = QIcon(icon)
    pulsante_back.setIcon(icon)
    pulsante_back.setIconSize(img.size())
    pulsante_back.setFixedSize(dimensioni, dimensioni)
    pulsante_back.setStyleSheet("""
            QPushButton{
                background-color: rgba(0, 0, 0, 0);
            }
            QPushButton:hover{
                background-color: "lightgray";
            }
            """)
    return pulsante_back


class VistaModificaPrenotazione(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setStyleSheet("""
            QPushButton{
                background-color: "#ff776d";
                color: "white";
                text-align: center;
                border-radius: 6px;
                font-family:Roboto;
                font-size: 15px;
            }
            QPushButton:hover{
                background-color: "red";
                font-size: 17px;
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
        #self.show()

    def init_ui(self):
        self.setWindowTitle("Gestionale Pizzeria")
        #label
        title = QLabel("Modifica Dati Prenotazione")
        title.setFont(label_font_tit)
        label_ricerca = QLabel("Nome cliente:")
        label_tavolo = QLabel("Tavolo:")
        label_persone = QLabel("Persone:")
        label_orario = QLabel("Orario:")
        label_calendario = QLabel("Giorno:")
        label_tabella = QLabel("Orari liberi:")

        linea = QFrame()
        linea.setFrameShape(QFrame.Shape.HLine)

        #layout
        layout = QVBoxLayout()
        layout.addStretch()
        layout.addWidget(title)
        layout.addWidget(linea)

        griglia = QGridLayout()
        griglia.setContentsMargins(50,0,50,0)
        griglia.addWidget(label_ricerca,0,0)
        griglia.addWidget(label_tavolo,0,1)
        griglia.addWidget(label_persone,0,2)
        griglia.addWidget(label_orario,0,3)

        barra_ricerca = QLineEdit()
        barra_ricerca.setFixedWidth(257)
        combobox_tavolo = QComboBox()
        combobox_tavolo.setFixedWidth(75)
        combobox_orario = QComboBox()
        combobox_orario.setFixedWidth(85)
        spinbox_persone = QSpinBox()
        spinbox_persone.setFixedWidth(40)

        griglia.addWidget(barra_ricerca,1,0,alignment=Qt.AlignmentFlag.AlignLeft)
        griglia.addWidget(combobox_tavolo,1,1)
        griglia.addWidget(spinbox_persone,1,2)
        griglia.addWidget(combobox_orario,1,3)

        tabella = crea_tabella(15,3,308,322)
        griglia.addWidget(tabella,3,1,1,3,alignment=Qt.AlignmentFlag.AlignCenter)
        tabella.setHorizontalHeaderLabels(["ORARIO","NUMERO\nPRENOTAZIONI","POSTI\nLIBERI"])

        calendario = QCalendarWidget()
        calendario.setMaximumSize(257, 332)
        griglia.addWidget(calendario,3,0,alignment=Qt.AlignmentFlag.AlignLeft)

        griglia.addWidget(label_calendario,2,0,1,2)
        griglia.addWidget(label_tabella,2,1,1,2)

        pulsante_conferma = QPushButton("Conferma\nmodifica")
        pulsante_conferma.setFixedSize(205, 74)

        layout.setSpacing(20)
        layout.addLayout(griglia)
        layout.addWidget(pulsante_conferma,alignment=Qt.AlignmentFlag.AlignCenter)

        self.setContentsMargins(10,0,10,0)
        layout.addLayout(griglia)
        layout.addStretch()
        self.setLayout(layout)
        self.setFixedSize(756, 662)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    vista = VistaModificaPrenotazione()
    vista.show()
    sys.exit(app.exec())