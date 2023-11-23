import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap, QIcon
from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout, QApplication, QSizePolicy, QHBoxLayout,
                             QGridLayout, QTableWidget, QHeaderView, QSpacerItem, QLineEdit, QTableWidgetItem,
                             QScrollBar, QScrollArea, QAbstractItemView, QCheckBox, QSpinBox, QComboBox,
                             QCalendarWidget, QFrame, QDialog)

# Font
label_font = QFont("Roboto", 24)
label_font_tit = QFont("Roboto", 24, weight=50)
label_font_piccolo = QFont("Roboto", 12)
header_font = QFont("Roboto", 10)


class VistaModificaDipendente(QDialog):
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
            QCalendarWidget QWidget#qt_calendar_navigationbar {
                background-color:"#ff776d" ; /* Colore di sfondo della barra di navigazione */
            }
        """)

    def init_ui(self):
        title = QLabel("<b>Modifica Dati Dipendente<\b>")
        title.setFont(label_font_tit)
        nome = QLabel("Nome:")
        nome.setFont(label_font_piccolo)
        cognome = QLabel("Cognome:")
        cognome.setFont(label_font_piccolo)
        email = QLabel("E-Mail:")
        email.setFont(label_font_piccolo)
        data = QLabel("Data di Nascita:")
        data.setFont(label_font_piccolo)
        stipendio = QLabel("Stipendio:")
        stipendio.setFont(label_font_piccolo)
        ruolo = QLabel("Ruolo:")
        ruolo.setFont(label_font_piccolo)
        username = QLabel("Nuovo Username:")
        username.setFont(label_font_piccolo)
        password = QLabel("Nuova Password:")
        password.setFont(label_font_piccolo)

        self.label_nome = QLabel()
        self.label_nome.setFixedSize(287, 30)
        self.label_cognome = QLabel()
        self.label_cognome.setFixedSize(287, 30)
        self.edit_email = QLineEdit()
        self.edit_email.setFixedSize(287,30)
        self.edit_stipendio = QLineEdit()
        self.edit_stipendio.setFixedSize(287,30)
        self.label_ruolo = QLabel()
        self.label_ruolo.setFixedSize(287, 30)
        self.edit_username = QLineEdit()
        self.edit_username.setFixedSize(287,30)
        self.edit_password = QLineEdit()
        self.edit_password.setFixedSize(287,30)

        self.pulsante = QPushButton("Conferma Modifica")
        self.pulsante.setFixedSize(205, 74)
        self.calendario = QCalendarWidget()
        self.calendario.setMaximumSize(287,207)
        linea = QFrame()
        linea.setFrameShape(QFrame.Shape.HLine)

        layout = QVBoxLayout()
        layout_orizzontale = QHBoxLayout()
        griglia_dx = QGridLayout()
        griglia_sx = QGridLayout()
        griglia_dx.setContentsMargins(20, 0, 20, 50)
        griglia_sx.setContentsMargins(20,0,20,50)

        griglia_sx.addWidget(nome,0,0)
        griglia_dx.addWidget(cognome,0,1)
        griglia_sx.addWidget(self.label_nome, 1, 0)
        griglia_dx.addWidget(self.label_cognome, 1, 1)
        griglia_sx.addWidget(email,2,0)
        griglia_dx.addWidget(data,2,1)
        griglia_sx.addWidget(self.edit_email,3,0)
        griglia_dx.addWidget(self.calendario,3,1,1,3)
        griglia_sx.addWidget(stipendio,4,0)
        griglia_sx.addWidget(self.edit_stipendio,5,0)
        griglia_sx.addWidget(ruolo,6,0)
        griglia_sx.addWidget(self.label_ruolo, 7, 0)
        griglia_sx.addWidget(username,8,0)
        griglia_dx.addWidget(password,8,1)
        griglia_sx.addWidget(self.edit_username,9,0)
        griglia_dx.addWidget(self.edit_password,9,1)

        layout.addWidget(title,alignment=Qt.AlignmentFlag.AlignTop)
        layout.addWidget(linea,alignment=Qt.AlignmentFlag.AlignTop)
        #layout.addStretch()
        layout_orizzontale.addLayout(griglia_sx)
        layout_orizzontale.addLayout(griglia_dx)
        layout.addLayout(layout_orizzontale)
        #layout.addStretch()
        layout.addWidget(self.pulsante,alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addSpacing(30)

        self.setContentsMargins(10, 0, 10, 0)
        self.setFixedSize(690,696)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VistaModificaDipendente()
    window.show()
    sys.exit(app.exec())
