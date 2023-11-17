import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QDialog, QLabel


class SecondWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Second Window")

        layout = QVBoxLayout()
        label = QLabel("This is the second window.")
        layout.addWidget(label)

        self.setLayout(layout)


class FirstWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("First Window")

        layout = QVBoxLayout()

        button_open_second = QPushButton("Open Second Window")
        button_open_second.clicked.connect(self.open_second_window)
        layout.addWidget(button_open_second)

        self.setLayout(layout)

    def open_second_window(self):
        second_window = SecondWindow()
        second_window.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    first_window = FirstWindow()
    first_window.show()

    sys.exit(app.exec())
