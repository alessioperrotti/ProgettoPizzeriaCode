from PyQt6.QtGui import QPainter, QPen
from PyQt6.QtCore import QPointF, QTimer, QTime
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem, QGraphicsLineItem
import math

class AnalogClock(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Analog Clock")
        self.setGeometry(100, 100, 400, 400)

        layout = QVBoxLayout(self)

        # Creazione della scena e della vista grafica
        scene = QGraphicsScene(self)
        view = QGraphicsView(scene)

        layout.addWidget(view)

        # Aggiunta del rendering anti-aliasing
        view.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Creazione dell'orologio analogico
        self.center = QPointF(200, 200)
        self.hour_hand = QGraphicsLineItem()
        self.minute_hand = QGraphicsLineItem()
        self.second_hand = QGraphicsLineItem()

        scene.addItem(QGraphicsEllipseItem(self.center.x() - 100, self.center.y() - 100, 200, 200))

        scene.addItem(self.hour_hand)
        scene.addItem(self.minute_hand)
        scene.addItem(self.second_hand)

        # Aggiornamento dell'orologio
        timer = QTimer(self)
        timer.timeout.connect(self.update_clock)
        timer.start(1000)  # Ogni 1000 millisecondi (1 secondo)

    def update_clock(self):
        current_time = QTime.currentTime()

        hours = current_time.hour()
        minutes = current_time.minute()
        seconds = current_time.second()

        # Aggiorna gli angoli delle lancette
        hour_angle = math.radians(30 * (hours % 12) + 0.5 * minutes - 90)
        minute_angle = math.radians(6 * minutes + 0.1 * seconds - 90)
        second_angle = math.radians(6 * seconds - 90)

        # Calcola le coordinate delle estremità delle lancette
        hour_x = 40 * math.cos(hour_angle)
        hour_y = 40 * math.sin(hour_angle)

        minute_x = 60 * math.cos(minute_angle)
        minute_y = 60 * math.sin(minute_angle)

        second_x = 80 * math.cos(second_angle)
        second_y = 80 * math.sin(second_angle)

        # Imposta le coordinate delle lancette
        self.hour_hand.setLine(self.center.x(), self.center.y(), self.center.x() + hour_x, self.center.y() + hour_y)
        self.minute_hand.setLine(self.center.x(), self.center.y(), self.center.x() + minute_x,
                                 self.center.y() + minute_y)
        self.second_hand.setLine(self.center.x(), self.center.y(), self.center.x() + second_x,
                                 self.center.y() + second_y)


if __name__ == "__main__":
    app = QApplication([])
    clock = AnalogClock()
    clock.show()
    app.exec()
