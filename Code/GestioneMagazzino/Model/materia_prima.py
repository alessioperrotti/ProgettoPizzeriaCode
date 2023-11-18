
class MateriaPrima(object):

    def __init__(self, codice, nome, costo_al_kg, qta_disponibile, qta_limite, qta_ordine_STD):

        self.codice = codice
        self.nome = nome
        self.costo_al_kg = costo_al_kg
        self.qta_disponibile = qta_disponibile
        self.qta_limite = qta_limite
        self.qta_ordine_STD = qta_ordine_STD
        self.data_scadenza = None
