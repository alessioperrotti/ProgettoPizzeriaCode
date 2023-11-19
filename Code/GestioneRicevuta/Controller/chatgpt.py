import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox, QDialog


class MainWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Finestra Principale")
        self.setGeometry(100, 100, 400, 200)

        self.layout = QVBoxLayout()

        self.text_input = QLineEdit(self)
        self.layout.addWidget(self.text_input)

        self.button = QPushButton("Mostra Messaggio", self)
        self.button.clicked.connect(self.show_message)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

    def show_message(self):
        input_text = self.text_input.text()

        if not input_text:
            QMessageBox.critical(self, "Errore", "Il campo di testo non può essere vuoto.", QMessageBox.StandardButton.Ok)
        else:
            QMessageBox.information(self, "Messaggio", f"Hai inserito il testo: {input_text}", QMessageBox.StandardButton.Ok)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
