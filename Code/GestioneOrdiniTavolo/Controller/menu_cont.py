from PyQt6.QtWidgets import QStackedWidget, QMessageBox
from Code.GestioneOrdiniTavolo.View.menu_view import VistaMenu, BoxProdotto
from Code.GestioneMenu.Model.gestore_menu import GestoreMenu
from Code.GestioneOrdiniTavolo.Model.gestore_ordini_tavolo import GestoreOrdiniTavolo
from Code.GestioneOrdiniTavolo.Model.ordine_tavolo import OrdineTavolo
from Code.GestioneOrdiniTavolo.View.visualizza_conto_view import VistaVisualizzaConto
from Code.GestioneOrdiniTavolo.Controller.visualizza_conto_cont import ContVisualizzaConto
from Code.GestioneOrdiniTavolo.Model.tavolo import Tavolo
from Code.GestioneMagazzino.Model.gestore_magazzino import GestoreMagazzino
from Code.GestioneOrdiniTavolo.View.msg_termina_servizio_view import VistaMsgTerminaServizio
from Code.GestioneOrdiniTavolo.Controller.msg_termina_servizio_cont import ContMsgTerminaServizio


class ContMenu(object):

    def __init__(self, view: VistaMenu, model: GestoreOrdiniTavolo, tavolo: Tavolo, stacked: QStackedWidget):

        self.view = view
        self.model = model
        self.tavolo = tavolo
        self.gestore_menu = GestoreMenu()
        self.magazzino = GestoreMagazzino()
        self.riempi_menu()
        self.ordine_corrente = OrdineTavolo(self.tavolo)
        stacked.addWidget(self.view)

        for box in self.lista_box:
            box.pulsante_piu.clicked.connect(lambda checked, current_box=box: self.aggiungi_alla_lista(current_box))
            box.pulsante_meno.setEnabled(False)
            box.pulsante_meno.clicked.connect(lambda checked, current_box=box: self.rimuovi_dalla_lista(current_box))

        self.view.pulsante_antipasti.clicked.connect(lambda: self.scroll_to_section("antipasti"))
        self.view.pulsante_pizze.clicked.connect(lambda: self.scroll_to_section("pizze"))
        self.view.pulsante_softdrinks.clicked.connect(lambda: self.scroll_to_section("softdrinks"))
        self.view.pulsante_birre.clicked.connect(lambda: self.scroll_to_section("birre"))

        self.view.pulsante_confermaordine.setEnabled(False)
        self.view.pulsante_confermaordine.clicked.connect(self.conferma_ordine)
        self.view.pulsante_visualizzaconto.setEnabled(len(self.ordine_corrente.lista_prodotti))
        self.view.pulsante_visualizzaconto.clicked.connect(self.open_visualizzaconto)
        self.view.pulsante_terminaservizio.clicked.connect(self.termina_servizio)

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
            box = BoxProdotto(elemento.nome, 'png/antipasto.png')

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
                self.view.pulsante_confermaordine.setEnabled(self.view.lista_recap.count() != 0)
                box.pulsante_meno.setEnabled(True)
                break
        prodotto = self.gestore_menu.estrai_per_nome(nome)
        self.ordine_corrente.aggiungi_prodotto(prodotto)


    def rimuovi_dalla_lista(self, box: BoxProdotto):

        nome = box.label_nome.text().title()
        for i in range(self.view.lista_recap.count()):
            item = self.view.lista_recap.item(i)
            if nome.title() == str(item.text().split(".")[0]):
                self.view.lista_recap.takeItem(i)
                self.view.pulsante_confermaordine.setEnabled(self.view.lista_recap.count() != 0)
                box.pulsante_meno.setEnabled(int(box.label_quantita.text()) != 0)
                break
        prodotto = self.gestore_menu.estrai_per_nome(nome)
        self.ordine_corrente.rimuovi_prodotto(prodotto)

    def conferma_ordine(self):

        disp = True

        for prodotto in self.ordine_corrente.lista_prodotti:
            for ingrediente in prodotto.ingredienti:
                # print(str(ingrediente))
                codice_mp = ingrediente[0].codice
                quantità = ingrediente[1]
                disp = self.magazzino.decrementa_disponibilita(codice_mp, quantità)
                if not disp:
                    error = QMessageBox()
                    error.setIcon(QMessageBox.Icon.Critical)
                    error.setText("Purtroppo non è possibile confermare l'ordine\nperchè siamo a corto di " + str(ingrediente[0].nome).lower())
                    error.exec()
                    break
            if not disp:
                break

        if disp:
            self.model.aggiungi_ordine(self.ordine_corrente)
            for tavolo in self.model.lista_tavoli:
                if int(tavolo.numero) == self.tavolo.numero:
                    tavolo.cambia_stato("in attesa")
            self.model.salva_ordini_su_file()
            self.model.carica_da_file()
            self.ordine_corrente.lista_prodotti = []

            message = QMessageBox()
            message.setIcon(QMessageBox.Icon.NoIcon)
            message.setWindowTitle("<b>Grazie!<\b>")
            message.setText("Il tuo ordine è in fase di\npreparazione e ti verrà consegnato\nal più presto.")
            message.exec()

            self.view.lista_recap.clear()
            self.view.pulsante_confermaordine.setEnabled(False)
            self.view.pulsante_visualizzaconto.setEnabled(True)

            for box in self.lista_box:
                box.label_quantita.setText("0")

    def scroll_to_section(self, tipo: str):

        if tipo == "antipasti":

            last_item = self.view.grid_antipasti.itemAtPosition(self.view.grid_antipasti.rowCount() - 1,
                                                                self.view.grid_antipasti.columnCount() - 1)

            self.view.scroll_area.ensureWidgetVisible(last_item.widget())

        elif tipo == "pizze":
            last_item = self.view.grid_pizze.itemAtPosition(self.view.grid_pizze.rowCount() - 1,
                                                                self.view.grid_pizze.columnCount() - 1)

            self.view.scroll_area.ensureWidgetVisible(last_item.widget())

        elif tipo == "softdrinks":
            last_item = self.view.grid_softdrinks.itemAtPosition(self.view.grid_softdrinks.rowCount() - 1,
                                                                self.view.grid_softdrinks.columnCount() - 1)

            self.view.scroll_area.ensureWidgetVisible(last_item.widget())

        elif tipo == "birre":
            last_item = self.view.grid_birre.itemAtPosition(self.view.grid_birre.rowCount() - 1,
                                                                self.view.grid_birre.columnCount() - 1)

            self.view.scroll_area.ensureWidgetVisible(last_item.widget())

    def open_visualizzaconto(self):

        dialog_visualizzaconto = VistaVisualizzaConto()
        controller_visualizzaconto = ContVisualizzaConto(dialog_visualizzaconto, self.model, self.tavolo.numero)
        controller_visualizzaconto.view.exec()

    def termina_servizio(self):

        dialog_conferma_elimina = VistaMsgTerminaServizio()
        controller_conferma = ContMsgTerminaServizio(dialog_conferma_elimina)
        controller_conferma.view.exec()
        if controller_conferma.conferma:
            self.tavolo.cambia_stato("libero")
            self.model.salva_ordini_su_file()
