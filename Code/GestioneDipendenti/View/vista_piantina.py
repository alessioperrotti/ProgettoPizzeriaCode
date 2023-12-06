import sys

from PyQt6.QtCore import Qt, QDateTime, QTimer
from PyQt6.QtGui import QFont, QPixmap, QIcon
from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout, QApplication, QSizePolicy, QHBoxLayout,
                             QGridLayout, QTableWidget, QHeaderView, QSpacerItem, QLineEdit, QTableWidgetItem,
                             QScrollBar, QScrollArea, QAbstractItemView, QDialog, QFrame)

# Font
label_font = QFont("Roboto", 12)
label_font_tit = QFont("Roboto", 32, weight=50)
label_font_piccolo = QFont("Roboto", 16)
header_font = QFont("Roboto", 10)
header_font.setBold(True)


def crea_etichetta(testo, colore_pulsante):
    layout_h = QHBoxLayout()

    etichetta = QLabel(testo)
    etichetta.setFont(label_font)

    pulsante = QPushButton()
    pulsante.setFixedSize(25, 25)
    pulsante.setStyleSheet(f"""
        QPushButton {{
            background-color: {colore_pulsante};
            border-radius: 2px;
        }}
    """)

    layout_h.addWidget(pulsante)
    layout_h.addWidget(etichetta)

    return layout_h


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


class VistaPiantina(QDialog):

    def __init__(self):
        super().__init__()
        self.nome_tavoli_map = {}
        self.nome_tavoli = []
        self.init_ui()
        self.n_tavolo = None
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
        """)

    def init_ui(self):
        title = QLabel("Piantina")
        title.setFont(label_font_tit)

        label_liberi = crea_etichetta("LIBERI", "grey")
        label_prenotati = crea_etichetta("PRENOTATI", "#007fff")
        label_occupati = crea_etichetta("OCCUPATI", "red")
        label_inattesa = crea_etichetta("IN ATTESA", "orange")
        label_serviti = crea_etichetta("SERVITI", "yellow")

        linea_v = QFrame()
        linea_v.setFrameShape(QFrame.Shape.VLine)
        linea_v.setFixedHeight(637)

        self.pulsante_back = crea_pulsante_back(35, "png/back.png")
        self.pulsante_consegna = QPushButton("Consegna")
        self.pulsante_consegna.setEnabled(False)
        self.pulsante_consegna.setFont(label_font_piccolo)
        self.pulsante_consegna.setFixedSize(190, 65)

        self.label_date = QLabel(self)
        self.label_date.setFont(label_font_piccolo)
        self.label_time = QLabel(self)
        self.label_time.setFont(label_font_piccolo)

        # Imposta il timer per aggiornare l'orario ogni secondo
        timer = QTimer(self)
        timer.timeout.connect(self.update_datetime)
        timer.start(1000)

        clock = QLabel()
        img = QPixmap("png/clock.png").scaled(35, 35)
        clock.setPixmap(img)

        layout = QVBoxLayout()
        layout_title = QHBoxLayout()
        layout_h = QHBoxLayout()
        layout_griglia = QGridLayout()
        layout_griglia.setSpacing(30)
        layout_v_dx = QVBoxLayout()

        layout.addLayout(layout_title)
        layout_title.addWidget(title, alignment=Qt.AlignmentFlag.AlignTop)
        layout_title.addStretch()
        layout_title.addWidget(self.label_date, alignment=Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        layout_title.addWidget(self.label_time, alignment=Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        layout_title.addWidget(clock, alignment=Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        layout_h.addLayout(layout_griglia)
        layout_h.addSpacing(130)
        layout_h.addWidget(linea_v, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout_h.addLayout(layout_v_dx)

        layout_v_dx.addSpacing(15)
        layout_v_dx.addLayout(label_liberi)
        layout_v_dx.addLayout(label_prenotati)
        layout_v_dx.addLayout(label_occupati)
        layout_v_dx.addLayout(label_inattesa)
        layout_v_dx.addLayout(label_serviti)
        layout_v_dx.addSpacing(15)
        layout_v_dx.addWidget(self.pulsante_consegna, alignment=Qt.AlignmentFlag.AlignCenter)
        layout_v_dx.addSpacing(200)
        layout_v_dx.addWidget(self.pulsante_back, alignment=Qt.AlignmentFlag.AlignRight)

        for row in range(5):
            for col in range(4):
                tavolo_numero = row * 4 + col + 1

                if tavolo_numero <= 4:
                    size = (170, 70)
                elif tavolo_numero <= 8:
                    size = (125, 70)
                elif tavolo_numero <= 12:
                    size = (100, 70)
                else:
                    size = (70, 70)

                if tavolo_numero <= 16:
                    tavolo_button = QPushButton(f"{tavolo_numero}")
                    layout_griglia.addWidget(tavolo_button, col, row, alignment=Qt.AlignmentFlag.AlignCenter)
                    tavolo_button.setCheckable(True)
                    self.nome_tavoli_map[tavolo_numero] = tavolo_button
                    tavolo_button.clicked.connect(
                        lambda checked, n_tavolo=tavolo_button.text(): self.on_tavolo_clicked(n_tavolo))
                    tavolo_button.setFixedSize(*size)
                    self.nome_tavoli.append(tavolo_button)

        layout.addLayout(layout_h)
        layout.addStretch()

        self.setLayout(layout)
        self.setFixedSize(994, 637)
        self.setContentsMargins(20, 0, 15, 10)

    def on_tavolo_clicked(self, nome):
        print(nome)
        self.n_tavolo = nome
        for button in self.nome_tavoli:
            if button.text() != nome:
                button.setChecked(False)
        self.pulsante_consegna.setEnabled(True)

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
