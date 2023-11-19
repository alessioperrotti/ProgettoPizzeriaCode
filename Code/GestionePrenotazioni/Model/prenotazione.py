class Prenotazione(object):
    def __init__(self,codice,data,nome_cliente,tavolo_assegnato):
        self.codice = codice
        self.data = data
        self.nome_cliente = nome_cliente
        self.tavolo_assegnato = tavolo_assegnato
        self.orario = None
        self.orario_fine = None

