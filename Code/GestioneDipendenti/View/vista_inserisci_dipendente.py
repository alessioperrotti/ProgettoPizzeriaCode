import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap, QIcon
from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout, QApplication, QSizePolicy, QHBoxLayout,
                             QGridLayout, QTableWidget, QHeaderView, QSpacerItem, QLineEdit, QTableWidgetItem,
                             QScrollBar, QScrollArea, QAbstractItemView, QCheckBox, QSpinBox, QComboBox,
                             QCalendarWidget, QFrame)

# Font
label_font = QFont("Roboto", 24)
label_font_tit = QFont("Roboto", 24, weight=50)
label_font_piccolo = QFont("Roboto", 12)
header_font = QFont("Roboto", 10)


class VistaInserisciDipendente(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.show()

    def init_ui(self):
        title = QLabel("<b>Inserimento Nuovo Dipendente<\b>")
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

        edit_nome = QLineEdit()
        edit_nome.setFixedSize(287,30)
        edit_cognome = QLineEdit()
        edit_cognome.setFixedSize(287,30)
        edit_email = QLineEdit()
        edit_email.setFixedSize(287,30)
        edit_stipendio = QLineEdit()
        edit_stipendio.setFixedSize(287,30)
        edit_ruolo = QComboBox()
        edit_ruolo.setFixedSize(287,30)
        edit_username = QLineEdit()
        edit_username.setFixedSize(287,30)
        edit_password = QLineEdit()
        edit_password.setFixedSize(287,30)

        pulsante = QPushButton("Conferma Inserimento")
        pulsante.setFixedSize(205, 74)
        calendario = QCalendarWidget()
        calendario.setMaximumSize(287,207)
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
        griglia_sx.addWidget(edit_nome,1,0)
        griglia_dx.addWidget(edit_cognome,1,1)
        griglia_sx.addWidget(email,2,0)
        griglia_dx.addWidget(data,2,1)
        griglia_sx.addWidget(edit_email,3,0)
        griglia_dx.addWidget(calendario,3,1,1,3)
        griglia_sx.addWidget(stipendio,4,0)
        griglia_sx.addWidget(edit_stipendio,5,0)
        griglia_sx.addWidget(ruolo,6,0)
        griglia_sx.addWidget(edit_ruolo,7,0)
        griglia_sx.addWidget(username,8,0)
        griglia_dx.addWidget(password,8,1)
        griglia_sx.addWidget(edit_username,9,0)
        griglia_dx.addWidget(edit_password,9,1)

        layout.addWidget(title,alignment=Qt.AlignmentFlag.AlignTop)
        layout.addWidget(linea,alignment=Qt.AlignmentFlag.AlignTop)
        #layout.addStretch()
        layout_orizzontale.addLayout(griglia_sx)
        layout_orizzontale.addLayout(griglia_dx)
        layout.addLayout(layout_orizzontale)
        #layout.addStretch()
        layout.addWidget(pulsante,alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addSpacing(30)

        self.setContentsMargins(10, 0, 10, 0)
        self.setFixedSize(690,696)
        self.setLayout(layout)


app = QApplication(sys.argv)

app.setStyleSheet("""
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
window = VistaInserisciDipendente()
window.show()
sys.exit(app.exec())
