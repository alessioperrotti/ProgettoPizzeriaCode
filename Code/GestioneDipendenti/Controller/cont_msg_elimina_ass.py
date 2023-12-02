from Code.GestioneDipendenti.View.vista_msg_elimina_assegnamento import VistaMsgEliminaAssegnamento


class ContMsgEliminaAss(object):
    def __init__(self,model,view: VistaMsgEliminaAssegnamento):
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