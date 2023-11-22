import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

font_tit = QFont("Roboto", 24, weight=50)
font_label = QFont("Roboto", 18, weight=350)

class VistaModificaMateriaPrima(QDialog):

    def __init__(self):

        super().__init__()
        self.initUI()
        self.show()
        self.setStyleSheet("""
        QPushButton{
            background-color: "#ff776d";
            color: "white";
            text-align: center;
            border-radius: 6px;
        }
        QPushButton:hover{
            background-color: "red";
            font-size: 18px;
        }
        QTableWidget {
            background-color: white;
            alternate-background-color: white;
            selection-background-color: darkcyan;
            border: 2px solid grey;
        }
    """)


    def initUI(self):

        main_layout = QVBoxLayout(self)
        grid1 = QGridLayout()
        grid2 = QGridLayout()
        hbox = QHBoxLayout()
        hbox_v1 = QVBoxLayout()
        hbox_v2 = QVBoxLayout()
        hbox_conferma = QHBoxLayout()

        label_titolo = QLabel("<b>Modifica Materia Prima</b>")
        label_titolo.setFont(font_tit)
        label_titolo.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        linea = QFrame()
        linea.setFrameShape(QFrame.Shape.HLine)

        label_codice = QLabel("<b>Codice:</b>")
        label_codice.setFont(font_label)
        self.label_codice2 = QLabel()
        self.label_codice2.setFixedSize(287,30)
        grid1.addWidget(label_codice, 1, 1)
        grid1.addWidget(self.label_codice2,2, 1)

        label_nome = QLabel("<b>Nome:</b>")
        label_nome.setFont(font_label)
        self.label_nome2 = QLabel()
        self.label_nome2.setFixedSize(287, 30)
        grid1.addWidget(label_nome, 1, 2)
        grid1.addWidget(self.label_nome2, 2, 2)

        hbox_v1.addSpacerItem(QSpacerItem(130, 130))

        label_costoAlKg = QLabel("Costo al Kg:")
        label_costoAlKg.setFont(font_label)
        self.campo_costoAlKg = QLineEdit()
        self.campo_costoAlKg.setFixedSize(287, 30)
        hbox_v1.addWidget(label_costoAlKg, alignment=Qt.AlignmentFlag.AlignVCenter)
        hbox_v1.addWidget(self.campo_costoAlKg, alignment=Qt.AlignmentFlag.AlignVCenter)

        hbox_v1.addSpacerItem(QSpacerItem(40, 40))

        label_qtaDisp = QLabel("Quantità disponibile:")
        label_qtaDisp.setFont(font_label)
        self.campo_qtaDisp = QLineEdit()
        self.campo_qtaDisp.setFixedSize(287, 30)
        hbox_v1.addWidget(label_qtaDisp, alignment=Qt.AlignmentFlag.AlignVCenter)
        hbox_v1.addWidget(self.campo_qtaDisp, alignment=Qt.AlignmentFlag.AlignVCenter)

        hbox_v1.addSpacerItem(QSpacerItem(33, 33))
        hbox_v2.addSpacerItem(QSpacerItem(30, 30))

        label_dataScadenza = QLabel("Data di scadenza:")
        label_dataScadenza.setFont(font_label)
        self.campo_dataScadenza = QCalendarWidget()
        self.campo_dataScadenza.setFixedSize(287,168)
        self.campo_dataScadenza.setStyleSheet("""
                    QCalendarWidget QWidget {
                        background-color: white;
                        color: black;
                    }

                    QCalendarWidget QToolButton {
                        color: black;
                        background-color: white;
                        border: 1px solid white;
                        border-radius: 4px;
                        padding: 5px;
                        font-size: 14px;
                    }

                    QCalendarWidget QToolButton:hover {
                        background-color: #d0d0d0;
                    }

                    QCalendarWidget QDateEdit {
                        color: black;
                        background-color: white;
                    }

                    QCalendarWidget QTableView {
                        alternate-background-color: #f0f0f0;
                    }

                    QCalendarWidget QTableView::item:selected {
                        background-color: #c0c0c0;
                    }
                """)

        hbox_v2.addWidget(label_dataScadenza)
        hbox_v2.addWidget(self.campo_dataScadenza)
        hbox_v2.addSpacerItem(QSpacerItem(50,50))

        label_qtaLimite = QLabel("Quantità limite:")
        label_qtaLimite.setFont(font_label)
        self.campo_qtaLimite = QLineEdit()
        self.campo_qtaLimite.setFixedSize(287, 30)
        grid2.addWidget(label_qtaLimite, 1, 1)
        grid2.addWidget(self.campo_qtaLimite, 2, 1)


        label_qtaOrdineSTD = QLabel("Quantità standard dell'ordine:")
        label_qtaOrdineSTD.setFont(font_label)
        self.campo_qtaOrdineSTD = QLineEdit()
        self.campo_qtaOrdineSTD.setFixedSize(287, 30)
        grid2.addWidget(label_qtaOrdineSTD, 1, 2)
        grid2.addWidget(self.campo_qtaOrdineSTD, 2, 2)

        self.pulsante_conferma = QPushButton("Conferma Modifica")
        self.pulsante_conferma.setFixedSize(206,89)
        self.pulsante_conferma.setFont(font_label)
        hbox_conferma.addWidget(self.pulsante_conferma)

        hbox.addLayout(hbox_v1)
        hbox.addLayout(hbox_v2)
        main_layout.addWidget(label_titolo, alignment=Qt.AlignmentFlag.AlignTop)
        main_layout.addWidget(linea)
        main_layout.addSpacerItem(QSpacerItem(20,20))
        main_layout.addLayout(grid1)
        main_layout.addLayout(hbox)
        main_layout.addLayout(grid2)
        main_layout.addSpacerItem(QSpacerItem(30, 30))
        main_layout.addLayout(hbox_conferma)

        self.setFixedSize(690,651)
        self.setLayout(main_layout)


def main():
    app = QApplication(sys.argv)
    ex = VistaModificaMateriaPrima()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

