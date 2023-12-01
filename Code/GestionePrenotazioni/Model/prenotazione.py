class Prenotazione(object):
    def __init__(self,codice,nome_cliente,tavolo_assegnato,n_persone,orario):
        self.codice = codice
        self.nome_cliente = nome_cliente
        self.tavolo_assegnato = tavolo_assegnato
        self.n_persone = n_persone
        self.orario = orario
        self.data = None
        # self.orario_fine = None


