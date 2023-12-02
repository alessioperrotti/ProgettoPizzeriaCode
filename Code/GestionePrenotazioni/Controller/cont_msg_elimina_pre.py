from Code.GestionePrenotazioni.View.vista_msg_elimina_prenotazione import VistaMsgEliminaPrenotazione


class ContMsgEliminaPre(object):
    def __init__(self,model,view: VistaMsgEliminaPrenotazione):
        self.model = model
        self.view = view
        self.conferma = False
        self.view.pulsante1.clicked.connect(self.annullato)
        self.view.pulsante2.clicked.connect(self.confermato)

    def confermato(self):
        self.conferma = True
        self.view.close()

    def annullato(self):
        self.conferma = False
        self.view.close()