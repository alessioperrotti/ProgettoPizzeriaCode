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

class VistaInserisciDipendente(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui(self)
        self.show()

    def init_ui(self):
        title = QLabel("Inserimento Nuovo Dipendente")
        nome = QLabel("Nome:")
        cognome = QLabel("Cognome:")
        email = QLabel("E-Mail:")
        data = QLabel("Data di Nascita:")
        stipendio = QLabel("Stipendio:")
        ruolo = QLabel("Ruolo:")
        username = QLabel("Nuovo Username:")
        password = QLabel("Nuova Password:")

        edit_nome = QLineEdit()
        edit_cognome = QLineEdit()
        edit_email = QLineEdit()
        edit_data = QLineEdit()
        edit_stipendio = QLineEdit()
        edit_ruolo = QComboBox()
        edit_username = QLineEdit()
        edit_password = QLineEdit()

        pulsante = QPushButton("Conferma Inserimento")
        calendario = QCalendarWidget()
        linea = QFrame()
        linea.setFrameShape(QFrame.Shape.HLine)

        layout = QVBoxLayout()
        griglia = QGridLayout()





