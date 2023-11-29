from matplotlib import pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg

from Code.GestioneOrdiniTavolo.Model.gestore_ordini_tavolo import GestoreOrdiniTavolo
from Code.GestioneRicevuta.Model.gestore_ricevuta import GestoreRicevuta
from Code.GestioneSistema.View.vista_statistiche import VistaStatistiche


class ContVistaStatistiche:
    def __init__(self, gestore_ric:GestoreRicevuta):
        self.view = VistaStatistiche()
        self.gestore_ric = gestore_ric

    def aggiorna_grafici(self):
        fig, ax = plt.subplots(figsize=(5, 2), layout='constrained')

        categories = ['rutabaga', 'cucumber', 'pumpkins']
        valori = [10, 100, 50]
        ax.bar(categories, valori)
        self.grafico1 = FigureCanvasQTAgg(fig)
        self.view.grid_layout.addWidget(self.grafico1, 0, 1)





