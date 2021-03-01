import sys
from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(638, 511)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setGeometry(QtCore.QRect(600, 40, 22, 441))
        self.verticalSlider.setMaximum(600)
        self.verticalSlider.setValue(50)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        # остальное без изменений
        self.setupUi(self)
        self.verticalSlider.valueChanged.connect(self.paint)
        self.do_paint = True
        self.setWindowTitle('Рост хорошего настроения')

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        size = self.verticalSlider.value()
        qp.setPen(QColor(255, 0, 0))
        qp.drawEllipse(0, 0, size, size)
        qp.drawArc(size // 4, size // 3 * 2, size // 2, size // 5, 180 * 16, 180 * 16)
        qp.drawEllipse(size // 4, size // 4, size // 5, size // 5)
        qp.drawEllipse(size // 2, size // 4, size // 5, size // 5)
        self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
