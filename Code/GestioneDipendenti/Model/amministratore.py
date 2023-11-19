from Code.GestioneDipendenti.Model.utilizzatore import Utilizzatore


class Amministratore(Utilizzatore):
    def __init__(self, nome, cognome, email,partita_IVA):
        super().__init__(nome, cognome, email)
        self.partita_IVA = partita_IVA