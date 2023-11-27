from Code.GestioneDipendenti.Model.utilizzatore import Utilizzatore


class Cameriere(Utilizzatore):
    def __init__(self, nome, cognome, email,username,password,stipendio):
        super().__init__(nome, cognome, email,username,password)
        self.data_ingaggio = None
        self.turno = None
        self.stipendio = stipendio
        self.ruolo = "Cameriere"

    def get_info_cameriere(self):
        print(f"Nome: {self.nome}")
        print(f"Cognome: {self.cognome}")
        print(f"Email: {self.email}")
        print(f"Ruolo: {self.ruolo}")
 #       print(f"Data di Nascita: {self.data_nascita.toString("dd-MM-yyyy")}")
        print(f"Data di Ingaggio: {self.data_ingaggio}")
        print(f"Username: {self.username}")
        print(f"Password: {self.password}")
