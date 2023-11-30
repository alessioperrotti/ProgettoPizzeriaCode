from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QStackedWidget, QTableWidgetItem

from Code.GestioneDipendenti.Controller.cont_modifica_turno import ContModificaTurno
from Code.GestioneDipendenti.Model.gestore_dipendenti import GestoreDipendenti
from Code.GestioneDipendenti.View.vista_gestione_turni_personale import VistaGestioneTurniPersonale
from Code.GestioneDipendenti.View.vista_modifica_turno import VistaModificaTurno


class ContGestioneTurni(object):
    def __init__(self, model: GestoreDipendenti, stacked: QStackedWidget):
        self.stacked = stacked
        self.view = VistaGestioneTurniPersonale()
        stacked.addWidget(self.view)
        self.model = model
        self.update_tabella()
        self.giorno_selezionato = None
        self.view.tabella.itemSelectionChanged.connect(self.colonna_selezionata)
        self.view.pulsante.clicked.connect(self.go_to_modifica)

    def colonna_selezionata(self):
        selected_items = self.view.tabella.selectedItems()
        abilita_pulsante = len(selected_items) > 0
        colonne_selezionate = []

        for item in selected_items:
            colonna_selezionata = item.column()
            colonne_selezionate.append(colonna_selezionata)
        if colonne_selezionate:
            indice_colonna_selezionata = colonne_selezionate[0]
            self.giorno_selezionato = self.view.tabella.horizontalHeaderItem(indice_colonna_selezionata).text()
            print(self.giorno_selezionato)

        self.view.pulsante.setEnabled(abilita_pulsante)

    def go_to_modifica(self):
        dialog_modifica = VistaModificaTurno()
        cont_modifica = ContModificaTurno(self.model, dialog_modifica)
        cont_modifica.riempi_labels(self.giorno_selezionato)
        cont_modifica.view.exec()
        self.update_tabella()

    def update_tabella(self):

        self.view.tabella.clearContents()
        #stampa di verifica
        for cuoco in self.model.lista_cuochi:
            for i in range(len(cuoco.turno)):
                print("indice_giorno = " + str(i) + " " + str(cuoco.nome) + " turno:" + str(cuoco.turno[i])+"\n")

        for cameriere in self.model.lista_camerieri:
            for i in range(len(cameriere.turno)):
                print("indice_giorno = " + str(i) + " " + str(cameriere.nome) + " turno:" + str(cameriere.turno[i])+"\n")

        # Crea una mappatura per i tipi di turno agli indici di riga
        # mappatura_turni = {"Pranzo": 0, "Cena": 1, "Pranzo & Cena": [0, 1]}
        #
        # for dipendente in self.model.lista_cuochi + self.model.lista_camerieri:
        #     for i, turno in enumerate(dipendente.turno):
        #         item_vuoto = QTableWidgetItem("vuoto")
        #         item_vuoto.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        #         item_nome = QTableWidgetItem(dipendente.nome + " " + dipendente.cognome)
        #         item_nome.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        #
        #         indice_riga = mappatura_turni.get(turno, None)
        #
        #         if indice_riga is not None:
        #             if isinstance(indice_riga, list):
        #                 for idx in indice_riga:
        #                     self.view.tabella.setItem(idx, i, item_nome)
        #             else:
        #                 self.view.tabella.setItem(indice_riga, i, item_nome)
        #         elif turno is None:
        #             self.view.tabella.setItem(0, i, item_vuoto)
        #             item_vuoto_corrente = QTableWidgetItem(item_vuoto.text())
        #             item_vuoto_corrente.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        #             self.view.tabella.setItem(1, i, item_vuoto_corrente)
        #         else:
        #             for k in range(self.view.tabella.rowCount()):
        #                 for j in range(self.view.tabella.columnCount()):
        #                     item_vuoto = QTableWidgetItem("vuoto")
        #                     item_vuoto.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        #                     self.view.tabella.setItem(k, j, item_vuoto)


        # for row in range(self.view.tabella.rowCount()):
        # for col in range(self.view.tabella.columnCount()):
        #     item = QTableWidgetItem("vuoto")
        #     self.view.tabella.setItem(0, col, item)
        #     item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

        for cuoco in self.model.lista_cuochi:
            #print(len(cuoco.turno))
            for i in range(len(cuoco.turno)):
                item_vuoto = QTableWidgetItem("vuoto")
                item_vuoto.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                item_nome = QTableWidgetItem(cuoco.nome + " " + cuoco.cognome)
                item_nome.setTextAlignment(Qt.AlignmentFlag.AlignCenter)


                if cuoco.turno[i] == "Pranzo":
                    self.view.tabella.setItem(0, i, item_nome)
                elif cuoco.turno[i] == "Cena":
                    print("porco")
                    self.view.tabella.setItem(1, i, item_nome)
                    print("cazzo")
                elif cuoco.turno[i] == "Pranzo & Cena":
                    self.view.tabella.setItem(0, i, item_nome)
                    current_item_nome_cena = QTableWidgetItem(item_nome.text())
                    current_item_nome_cena.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    self.view.tabella.setItem(1, i, current_item_nome_cena)
                # elif cuoco.turno[i] is None:
                #     self.view.tabella.setItem(0, i, item_vuoto)
                #     current_item_vuoto = QTableWidgetItem(item_vuoto.text())
                #     current_item_vuoto.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                #     self.view.tabella.setItem(1, i, current_item_vuoto)

        for cameriere in self.model.lista_camerieri:
            #print(len(cameriere.turno))
            for i in range(len(cameriere.turno)):
                item_nome = QTableWidgetItem(cameriere.nome + " " + cameriere.cognome)
                item_nome.setTextAlignment(Qt.AlignmentFlag.AlignCenter)


                if cameriere.turno[i] == "Pranzo":
                    self.view.tabella.setItem(0, i, item_nome)
                elif cameriere.turno[i] == "Cena":
                    self.view.tabella.setItem(1, i, item_nome)
                elif cameriere.turno[i] == "Pranzo & Cena":
                    self.view.tabella.setItem(0, i, item_nome)
                    current_item_nome_cena = QTableWidgetItem(item_nome.text())
                    current_item_nome_cena.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    self.view.tabella.setItem(1, i, current_item_nome_cena)
                # elif cameriere.turno[i] is None:
                #     self.view.tabella.setItem(0, i, item_vuoto)
                #     current_item_vuoto = QTableWidgetItem(item_vuoto.text())
                #     current_item_vuoto.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                #     self.view.tabella.setItem(1, i, current_item_vuoto)


