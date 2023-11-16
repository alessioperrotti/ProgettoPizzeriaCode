import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont, QPixmap, QIcon
from PyQt6.QtCore import Qt


class VistaInserisciProdotto(QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()


    def initUI(self):

        main_layout = QVBoxLayout(self)
