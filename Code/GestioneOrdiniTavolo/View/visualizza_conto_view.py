import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QApplication, QTableWidget, QHeaderView,
                             QScrollArea, QFrame, QDialog)

# Font
label_font = QFont("Roboto", 24)
label_font_tit = QFont("Roboto", 32, weight=50)
label_font_piccolo = QFont("Roboto", 10)
header_font = QFont("Roboto", 10)
header_font.setBold(True)


def crea_tabella(righe, colonne, larghezza, altezza):
    tabella = QTableWidget()
    tabella.setRowCount(righe)
    tabella.setColumnCount(colonne)
    header = tabella.horizontalHeader()
    header.setFont(header_font)
    header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    tabella.verticalHeader().setVisible(False)
    tabella.horizontalHeader().setVisible(False)
    tabella.setFixedSize(larghezza, altezza)
    return tabella


class VistaVisualizzaConto(QDialog):

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setStyleSheet("""
           QPushButton{
               background-color: "#ff776d";
               color: "white";
               text-align: center;
               border-radius: 6px;
               font-size: 12px;

           }
           QPushButton:hover{
               background-color: "red";
               font-size: 12px;
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

    def init_ui(self):
        self.setWindowTitle("Gestionale Pizzeria")

        self.title = QLabel()
        self.title.setFont(QFont("Roboto", 18))
        frame1 = QFrame()
        frame1.setFrameShape(QFrame.Shape.HLine)
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)  # Per consentire la ridimensionamento automatico del widget interno


        self.contenitore = QWidget()

        layout = QVBoxLayout()
        self.layoutOrdini = QVBoxLayout()
        self.contenitore.setLayout(self.layoutOrdini)
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_area.setWidget(self.contenitore)

        frame2 = QFrame()
        frame2.setFrameShape(QFrame.Shape.HLine)

        layout_totale = QHBoxLayout()
        label_totale = QLabel("<b>TOTALE:</b> ........................................................€")
        label_totale.setFont(QFont("Roboto", 18))
        label_totale.setFixedSize(249, 22)
        self.label_totale_val = QLabel()
        layout_totale.addWidget(label_totale)
        layout_totale.addWidget(self.label_totale_val)

        layout.addWidget(self.title)
        layout.addWidget(frame1)
        layout.addWidget(self.scroll_area)
        layout.addWidget(frame2)
        layout.addLayout(layout_totale)

        layout.setContentsMargins(20, 20, 20, 20)
        self.setFixedSize(462, 516)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VistaVisualizzaConto()
    window.show()
    sys.exit(app.exec())
