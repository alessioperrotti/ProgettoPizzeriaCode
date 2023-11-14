import sys
# tab: 481,404
# button: 147,49
# search_label: 336
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout, QApplication, QSizePolicy, QHBoxLayout,
                             QGridLayout, QTableWidget, QHeaderView, QSpacerItem, QLineEdit, QTableWidgetItem,
                             QScrollBar, QScrollArea)

label_font = QFont("Roboto", 24)
label_font_tit = QFont("Roboto", 32, weight=50)
label_font_piccolo = QFont("Roboto", 10)
header_font = QFont("Roboto",10)


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
    pulsante.setFixedSize(147, 49)
    return pulsante
def crea_immagine(directory, dimensione):
    label_foto = QLabel()
    pixmap = QPixmap(directory)
    scaled_pixmap = pixmap.scaled(dimensione, dimensione, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
    label_foto.setPixmap(scaled_pixmap)
    return label_foto
from PyQt6.QtWidgets import QTableWidget, QHeaderView
from PyQt6.QtGui import QFont


def crea_tabella(n_colonne, larghezza, altezza, parent=None):

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

    # Imposta il numero di colonne
    tabella.setColumnCount(n_colonne)

    # Crea l'intestazione
    header = tabella.horizontalHeader()
    header.setFont(header_font)
    font = header.font()
    font.setBold(True)
    header.setFont(font)
    header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    # Imposta le dimensioni della tabella
    tabella.setFixedWidth(larghezza)
    tabella.setFixedHeight(altezza)

    return tabella

class VistaGestisciDipendenti(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Layout principale
        label= QLabel("Gestione Dipendenti")
        label.setFont(label_font_tit)

        # Creazione dei bottoni
        pulsante_mostra = crea_pulsante("Mostra info\ndipendente")
        pulsante_modifica = crea_pulsante("Modifica\ndipendente")
        pulsante_inserisci = crea_pulsante("Inserisci nuovo\ndipendente")
        pulsante_elimina = crea_pulsante("Elimina\ndipendente")
        back = crea_immagine("png/back.png", 35)

        #Layout
        layout = QVBoxLayout()
        layout_pulsanti = QVBoxLayout()
        griglia = QGridLayout()
        layout_tabella = QHBoxLayout()

        tabella = crea_tabella(2, 481,404)
        tabella.setHorizontalHeaderLabels(["NOME", "RUOLO"])

        # Crea l'area di scorrimento e incorpora la tabella al suo interno
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(tabella)
        layout_tabella.addWidget(scroll_area, alignment=Qt.AlignmentFlag.AlignLeft)
        scroll_area.setFixedSize(501, 380)

        #Posiziono oggetti
        layout.setContentsMargins(20,0,10,0)
        layout.addWidget(label)
        layout.addStretch()

        #layout_tabella.addWidget(tabella,alignment=Qt.AlignmentFlag.AlignLeft)

        griglia.addWidget(pulsante_mostra,1,1)
        griglia.addWidget(pulsante_modifica ,2,1)
        griglia.addWidget(pulsante_inserisci,3,1)
        griglia.addWidget(pulsante_elimina,4,1)

        layout.addLayout(layout_tabella)
        layout.addStretch()
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
    window = VistaGestisciDipendenti()
    app.exec()
