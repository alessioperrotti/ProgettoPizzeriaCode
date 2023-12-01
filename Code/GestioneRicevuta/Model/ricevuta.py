class Ricevuta:
    def __init__(self, ammontareLordo=None, data=None, listaProdotti=None, nomeAcquirente=None, numero=None, ora=None, tavolo=None):
        self.ora = ora
        self.numero = numero
        self.nomeAcquirente = nomeAcquirente
        self.listaProdotti = listaProdotti
        self.data = data
        self.ammontareLordo = ammontareLordo
        self.tavolo = tavolo
