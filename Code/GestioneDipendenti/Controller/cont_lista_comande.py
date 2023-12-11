from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget, QFrame, QVBoxLayout, QLabel, QGridLayout, QStackedWidget, QSizePolicy, QPushButton

from Code.GestioneDipendenti.View.vista_lista_comande import VistaListaComande
from Code.GestioneOrdiniTavolo.Model.gestore_ordini_tavolo import GestoreOrdiniTavolo
from Code.GestioneOrdiniTavolo.Model.ordine_tavolo import OrdineTavolo


class ContListaComande():
    def __init__(self, gestore_ord: GestoreOrdiniTavolo,stacked_widget:QStackedWidget):
        self.view = VistaListaComande()
        self.gestore_ord = gestore_ord
        stacked_widget.addWidget(self.view)
        self.ordine_da_evadere = None
        # self.timer = QTimer(self.view)
        # self.timer.timeout.connect(self.aggiorna_lista)
        # self.timer.start(1000)

    def aggiorna_lista(self):
        griglia = QGridLayout()
        nuovo_cont = QWidget()
        nuovo_cont.setLayout(griglia)
        nuovo_cont.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        #lista di ordini da preparare
        lista_ordini = []

        for ordine in self.gestore_ord.lista_ordini:
            if ordine.pronto == False:
                lista_ordini.append(ordine)

        lista_ordini.sort(key=lambda x: x.orario)


        #per ogni ordine creo un riquadro
        contatore = 0
        if lista_ordini == []:
            self.view.scroll_area.setWidget(nuovo_cont)

        for ordine in lista_ordini:

            riga = contatore // 3
            colonna = contatore % 3

            riquadro = RiquadroOrdine(ordine, self.aggiorna_lista)
            griglia.addWidget(riquadro,riga,colonna)



            self.view.scroll_area.setWidget(nuovo_cont)
            contatore += 1

        self.gestore_ord.salva_ordini_su_file()





class RiquadroOrdine(QWidget):
    def __init__(self,ordine: OrdineTavolo, update_lista):
        self.update = update_lista
        self.ordine = ordine
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.frame = QFrame()
        frame1 = QFrame()
        frame2 = QFrame()
        frame3 = QFrame()

        # self.frame.setFrameShape(QFrame.Shape.Box)
        #self.frame.setStyleSheet(".QFrame {border: 1px solid black; border-radius: 3px; background-color: #FFFFFF;}")
        frame1.setStyleSheet(".QFrame {border: 0.5px solid black; border-radius: 1px; background-color: #ff776d;}")
        frame2.setStyleSheet(".QFrame {border: 0.5px solid black; border-radius: 1px; background-color: #FFFFFF;}")
        frame3.setStyleSheet(".QFrame {border: 0.5px solid black; border-radius: 1px; background-color: #ff776d;}")

        #frame3.setStyleSheet(".border: 1px solid black; border-radius: 5px; padding: 5px")

        layout_frame = QVBoxLayout()
        layout_frame.addWidget(frame1)
        layout_frame.setSpacing(0)
        layout_frame.addWidget(frame2)
        layout_frame.setSpacing(0)
        layout_frame.addWidget(frame3)

        layout_frame.setContentsMargins(0, 0, 0, 0)
        frame1.setFixedWidth(240)
        frame1.setFixedHeight(50)
        frame2.setFixedWidth(240)
        #frame2.setMinimumHeight(160)
        frame2.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        frame3.setFixedWidth(240)

        frame3.setFixedHeight(40)

        layout_frame1 = QVBoxLayout()
        frame1.setLayout(layout_frame1)
        n_tavolo = QLabel("Tavolo " + str(self.ordine.tavolo.numero))
        orario_ordine = QLabel(str(self.ordine.orario.strftime("%H:%M")))
        layout_frame1.addWidget(n_tavolo)
        layout_frame1.addWidget(orario_ordine)

        layout_frame2 = QVBoxLayout()
        frame2.setLayout(layout_frame2)
        self.ordine.lista_prodotti.sort(key=lambda x: x.nome)
        for prodotto in self.ordine.lista_prodotti:
            stringa = (f'<font color="black">&#8226;</font> ' + prodotto.nome)
            lab = QLabel(stringa)
            layout_frame2.addWidget(lab)
        layout_frame2.addStretch()


        layout_frame3 = QVBoxLayout()
        layout_frame3.setContentsMargins(0, 0, 0, 0)
        frame3.setLayout(layout_frame3)
        self.pulsante = QPushButton("EVADI ORDINE")

        self.pulsante.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.pulsante.clicked.connect(self.evadi_ordine)
        layout_frame3.addWidget(self.pulsante)



        self.frame.setLayout(layout_frame)
        layout = QVBoxLayout()
        layout.addWidget(self.frame)
        self.setLayout(layout)

    def evadi_ordine(self):
        self.ordine.pronto = True
        self.update()



if __name__ == "__main__":
    import sys
    from PyQt6.QtWidgets import QApplication
    gest = GestoreOrdiniTavolo()
    app = QApplication(sys.argv)
    cont = ContListaComande(gest)
    cont.view.show()

    sys.exit(app.exec())
