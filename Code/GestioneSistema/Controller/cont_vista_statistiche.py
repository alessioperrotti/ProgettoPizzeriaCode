from PyQt6.QtWidgets import QStackedWidget, QVBoxLayout, QGridLayout
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qtagg import (FigureCanvasQTAgg)

from Code.GestioneOrdiniTavolo.Model.gestore_ordini_tavolo import GestoreOrdiniTavolo
from Code.GestioneRicevuta.Model.gestore_ricevuta import GestoreRicevuta
from Code.GestioneSistema.View.vista_statistiche import VistaStatistiche


class ContVistaStatistiche:
    def __init__(self, gestore_ric:GestoreRicevuta, gestore_ord:GestoreOrdiniTavolo,stacked:QStackedWidget):

        self.view = VistaStatistiche()
        self.gestore_ric = gestore_ric
        self.gestore_ord = gestore_ord
        self.stacked = stacked
        stacked.addWidget(self.view)
        self.aggiorna_grafici()

    def aggiorna_grafici(self):
        self.stacked.removeWidget(self.view)
        self.view = VistaStatistiche()
        self.stacked.addWidget(self.view)

        # grafico 2, numero di prodotti venduti per giorno
        fig, ax = plt.subplots(figsize=(5, 2), layout='constrained')
        lista_asse_x = []
        lista_asse_y = []
        ultimo_giorno = None
        contatoreProdottiPerGiorno = 0

        for ricevuta in self.gestore_ric.lista_ricevute:
            data = ricevuta.data

            if ultimo_giorno != data:

                if ultimo_giorno is not None:
                    lista_asse_y.append(contatoreProdottiPerGiorno)

                contatoreProdottiPerGiorno=0
                ultimo_giorno = data #ricevuta.data.strftime("%d/%m")
                lista_asse_x.append(data.strftime("%d/%m"))
                for prodotto in ricevuta.listaProdotti:
                    contatoreProdottiPerGiorno += 1
            else:
                for prodotto in ricevuta.listaProdotti:
                    contatoreProdottiPerGiorno += 1

        lista_asse_y.append(contatoreProdottiPerGiorno)


        ax.bar(lista_asse_x,lista_asse_y)
        self.grafico2 = FigureCanvasQTAgg(fig)

        self.view.l2 = QVBoxLayout()
        self.view.l2.addWidget(self.view.label2)
        self.view.l2.addWidget(self.grafico2)

        # grafico 4, numero di clienti per giorno
        fig, ax = plt.subplots(figsize=(5, 2), layout='constrained')
        lista_asse_x = []
        lista_asse_y = []

        ultimo_giorno = None
        contatoreClientiPerGiorno = 0
        for ricevuta in self.gestore_ric.lista_ricevute:
            data = ricevuta.data
            if ultimo_giorno != data:

                if ultimo_giorno is not None:
                    lista_asse_y.append(contatoreClientiPerGiorno)

                contatoreClientiPerGiorno = 0
                ultimo_giorno = data
                lista_asse_x.append(data.strftime("%d/%m"))
                contatoreClientiPerGiorno += ricevuta.tavolo.posti_disponibili
            else:
                contatoreClientiPerGiorno += ricevuta.tavolo.posti_disponibili
        lista_asse_y.append(contatoreClientiPerGiorno)


        ax.bar(lista_asse_x, lista_asse_y)
        self.grafico4 = FigureCanvasQTAgg(fig)

        self.view.l4 = QVBoxLayout()
        self.view.l4.addWidget(self.view.label4)
        self.view.l4.addWidget(self.grafico4)

        #grafico 3, quantita prodotti venduti per prodotto

        fig, ax = plt.subplots(figsize=(5, 2), layout='constrained')
        lista_asse_x = []
        lista_asse_y = []
        ax.xaxis.set_tick_params(labelsize='small')

        # per ogni prodotto ci sono due liste, una con i nomi e una con le quantita

        for ricevuta in self.gestore_ric.lista_ricevute:
            for prodotto in ricevuta.listaProdotti:
                if prodotto.codice.__str__() in lista_asse_x:
                    lista_asse_y[lista_asse_x.index(prodotto.codice.__str__())] += 1
                else:
                    lista_asse_x.append(prodotto.codice.__str__())
                    lista_asse_y.append(1)


        ax.bar(lista_asse_x, lista_asse_y)
        self.grafico3 = FigureCanvasQTAgg(fig)

        self.view.l3 = QVBoxLayout()
        self.view.l3.addWidget(self.view.label3)
        self.view.l3.addWidget(self.grafico3)

        #grafico 1, fatturato per giorno
        fig, ax = plt.subplots(figsize=(5, 2), layout='constrained')


        lista_asse_x = []
        lista_asse_y = []

        ultimo_giorno = None
        fatturatoperGiorno = 0
        for ricevuta in self.gestore_ric.lista_ricevute:
            data = ricevuta.data

            if ultimo_giorno != data:

                if ultimo_giorno is not None:
                    lista_asse_y.append(fatturatoperGiorno)

                fatturatoperGiorno = 0
                ultimo_giorno = data
                lista_asse_x.append(data.strftime("%d/%m"))
                fatturatoperGiorno += ricevuta.ammontareLordo
            else:
                fatturatoperGiorno += ricevuta.ammontareLordo

        lista_asse_y.append(fatturatoperGiorno)

        ax.bar(lista_asse_x, lista_asse_y)
        self.grafico1 = FigureCanvasQTAgg(fig)

        self.view.l1 = QVBoxLayout()
        self.view.l1.addWidget(self.view.label1)
        self.view.l1.addWidget(self.grafico1)




        #setto i layout


        self.view.grid_layout.addLayout(self.view.l1, 0, 0)
        self.view.grid_layout.addLayout(self.view.l2, 0, 1)
        self.view.grid_layout.addLayout(self.view.l3, 1, 0)
        self.view.grid_layout.addLayout(self.view.l4, 1, 1)





