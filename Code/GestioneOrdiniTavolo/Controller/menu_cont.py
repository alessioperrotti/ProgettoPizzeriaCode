from Code.GestioneOrdiniTavolo.View.menu_view import VistaMenu, BoxProdotto
from Code.GestioneMenu.Model.gestore_menu import GestoreMenu
from Code.GestioneOrdiniTavolo.Model.gestore_ordini_tavolo import GestoreOrdiniTavolo

class ContMenu(object):

    def __init__(self, view: VistaMenu, model: GestoreOrdiniTavolo):

        self.view = view
        self.model = model
        self.gestore_menu = GestoreMenu()
        self.view.pulsante_antipasti.clicked.connect(
            lambda : self.view.scroll_area.ensureVisible(self.view.label_antipasti))
        self.view.pulsante_pizze.clicked.connect(
            lambda: self.view.scroll_area.ensureVisible(self.view.label_pizze))
        self.view.pulsante_softdrinks.clicked.connect(
            lambda: self.view.scroll_area.ensureVisible(self.view.label_softdrinks))
        self.view.pulsante_birre.clicked.connect(
            lambda: self.view.scroll_area.ensureVisible(self.view.label_birre))

    def riempi_menu(self):

        lista_antipasti = []
        lista_pizze = []
        lista_softdrinks = []
        lista_birre = []

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
            box = BoxProdotto(elemento.nome, 'png/antipasto.png')
            self.view.grid_antipasti.addWidget(box, riga, colonna)

        for indice, elemento in enumerate(lista_pizze):
            riga = indice // 3
            colonna = indice % 3
            box = BoxProdotto(elemento.nome, 'png/pizza.png')
            self.view.grid_pizze.addWidget(box, riga, colonna)

        for indice, elemento in enumerate(lista_softdrinks):
            riga = indice // 3
            colonna = indice % 3
            box = BoxProdotto(elemento.nome, 'png/softdrink.png')
            self.view.grid_softdrinks.addWidget(box, riga, colonna)

        for indice, elemento in enumerate(lista_birre):
            riga = indice // 3
            colonna = indice % 3
            box = BoxProdotto(elemento.nome, 'png/birra.png')
            self.view.grid_birre.addWidget(box, riga, colonna)



