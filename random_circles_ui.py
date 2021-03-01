import sys
from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
from random import randint


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(709, 521)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 180, 221, 91))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 709, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Button"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Вызываем метод для загрузки интерфейса из класса Ui_MainWindow,
        # остальное без изменений
        self.setupUi(self)
        self.pushButton.clicked.connect(self.paint)
        self.do_paint = True
        self.circles = 0
        self.setWindowTitle('Git и случайные окружности')

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.circles += 1
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        for i in range(self.circles):
            qp.setPen(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            size = randint(0, 200)
            x1, y1 = randint(0, 709 - size), randint(0, 521 - size)
            qp.drawEllipse(x1, y1, size, size)
            self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
