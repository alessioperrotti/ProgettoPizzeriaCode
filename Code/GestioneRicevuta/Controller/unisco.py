import sys
from PyQt6.QtWidgets import QApplication, QWidget, QStackedWidget, QPushButton, QVBoxLayout

from Code.GestioneMenu.Model.prodotto import Prodotto
from Code.GestioneOrdiniTavolo.Model.gestore_ordini_tavolo import GestoreOrdiniTavolo
from Code.GestioneOrdiniTavolo.Model.ordine_tavolo import OrdineTavolo
from Code.GestioneOrdiniTavolo.Model.tavolo import Tavolo
from Code.GestioneRicevuta.Controller.cont_vista_gestione_ricevute import ContVistaGestioneRicevute
from Code.GestioneRicevuta.Controller.cont_vista_inserisci_ricevuta import ContVistaInserisciRicevuta
from Code.GestioneRicevuta.Model.gestore_ricevuta import GestoreRicevuta
from Code.GestioneRicevuta.Model.ricevuta import Ricevuta


class MainWindow(QWidget):
    def __init__(self, app):
        super(MainWindow, self).__init__()
        self.stacked = QStackedWidget()
        self.init_ui()
        self.show()


    def init_ui(self):
        gestore_ric = GestoreRicevuta()
        ric1 = Ricevuta(1,"c",None,"Andrea",3,"esempio1")
        ric2 = Ricevuta(1,"c",None,"Alessio",3,"esempio1")

        # gestore_ric.aggiungi_ricevuta(1,"c",None,"Andrea","esempio1")
        # gestore_ric.aggiungi_ricevuta(1,"c",None,"Ale","esempio1")

        gestore_ord = GestoreOrdiniTavolo()


        tavolo1 = Tavolo(1, 10, None)
        tavolo2 = Tavolo(2, 10, None)
        tavolo3 = Tavolo(3, 10, None)
        tavolo4 = Tavolo(4, 10, None)
        tavolo5 = Tavolo(5, 10, None)

        lista_tav = []
        lista_tav.append(tavolo1)
        lista_tav.append(tavolo2)
        lista_tav.append(tavolo3)
        lista_tav.append(tavolo4)
        lista_tav.append(tavolo5)


        prod1 = Prodotto("pizzamarghe", 2, 15)
        prod2 = Prodotto("pizzasals", 3, 20)

        ord1 = OrdineTavolo(1, 1, 1, tavolo1)
        ord1.aggiungi_prodotto(prod1)
        ord1.aggiungi_prodotto(prod2)
        ord3 = OrdineTavolo(1,1,2,tavolo1)
        ord3.aggiungi_prodotto(prod1)
        ord3.aggiungi_prodotto(prod1)
        ord2 = OrdineTavolo(1, 1, 1, tavolo2)
        ord2.aggiungi_prodotto(prod1)
        ord2.aggiungi_prodotto(prod2)
        ord2.aggiungi_prodotto(prod2)

        gestore_ord.conferma_ordine(ord1)
        gestore_ord.conferma_ordine(ord2)
        gestore_ord.conferma_ordine(ord3)
        gestore_ord.conferma_ordine(ord3)
        gestore_ord.conferma_ordine(ord3)
        gestore_ord.conferma_ordine(ord3)
        gestore_ord.conferma_ordine(ord3)
        gestore_ord.conferma_ordine(ord3)
        gestore_ord.conferma_ordine(ord3)
        gestore_ord.conferma_ordine(ord3)




        self.cont_gestione_ric = ContVistaGestioneRicevute(gestore_ric, gestore_ord,lista_tav, self.stacked)
        self.stacked.addWidget(self.cont_gestione_ric.view)
        self.stacked.setCurrentWidget(self.cont_gestione_ric.view)

        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow(app)

    sys.exit(app.exec())
