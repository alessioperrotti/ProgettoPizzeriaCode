from Code.GestioneDipendenti.Model.utilizzatore import Utilizzatore


class Cuoco(Utilizzatore):
    def __init__(self, nome, cognome, email,stipendio):
        super().__init__(nome, cognome, email)
        self.data_ingaggio = None
        self.stipendio = stipendio