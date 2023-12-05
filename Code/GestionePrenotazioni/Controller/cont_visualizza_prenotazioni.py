from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QTableWidgetItem

from Code.GestionePrenotazioni.Model.gestore_prenotazioni import GestorePrenotazioni
from Code.GestionePrenotazioni.View.vista_visualizza_prenotazioni import VistaVisualizzaPrenotazioni


class ContVisualizzaPrenotazioni(object):

    def __init__(self, model: GestorePrenotazioni):
        self.view = VistaVisualizzaPrenotazioni()
        self.model = model
        self.update_tabella()
        self.view.search_edit.textChanged.connect(self.filtra_elementi)

    def update_tabella(self):
        self.view.tab.setRowCount(len(self.model.lista_prenotazioni))

        i = 0
        for x in self.model.lista_prenotazioni:
            item_nome = QTableWidgetItem(x.nome_cliente)
            item_nome.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.view.tab.setItem(i, 0, item_nome)

            item_tav = QTableWidgetItem(str(x.tavolo_assegnato.numero))
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
