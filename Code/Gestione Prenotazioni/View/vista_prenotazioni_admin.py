import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout, QApplication, QSizePolicy, QHBoxLayout,
                             QGridLayout, QTableWidget, QHeaderView, QSpacerItem, QLineEdit, QTableWidgetItem)

label_font = QFont("Roboto", 24)
label_font_tit = QFont("Roboto", 32, weight=50)
label_font_piccolo = QFont("Roboto", 14)

def crea_pulsante(nome):
    pulsante = QPushButton()
    label = QLabel(nome)
    label.setFont(label_font_piccolo)
    layout = QHBoxLayout()
    layout.addStretch()
    layout.addWidget(label)
    layout.addStretch()
    pulsante.setLayout(layout)
    pulsante.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
    pulsante.setStyleSheet(
        "color:white; background-color: #ff776d ;text-align: center; border-radius: 6px")  # testo bianco senza bordo
    pulsante.setFixedSize(150, 75)
    return pulsante
def crea_immagine(directory, dimensione):
    label_foto = QLabel()
    pixmap = QPixmap(directory)
    scaled_pixmap = pixmap.scaled(dimensione, dimensione, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
    label_foto.setPixmap(scaled_pixmap)
    return label_foto
from PyQt6.QtWidgets import QTableWidget, QHeaderView
from PyQt6.QtGui import QFont

def Tabella(n_colonne, larghezza, altezza, parent=None):
    tabella = QTableWidget(parent)
    tabella.setStyleSheet("""
        QTableWidget {
            background-color: white;
            alternate-background-color: white;
            selection-background-color: darkcyan;
            border: 2px solid black;
        }

        QTableWidget::item {
            border: 1px solid black;
        } 

        QHeaderView::section {
            background-color: lightgray;
        }
    """)

    tabella.setColumnCount(n_colonne)

    header = tabella.horizontalHeader()
    header.setFont(label_font_piccolo)  # Sostituisci con la tua fonte desiderata
    header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)

    # Aggiungi il contenuto delle colonne
    for i in range(1, n_colonne):
        header.setSectionResizeMode(i, QHeaderView.ResizeMode.ResizeToContents)

    tabella.setFixedWidth(larghezza)
    tabella.setFixedHeight(altezza)

    return tabella

class VistaPrenotazioniAdmin(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Layout principale
        label= QLabel("Gestione Prenotazioni")
        label.setFont(label_font_tit)

        # Campo di ricerca
        search_label = QLabel('Cerca:')
        search_label.setFont(label_font_piccolo)
        search_edit = QLineEdit()
        search_edit.setFixedWidth(400)

        # Creazione dei bottoni
        pulsante_modifica = crea_pulsante("Modifica\nprenotazione")
        pulsante_aggiungi = crea_pulsante("Aggiungi\nprenotazione")
        pulsante_elimina = crea_pulsante("Elimina\nprenotazione")
        back = crea_immagine("png/back.png", 35)

        #Layout
        layout = QVBoxLayout()
        layout_pulsanti = QVBoxLayout()
        griglia = QGridLayout()
        layout_tabella = QHBoxLayout()

        tabella = Tabella(6, 560, 400)
        tabella.setHorizontalHeaderLabels(["NOME CLIENTE","TAVOLO","ORARIO","GIORNO","POSTI","CODICE"])
        tabella.setFont(label_font_piccolo)

        #Posiziono oggetti
        layout.setContentsMargins(20,0,10,0)
        layout.addWidget(label)
        layout.addWidget(search_label)
        layout.addWidget(search_edit)

        layout_tabella.addWidget(tabella,alignment=Qt.AlignmentFlag.AlignLeft)

        griglia.addWidget(pulsante_modifica,1,1)
        griglia.addWidget(pulsante_aggiungi ,2,1)
        griglia.addWidget(pulsante_elimina,3,1)

        layout.addLayout(layout_tabella)
        layout_tabella.addLayout(layout_pulsanti)
        layout_pulsanti.addLayout(griglia)
        layout_pulsanti.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(back)
        layout.addSpacing(10)

        self.setLayout(layout)
        self.setFixedSize(756,637)
        self.show()

if __name__ == '__main__':
    app = QApplication([])
    window = VistaPrenotazioniAdmin()
    app.exec()
