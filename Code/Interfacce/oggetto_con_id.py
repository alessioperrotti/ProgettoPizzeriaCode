import uuid
from abc import ABC


class OggettoConID(ABC):
    ultimo_codice = 0
    @classmethod
    def genera_id(cls):
        cls.ultimo_codice += 1
        return cls.ultimo_codice
