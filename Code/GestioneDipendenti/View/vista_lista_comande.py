import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap, QIcon
from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout, QApplication, QSizePolicy, QHBoxLayout,
                             QGridLayout, QTableWidget, QHeaderView, QSpacerItem, QLineEdit, QTableWidgetItem,
                             QScrollBar, QScrollArea, QAbstractItemView, QDialog)


# Font
label_font = QFont("Roboto", 24)
label_font_tit = QFont("Roboto", 32, weight=50)
label_font_piccolo = QFont("Roboto", 10)
header_font = QFont("Roboto", 10)
header_font.setBold(True)

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
                background-color: rgba(0,0,0,0);
            }
            QPushButton:hover{
                background-color: "lightgray";
            }
            """)
    return pulsante_back

class VistaListaComande(QDialog):

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VistaListaComande()
    window.show()
    sys.exit(app.exec())