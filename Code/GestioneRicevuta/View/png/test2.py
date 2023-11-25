import sys

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, \
    QSizePolicy, QHeaderView


class MiVentana(QWidget):
    def __init__(self):
        super().__init__()

        # Crear la tabla
        self.tabla = QTableWidget(self)
        self.tabla.setRowCount(5)
        self.tabla.setColumnCount(3)

        # Rellenar la tabla con datos de ejemplo
        for i in range(5):
            for j in range(3):
                item = QTableWidgetItem(f'Dato {i}, {j}')
                self.tabla.setItem(i, j, item)

        # Crear botones
        self.boton1 = QPushButton('Botón 1', self)
        self.boton2 = QPushButton('Botón 2', self)

        # Configurar la política de tamaño para la tabla
        tablaSizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        tablaSizePolicy.setHorizontalStretch(1)
        self.tabla.setSizePolicy(tablaSizePolicy)
        self.tabla.horizontalHeader().ResizeMode(QHeaderView.Stretch)
        # Configurar la política de tamaño para los botones
        botonSizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        botonSizePolicy.setHorizontalStretch(0)
        self.boton1.setSizePolicy(botonSizePolicy)
        self.boton2.setSizePolicy(botonSizePolicy)

        # Crear diseño vertical
        layout = QVBoxLayout(self)
        layout.addWidget(self.tabla)

        # Crear sublayout para los botones
        sublayout = QVBoxLayout()
        sublayout.addWidget(self.boton1)
        sublayout.addWidget(self.boton2)

        # Agregar el sublayout a la derecha de la tabla
        layout.addLayout(sublayout)

        # Configurar el diseño principal del widget
        self.setLayout(layout)

        # Conectar eventos de los botones a funciones
        self.boton1.clicked.connect(self.on_boton1_click)
        self.boton2.clicked.connect(self.on_boton2_click)

    def on_boton1_click(self):
        print("¡Botón 1 clickeado!")

    def on_boton2_click(self):
        print("¡Botón 2 clickeado!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec())
