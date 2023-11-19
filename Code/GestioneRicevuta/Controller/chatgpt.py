import sys

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

class Finestra(QWidget):
    def __init__(self):
        super().__init__()

        # Creazione del layout verticale
        layout_verticale = QVBoxLayout()

        # Aggiungi le label all'elenco con un "puntino" a sinistra
        for i in range(1, 6):  # Cambia questo intervallo a seconda di quante label desideri
            label = QLabel(f'<font color="black">&#8226;</font> Label {i}')  # &#8226; è il codice HTML per un punto di lista
            layout_verticale.addWidget(label)

        # Imposta il layout principale per la finestra
        self.setLayout(layout_verticale)

        # Impostazioni della finestra principale
        self.setWindowTitle("Finestra con Elenco di QLabel")
        self.setGeometry(100, 100, 400, 300)

if __name__ == '__main__':
    app = QApplication([])

    finestra = Finestra()
    finestra.show()

    sys.exit(app.exec())
