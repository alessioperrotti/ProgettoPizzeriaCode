from Code.GestioneMenu.Model.prodotto import Prodotto
import pickle


class GestoreMenu(object):

    def __init__(self):
        self.lista_prodotti: list[Prodotto] = []
        self.file_pickle_path = "listaProdotti.pickle"
        self.carica_da_file()

    def aggiungi_prodotto(self, prodotto):
        self.lista_prodotti.append(prodotto)
        self.salva_su_file()
        self.carica_da_file()

    def estrai_per_nome(self, nome):

        elemento_cercato = None
        for x in self.lista_prodotti:
            if x.nome == nome:
                elemento_cercato = x
        return elemento_cercato

    def estrai_per_codice(self, codice):

        elemento_cercato = None
        for x in self.lista_prodotti:
            if int(x.codice) == int(codice):
                elemento_cercato = x
        return elemento_cercato


    def elimina_prodotto(self, nome):

        elemento_da_eliminare = self.estrai_per_nome(nome)
        self.lista_prodotti.remove(elemento_da_eliminare)
        self.salva_su_file()
        self.carica_da_file()

    def modifica_prodotto(self, nome_prod, nuovo_prezzo, nuovi_ingredienti):

        prodotto_da_mod: Prodotto = self.estrai_per_nome(nome_prod)

        for x in self.lista_prodotti:
            if str(prodotto_da_mod.nome) == str(x.nome):
                x.prezzo_al_pubblico = nuovo_prezzo
                x.ingredienti = nuovi_ingredienti

        self.salva_su_file()
        self.carica_da_file()

    def carica_da_file(self):

        try:
            with open(self.file_pickle_path, 'rb') as file:
                self.lista_prodotti = pickle.load(file)
                file.close()
        except FileNotFoundError:
            print("file non trovato")
        except EOFError as e:
            print(e)

    def salva_su_file(self):

        try:
            with open(self.file_pickle_path, 'wb') as file:
                pickle.dump(self.lista_prodotti, file, pickle.HIGHEST_PROTOCOL)
            file.close()
        except FileNotFoundError as e:
            print(e)

    def get_info_prodotti(self):
        lista_prodotti = self.lista_prodotti.copy()
        return lista_prodotti