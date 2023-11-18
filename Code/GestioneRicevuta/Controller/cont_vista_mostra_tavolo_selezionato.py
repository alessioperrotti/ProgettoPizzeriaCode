import sys
from datetime import datetime
from os.path import dirname, abspath

import PyQt6
from PyQt6.QtWidgets import QApplication

from Code.GestioneMenu.Model.prodotto import Prodotto
from Code.GestioneOrdiniTavolo.Model.ordine_tavolo import OrdineTavolo
from Code.GestioneRicevuta.View.vista_inserisci_ricevuta import VistaInserisciRicevuta



from Code.GestioneRicevuta.Model.ricevuta import Ricevuta
from Code.GestioneRicevuta.Model.gestore_ricevuta import GestoreRicevuta
from PyQt6.QtCore import pyqtSignal

from Code.GestioneRicevuta.View.vista_mostra_tavolo_selezionato import VistaMostraTavoloSelezionato


class ContVistaMostraTavoloSelezionato():

    def __init__(self, gestore_ric:GestoreRicevuta, gestore_ord, ricevutaControllerGestione:Ricevuta, ordini:list[OrdineTavolo]):
        self.ric = ricevutaControllerGestione #è la ricevuta temporanea che ancora non ha nome dell' acquirente, viene poi conclusa e aggiunta nel controller Gesione
        self.view = VistaMostraTavoloSelezionato()
        self.ordini = ordini
        self.gestore_ric = gestore_ric
        self.view.pulsante_aggiungi.clicked.connect(self.aggiungi_tavolo_alla_ricevuta)

    def aggiungi_tavolo_alla_ricevuta(self):
        totale = 0
        listaProdotti = []
        for ordine in self.ordini:
            totale += ordine.prezzo_totale
            listaProdotti.append(ordine.lista_prodotti)
        data = datetime.now().date()
        nomeAcquirente = None
        numero = 
        self.ric = Ricevuta(totale, data, listaProdotti, nomeAcquirente, numero, ora)

        pass
    def mostra_tavolo_selezionato(self):
        pass

    def stampa_ricevuta(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gestore = GestoreRicevuta()
    cont = ContVistaInserisciRicevuta(gestore)
    cont.view.show()
    sys.exit(app.exec())



