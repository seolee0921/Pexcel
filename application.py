import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from win32api import GetSystemMetrics

GUI_XSIZE = int(GetSystemMetrics(0) / 3 * 2)
GUI_YSIZE = int(GetSystemMetrics(1) / 3 * 2)

class APP(QWidget):

    def __init__(self):
        super().__init__()
        self.INITUI()


    def INITUI(self):
        self.CSS()
        self.CENTER()
        self.IMAGE()

        self.show()

    def IMAGE(self):


    def CENTER(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def CSS(self):
        self.setStyleSheet("background: #37373F")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.resize(GUI_XSIZE, GUI_YSIZE)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_rect(qp)
        qp.end()

    def draw_rect(self, qp):
        qp.setBrush(QColor(28, 28, 31))
        qp.setPen(QPen(QColor(), -1))
        qp.drawRect(0, 40, 75, GUI_YSIZE)

        qp.setPen(QColor(28, 28, 31))
        qp.drawLine(0, 40, GUI_XSIZE, 40)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = APP()
    sys.exit(app.exec_())