import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

font_label = QFont("Roboto", 20, weight=350)
font_valore = QFont("Roboto", 20, weight=50)
font_titolo = QFont("Roboto", 24, weight=450)

class VistaMateriaPrima(QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()


    def initUI(self):

        main_layout = QVBoxLayout()
        hbox = QHBoxLayout()
        vbox_nomecampo = QVBoxLayout()
        vbox_valorecampo = QVBoxLayout()

        label_titolo = QLabel("<b>Scheda Dati Materia Prima</b>")
        label_titolo.setFont(font_titolo)
        label_titolo.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        linea = QFrame(self)
        linea.setFrameShape(QFrame.Shape.HLine)

        label_codice1 = QLabel("Codice:")
        label_nome1 = QLabel("Nome:")
        label_costoAlKg1 = QLabel("Costo al Kg:")
        label_dataScadenza1 = QLabel("Data di scadenza:")
        label_qtaDisp1 = QLabel("Quantità\ndisponibile:")
        label_qtaLimite1 = QLabel("Quantità limite:")
        label_qtaOrdineSTD1 = QLabel("Quantità standard\ndell'ordine:")

        labels1 = [label_codice1, label_nome1, label_costoAlKg1, label_dataScadenza1,
                   label_qtaDisp1, label_qtaLimite1, label_qtaOrdineSTD1]

        for x in labels1:
            x.setFixedSize(175, 45)
            vbox_nomecampo.addWidget(x)
            vbox_nomecampo.addSpacerItem(QSpacerItem(175, 20))
            x.setFont(font_label)

        self.label_codice2 = QLabel("valore codice")
        self.label_nome2 = QLabel("valore nome")
        self.label_costoAlKg2 = QLabel("valore costoalkg")
        self.label_dataScadenza2 = QLabel("valore datascadenza:")
        self.label_qtaDisp2 = QLabel("valore qtadisp")
        self.label_qtaLimite2 = QLabel("valore qtalimite")
        self.label_qtaOrdineSTD2 = QLabel("valore qtaordinestd")

        labels2 = [self.label_codice2, self.label_nome2, self.label_costoAlKg2,
                   self.label_dataScadenza2, self.label_qtaDisp2, self.label_qtaLimite2, self.label_qtaOrdineSTD2]

        for x in labels2:
            x.setFixedSize(180, 45)
            vbox_valorecampo.addWidget(x)
            vbox_valorecampo.addSpacerItem(QSpacerItem(175, 20))
            x.setFont(font_valore)

        vbox_nomecampo.addStretch()
        vbox_valorecampo.addStretch()

        main_layout.addWidget(label_titolo, alignment=Qt.AlignmentFlag.AlignTop)
        main_layout.addWidget(linea, alignment=Qt.AlignmentFlag.AlignTop)
        hbox.addLayout(vbox_nomecampo)
        hbox.addLayout(vbox_valorecampo)
        main_layout.addSpacerItem(QSpacerItem(514, 20))
        main_layout.addLayout(hbox)
        main_layout.addStretch()
        self.setFixedSize(514, 626)
        self.setLayout(main_layout)


app = QApplication(sys.argv)
app.setStyleSheet("""
    QPushButton{
        background-color: "#ff776d";
        color: "white";
        text-align: center;
        border-radius: 6px;
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
""")

window = VistaMateriaPrima()
window.show()
sys.exit(app.exec())


