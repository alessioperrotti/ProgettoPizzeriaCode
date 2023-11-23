import pickle

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QLabel, QSizePolicy

from Code.GestioneMenu.Model.prodotto import Prodotto
from Code.GestioneRicevuta.Model.gestore_ricevuta import GestoreRicevuta
from Code.GestioneRicevuta.Model.ricevuta import Ricevuta
from Code.GestioneRicevuta.View.vista_info_ricevuta import VistaInfoRicevuta




class ContVistaInfoRicevuta():


    def __init__(self, gestore_ric:GestoreRicevuta):

        super().__init__()
        self.ricevuta_selezionata = None
        self.view = VistaInfoRicevuta()
        self.gestore_ric = gestore_ric
        self.numero_selezionato = None

    def imposta_info(self):

        self.ricevuta_selezionata = self.gestore_ric.ricerca_ricevuta_numero(self.numero_selezionato)

        self.view.lab_num_s.setText(str(self.ricevuta_selezionata.numero))


        self.view.lab_amm_s.setText(str(self.ricevuta_selezionata.ammontareLordo))

        self.view.lab_nom_s.setText(self.ricevuta_selezionata.nomeAcquirente)

        self.view.lab_ora_s.setText(self.ricevuta_selezionata.ora)

        self.view.lab_data_s.setText(self.ricevuta_selezionata.data)

        self.imposta_lista()


    def imposta_lista(self):

        list = self.ricevuta_selezionata.listaProdotti

        self.ricevuta_selezionata.listaProdotti.sort(key=lambda x: x.nome)
        for prodotto in self.ricevuta_selezionata.listaProdotti:
            lab = QLabel(f'<font color="black">&#8226;</font> '+ prodotto.nome + " € " + str(prodotto.prezzo_al_pubblico))
            lab.setFont(QFont("Roboto", 12))
            lab.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            self.view.layout_lista.addWidget(lab)
            self.view.layout_lista.addSpacing(5)

        self.view.layout_lista.addStretch()

