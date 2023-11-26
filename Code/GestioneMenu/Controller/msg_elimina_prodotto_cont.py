from Code.GestioneMenu.View.msg_elimina_prodotto_view import VistaMsgEliminaProdotto

class ContMsgEliminaProdotto(object):
    def __init__(self, view: VistaMsgEliminaProdotto):
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