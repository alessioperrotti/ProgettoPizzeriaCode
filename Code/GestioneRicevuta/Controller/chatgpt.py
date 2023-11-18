import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QScrollArea
from PyQt6 import QtCore

class Finestra(QWidget):
    def __init__(self):
        super().__init__()

        # Creazione del layout principale
        layout = QVBoxLayout()

        # Creazione dell'area di scorrimento
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        # Nascondi le barre di scorrimento
        scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        # Widget contenitore per le label
        content_widget = QWidget(scroll_area)
        scroll_area.setWidget(content_widget)

        # Layout per il widget contenitore
        content_layout = QVBoxLayout(content_widget)

        # Creazione delle label e aggiunta al layout
        for i in range(6):
            label = QLabel(f"Label {i + 1}")
            content_layout.addWidget(label)

        # Aggiunta dell'area di scorrimento al layout principale
        layout.addWidget(scroll_area)

        # Impostazione del layout principale per la finestra
        self.setLayout(layout)

        # Impostazioni della finestra principale
        self.setWindowTitle("Finestra con Scrollbar")
        self.setGeometry(100, 100, 400, 300)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    finestra = Finestra()
    finestra.show()
    sys.exit(app.exec())
