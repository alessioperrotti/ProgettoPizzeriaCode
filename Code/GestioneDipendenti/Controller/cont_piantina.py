from PyQt6.QtWidgets import QPushButton, QWidget, QStackedWidget
from datetime import datetime
from Code.GestioneDipendenti.View.vista_piantina import VistaPiantina
from Code.GestionePrenotazioni.Model.gestore_prenotazioni import GestorePrenotazioni


class ContPiantina(object):
    def __init__(self, model: GestorePrenotazioni, stacked: QStackedWidget):
        self.stacked = stacked
        self.view = VistaPiantina()
        stacked.addWidget(self.view)
        self.model = model
        self.tavolo_selezionato = None
        self.view.pulsante_consegna.clicked.connect(self.cambia_colore)
        self.view.pulsante_consegna.clicked.connect(self.update_tabella)
        self.update_tabella()
        # self.model.gestore_ordini_tavolo.carica_da_file()

    def cambia_colore(self):
        self.tavolo_selezionato = self.model.ricerca_tavolo(self.view.n_tavolo)
        self.tavolo_selezionato.cambia_stato("servito")

        # for prenotazione in self.model.lista_prenotazioni:
        #     if int(prenotazione.tavolo_assegnato.numero) == int(self.view.n_tavolo):
        #         print("c")
        #         prenotazione.tavolo_assegnato.cambia_stato("servito")

        self.model.salva_dati("lista_prenotazioni.pickle", "lista_tavoli.pickle")

    def update_tabella(self):
        data_corrente = datetime.now().date()
        # print(data_corrente)

        for tavolo in self.model.lista_tavoli:
            numero_tavolo = tavolo.numero
            stato_tavolo = tavolo.stato
            tavolo_button = self.view.nome_tavoli_map[numero_tavolo]

            # tavolo_prenotato = False
            # for prenotazione in self.model.lista_prenotazioni:
            #     if (int(prenotazione.tavolo_assegnato.numero) == int(numero_tavolo) and prenotazione.data.toPyDate() == data_corrente
            #             and prenotazione.tavolo_assegnato.stato == "prenotato"):
            #         # print("stessa data")
            #         tavolo_prenotato = True
            #         break

            # if tavolo_button is not None:
            #     if tavolo_prenotato:

            if stato_tavolo == "prenotato":
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
                                                background-color: "#f75e25";
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
                                                background-color: "#fb6f4c";
                                                color: "black";
                                            }
                        QPushButton:hover{
                            font-size: 15px;
                            font-weight: bold;
                        }""")
            else:
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
