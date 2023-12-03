from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTableWidgetItem, QStackedWidget

from Code.GestionePrenotazioni.Controller.cont_inserisci_prenotazione import ContInserisciPrenotazione
from Code.GestionePrenotazioni.Controller.cont_modifica_prenotazione import ContModificaPrenotazione
from Code.GestionePrenotazioni.Controller.cont_msg_elimina_pre import ContMsgEliminaPre
from Code.GestionePrenotazioni.Model.gestore_prenotazioni import GestorePrenotazioni
from Code.GestionePrenotazioni.View.vista_gestione_prenotazioni import VistaGestionePrenotazioni
from Code.GestionePrenotazioni.View.vista_inserisci_prenotazione import VistaInserisciPrenotazione
from Code.GestionePrenotazioni.View.vista_modifica_prenotazione import VistaModificaPrenotazione
from Code.GestionePrenotazioni.View.vista_msg_elimina_prenotazione import VistaMsgEliminaPrenotazione


class ContGestionePrenotazioni(object):

    def __init__(self, model: GestorePrenotazioni, stacked: QStackedWidget):
        self.view = VistaGestionePrenotazioni()
        self.stacked = stacked
        stacked.addWidget(self.view)
        self.model = model
        self.update_tabella()
        self.codice_selezionato = None
        self.nome_selezionato = None
        self.view.tab.itemSelectionChanged.connect(self.riga_selezionata)
        self.view.search_edit.textChanged.connect(self.filtra_elementi)
        self.view.pulsante_inserisci.clicked.connect(self.click_inserisci)
        self.view.pulsante_modifica.clicked.connect(self.click_modifica)
        self.view.pulsante_elimina.clicked.connect(self.click_elimina)

        self.model.stampa_lista_tavoli()

    def riga_selezionata(self):
        selected_items = self.view.tab.selectedItems()
        abilita_pulsante = len(selected_items) > 0
        for item in selected_items:
            if item.column() == 0:
                self.nome_selezionato = str(item.text())
                # nome_cognome = str(item.text())
                # self.cognome_selezionato = nome_cognome.split()[1]  # Estraggo solo il cognome
            elif item.column() == 5:
                self.codice_selezionato = int(item.text())

        self.view.pulsante_elimina.setEnabled(abilita_pulsante)
        self.view.pulsante_modifica.setEnabled(abilita_pulsante)

    def click_inserisci(self):
        dialog_inserisci = VistaInserisciPrenotazione()
        cont_inserisci = ContInserisciPrenotazione(self.model, dialog_inserisci)
        cont_inserisci.riempi_labels()
        cont_inserisci.view.exec()
        self.update_tabella()

    def click_modifica(self):
        dialog_modifica = VistaModificaPrenotazione()
        prenotazione_temp = self.model.ricerca_prenotazione_codice(self.codice_selezionato)
        cont_modifica = ContModificaPrenotazione(dialog_modifica, self.model, prenotazione_temp)
        cont_modifica.view.exec()
        self.update_tabella()

    def click_elimina(self):
        vista_msg = VistaMsgEliminaPrenotazione()
        cont_msg = ContMsgEliminaPre(self.model, vista_msg)
        cont_msg.view.exec()
        if cont_msg.conferma:
            cont_msg.view.close()
            self.model.elimina_prenotazione(self.codice_selezionato)

            self.update_tabella()
            self.codice_selezionato = None
            self.view.tab.clearSelection()

    def update_tabella(self):
        self.view.tab.setRowCount(len(self.model.lista_prenotazioni))

        i = 0
        for x in self.model.lista_prenotazioni:
            item_nome = QTableWidgetItem(x.nome_cliente)
            item_nome.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.view.tab.setItem(i, 0, item_nome)

            item_tav = QTableWidgetItem(x.tavolo_assegnato)
            item_tav.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.view.tab.setItem(i, 1, item_tav)

            item_orario = QTableWidgetItem(x.orario)
            item_orario.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.view.tab.setItem(i, 2, item_orario)

            item_giorno = QTableWidgetItem(x.data.toString("dd-MM-yyyy"))
            item_giorno.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.view.tab.setItem(i, 3, item_giorno)

            item_posti = QTableWidgetItem(str(x.n_persone))
            item_posti.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.view.tab.setItem(i, 4, item_posti)

            stringa_codice = "{:04d}".format(int(x.codice))
            item_codice = QTableWidgetItem(stringa_codice)
            item_codice.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.view.tab.setItem(i, 5, item_codice)
            i += 1

    def filtra_elementi(self):
        testo_ricerca = self.view.search_edit.text().lower()
        for row in range(self.view.tab.rowCount()):
            nome_prenotazione = self.view.tab.item(row, 0).text().lower()
            self.view.tab.setRowHidden(row, testo_ricerca not in nome_prenotazione)


