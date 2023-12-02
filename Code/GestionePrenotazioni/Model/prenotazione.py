class Prenotazione(object):
    def __init__(self,codice,nome_cliente,tavolo_assegnato,n_persone,orario):
        self.codice = codice
        self.nome_cliente = nome_cliente
        self.tavolo_assegnato = tavolo_assegnato
        self.n_persone = n_persone
        self.orario = orario
        self.data = None
        # self.orario_fine = None

        #ho prenotazioni a cui è associato un orario
        #ho lista di prenotazioni
        #ricerco tutte quelle che hanno un orario specifico
        #conto quante prenotazioni ci sono in quell'orario
        #faccio la somma delle persone totali


