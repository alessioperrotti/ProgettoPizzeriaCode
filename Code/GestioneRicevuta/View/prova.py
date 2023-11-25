import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Finestra Principale')

        self.button = QPushButton('Apri Seconda Finestra', self)
        self.button.clicked.connect(self.show_second_window)

        self.show()

    def show_second_window(self):
        self.second_window = SecondWindow(self)
        self.second_window.show()

        # Disabilita la finestra principale
        self.setDisabled(True)

    def enable_main_window(self):
        # Abilita nuovamente la finestra principale quando la seconda finestra è chiusa
        self.setDisabled(False)


class SecondWindow(QWidget):
    def __init__(self, main_window):
        super(SecondWindow, self).__init__()

        self.main_window = main_window

        self.init_ui()

    def init_ui(self):
        self.setGeometry(200, 200, 300, 200)
        self.setWindowTitle('Seconda Finestra')

        label = QLabel('Questa è la seconda finestra', self)

        button_back = QPushButton('Torna alla Finestra Principale', self)
        button_back.clicked.connect(self.show_main_window)

        self.show()

    def show_main_window(self):
        self.main_window.enable_main_window()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())
