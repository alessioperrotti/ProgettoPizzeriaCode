import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap, QIcon
from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout, QApplication, QSizePolicy, QHBoxLayout,
                             QGridLayout, QTableWidget, QHeaderView, QSpacerItem, QLineEdit, QTableWidgetItem,
                             QScrollBar, QScrollArea, QAbstractItemView, QDialog)

from Code.GestioneDipendenti.View.vista_inserisci_dipendente import VistaInserisciDipendente
from Code.GestioneDipendenti.View.vista_visualizza_dipendente import VistaVisualizzaDipendente

# Font
label_font = QFont("Roboto", 24)
label_font_tit = QFont("Roboto", 32, weight=50)
label_font_piccolo = QFont("Roboto", 10)
header_font = QFont("Roboto", 10)
header_font.setBold(True)


def crea_tabella(righe, colonne, larghezza, altezza):
    tabella = QTableWidget()
    tabella.setRowCount(righe)
    tabella.setColumnCount(colonne)
    header = tabella.horizontalHeader()
    header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
    tabella.verticalHeader().setVisible(False)
    tabella.setFixedSize(larghezza, altezza)
    tabella.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
    return tabella


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
            }
            QPushButton:hover{
                background-color: "lightgray";
            }
            """)
    return pulsante_back


class VistaGestioneDipendenti(QDialog):

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
                font-size: 13px;
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
        # self.show()

    def init_ui(self):
        self.setWindowTitle("Gestionale Pizzeria")
        title = QLabel("Gestione Dipendenti")
        title.setFont(label_font_tit)

        layout = QVBoxLayout()
        layout_orizzontale = QHBoxLayout()
        layout_pulsanti = QVBoxLayout()
        #Pulsanti
        self.pulsante_mostra = QPushButton("Mostra info\ndipendente")
        self.pulsante_mostra.setFixedSize(147, 49)
        self.pulsante_mostra.setEnabled(False)

        self.pulsante_modifica = QPushButton("Modifica\ndipendente")
        self.pulsante_modifica.setFixedSize(147, 49)
        self.pulsante_modifica.setEnabled(False)

        self.pulsante_aggiungi = QPushButton("Aggiungi\nnuovo dipendente")
        self.pulsante_aggiungi.setFixedSize(147, 49)

        self.pulsante_elimina = QPushButton("Elimina\ndipendente")
        self.pulsante_elimina.setFixedSize(147, 49)
        self.pulsante_elimina.setEnabled(False)

        # Pulsante Back
        self.pulsante_back = crea_pulsante_back(35, "png/back.png")

        # Tabella
        self.tab = crea_tabella(0, 2, 481, 404)
        self.tab.setHorizontalHeaderLabels(["NOME", "RUOLO"])
        self.tab.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tab.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

        layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignTop)

        layout_orizzontale.addWidget(self.tab, alignment=Qt.AlignmentFlag.AlignLeft)
        layout_orizzontale.addLayout(layout_pulsanti)

        # Sistemo i Pulsanti
        layout_pulsanti.addStretch()
        layout_pulsanti.addWidget(self.pulsante_mostra, alignment=Qt.AlignmentFlag.AlignCenter)
        layout_pulsanti.addSpacing(10)
        layout_pulsanti.addWidget(self.pulsante_modifica, alignment=Qt.AlignmentFlag.AlignCenter)
        layout_pulsanti.addSpacing(10)
        layout_pulsanti.addWidget(self.pulsante_aggiungi, alignment=Qt.AlignmentFlag.AlignCenter)
        layout_pulsanti.addSpacing(10)
        layout_pulsanti.addWidget(self.pulsante_elimina, alignment=Qt.AlignmentFlag.AlignCenter)
        layout_pulsanti.addStretch()

        layout.addLayout(layout_orizzontale)
        layout.addWidget(self.pulsante_back)

        layout.setContentsMargins(30, 20, 10, 20)
        self.setFixedSize(756, 637)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VistaGestioneDipendenti()
    window.show()
    sys.exit(app.exec())
