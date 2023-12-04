import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QFrame
from PyQt6.QtCore import Qt

class PiantinaApp(QWidget):
    def __init__(self):
        super().__init__()

        # Layout della griglia
        layout = QGridLayout(self)

        # Aggiungi label dei tavoli alla griglia
        for row in range(4):
            for col in range(4):
                tavolo_label = QLabel(f"Tavolo {row * 4 + col + 1}")
                tavolo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                tavolo_label.setFrameShape(QFrame.Shape.Box)  # Aggiunge un bordo per evidenziare la cliccabilità
                tavolo_label.setStyleSheet("QLabel { background-color : lightblue; }")  # Imposta lo stile
                tavolo_label.setCursor(Qt.CursorShape.PointingHandCursor)  # Cambia il cursore al puntatore della mano
                tavolo_label.mousePressEvent = lambda event, tavolo=tavolo_label.text(): self.on_tavolo_clicked(tavolo)
                layout.addWidget(tavolo_label, row, col)

        # Imposta alcune opzioni della finestra
        self.setWindowTitle("Piantina con Tavoli")
        self.setGeometry(100, 100, 400, 300)

    def on_tavolo_clicked(self, tavolo):
        print(f"Tavolo {tavolo} cliccato!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PiantinaApp()
    window.show()
    sys.exit(app.exec())
