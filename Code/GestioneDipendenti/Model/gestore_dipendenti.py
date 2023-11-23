from Code.GestioneDipendenti.Model.cameriere import Cameriere
from Code.GestioneDipendenti.Model.cuoco import Cuoco


class GestoreDipendenti():
    def __init__(self):
        self.lista_cuochi = []
        self.lista_camerieri = []

    def aggiungi_cuoco(self, cuoco):
        self.lista_cuochi.append(cuoco)

    # def ricerca_cuoco_nome(self, nome):
    #     list = []
    #     for cuoco in self.lista_cuochi:
    #         if nome == cuoco.nome:
    #             list.append(cuoco)

    def estrai_cuoco_nome(self, nome):
        for cuoco in self.lista_cuochi:
            if nome == cuoco.nome:
                print("trovato")
                return cuoco

    def elimina_cuoco(self, nome):
        cuoco_da_eliminare = self.estrai_cuoco_nome(nome)
        self.lista_cuochi.remove(cuoco_da_eliminare)

    def modifica_cuoco(self, nome_ricerca, new_email, new_stipendio,
                           new_data_nascita, new_username, new_password):
        cuoco: Cuoco = self.estrai_cuoco_nome(nome_ricerca)
        for x in self.lista_cuochi:
            if cuoco.nome == x.nome:
                x.email = new_email
                x.stipendio = new_stipendio
                x.data_nascita = new_data_nascita
                x.username = new_username
                x.password = new_password
                print(x.email)

    #########################################################################
    def aggiungi_cameriere(self, cameriere):
        self.lista_camerieri.append(cameriere)

    # def ricerca_cameriere_nome(self, nome):
    #     list = []
    #     for cameriere in self.lista_camerieri:
    #         if nome == cameriere.nome:
    #             list.append(cameriere)

    def estrai_cameriere_nome(self, nome):
        for cameriere in self.lista_camerieri:
            if nome == cameriere.nome:
                return cameriere

    def elimina_cameriere(self, nome):
        cameriere_da_eliminare = self.estrai_cameriere_nome(nome)
        self.lista_camerieri.remove(cameriere_da_eliminare)

    def modifica_cameriere(self, nome,new_email, new_stipendio,
                              new_data_nascita, new_username, new_password):
        cameriere: Cameriere = self.estrai_cameriere_nome(nome)
        for x in self.lista_camerieri:
            if cameriere.nome == x.nome:
                x.email = new_email
                x.stipendio = new_stipendio
                x.data_nascita = new_data_nascita
                x.username = new_username
                x.password = new_password




