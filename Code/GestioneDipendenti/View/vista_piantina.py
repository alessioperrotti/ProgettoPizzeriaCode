import sys

from PyQt6.QtCore import Qt, QDateTime, QTimer
from PyQt6.QtGui import QFont, QPixmap, QIcon
from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout, QApplication, QSizePolicy, QHBoxLayout,
                             QGridLayout, QTableWidget, QHeaderView, QSpacerItem, QLineEdit, QTableWidgetItem,
                             QScrollBar, QScrollArea, QAbstractItemView, QDialog, QFrame)

# Font
label_font = QFont("Roboto", 24)
label_font_tit = QFont("Roboto", 32, weight=50)
label_font_piccolo = QFont("Roboto", 16)
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


def on_tavolo_clicked(nome):
    print(f"Tavolo {nome} cliccato!")


class VistaPiantina(QDialog):

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
                font-size: 23px;
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

    def init_ui(self):
        title = QLabel("Piantina")
        title.setFont(label_font_tit)

        label_liberi = QLabel("LIBERI")
        label_prenotati = QLabel("PRENOTATI")
        label_occupati = QLabel("OCCUPATI")
        label_inattesa = QLabel("IN ATTESA")
        label_serviti = QLabel("SERVITI")

        linea = QFrame()
        linea.setFrameShape(QFrame.Shape.VLine)
        linea.setFixedHeight(637)

        self.pulsante_back = crea_pulsante_back(35, "png/back.png")
        self.pulsante_consegna = QPushButton("Consegna")
        self.pulsante_consegna.setFont(label_font_piccolo)
        self.pulsante_consegna.setFixedSize(190, 65)

        self.label_date = QLabel(self)
        self.label_date.setFont(label_font_piccolo)
        self.label_time = QLabel(self)
        self.label_time.setFont(label_font_piccolo)

        # self.tav1 = QPushButton("1")
        # self.tav2 = QPushButton("2")
        # self.tav3 = QPushButton("3")
        # self.tav4 = QPushButton("4")
        # self.tav5 = QPushButton("5")
        # self.tav6 = QPushButton("6")
        # self.tav7 = QPushButton("7")
        # self.tav8 = QPushButton("8")
        # self.tav9 = QPushButton("9")
        # self.tav10 = QPushButton("10")
        # self.tav11 = QPushButton("11")
        # self.tav12 = QPushButton("12")
        # self.tav13 = QPushButton("13")
        # self.tav14 = QPushButton("14")
        # self.tav15 = QPushButton("15")
        # self.tav16 = QPushButton("16")
        # self.tav17 = QPushButton("17")

        # Imposta il timer per aggiornare l'orario ogni secondo
        timer = QTimer(self)
        timer.timeout.connect(self.update_datetime)
        timer.start(1000)

        layout = QVBoxLayout()
        layout_title = QHBoxLayout()
        layout_h = QHBoxLayout()
        layout_griglia = QGridLayout()
        layout_griglia.setSpacing(20)
        layout_v_dx = QVBoxLayout()

        layout.addLayout(layout_title)
        layout_title.addWidget(title, alignment=Qt.AlignmentFlag.AlignTop)
        layout_title.addStretch()
        layout_title.addWidget(self.label_date, alignment=Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop)
        layout_title.addWidget(self.label_time, alignment=Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop)
        # layout_title.addWidget(clock, alignment=Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        layout_h.addSpacing(0)
        layout_h.addLayout(layout_griglia)
        layout_h.addWidget(linea, alignment=Qt.AlignmentFlag.AlignRight)
        layout_h.addLayout(layout_v_dx)

        layout_v_dx.addWidget(label_liberi)
        layout_v_dx.addWidget(label_prenotati)
        layout_v_dx.addWidget(label_occupati)
        layout_v_dx.addWidget(label_inattesa)
        layout_v_dx.addWidget(label_serviti)
        layout_v_dx.addWidget(self.pulsante_consegna)
        layout_v_dx.addSpacing(200)
        layout_v_dx.addWidget(self.pulsante_back, alignment=Qt.AlignmentFlag.AlignRight)

        for row in range(4):
            for col in range(4):
                tavolo_label = QLabel(f"Tavolo {row * 4 + col + 1}")
                tavolo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                tavolo_label.setFrameShape(QFrame.Shape.Box)  # Aggiunge un bordo per evidenziare la cliccabilità
                tavolo_label.setStyleSheet("QLabel { background-color : lightblue; }")  # Imposta lo stile
                tavolo_label.setCursor(Qt.CursorShape.PointingHandCursor)  # Cambia il cursore al puntatore della mano
                tavolo_label.mousePressEvent = lambda event, nome=tavolo_label.text(): on_tavolo_clicked(nome)
                layout_griglia.addWidget(tavolo_label, row, col)

                # Imposta larghezza e altezza uguali per fare in modo che le dimensioni siano quadrate
                tavolo_label.setFixedSize(150, 100)

        # layout_griglia.addWidget(self.tav1, 0, 0,2,0)
        # layout_griglia.addWidget(self.tav2, 0, 1,2,0)
        # layout_griglia.addWidget(self.tav3, 0, 2,2,0)
        # layout_griglia.addWidget(self.tav4, 0, 3,2,0)
        # layout_griglia.addWidget(self.tav5, 1, 0)
        # layout_griglia.addWidget(self.tav6, 1, 1)
        # layout_griglia.addWidget(self.tav7, 1, 2)
        # layout_griglia.addWidget(self.tav8, 1, 3)
        # layout_griglia.addWidget(self.tav9, 2, 0)
        # layout_griglia.addWidget(self.tav10, 2, 1)
        # layout_griglia.addWidget(self.tav11, 2, 2)
        # layout_griglia.addWidget(self.tav12, 2, 3)
        # layout_griglia.addWidget(self.tav13, 3, 0)
        # layout_griglia.addWidget(self.tav14, 3, 1)
        # layout_griglia.addWidget(self.tav15, 3, 2)
        # layout_griglia.addWidget(self.tav16, 3, 3)
        # layout_griglia.addWidget(self.tav17, 4, 0)

        layout.addLayout(layout_h)
        layout.addStretch()

        self.setLayout(layout)
        self.setFixedSize(994, 637)
        self.setContentsMargins(20, 0, 10, 10)

    def update_datetime(self):
        # Ottieni la data e l'orario corrente
        current_datetime = QDateTime.currentDateTime()
        current_date = current_datetime.toString('dddd')
        current_time = current_datetime.toString('hh:mm')

        # Aggiorna le etichette con la data e l'orario corrente
        self.label_date.setText(f' {current_date}')
        self.label_time.setText(f' {current_time}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VistaPiantina()
    window.show()
    sys.exit(app.exec())
