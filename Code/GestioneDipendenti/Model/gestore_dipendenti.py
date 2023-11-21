from Code.GestioneDipendenti.Model.cuoco import Cuoco
from Code.GestioneDipendenti.Model.cameriere import Cameriere

class GestoreDipendenti():
    def __init__(self):
        self.lista_cuochi = []
        self.lista_camerieri = []

    def aggiungi_cuoco(self,nome, cognome, email, stipendio,username,password):
        self.lista_cuochi.append(Cuoco(nome, cognome, email, stipendio,username,password))

    def ricerca_cuoco_nome(self, nome):
        list = []
        for cuoco in self.lista_cuochi:
            if nome == cuoco.nome:
                list.append(cuoco)

    def ricerca_cuoco_cognome(self, cognome):
        for cuoco in self.lista_cuochi:
            if cognome == cuoco.cognome:
                return cuoco

    def elimina_cuoco(self, cognome):
        cuoco_da_eliminare = self.ricerca_cuoco_cognome(cognome)
        self.lista_camerieri.remove(cuoco_da_eliminare)

#########################################################################
    def aggiungi_cameriere(self, nome, cognome, email, stipendio,username,password):
        self.lista_camerieri.append(Cuoco(nome, cognome, email, stipendio,username,password))

    def ricerca_cameriere_nome(self, nome):
        list = []
        for cameriere in self.lista_camerieri:
            if nome == cameriere.nome:
                list.append(cameriere)

    def ricerca_cameriere_cognome(self, cognome):
        for cameriere in self.lista_camerieri:
            if cognome == cameriere.cognome:
                return cameriere

    def elimina_cameriere(self, cognome):
        cameriere_da_eliminare = self.ricerca_cameriere_cognome(cognome)
        self.lista_camerieri.remove(cameriere_da_eliminare)