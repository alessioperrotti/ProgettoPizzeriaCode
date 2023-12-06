from Code.GestioneOrdiniTavolo.View.msg_termina_servizio_view import VistaMsgTerminaServizio

class ContMsgTerminaServizio(object):
    def __init__(self, view: VistaMsgTerminaServizio):
        self.view = view
        self.conferma = False
        self.view.pulsante2.clicked.connect(self.confermato)
        self.view.pulsante1.clicked.connect(self.annullato)

    def confermato(self):
        self.conferma = True
        self.view.close()

    def annullato(self):
        self.conferma = False
        self.view.close()