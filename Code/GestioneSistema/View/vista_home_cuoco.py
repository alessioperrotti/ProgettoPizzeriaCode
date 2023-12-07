import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap, QIcon
from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout, QApplication, QSizePolicy, QHBoxLayout,
                             QGridLayout, QTableWidget, QHeaderView)

label_font = QFont("Roboto", 24)
label_font_tit = QFont("Roboto", 32, weight=50)
label_font_piccolo = QFont("Roboto", 14)


def crea_pulsante(nome, directory):
    pulsante = QPushButton()
    label = QLabel(nome)
    label.setFont(label_font_piccolo)
    label.setStyleSheet("""QLabel{color: "white"}""")
    layout = QHBoxLayout()
    layout.addStretch()
    layout.addWidget(crea_immagine(directory, 50))
    layout.addWidget(label)
    layout.addStretch()
    pulsante.setLayout(layout)
    pulsante.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
    pulsante.setStyleSheet("""
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
    """)
    pulsante.setFixedSize(250, 200)
    return pulsante


def crea_immagine(directory, dimensione):
    label_foto = QLabel()
    pixmap = QPixmap(directory)
    scaled_pixmap = pixmap.scaled(dimensione, dimensione, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
    label_foto.setPixmap(scaled_pixmap)
    return label_foto


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
                background-color: rgba(0, 0, 0, 0);
                color: "white";
                text-align: center;
                border-radius: 6px;
            }
            QPushButton:hover{
                background-color: "lightgray";
            }
            """)
    return pulsante_back


class VistaHomeCuoco(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        # definizione oggetti
        label = QLabel("ACCESSO: Cuoco")
        label.setFont(label_font_tit)
        self.p_comande = crea_pulsante("Lista Comande", "png_icone/menu.png")  # cambiare icona
        self.p_turni = crea_pulsante("Visualizza Turni", "png_icone/turni.png")
        self.pulsante_back = crea_pulsante_back(35, "png/back.png")

        # definizione layout
        layout = QVBoxLayout()
        griglia = QGridLayout()
        layout_centrale = QHBoxLayout()
        layout_orizzontale = QHBoxLayout()

        # inserimento oggetti nei layout
        layout_centrale.addStretch()
        layout_centrale.addLayout(griglia)
        layout_centrale.addStretch()

        griglia.addWidget(self.p_comande, 1, 1)
        griglia.addWidget(self.p_turni, 1, 2)

        layout.addSpacing(10)
        layout.addWidget(label)
        layout.addStretch()

        layout.addLayout(layout_centrale)
        layout.addSpacing(170)

        layout.addWidget(self.pulsante_back, alignment=Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignBottom)

        layout_orizzontale.addLayout(layout)
        layout_orizzontale.addSpacing(20)

        self.setFixedSize(994, 637)
        self.setLayout(layout_orizzontale)
        self.setContentsMargins(20, 20, 20, 10)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    vista = VistaHomeCuoco()
    vista.show()
    sys.exit(app.exec())
