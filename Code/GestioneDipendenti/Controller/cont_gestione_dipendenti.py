import sys
from PyQt6.QtWidgets import QApplication, QTableWidgetItem, QVBoxLayout, QMessageBox, QStackedWidget

from Code.GestioneDipendenti.Controller.cont_inserisci_dipendente import ContInserisciDipendente
from Code.GestioneDipendenti.Controller.cont_modifica_dipendente import ContModificaDipendente
from Code.GestioneDipendenti.Controller.cont_mostra_dipendente import ContMostraDipendente
from Code.GestioneDipendenti.Controller.cont_msg_elimina_dip import ContMsgEliminaDip
from Code.GestioneDipendenti.Model.gestore_dipendenti import GestoreDipendenti
from Code.GestioneDipendenti.View.vista_gestione_dipendenti import VistaGestioneDipendenti
from Code.GestioneDipendenti.View.vista_inserisci_dipendente import VistaInserisciDipendente
from Code.GestioneDipendenti.View.vista_modifica_dipendente import VistaModificaDipendente
from Code.GestioneDipendenti.View.vista_msg_elimina_dipendente import VistaMsgEliminaDipendente
from Code.GestioneDipendenti.View.vista_visualizza_dipendente import VistaVisualizzaDipendente



class ContGestioneDipendenti(object):
    def __init__(self, model: GestoreDipendenti, stacked: QStackedWidget):
        self.stacked = stacked
        self.view = VistaGestioneDipendenti()
        stacked.addWidget(self.view)
        self.model = model
        self.update_tabella()
        self.nome_selezionato = None
        self.ruolo_selezionato = None
        self.view.pulsante_aggiungi.clicked.connect(self.go_to_inserimento)
        self.view.pulsante_mostra.clicked.connect(self.go_to_mostrainfo)
        self.view.tab.itemSelectionChanged.connect(self.riga_selezionata)
        self.view.pulsante_elimina.clicked.connect(self.delete_dipendente)
        self.view.pulsante_modifica.clicked.connect(self.go_to_modifica)
        self.view.pulsante_back.clicked.connect(lambda: self.stacked.setCurrentWidget(self.stacked.widget(0)))

    def riga_selezionata(self):
        selected_items = self.view.tab.selectedItems()
        abilita_pulsante = len(selected_items) > 0
        for item in selected_items:
            if item.column() == 0:
                self.nome_selezionato = str(item.text())
            elif item.column() == 1:
                self.ruolo_selezionato = str(item.text())

        self.view.pulsante_mostra.setEnabled(abilita_pulsante)
        self.view.pulsante_elimina.setEnabled(abilita_pulsante)
        self.view.pulsante_modifica.setEnabled(abilita_pulsante)

    def go_to_mostrainfo(self):
        dialog_mostrainfo = VistaVisualizzaDipendente()
        controller_mostrainfo = ContMostraDipendente(dialog_mostrainfo, self.model)
        if self.ruolo_selezionato == "Cuoco":
            dipendente_temp = self.model.estrai_cuoco_nome(
                self.nome_selezionato)  # estrae col nome ottenuto dalla tabella
            controller_mostrainfo.riempi_labels_cuoco(dipendente_temp)
        if self.ruolo_selezionato == "Cameriere":
            dipendente_temp = self.model.estrai_cameriere_nome(
                self.nome_selezionato)  # estrae col nome ottenuto dalla tabella
            controller_mostrainfo.riempi_labels_cameriere(dipendente_temp)
        controller_mostrainfo.view.exec()

    def go_to_inserimento(self):
        vista_inserisci = VistaInserisciDipendente()
        cont_inserisci = ContInserisciDipendente(self.model, vista_inserisci)
        cont_inserisci.view.exec()
        self.update_tabella()

    def delete_dipendente(self):
        vista_msg = VistaMsgEliminaDipendente()
        cont_msg = ContMsgEliminaDip(self.model,vista_msg)
        if self.ruolo_selezionato == "Cuoco":
            cont_msg.view.exec()
            if cont_msg.conferma:
                self.model.elimina_cuoco(self.nome_selezionato)
                self.update_tabella()
                self.nome_selezionato = None
        if self.ruolo_selezionato == "Cameriere":
            cont_msg.view.exec()
            if cont_msg.conferma:
                self.model.elimina_cameriere(self.nome_selezionato)
                self.update_tabella()
                self.nome_selezionato = None
        self.view.tab.clearSelection()

    def go_to_modifica(self):
        dialog_modifica = VistaModificaDipendente()
        cont_modifica = ContModificaDipendente(self.model, dialog_modifica)
        if self.ruolo_selezionato == "Cuoco":
            dipendente_temp = self.model.estrai_cuoco_nome(self.nome_selezionato)
            cont_modifica.cuoco = dipendente_temp
            cont_modifica.riempi_labels_cuoco(dipendente_temp)
        if self.ruolo_selezionato == "Cameriere":
            dipendente_temp = self.model.estrai_cameriere_nome(self.nome_selezionato)
            cont_modifica.cameriere = dipendente_temp
            cont_modifica.riempi_labels_cameriere(dipendente_temp)
        cont_modifica.view.exec()
        self.update_tabella()

    def update_tabella(self):
        camerieri = self.model.lista_camerieri
        cuochi = self.model.lista_cuochi
        self.view.tab.setRowCount(len(camerieri + cuochi))

        i = 0
        for x in camerieri:
            self.view.tab.setItem(i, 0, QTableWidgetItem(x.nome))
            self.view.tab.setItem(i, 1, QTableWidgetItem(x.ruolo))
            i += 1

        for x in cuochi:
            self.view.tab.setItem(i, 0, QTableWidgetItem(x.nome))
            self.view.tab.setItem(i, 1, QTableWidgetItem(x.ruolo))
            i += 1
