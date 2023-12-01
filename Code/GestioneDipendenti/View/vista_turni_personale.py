import sys

from PyQt6.QtCore import Qt, QTime, QTimer, QDateTime
from PyQt6.QtGui import QFont, QPixmap, QIcon
from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout, QApplication, QSizePolicy, QHBoxLayout,
                             QGridLayout, QTableWidget, QHeaderView, QSpacerItem, QLineEdit, QTableWidgetItem,
                             QScrollBar, QScrollArea, QAbstractItemView, QFrame, QComboBox)

# Font
label_font = QFont("Roboto", 20)
label_font_tit = QFont("Roboto", 32, weight=50)
label_font_piccolo = QFont("Roboto", 12)
header_font = QFont("Roboto", 10)
header_font.setBold(True)


def crea_tabella(righe, colonne, larghezza, altezza):
    tabella = QTableWidget()
    tabella.setRowCount(righe)
    tabella.setColumnCount(colonne)
    header_h = tabella.horizontalHeader()
    header_h.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    header_v = tabella.verticalHeader()
    header_v.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    #tabella.verticalHeader().setVisible(False)
    tabella.setFixedSize(larghezza, altezza)
    tabella.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectColumns)
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

class VistaTurniPersonale(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.show()

    def init_ui(self):
        title = QLabel("Gestione Turni Personale")
        title.setFont(label_font_tit)

        self.tabella = crea_tabella(2,6,870,360)
        #self.tabella.setContentsMargins(0,100,0,0)
        self.tabella.setHorizontalHeaderLabels(["LUNEDI","MARTEDI","MERCOLEDI","VENERDI","SABATO","DOMENICA"])
        self.tabella.setVerticalHeaderLabels(["TURNO PRANZO\n12:30-15:30","TURNO CENA\n19:30-00.30"])

        self.pulsante_back = crea_pulsante_img(35,"png/back.png")

        clock = QLabel()
        img = QPixmap("png/check.png").scaled(35,35)
        clock.setPixmap(img)

        self.label_date = QLabel(self)
        self.label_date.setFont(label_font_piccolo)
        self.label_time = QLabel(self)
        self.label_time.setFont(label_font_piccolo)

        # Imposta il timer per aggiornare l'orario ogni secondo
        timer = QTimer(self)
        timer.timeout.connect(self.update_datetime)
        timer.start(1000)

        layout = QVBoxLayout()
        layout_title = QHBoxLayout()

        layout_title.addWidget(title,alignment=Qt.AlignmentFlag.AlignTop)
        layout_title.addStretch()
        layout_title.addWidget(self.label_date,alignment=Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        layout_title.addWidget(self.label_time,alignment=Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        layout_title.addWidget(clock,alignment=Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        layout.addLayout(layout_title)
        layout.addWidget(self.tabella,alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addSpacing(65)
        layout.addWidget(self.pulsante_back,alignment=Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)

        self.setLayout(layout)
        self.setFixedSize(994,637)
        self.setContentsMargins(20,20,20,10)


    def update_datetime(self):
        # Ottieni la data e l'orario corrente
        current_datetime = QDateTime.currentDateTime()
        current_date = current_datetime.toString('dddd')
        current_time = current_datetime.toString('hh:mm')

        # Aggiorna le etichette con la data e l'orario corrente
        self.label_date.setText(f' {current_date}')
        self.label_time.setText(f' {current_time}')



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
        font-size: 17px;
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
window = VistaTurniPersonale()
window.show()
sys.exit(app.exec())