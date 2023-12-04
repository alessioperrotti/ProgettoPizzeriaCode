from PyQt6.QtWidgets import QStackedWidget, QFrame, QHBoxLayout
from Code.GestioneOrdiniTavolo.View.menu_view import VistaMenu, BoxProdotto
from Code.GestioneMenu.Model.gestore_menu import GestoreMenu
from Code.GestioneOrdiniTavolo.Model.gestore_ordini_tavolo import GestoreOrdiniTavolo
from Code.GestioneOrdiniTavolo.Model.ordine_tavolo import OrdineTavolo

class ContMenu(object):

    def __init__(self, view: VistaMenu, model: GestoreOrdiniTavolo, numtavolo, stacked: QStackedWidget):

        self.view = view
        self.model = model
        self.tavolo = numtavolo
        self.gestore_menu = GestoreMenu()
        self.riempi_menu()
        self.ordine_corrente = OrdineTavolo(numtavolo)
        stacked.addWidget(self.view)


        for box in self.lista_box:
            box.pulsante_piu.clicked.connect(lambda checked, current_box=box: self.aggiungi_alla_lista(current_box))
            box.pulsante_meno.clicked.connect(lambda checked, current_box=box: self.rimuovi_dalla_lista(current_box))

        self.view.pulsante_antipasti.clicked.connect(
            lambda: self.view.scroll_area.ensureVisible(self.view.label_antipasti))
        self.view.pulsante_pizze.clicked.connect(
            lambda: self.view.scroll_area.ensureVisible(self.view.label_pizze))
        self.view.pulsante_softdrinks.clicked.connect(
            lambda: self.view.scroll_area.ensureVisible(self.view.label_softdrinks))
        self.view.pulsante_birre.clicked.connect(
            lambda: self.view.scroll_area.ensureVisible(self.view.label_birre))

        self.view.pulsante_confermaordine.setEnabled(self.view.lista_recap.count() != 0)
        self.view.pulsante_confermaordine.clicked.connect(self.conferma_ordine)

    def riempi_menu(self):

        lista_antipasti = []
        lista_pizze = []
        lista_softdrinks = []
        lista_birre = []
        self.lista_box = []

        for prodotto in self.gestore_menu.lista_prodotti:
            if prodotto.tipologia.lower() == "antipasto":
                lista_antipasti.append(prodotto)
            elif prodotto.tipologia.lower() == "pizza":
                lista_pizze.append(prodotto)
            elif prodotto.tipologia.lower() == "soft drink":
                lista_softdrinks.append(prodotto)
            elif prodotto.tipologia.lower() == "birra":
                lista_birre.append(prodotto)

        for indice, elemento in enumerate(lista_antipasti):
            riga = indice // 3
            colonna = indice % 3
            box_layout = QHBoxLayout()
            frame = QFrame()
            frame.setFixedSize(147,204)
            frame.setStyleSheet(".border: 1px solid black; border-radius: 5px; padding: 5px")
            box = BoxProdotto(elemento.nome, 'png/antipasto.png')
            box_layout.addWidget(box)
            frame.setLayout(box_layout)
            self.view.grid_antipasti.addWidget(box, riga, colonna)

            self.lista_box.append(box)

        for indice, elemento in enumerate(lista_pizze):
            riga = indice // 3
            colonna = indice % 3
            box = BoxProdotto(elemento.nome, 'png/pizza.png')
            self.view.grid_pizze.addWidget(box, riga, colonna)
            self.lista_box.append(box)

        for indice, elemento in enumerate(lista_softdrinks):
            riga = indice // 3
            colonna = indice % 3
            box = BoxProdotto(elemento.nome, 'png/softdrink.png')
            self.view.grid_softdrinks.addWidget(box, riga, colonna)
            self.lista_box.append(box)

        for indice, elemento in enumerate(lista_birre):
            riga = indice // 3
            colonna = indice % 3
            box = BoxProdotto(elemento.nome, 'png/birra.png')
            self.view.grid_birre.addWidget(box, riga, colonna)
            self.lista_box.append(box)


    def aggiungi_alla_lista(self, box: BoxProdotto):

        nome = box.label_nome.text().title()
        for x in self.gestore_menu.lista_prodotti:
            if str(x.nome).lower() == nome.lower():
                prezzo = str(x.prezzo_al_pubblico)
                self.view.lista_recap.addItem(nome + "....€" + prezzo)
                break
        prodotto = self.gestore_menu.estrai_per_nome(nome)
        self.ordine_corrente.aggiungi_prodotto(prodotto)


    def rimuovi_dalla_lista(self, box: BoxProdotto):

        nome = box.label_nome.text().title()
        for i in range(self.view.lista_recap.count()):
            item = self.view.lista_recap.itemAt(i)
            if nome.lower() == str(item.text().split(".")[0]):
                self.view.lista_recap.removeItemWidget(item)
                break
        prodotto = self.gestore_menu.estrai_per_nome(nome)
        self.ordine_corrente.rimuovi_prodotto(prodotto)

    def conferma_ordine(self):

        self.model.aggiungi_ordine(self.ordine_corrente)
        self.model.conferma_ordine(self.ordine_corrente)
        self.ordine_corrente = None
        self.view.lista_recap.clear()

        for box in self.lista_box:
            box.label_quantita.setText("0")


