import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QStackedWidget


class Model:
    def __init__(self):
        self.data = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data


class View1(QWidget):
    def __init__(self, controller):
        super().__init__()

        self.controller = controller

        layout = QVBoxLayout()
        self.label = QLabel("Schermata 1")
        layout.addWidget(self.label)

        button = QPushButton("Vai a Schermata 2")
        button.clicked.connect(self.controller.switch_to_view2)
        layout.addWidget(button)

        self.setLayout(layout)


class Controller1:
    def __init__(self, stacked_widget):
        self.model = Model()
        self.view = View1(self)
        self.stacked_widget = stacked_widget

    def switch_to_view2(self):
        self.stacked_widget.setCurrentIndex(1)


class View2(QWidget):
    def __init__(self, controller):
        super().__init__()

        self.controller = controller

        layout = QVBoxLayout()
        self.label = QLabel("Schermata 2")
        layout.addWidget(self.label)

        button = QPushButton("Vai a Schermata 1")
        button.clicked.connect(self.controller.switch_to_view1)
        layout.addWidget(button)

        self.setLayout(layout)


class Controller2:
    def __init__(self, stacked_widget):
        self.model = Model()
        self.view = View2(self)
        self.stacked_widget = stacked_widget

    def switch_to_view1(self):
        self.stacked_widget.setCurrentIndex(0)


class MainApp(QApplication):
    def __init__(self, sys_argv):
        super(MainApp, self).__init__(sys_argv)

        self.stacked_widget = QStackedWidget()

        self.controller1 = Controller1(self.stacked_widget)
        self.controller2 = Controller2(self.stacked_widget)

        self.stacked_widget.addWidget(self.controller1.view)
        self.stacked_widget.addWidget(self.controller2.view)

        self.stacked_widget.show()


if __name__ == '__main__':
    app = MainApp(sys.argv)
    sys.exit(app.exec())
