#!/usr/bin/python

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QLCDNumber, QSlider, QLabel, QPushButton, QVBoxLayout, QApplication, QSpacerItem,
                             QSizePolicy, QHBoxLayout, QFrame, QLineEdit, QGridLayout)
from PyQt6.QtGui import QFont, QPixmap

label_font = QFont("Roboto", 24)
label_font_tit = QFont("Roboto", 40, weight=50)
label_font_piccolo = QFont("Roboto", 14)

def Pulsante(nome):
    pulsante = QPushButton(nome)
    pulsante.setFont(label_font)
    pulsante.setSizePolicy(QSizePolicy.Policy.Minimum,QSizePolicy.Policy.Minimum)
    pulsante.setStyleSheet("background-color: #ff776d; border: 2px solid black; border-radius: 10px; padding: 10px")
    return pulsante

class Vista_Login(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
# Definizione oggetti

        label = QLabel("Benvenuti!")
        label.setFont(label_font_tit)
        spazio_verticale = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        spazio_tra_pulsanti = QSpacerItem(20, 20)
        pulsante1 = Pulsante("Accedi al sistema")
        pulsante1.setFixedSize(360, 80)
        pulsante2 = Pulsante("Accedi come cliente")
        pulsante2.setFixedSize(360, 80)

# Definizione Layout
        layout = QVBoxLayout()
# Inserimento Item nel Layout
        layout.addItem(spazio_verticale)
        layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)

        layout.addSpacerItem(spazio_tra_pulsanti)
        layout.addWidget(pulsante1, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addSpacerItem(spazio_tra_pulsanti)
        layout.addWidget(pulsante2, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addItem(spazio_verticale)

        self.setFixedSize(994, 637)
        self.setLayout(layout)

        self.show()



class Vista_Login_Dipendente(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        #Definizione oggetti
        label1 = QLabel("Login")
        label1.setFont(label_font_tit)
        label2 = QLabel("inserisci le <b>credenziali</b> per accedere al sistema")
        label2.setFont(label_font_piccolo)
        #label2.setFont(label_font)
        frame = QFrame()
        spazio = QSpacerItem(20, 40,QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        frame.setStyleSheet('.QFrame {border: 2px solid black; border-radius: 10px; padding: 10px}')
        frame.setSizePolicy(QSizePolicy.Policy.Minimum,QSizePolicy.Policy.Minimum)

        user_label = QLabel("Username: ")
        user_label.setFont(label_font_piccolo)
        pass_label = QLabel("Password: ")
        pass_label.setFont(label_font_piccolo)


        user_line = QLineEdit()
        pass_line = QLineEdit()
        user_line.setStyleSheet("border: 2px solid black; border-radius: 4px;")
        pass_line.setStyleSheet("border: 2px solid black; border-radius: 4px;")

        pulsante = Pulsante("Login")
        pulsante.setFont(label_font_piccolo)
        label_foto = QLabel()
        pixmap = QPixmap("png/key.png")
        scaled_pixmap = pixmap.scaled(50, 50, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
        label_foto.setPixmap(scaled_pixmap)


        #Definizione Layout
        layout = QVBoxLayout()
        frame_layout = QVBoxLayout()
        login_layout = QHBoxLayout()
        insert_layout = QGridLayout()


        #Inserimento Oggetti Layout
        insert_layout.addWidget(user_label,1,1)
        insert_layout.addWidget(user_line,1,2)
        insert_layout.addWidget(pass_label,2,1)
        insert_layout.addWidget(pass_line,2,2)
        insert_layout.addWidget(pulsante,3,2)


        login_layout.addWidget(label1)
        login_layout.addWidget(label_foto)
        login_layout.addStretch()


        frame_layout.addLayout(login_layout)
        frame_layout.addSpacerItem(QSpacerItem(1,10))
        frame_layout.addWidget(label2)
        frame_layout.addSpacerItem(QSpacerItem(1,10))
        frame_layout.addLayout(insert_layout)
        frame.setLayout(frame_layout)

        layout.addSpacerItem(spazio)
        layout.addWidget(frame, alignment= Qt.AlignmentFlag.AlignCenter)
        layout.addSpacerItem(spazio)

        self.setFixedSize(994, 637)
        self.setLayout(layout)
        self.show()





def main():
    app = QApplication(sys.argv)
    ex = Vista_Login_Dipendente()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()