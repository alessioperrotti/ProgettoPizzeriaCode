import uuid
from abc import ABC


class OggettoConID(ABC):
    def genera_id(self):
        return int(uuid.uuid4())
