import sys
import os
import platform
from _ast import Lambda

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from main_window import *
WINDOW_SIZE = 0;
class AppWindow(QMainWindow):
    def __init__(self):
        super(AppWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("C:/Users/abdel/OneDrive/Bureau/Projet Geodesie/icon.png"))
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(255, 255, 255, 255))
        self.ui.centralwidget.setGraphicsEffect(self.shadow)
        self.ui.stackedWidget.setCurrentWidget(self.ui.Home)
        self.ui.fct1.clicked.connect(lambda : self.ui.stackedWidget.setCurrentWidget(self.ui.fonction1))
        self.ui.fct2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.fonction2))
        self.ui.fct3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.fonction3))
        self.ui.fct4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.fonction4))
        self.ui.fct5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.fonction5))
        self.ui.fct6.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.fonction6))
        self.ui.fct7.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.fonction7))
        self.ui.fct8.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.fonction8))
        self.ui.homeButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Home))
        self.ui.pushButton_leftMenu.clicked.connect(lambda :self.slideLeftMenu())
        self.show()


    def slideLeftMenu(self):
        width = self.ui.left_side_menu.width()
        if width == 50:
            newWidth = 190
        else:
            newWidth = 50

        self.animation = QPropertyAnimation(self.ui.left_side_menu, b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()


def main():
   app = QtWidgets.QApplication(sys.argv)
   application = AppWindow()
   application.show()
   sys.exit(app.exec_())

if __name__ == "__main__":
    main()