from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QFrame, QScrollArea, QWidget, QLabel


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Creazione del frame con bordo nero
        frame = QFrame(self)
        frame.setFrameStyle(QFrame.Box | QFrame.Plain)  # Imposta uno stile di cornice
        frame.setStyleSheet("QFrame { border: 2px solid black; }")  # Imposta il colore del bordo
        frame_layout = QVBoxLayout(frame)

        # Creazione dell'area di scorrimento
        scroll_area = QScrollArea()
        scroll_content = QWidget(scroll_area)
        scroll_layout = QVBoxLayout(scroll_content)

        # Aggiungi contenuto all'area di scorrimento (puoi aggiungere qualsiasi widget desiderato qui)
        for i in range(20):
            label = QLabel(f"Elemento {i}")
            scroll_layout.addWidget(label)

        # Imposta il layout dell'area di scorrimento
        scroll_content.setLayout(scroll_layout)

        # Imposta il widget interno dell'area di scorrimento
        scroll_area.setWidget(scroll_content)

        # Aggiungi l'area di scorrimento al layout del frame
        frame_layout.addWidget(scroll_area)

        # Imposta il layout del frame
        frame.setLayout(frame_layout)

        # Imposta il widget centrale della finestra principale
        self.setCentralWidget(frame)

        # Imposta le dimensioni della finestra principale
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Frame con Bordo e Scroll Area')


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
