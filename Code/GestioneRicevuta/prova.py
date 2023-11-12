import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

class ClickableButtonExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Esempio di QPushButton Cliccabile")
        self.setGeometry(100, 100, 400, 300)

        # Creazione del widget centrale
        central_widget = QWidget()

        # Creazione del layout verticale
        layout = QVBoxLayout()

        # Creazione di un QPushButton
        clickable_button = QPushButton("Cliccami!")
        clickable_button.clicked.connect(self.on_button_clicked)

        # Aggiunta del QPushButton al layout
        layout.addWidget(clickable_button)

        # Impostazione del layout centrale per il widget
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)

    def on_button_clicked(self):
        print("Il pulsante è stato cliccato!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ClickableButtonExample()
    window.show()
    sys.exit(app.exec())
