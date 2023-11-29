import pickle

from Code.GestioneRicevuta.Model.ricevuta import Ricevuta


class GestoreRicevuta:

    def __init__(self):
        self.lista_ricevute = []
        self.ultimo_codice_ricevuta = 0
        self.nome_file = "lista_ricevute.pickle"
        try:
            self.carica_da_file(self.nome_file)
        except FileNotFoundError:
            print("dati ricevute non trovati")

    def aggiungi_ricevuta(self, ammontareLordo, data, listaProdotti, nomeAcquirente, ora):
        numero = self.genera_id()
        self.lista_ricevute.append(Ricevuta(ammontareLordo, data, listaProdotti, nomeAcquirente, numero, ora))
        self.salva_su_file(self.nome_file)
        return numero

    def ricerca_ricevuta_nome(self, nomeAcquirente):
        list = []
        for ricevuta in self.lista_ricevute:
            if nomeAcquirente == ricevuta.nomeAcquirente:
                list.append(ricevuta)

    def ricerca_ricevuta_numero(self, numero):
        for ricevuta in self.lista_ricevute:
            if numero == ricevuta.numero:
                return ricevuta

    def elimina_ricevuta(self, numero):
        ricevuta_da_eliminare = self.ricerca_ricevuta_numero(numero)
        self.lista_ricevute.remove(ricevuta_da_eliminare)
        self.salva_su_file(self.nome_file)

    def genera_id(self):
        self.ultimo_codice_ricevuta += 1
        return self.ultimo_codice_ricevuta

    def salva_su_file(self, nome_file):
        # Salva lista di ricevute e ultimo codice in un file utilizzando pickle
        dati = {

            'cod': self.ultimo_codice_ricevuta,
            'lista': self.lista_ricevute

        }

        with open(nome_file, 'wb') as file:
            pickle.dump(dati, file)
        file.close()

    def carica_da_file(self, nome_file):
        # Carica i dati da un file utilizzando pickle
        with open(nome_file, 'rb') as file:
            dati = pickle.load(file)

        file.close()

        # Aggiorna i dati correnti con i dati caricati
        self.ultimo_codice_ricevuta = dati['cod']
        self.lista_ricevute = dati['lista']
