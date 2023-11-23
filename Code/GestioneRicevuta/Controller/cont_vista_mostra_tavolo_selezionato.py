import sys
from datetime import datetime
from os.path import dirname, abspath

import PyQt6
from PyQt6.QtWidgets import QApplication, QLabel, QHBoxLayout, QVBoxLayout, QScrollArea, QFrame, QSizePolicy

from Code.GestioneMenu.Model.prodotto import Prodotto
from Code.GestioneOrdiniTavolo.Model.ordine_tavolo import OrdineTavolo
from Code.GestioneRicevuta.View.vista_inserisci_ricevuta import VistaInserisciRicevuta



from Code.GestioneRicevuta.Model.ricevuta import Ricevuta
from Code.GestioneRicevuta.Model.gestore_ricevuta import GestoreRicevuta
from PyQt6.QtCore import pyqtSignal

from Code.GestioneRicevuta.View.vista_mostra_tavolo_selezionato import VistaMostraTavoloSelezionato


class ContVistaMostraTavoloSelezionato():

    def __init__(self, gestore_ric:GestoreRicevuta, ricevutaControllerGestione:Ricevuta):

        self.ric = ricevutaControllerGestione #è la ricevuta temporanea che ancora non ha nome dell' acquirente, viene poi conclusa e aggiunta nel controller Gesione
        self.view = VistaMostraTavoloSelezionato()
        self.ordini:list[OrdineTavolo] = []
        self.gestore_ric = gestore_ric


    def aggiungi_tavolo_alla_ricevuta(self):

        totale = 0
        listaProdotti = []
        for ordine in self.ordini:
            totale += ordine.prezzo_totale

            for prodotto in ordine.lista_prodotti:
                listaProdotti.append(prodotto)
        data = datetime.now().date().__str__()
        nomeAcquirente = None
        numero = 1
        ora_corrente = datetime.now().time()
        ora = ora_corrente.strftime("%H:%M:%S")
        self.ric = Ricevuta(totale, data, listaProdotti, nomeAcquirente, numero, ora)

        self.view.close()




    def aggiorna_lista(self):


        self.view = VistaMostraTavoloSelezionato()
        self.view.pulsante_aggiungi.clicked.connect(self.aggiungi_tavolo_alla_ricevuta)
        num_tav = self.ordini[0].tavolo.numero
        self.view.title.setText("Conto Tavolo n. "+str(num_tav))
        i=1
        for ordine in self.ordini:

            tit = QLabel("Ordine "+str(i))
            self.view.layoutOrdini.addWidget(tit)
            layout = QHBoxLayout()
            layout.addSpacing(20)
            layoutprodotti = QVBoxLayout()
            layout.addLayout(layoutprodotti)
            layoutprodotti.addSpacing(2)

            for prodotto in ordine.lista_prodotti:
                label = QLabel(f'<font color="black">&#8226;</font> ' + prodotto.nome)
                label.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

                layoutprodotti.addWidget(label)
                layoutprodotti.addSpacing(2)
                self.view.layoutOrdini.addLayout(layout)

            layoutprodotti.addSpacing(10)
            i+=1

        self.view.layoutOrdini.addStretch()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    gestore = GestoreRicevuta()
    cont = ContVistaMostraTavoloSelezionato(gestore)
    cont.view.show()
    sys.exit(app.exec())



