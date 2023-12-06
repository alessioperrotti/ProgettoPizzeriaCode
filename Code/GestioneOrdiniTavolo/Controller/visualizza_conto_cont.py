from Code.GestioneOrdiniTavolo.View.visualizza_conto_view import VistaVisualizzaConto
from Code.GestioneOrdiniTavolo.Model.gestore_ordini_tavolo import GestoreOrdiniTavolo
from Code.GestioneOrdiniTavolo.Model.ordine_tavolo import OrdineTavolo
from PyQt6.QtWidgets import QLabel, QHBoxLayout, QVBoxLayout, QSizePolicy
from PyQt6.QtGui import QFont

class ContVisualizzaConto(object):

    def __init__(self, view: VistaVisualizzaConto, model: GestoreOrdiniTavolo, numtavolo):

        self.view = view
        self.model = model
        self.model.carica_da_file()
        self.numtavolo = numtavolo
        self.ordini: list[OrdineTavolo] = []
        self.totale = 0
        self.riempi_vista()

    def riempi_vista(self):

        self.view.title.setText("<b>Conto Tavolo n°</b>" + str(self.numtavolo))

        for x in self.model.lista_ordini:
            if x.tavolo.numero == self.numtavolo:
                if not x.pagato:
                    self.ordini.append(x)

        i = 0
        for ordine in self.ordini:

            self.totale += ordine.prezzo_totale
            tit = QLabel("<b>Ordine</b> " + str(i+1))
            self.view.layoutOrdini.addWidget(tit)
            layout = QHBoxLayout()
            layout.addSpacing(20)
            layoutprodotti = QVBoxLayout()
            layout.addLayout(layoutprodotti)
            layoutprodotti.addSpacing(2)

            for prodotto in ordine.lista_prodotti:
                label = QLabel(f'<font color="black">&#8226;</font> ' + prodotto.nome + "  €" + str(prodotto.prezzo_al_pubblico))
                label.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

                layoutprodotti.addWidget(label)
                layoutprodotti.addSpacing(2)
                self.view.layoutOrdini.addLayout(layout)

            layoutprodotti.addSpacing(10)
            i += 1

        self.view.layoutOrdini.addStretch()
        self.view.label_totale_val.setText("€ " + str(self.totale))
        self.view.label_totale_val.setFont(QFont("Roboto", 18))


