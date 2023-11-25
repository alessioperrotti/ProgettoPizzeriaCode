from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QPen, QColor
from PyQt6.QtCore import Qt, QTimer, QDateTime

class AnalogClock(QWidget):
    def __init__(self):
        super().__init__()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)  # Aggiorna l'orologio ogni 1000 millisecondi (1 secondo)

        self.setWindowTitle('Analog Clock')
        self.setGeometry(100, 100, 400, 400)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        side = min(self.width(), self.height())
        painter.setViewport((self.width() - side) // 2, (self.height() - side) // 2, side, side)
        painter.setWindow(-50, -50, 100, 100)

        self.drawClock(painter)

    def drawClock(self, painter):
        # Disegna la cornice dell'orologio
        pen = QPen()
        pen.setWidth(2)
        painter.setPen(pen)
        painter.drawEllipse(-45, -45, 90, 90)

        # Disegna le lancette dell'orologio
        now = QDateTime.currentDateTime()
        hour = now.time().hour()
        minute = now.time().minute()
        second = now.time().second()

        # Lancetta delle ore
        pen.setWidth(4)
        painter.setPen(pen)
        hour_angle = 30 * (hour % 12 + minute / 60)
        painter.drawLine(0, 0, 20 * Qt.cos(hour_angle), 20 * Qt.sin(hour_angle))

        # Lancetta dei minuti
        pen.setWidth(2)
        painter.setPen(pen)
        minute_angle = 6 * minute
        painter.drawLine(0, 0, 30 * Qt.cos(minute_angle), 30 * Qt.sin(minute_angle))

        # Lancetta dei secondi
        pen.setColor(QColor(255, 0, 0))  # Colore rosso per la lancetta dei secondi
        pen.setWidth(1)
        painter.setPen(pen)
        second_angle = 6 * second
        painter.drawLine(0, 0, 35 * Qt.cos(second_angle), 35 * Qt.sin(second_angle))

if __name__ == '__main__':
    app = QApplication([])
    clock = AnalogClock()
    clock.show()
    app.exec()
