from Code.GestioneMagazzino.View.msg_elimina_materiaprima_view import VistaMsgEliminaMateriaPrima

class ContMsgEliminaMateriaPrima(object):
    def __init__(self, view: VistaMsgEliminaMateriaPrima):
        self.view = view
        self.conferma = False
        self.view.pulsante2.clicked.connect(self.confermato)
        self.view.pulsante1.clicked.connect(self.annullato)

    def confermato(self):
        print("confermato")
        self.conferma = True
        self.view.close()

    def annullato(self):
        print("annullato")
        self.conferma = False
        self.view.close()