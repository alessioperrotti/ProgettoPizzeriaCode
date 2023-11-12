import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout, QApplication, QSizePolicy, QHBoxLayout,
                             QGridLayout, QTableWidget, QHeaderView, QSpacerItem)

label_font = QFont("Roboto", 24)
label_font_tit = QFont("Roboto", 32, weight=50)
label_font_piccolo = QFont("Roboto", 14)


def crea_pulsante(nome, directory):
    pulsante = QPushButton()
    label = QLabel(nome)
    label.setFont(label_font_piccolo)
    layout = QHBoxLayout()
    # spacer_item = QSpacerItem(20, 1, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
    # layout.addItem(spacer_item)
    layout.addStretch()
    layout.addWidget(crea_immagine(directory, 50))
    layout.addWidget(label)
    layout.addStretch()
    #layout.setAlignment(crea_immagine(directory, 50), Qt.AlignmentFlag.AlignLeft)
    pulsante.setLayout(layout)
    pulsante.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
    pulsante.setStyleSheet(
        "color:white;background-color: #ff776d; border: 2px; border-radius: 6px;")  # testo bianco senza bordo,png nero
    pulsante.setFixedSize(250, 200)
    return pulsante


def crea_immagine(directory, dimensione):
    label_foto = QLabel()
    pixmap = QPixmap(directory)
    scaled_pixmap = pixmap.scaled(dimensione, dimensione, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
    label_foto.setPixmap(scaled_pixmap)
    return label_foto


class VistaHomeCuoco(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        # definizione oggetti
        label = QLabel("ACCESSO: Cameriere")
        label.setFont(label_font_tit)
        pulsante1 = crea_pulsante("Piantina", "png/piantinaTavoli.png")
        pulsante2 = crea_pulsante("Visualizza Turni", "png/turni.png")
        pulsante3 = crea_pulsante("Prenotazioni", "png/turni.png") #cambiare png
        back = crea_immagine("png/back.png", 35)

        # definizione layout
        layout = QVBoxLayout()
        griglia = QGridLayout()
        layout_centrale = QHBoxLayout()
        layout_orizzontale = QHBoxLayout()

        # inserimento oggetti nei layout
        layout_centrale.addStretch()
        layout_centrale.addLayout(griglia)
        layout_centrale.addStretch()

        griglia.addWidget(pulsante1, 1, 1)
        griglia.addWidget(pulsante2, 1, 2)
        griglia.addWidget(pulsante3, 1, 3)


        layout.addSpacing(10)
        layout.addWidget(label)
        layout.addStretch()

        layout.addLayout(layout_centrale)
        layout.addSpacing(170)

        layout.addWidget(back)
        layout.addSpacing(10)

        layout_orizzontale.addSpacing(20)
        layout_orizzontale.addLayout(layout)
        layout_orizzontale.addSpacing(20)

        self.setFixedSize(994, 637)
        self.setLayout(layout_orizzontale)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    vista = VistaHomeCuoco()
    vista.show()
    sys.exit(app.exec())