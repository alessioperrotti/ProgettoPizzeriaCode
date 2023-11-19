import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap, QIcon
from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout, QApplication, QSizePolicy, QHBoxLayout,
                             QGridLayout, QTableWidget, QHeaderView, QSpacerItem, QLineEdit, QTableWidgetItem,
                             QScrollBar, QScrollArea, QAbstractItemView, QFrame, QComboBox)

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
    header.setSectionResizeMode(0,QHeaderView.ResizeMode.Stretch)
    header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
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

class VistaGestioneTurniPersonale(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.show()


app = QApplication(sys.argv)

app.setStyleSheet("""
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
window = VistaGestioneTurniPersonale()
window.show()
sys.exit(app.exec())