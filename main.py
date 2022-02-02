import random
import sys

from UI import Ui_MainWindow as mV
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtWidgets import QApplication, QMainWindow

NUMBER_OF_CIRCLES = 10
WIDTH, HEIGHT = 800, 600
MAX_SIZE = 100


class Example(QMainWindow, mV):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Git и желтые окружности')
        self.do_paint = False
        self.btn.clicked.connect(self.paint)
        self.already_painted = False

    def paintEvent(self, event):
        if self.do_paint:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw_flag(self.qp)
            self.qp.end()
            self.do_paint = False
            self.already_painted = True

    def paint(self):
        if not self.already_painted:
            self.do_paint = True
            self.repaint()

    def draw_flag(self, qp):
        for _ in range(NUMBER_OF_CIRCLES):
            qp.setBrush(QBrush(QColor(
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )))
            size = random.randint(0, MAX_SIZE)
            qp.drawEllipse(random.randint(0, WIDTH), random.randint(0, HEIGHT),
                           size, size)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
