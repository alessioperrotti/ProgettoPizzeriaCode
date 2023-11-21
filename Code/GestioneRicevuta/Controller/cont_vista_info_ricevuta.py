from PyQt6.QtWidgets import QLabel

from Code.GestioneRicevuta.Model.gestore_ricevuta import GestoreRicevuta
from Code.GestioneRicevuta.Model.ricevuta import Ricevuta
from Code.GestioneRicevuta.View.vista_info_ricevuta import VistaInfoRicevuta


class ContVistaInfoRicevuta():
    def __init__(self, gestore_ric:GestoreRicevuta, ricevuta_selezionata:Ricevuta):
        super().__init__()
        self.view = VistaInfoRicevuta()
        self.gestore_ric = gestore_ric
        self.ricevuta_selezionata = ricevuta_selezionata

    def imposta_info(self):
        self.view.lab_num_s = self.ricevuta_selezionata.numero
        self.view.lab_amm_s = self.ricevuta_selezionata.ammontareLordo
        self.view.lab_nom_s = self.ricevuta_selezionata.nomeAcquirente
        self.view.lab_ora_s = self.ricevuta_selezionata.ora
        self.view.lab_data_s = self.ricevuta_selezionata.data
        self.imposta_lista()

    def imposta_lista(self):
        self.ricevuta_selezionata.listaProdotti.sort(key=lambda x: x.nome)
        for prodotto in self.ricevuta_selezionata.listaProdotti:
            self.view.layout_lista.addWidget(QLabel(f'<font color="black">&#8226;</font> '+ prodotto.nome + " " + str(prodotto.prezzo)))
        pass



