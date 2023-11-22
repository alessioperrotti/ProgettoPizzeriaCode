
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
                print("x")
                return cuoco

    def elimina_cuoco(self, cognome):
        cuoco_da_eliminare = self.estrai_cuoco_nome(cognome)
        self.lista_camerieri.remove(cuoco_da_eliminare)

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

    def elimina_cameriere(self, cognome):
        cameriere_da_eliminare = self.estrai_cameriere_nome(cognome)
        self.lista_camerieri.remove(cameriere_da_eliminare)
