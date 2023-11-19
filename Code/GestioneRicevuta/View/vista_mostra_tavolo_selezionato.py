import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap, QIcon
from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout, QApplication, QSizePolicy, QHBoxLayout,
                             QGridLayout, QTableWidget, QHeaderView, QSpacerItem, QLineEdit, QTableWidgetItem,
                             QScrollBar, QScrollArea, QAbstractItemView, QFrame, QDialog)

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



class VistaMostraTavoloSelezionato(QDialog):

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

        self.title = QLabel("Conto Tavolo n.")
        self.title.setFont(label_font_piccolo)
        frame1 = QFrame()
        frame1.setFrameShape(QFrame.Shape.HLine)
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)  # Per consentire la ridimensionamento automatico del widget interno

        self.pulsante_aggiungi = QPushButton("Aggiungi Alla\nricevuta")
        self.pulsante_aggiungi.setFixedSize(150, 50)
        self.contenitore = QWidget()

        layout = QVBoxLayout()
        self.layoutOrdini = QVBoxLayout()
        self.contenitore.setLayout(self.layoutOrdini)
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_area.setWidget(self.contenitore)

        layout.addWidget(self.title)
        layout.addWidget(frame1)
        layout.addWidget(self.scroll_area)
        layout.addWidget(self.pulsante_aggiungi, alignment=Qt.AlignmentFlag.AlignCenter)




        layout.setContentsMargins(20, 20, 20, 20)
        self.setFixedSize(462, 516)
        self.setLayout(layout)






if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VistaMostraTavoloSelezionato()
    window.show()
    sys.exit(app.exec())
