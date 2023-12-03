
class Tavolo(object):

    def __init__(self, numero, posti_disponibili):

        self.numero = numero
        self.posti_disponibili = posti_disponibili
        self.stato = "libero"

    def cambia_stato(self, nuovo_stato):
        self.stato = nuovo_stato