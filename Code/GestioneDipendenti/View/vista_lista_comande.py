import sys

from PyQt6.QtCore import Qt, QTimer, QDateTime
from PyQt6.QtGui import QFont, QPixmap, QIcon
from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout, QApplication, QSizePolicy, QHBoxLayout,
                             QGridLayout, QTableWidget, QHeaderView, QSpacerItem, QLineEdit, QTableWidgetItem,
                             QScrollBar, QScrollArea, QAbstractItemView, QDialog)


# Font
label_font = QFont("Roboto", 24)
label_font_tit = QFont("Roboto", 32, weight=50)
label_font_piccolo = QFont("Roboto", 10)
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

class VistaListaComande(QDialog):



    def __init__(self):
        super().__init__()

        self.label_time = None
        self.label_date = None
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
    def update_datetime(self):
        current_datetime = QDateTime.currentDateTime()
        current_date = current_datetime.toString('dddd')
        current_time = current_datetime.toString('hh:mm')

        # Aggiorna le etichette con la data e l'orario corrente

        self.giorno_ora.setText(f' {current_date} {current_time}')



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

    def init_ui(self):
        titolo = QLabel("Lista Comande:")
        titolo.setFont(label_font_tit)
        self.giorno_ora = QLabel()
        self.giorno_ora.setFont(label_font_tit)

        self.layout = QVBoxLayout()
        layout1 = QHBoxLayout()
        layout1.addWidget(titolo)
        layout1.addStretch()
        layout1.addWidget(self.giorno_ora)
        self.lay_orizz = QHBoxLayout()
        self.scroll_area = QScrollArea()
        self.grid = QGridLayout()
        #self.grid.addWidget(QLabel("c"), 0 ,0)
        self.pulsante_back = crea_pulsante_back(35, "png/back.png")
        self.contenitore  = QWidget()
        self.contenitore.setLayout(self.grid)

        self.scroll_area.setWidget(self.contenitore)
        self.scroll_area.setWidgetResizable(True)

        self.layout_scroll_area = QVBoxLayout()
        self.layout_scroll_area.addWidget(self.scroll_area)
        self.lay_orizz.addLayout(self.layout_scroll_area)
        self.lay_orizz.addSpacing(10)
        self.lay_orizz.addWidget(self.pulsante_back, alignment=Qt.AlignmentFlag.AlignBottom)



        self.layout.addLayout(layout1)
        self.layout.addSpacing(20)
        self.layout.addLayout(self.lay_orizz)









       # layout1.addWidget(self.orologio)

        timer = QTimer(self)
        timer.timeout.connect(self.update_datetime)
        timer.start(1000)

        self.setContentsMargins(15, 10, 15,10)
        self.setFixedSize(994, 637)
        self.setLayout(self.layout)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VistaListaComande()
    window.show()
    sys.exit(app.exec())