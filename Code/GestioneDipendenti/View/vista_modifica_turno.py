import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap, QIcon
from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout, QApplication, QSizePolicy, QHBoxLayout,
                             QGridLayout, QTableWidget, QHeaderView, QSpacerItem, QLineEdit, QTableWidgetItem,
                             QScrollBar, QScrollArea, QAbstractItemView, QFrame, QComboBox, QDialog)

# Font
label_font = QFont("Roboto", 24)
label_font_tit = QFont("Roboto", 20, weight=50)
label_font_piccolo = QFont("Roboto", 10)
header_font = QFont("Roboto", 10)
header_font.setBold(True)

def crea_tabella(righe, colonne, larghezza, altezza):
    tabella = QTableWidget()
    tabella.setRowCount(righe)
    tabella.setColumnCount(colonne)
    header = tabella.horizontalHeader()
    header.setSectionResizeMode(0,QHeaderView.ResizeMode.Stretch)
    header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
    header.setSectionResizeMode(2, QHeaderView.ResizeMode.Fixed)
    tabella.verticalHeader().setVisible(False)
    tabella.setFixedSize(larghezza, altezza)
    tabella.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
    tabella.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
    return tabella

def crea_pulsante_img(dimensioni, directory):
    pulsante_img = QPushButton()
    img = QPixmap(directory)
    icon = img.scaledToWidth(dimensioni)
    icon = QIcon(icon)
    pulsante_img.setIcon(icon)
    pulsante_img.setIconSize(img.size())
    pulsante_img.setFixedSize(dimensioni, dimensioni)
    pulsante_img.setStyleSheet("""
            QPushButton{
                background-color: rgba(0, 0, 0, 0);
            }
            QPushButton:hover{
                background-color: "lightgray";
            }
            """)
    return pulsante_img

class VistaModificaTurno(QDialog):
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

    def init_ui(self):
        title = QLabel("<b>Modifica Turni:<\b>")
        title.setFont(label_font_tit)
        self.giorno_title = QLabel()
        self.giorno_title.setFont(label_font_tit)

        linea = QFrame()
        linea.setFrameShape(QFrame.Shape.HLine)

        s_cuoco = QLabel("<b>Selezione Cuoco:<\b>")
        s_cuoco.setFont(label_font_piccolo)
        s_cameriere = QLabel("<b>Selezione Cameriere:<\b>")
        s_cameriere.setFont(label_font_piccolo)

        self.cuoco = QComboBox()
        self.cuoco.setFixedSize(146,29)
        self.cameriere = QComboBox()
        self.cameriere.setFixedSize(146, 29)

        self.turno_cuoco = QComboBox()
        self.turno_cuoco.addItem("Pranzo")
        self.turno_cuoco.addItem("Cena")
        self.turno_cuoco.addItem("Pranzo & Cena")
        self.turno_cuoco.setFixedSize(146, 29)

        self.turno_cameriere = QComboBox()
        self.turno_cameriere.addItem("Pranzo")
        self.turno_cameriere.addItem("Cena")
        self.turno_cameriere.addItem("Pranzo & Cena")
        self.turno_cameriere.setFixedSize(146, 29)

        self.pulsante = QPushButton("Conferma")
        self.pulsante.setFixedSize(146,39)

        #modificare le img
        self.p_agg_cuoco = crea_pulsante_img(24,"png_icone/user-add.png")
        self.p_agg_cameriere = crea_pulsante_img(24, "png_icone/user-add.png")
        #aggiungere quando inserisco i clienti
        self.p_rim_cuoco = crea_pulsante_img(20, "png_icone/remove-user.png")
        self.p_rim_cameriere = crea_pulsante_img(20, "png_icone/remove-user.png")

        self.tab_cuoco = crea_tabella(0,3,400,116)
        self.tab_cuoco.setHorizontalHeaderLabels(["Nome Cuoco:","Turno",""])
        self.tab_cuoco.setColumnWidth(2, 10)

        self.tab_cameriere = crea_tabella(0,3,400,116)
        self.tab_cameriere.setColumnWidth(2, 10)
        self.tab_cameriere.setHorizontalHeaderLabels(["Nome Cameriere:", "Turno",""])

        layout = QVBoxLayout()
        layout_title = QHBoxLayout()
        griglia = QGridLayout()
        griglia.setVerticalSpacing(10)
        griglia.setContentsMargins(10,25,10,20)

        griglia.addWidget(s_cuoco,0,0)
        griglia.addWidget(self.cuoco,1,0)
        griglia.addWidget(self.turno_cuoco,1,1)
        griglia.addWidget(self.p_agg_cuoco,1,2)

        griglia.addWidget(s_cameriere,2,0)
        griglia.addWidget(self.cameriere,3,0)
        griglia.addWidget(self.turno_cameriere,3,1)
        griglia.addWidget(self.p_agg_cameriere,3,2)

        griglia.addWidget(self.pulsante,4,0,alignment=Qt.AlignmentFlag.AlignBottom)
        griglia.setRowStretch(4, 1)

        layout_title.addWidget(title,alignment=Qt.AlignmentFlag.AlignTop)
        layout_title.addWidget(self.giorno_title,alignment=Qt.AlignmentFlag.AlignTop)
        layout.addLayout(layout_title)
        layout.addWidget(linea,alignment=Qt.AlignmentFlag.AlignTop)
        layout.addLayout(griglia)
        layout.addWidget(self.tab_cuoco)
        layout.addWidget(self.tab_cameriere)

        self.setLayout(layout)
        self.setFixedSize(420,570)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VistaModificaTurno()
    window.show()
    sys.exit(app.exec())