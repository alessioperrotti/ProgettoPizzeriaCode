from Code.GestioneDipendenti.View.vista_modifica_turno import VistaModificaTurno


class ContModificaTurno(object):
    def __init__(self, model, view: VistaModificaTurno):
        self.view = view
        self.model = model
        self.cuoco = None
        self.cameriere = None