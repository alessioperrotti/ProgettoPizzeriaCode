#!/usr/bin/python

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton, QVBoxLayout, QApplication, QSpacerItem,
                             QSizePolicy, QHBoxLayout, QFrame, QLineEdit, QGridLayout)

label_font = QFont("Roboto", 24)
label_font_tit = QFont("Roboto", 40, weight=50)
label_font_piccolo = QFont("Roboto", 14)


def Pulsante(nome):
    pulsante = QPushButton(nome)
    pulsante.setFont(label_font)
    pulsante.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
    #pulsante.setStyleSheet("background-color: #ff776d; border: 2px solid black; border-radius: 10px; padding: 10px")
    return pulsante


class VistaLoginDipendente(QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("""
            QPushButton{
                background-color: "#ff776d";
                color: "white";
                text-align: center;
                border-radius: 6px;
                font-size: 24px;
                padding: 10px;
            }
            QPushButton:hover{
                background-color: "red";
                font-size: 24px;
            }
            QTableWidget {
                background-color: white;
                alternate-background-color: white;
                selection-background-color: darkcyan;
                border: 2px solid grey;
            }
            QHeaderView:section {
                font-weight: bold;
                background-color: lightgray;
            }
            QHeaderView:active {
                background-color: gray;
            }
        """)

        self.init_ui()

    def init_ui(self):
        # Definizione oggetti
        self.label1 = QLabel("Login")
        self.label1.setFont(label_font_tit)
        self.label2 = QLabel("inserisci le <b>credenziali</b> per accedere al sistema")
        self.label2.setFont(label_font_piccolo)
        # self.label2.setFont(label_font)
        frame = QFrame()
        spazio = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        frame.setStyleSheet('.QFrame {border: 2px solid black; border-radius: 10px; padding: 10px; background-color: #dddddd}')
        frame.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.user_label = QLabel("Username: ")
        self.user_label.setFont(label_font_piccolo)
        self.pass_label = QLabel("Password: ")
        self.pass_label.setFont(label_font_piccolo)

        self.user_line = QLineEdit()
        self.pass_line = QLineEdit()
        self.pass_line.setEchoMode(QLineEdit.EchoMode.Password)
        self.user_line.setStyleSheet("border: 2px solid black; border-radius: 4px;")
        self.pass_line.setStyleSheet("border: 2px solid black; border-radius: 4px;")

        self.pulsante= Pulsante("Login")
        (self.pulsante.setFont(label_font_piccolo))
        label_foto = QLabel()
        pixmap = QPixmap("png/key.png")
        scaled_pixmap = pixmap.scaled(50, 50, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
        label_foto.setPixmap(scaled_pixmap)

        # Definizione Layout
        layout = QVBoxLayout()
        frame_layout = QVBoxLayout()
        login_layout = QHBoxLayout()
        insert_layout = QGridLayout()

        # Inserimento Oggetti Layout
        insert_layout.addWidget(self.user_label, 1, 1)
        insert_layout.addWidget(self.user_line, 1, 2)
        insert_layout.addWidget(self.pass_label, 2, 1)
        insert_layout.addWidget(self.pass_line, 2, 2)
        insert_layout.addWidget(self.pulsante, 3, 2)

        login_layout.addWidget(self.label1)
        login_layout.addWidget(label_foto)
        login_layout.addStretch()

        frame_layout.addLayout(login_layout)
        frame_layout.addSpacerItem(QSpacerItem(1, 10))
        frame_layout.addWidget(self.label2)
        frame_layout.addSpacerItem(QSpacerItem(1, 10))
        frame_layout.addLayout(insert_layout)
        frame.setLayout(frame_layout)

        layout.addSpacerItem(spazio)
        layout.addWidget(frame, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addSpacerItem(spazio)

        self.setFixedSize(994, 637)
        self.setLayout(layout)



def main():
    app = QApplication(sys.argv)
    ex = VistaLoginDipendente()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
