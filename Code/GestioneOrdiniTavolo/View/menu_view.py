from PyQt6.QtWidgets import *

class VistaMenu(QWidget):

    def __init__(self):

        super().__init__()
        self.initUI()
        self.setStyleSheet("""
                    QPushButton{
                        background-color: "#ff776d";
                        color: "white";
                        text-align: center;
                        border-radius: 6px;
                        font-family:Roboto;
                    }
                    QPushButton:hover{
                        background-color: "red";
                        font-size: 13px;
                    }
                    QTableWidget {
                        background-color: white;
                        alternate-background-color: white;
                        selection-background-color: darkcyan;
                        border: 2px solid grey;
                    }
                    QHeaderView:section {
                        background-color: lightgray;
                        font-weight: bold;
                    }
                    QHeaderView:active {
                        background-color: gray;
                    }
                """)


    def initUI(self):

        main_layout = QHBoxLayout(self)
        vbox_sinistra = QVBoxLayout()
        vbox_centrale = QVBoxLayout()
        vbox_destra = QVBoxLayout()

