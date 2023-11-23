from Code.GestioneMagazzino.View.msg_elimina_materiaprima_view import VistaMsgEliminaMateriaPrima

class ContMsgEliminaMateriaPrima(object):
    def __init__(self, view: VistaMsgEliminaMateriaPrima):
        self.view = view
        self.view.pulsante2.clicked.connect(self.confermato)

    def confermato(self):
        return True