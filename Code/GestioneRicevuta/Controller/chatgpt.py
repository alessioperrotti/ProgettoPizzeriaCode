import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QScrollArea

class Finestra(QWidget):
    def __init__(self):
        super().__init__()

        # Crea una QScrollArea
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)  # Per consentire la ridimensionamento automatico del widget interno

        # Crea un widget per contenere le label
        contenitore_labels = QWidget()
        layout_labels = QVBoxLayout(contenitore_labels)

        # Aggiungi alcune label di esempio
        for i in range(20):
            label = QLabel(f"Label {i}")
            layout_labels.addWidget(label)

        # Imposta il widget contenitore come widget interno della QScrollArea
        self.scroll_area.setWidget(contenitore_labels)

        # Layout principale
        layout_principale = QVBoxLayout(self)
        layout_principale.addWidget(self.scroll_area)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    finestra = Finestra()
    finestra.show()
    sys.exit(app.exec())
