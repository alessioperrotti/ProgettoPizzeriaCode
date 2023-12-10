from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QFrame
from PyQt6.QtGui import QColor

class CustomFrame(QWidget):
    def __init__(self):
        super().__init__()

        # Creazione del frame principale
        main_frame = QFrame(self)
        main_layout = QHBoxLayout(main_frame)

        # Creazione delle tre parti con colori diversi
        left_part = QFrame(main_frame)
        left_part.setStyleSheet("background-color: lightblue;")

        center_part = QFrame(main_frame)
        center_part.setStyleSheet("background-color: white;")

        right_part = QFrame(main_frame)
        right_part.setStyleSheet("background-color: lightcoral;")

        # Aggiunta delle parti al layout principale
        main_layout.addWidget(left_part)
        main_layout.addWidget(center_part)
        main_layout.addWidget(right_part)

        # Impostazione del layout principale per il frame
        main_frame.setLayout(main_layout)

        # Impostazione del layout principale per il widget
        layout = QHBoxLayout(self)
        layout.addWidget(main_frame)
        self.setLayout(layout)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    frame = CustomFrame()
    frame.show()
    sys.exit(app.exec())
