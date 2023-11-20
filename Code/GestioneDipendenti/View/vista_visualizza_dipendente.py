import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap, QIcon
from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout, QApplication, QSizePolicy, QHBoxLayout,
                             QGridLayout, QTableWidget, QHeaderView, QSpacerItem, QLineEdit, QTableWidgetItem,
                             QScrollBar, QScrollArea, QAbstractItemView, QFrame)

# Font
label_font = QFont("Roboto", 24)
label_font_tit = QFont("Roboto", 20, weight=50)
label_font_piccolo = QFont("Roboto", 12)
header_font = QFont("Roboto", 10)
header_font.setBold(True)


class VistaVisualizzaDipendente(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        title = QLabel("<b>Scheda Dati Dipendente<\b>")
        title.setFont(label_font_tit)
        linea_top = QFrame()
        linea_top.setFrameShape(QFrame.Shape.HLine)

        nome = QLabel("<b>Nome:<\b>")
        nome.setFont(label_font_piccolo)
        cognome = QLabel("<b>Cognome:<\b>")
        cognome.setFont(label_font_piccolo)
        email = QLabel("<b>E-Mail:<\b>")
        email.setFont(label_font_piccolo)
        data_nascita = QLabel("<b>Data di Nascita:<\b>")
        data_nascita.setFont(label_font_piccolo)
        data_ingaggio = QLabel("<b>Data di Ingaggio:<\b>")
        data_ingaggio.setFont(label_font_piccolo)
        stipendio = QLabel("<b>Stipendio:<\b>")
        stipendio.setFont(label_font_piccolo)
        ruolo = QLabel("<b>Ruolo:<\b>")
        ruolo.setFont(label_font_piccolo)
        username = QLabel("<b>Username:<\b>")
        username.setFont(label_font_piccolo)
        password = QLabel("<b>Password:<\b>")
        password.setFont(label_font_piccolo)

        campo_nome = QLabel()
        campo_nome.setFont(label_font_piccolo)
        campo_cognome = QLabel()
        campo_cognome.setFont(label_font_piccolo)
        campo_email = QLabel()
        campo_email.setFont(label_font_piccolo)
        campo_data_nascita = QLabel()
        campo_data_nascita.setFont(label_font_piccolo)
        campo_data_ingaggio = QLabel()
        campo_data_ingaggio.setFont(label_font_piccolo)
        campo_stipendio = QLabel()
        campo_stipendio.setFont(label_font_piccolo)
        campo_ruolo = QLabel()
        campo_ruolo.setFont(label_font_piccolo)
        campo_username = QLabel()
        campo_username.setFont(label_font_piccolo)
        campo_password = QLabel()
        campo_password.setFont(label_font_piccolo)

        linea_bottom = QFrame()
        linea_bottom.setFrameShape(QFrame.Shape.HLine)

        layout = QVBoxLayout()
        griglia_top = QGridLayout()
        griglia_top.setSpacing(50)
        griglia_top.setContentsMargins(20, 20, 20, 20)
        griglia_bottom = QGridLayout()
        griglia_bottom.setContentsMargins(20, 20, 20, 0)

        griglia_top.addWidget(nome, 0, 0)
        griglia_top.addWidget(campo_nome, 0, 1)
        griglia_top.addWidget(email, 0, 2)
        griglia_top.addWidget(campo_email, 0, 3)
        griglia_top.addWidget(cognome, 1, 0)
        griglia_top.addWidget(campo_cognome, 1, 1)
        griglia_top.addWidget(data_ingaggio, 1, 2)
        griglia_top.addWidget(campo_data_ingaggio, 1, 3)
        griglia_top.addWidget(ruolo, 2, 0)
        griglia_top.addWidget(campo_ruolo, 2, 1)
        griglia_top.addWidget(stipendio, 2, 2)
        griglia_top.addWidget(campo_stipendio, 2, 3)
        griglia_top.addWidget(data_nascita, 3, 0)
        griglia_top.addWidget(campo_data_nascita, 3, 1)

        griglia_bottom.addWidget(username, 0, 0)
        griglia_bottom.addWidget(campo_username, 0, 1)
        griglia_bottom.addWidget(password, 0, 2)
        griglia_bottom.addWidget(campo_password, 0, 3)

        layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignTop)
        layout.addWidget(linea_top, alignment=Qt.AlignmentFlag.AlignTop)
        layout.addStretch()
        layout.addLayout(griglia_top)
        layout.addStretch()
        layout.addWidget(linea_bottom)
        layout.addLayout(griglia_bottom)

        self.setLayout(layout)
        self.setFixedSize(904, 425)
        self.setContentsMargins(10, 0, 10, 20)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VistaVisualizzaDipendente()
    window.show()
    sys.exit(app.exec())
