import random
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtWidgets import QApplication, QMainWindow

NUMBER_OF_CIRCLES = 10
WIDTH, HEIGHT = 800, 600
MAX_SIZE = 100
COLOR = QColor('yellow')


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
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
        qp.setBrush(QBrush(COLOR))
        for _ in range(NUMBER_OF_CIRCLES):
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
