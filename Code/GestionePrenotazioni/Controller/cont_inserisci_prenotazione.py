from Code.GestionePrenotazioni.View.vista_inserisci_prenotazione import VistaInserisciPrenotazione
from Code.GestionePrenotazioni.Model.prenotazione import Prenotazione
from PyQt6.QtCore import QDate


class ContInserisciPrenotazione(object):

    def __init__(self, model, view: VistaInserisciPrenotazione):
        self.view = view
        self.model = model
        self.view.pulsante_conferma.clicked.connect(self.conferma_inserimento)

    def conferma_inserimento(self):
        nome = self.view.campo_nome.text()
        n_persone = self.view.spinbox_persone.value()
        print(n_persone)
        tavolo = self.view.combobox_tavolo.currentText()
        orario = self.view.combobox_orario.currentText()
        codice = self.model.genera_codice()

        nuova_prenotazione = Prenotazione(codice,nome,tavolo,n_persone,orario)
        nuova_prenotazione.data = self.view.calendario.selectedDate()
        print(nuova_prenotazione.codice)
        #nuova_prenotazione.orario_fine = bohh
        self.model.aggiungi_prenotazione(nuova_prenotazione)

        self.view.close()

    def riempi_labels(self):
        orari_prenotazioni = ["12:30", "13:00", "13:30","14:00","14:30","15:00"]
        self.view.combobox_orario.addItems(orari_prenotazioni)

        for numero_tavolo in range(1, 17):
            self.view.combobox_tavolo.addItem(str(numero_tavolo))


