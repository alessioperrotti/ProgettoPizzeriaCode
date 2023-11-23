import pickle
import uuid
from abc import ABC


class OggettoConID(ABC):
    ultimo_codice_ricevuta = 0
    ultimo_codice_ordine = 0
    ultimo_codice_prodotto = 0
    # e tutti i codici che ci servono
    @classmethod
    def genera_id(cls, tipo):
        if tipo == "ricevuta":
            cls.ultimo_codice_ricevuta += 1
            return cls.ultimo_codice_ricevuta
        elif tipo == "ordine":
            cls.ultimo_codice_ordine += 1
            return cls.ultimo_codice_ordine
        elif tipo == "prodotto":
            cls.ultimo_codice_prodotto += 1
            return cls.ultimo_codice_prodotto


    @classmethod
    def salva_su_file(cls, nome_file):
        # Salva gli attributi di classe in un file utilizzando pickle
        dati = {
            'cod_ric': cls.ultimo_codice_ricevuta,
            'cod_ord': cls.ultimo_codice_ordine,
            'cod_prod': cls.ultimo_codice_prodotto
        }

        with open(nome_file, 'wb') as file:
            pickle.dump(dati, file)
        file.close()

    @classmethod
    def carica_da_file(cls, nome_file):
        # Carica gli attributi di classe da un file utilizzando pickle
        with open(nome_file, 'rb') as file:
            dati = pickle.load(file)
            
        file.close()

        # Aggiorna gli attributi di classe con i dati caricati
        cls.ultimo_codice_ricevuta = dati['cod_ric']

        cls.ultimo_codice_ordine= dati['cod_ord']
        cls.ultimo_codice_prodotto = dati['cod_prod']
