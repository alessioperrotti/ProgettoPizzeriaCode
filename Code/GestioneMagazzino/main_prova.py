import sys
from PyQt6.QtWidgets import QApplication
from Code.GestioneMagazzino.Controller.gestione_magazzino_cont import ContGestioneMagazzino
from Code.GestioneMagazzino.View.gestione_magazzino_view import VistaGestioneMagazzino
from Code.GestioneMagazzino.Model.gestore_magazzino import GestoreMagazzino

app = QApplication(sys.argv)

gestione_view = VistaGestioneMagazzino()
gestore = GestoreMagazzino()
gestione_cont = ContGestioneMagazzino(gestore, gestione_view)
gestione_view.show()

sys.exit(app.exec())


