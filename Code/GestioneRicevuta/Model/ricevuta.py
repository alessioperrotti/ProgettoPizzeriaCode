class Ricevuta:
    def __init__(self, ammontare_lordo=None, data=None, lista_prodotti=None, nome_acquirente=None, numero=None, ora=None, tavolo=None):
        self.ora = ora
        self.numero = numero
        self.nomeAcquirente = nome_acquirente
        self.listaProdotti = lista_prodotti
        self.data = data
        self.ammontareLordo = ammontare_lordo
        self.tavolo = tavolo
