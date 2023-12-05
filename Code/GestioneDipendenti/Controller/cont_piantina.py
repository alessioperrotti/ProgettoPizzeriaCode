from PyQt6.QtWidgets import QPushButton, QWidget

from Code.GestioneDipendenti.View.vista_piantina import VistaPiantina
from Code.GestionePrenotazioni.Model.gestore_prenotazioni import GestorePrenotazioni


class ContPiantina(object):
    def __init__(self, model: GestorePrenotazioni, view: VistaPiantina):
        self.view = view
        self.model = model
        self.tavolo_selezionato = None
        self.view.pulsante_consegna.clicked.connect(self.cambia_colore)
        self.view.pulsante_consegna.clicked.connect(self.update_tabella)
        self.update_tabella()

    def cambia_colore(self):
        self.tavolo_selezionato = self.model.ricerca_tavolo(self.view.n_tavolo)
        self.tavolo_selezionato.cambia_stato("servito")

        self.model.salva_dati("lista_prenotazioni.pickle")
        # print("tavolo: "+str(self.tavolo_selezionato.numero)+" posti: "+str(self.tavolo_selezionato.posti_disponibili))
        # print(self.tavolo_selezionato.stato)


    def update_tabella(self):
        for tavolo in self.model.lista_tavoli:
            numero_tavolo = tavolo.numero
            stato_tavolo = tavolo.stato
            tavolo_button = self.view.nome_tavoli_map[numero_tavolo]

            if tavolo_button is not None:
                if str(stato_tavolo) == "libero":
                    tavolo_button.setStyleSheet("""
                            QPushButton{
                                background-color: "grey";
                                color: "black";
                                text-align: center;
                                border-radius: 6px;
                                border: 3px solid lightgrey;
                                font-family: Roboto;
                            }
                            QPushButton:checked{
                                                    background-color: "lightgrey";
                                                    color: "black";
                                                }
                            QPushButton:hover{
                                font-size: 15px;
                                font-weight: bold;
                            }""")
                elif stato_tavolo == "servito":
                    tavolo_button.setStyleSheet("""
                            QPushButton{
                                background-color: "yellow";
                                color: "black";
                                text-align: center;
                                border-radius: 6px;
                                border: 3px solid lightgrey;
                                font-family: Roboto;
                            }QPushButton:checked{
                                                    background-color: "lightyellow";
                                                    color: "black";
                                                }
                            QPushButton:hover{
                                font-size: 15px;
                                font-weight: bold;
                            }""")
                elif stato_tavolo == "prenotato":
                    tavolo_button.setStyleSheet("""
                            QPushButton{
                                background-color: "#007fff";
                                color: "white";
                                text-align: center;
                                border-radius: 6px;
                                border: 3px solid lightgrey;
                                font-family: Roboto;
                            }QPushButton:checked{
                                                    background-color: "lightblue";
                                                    color: "black";
                                                }
                            QPushButton:hover{
                                font-size: 15px;
                                font-weight: bold;
                            }""")
                elif stato_tavolo == "occupato":
                    tavolo_button.setStyleSheet("""
                            QPushButton{
                                background-color: "red";
                                color: "white";
                                text-align: center;
                                border-radius: 6px;
                                border: 3px solid lightgrey;
                                font-family: Roboto;
                            }QPushButton:checked{
                                                    background-color: "lightred";
                                                    color: "black";
                                                }
                            QPushButton:hover{
                                font-size: 15px;
                                font-weight: bold;
                            }""")
                elif stato_tavolo == "in attesa":
                    tavolo_button.setStyleSheet("""
                            QPushButton{
                                background-color: "orange";
                                color: "black";
                                text-align: center;
                                border-radius: 6px;
                                border: 3px solid lightgrey;
                                font-family: Roboto;
                            }QPushButton:checked{
                                                    background-color: "lightorange";
                                                    color: "black";
                                                }
                            QPushButton:hover{
                                font-size: 15px;
                                font-weight: bold;
                            }""")






