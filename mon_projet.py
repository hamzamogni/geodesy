from interface import *
from main import *
from backend import *

progressBarValue = 0


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
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
        self.ui.fct1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.fonction1))
        self.ui.fct2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.fonction2))
        self.ui.fct3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.fonction3))
        self.ui.fct4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.fonction4))
        self.ui.fct5.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.fonction5))
        self.ui.fct6.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.fonction6))
        self.ui.fct7.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.fonction7))
        self.ui.fct8.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.fonction8))
        self.ui.homeButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Home))
        self.ui.pushButton_leftMenu.clicked.connect(lambda: self.slideLeftMenu())

        self.ui.calculer.clicked.connect(lambda: self.page1(self.ui.a.text(), self.ui.b.text()))

        self.ui.page1_erreur.setVisible(False)

        self.show()

    def page1(self, a, b):
        self.ui.page1_erreur.setVisible(False)
        try:
            a_float = float(a)
            b_float = float(b)
        except ValueError:
            self.page1_clear_outputs()
            self.show_error(self.ui.page1_erreur, "Merci d'entrer des valeurs justes pour a et b")
        else:
            res = get_ellipsoid_parameters(a_float, b_float)

            self.ui.applatissement.setText(str(res["applatissement"]))
            self.ui.premier_e.setText(str(res["excentricite_1"]))
            self.ui.deuxieme_e.setText(str(res["excentricite_2"]))
            self.ui.e_angulaire.setText(str(res["excentricite_ang"]))
            self.ui.c_a_pole.setText(str(res["courbure_pole"]))

    def page1_clear_outputs(self):
        self.ui.applatissement.clear()
        self.ui.premier_e.clear()
        self.ui.deuxieme_e.clear()
        self.ui.e_angulaire.clear()
        self.ui.c_a_pole.clear()

    def show_error(self, label_obj, erreur):
        label_obj.setStyleSheet("color: red")
        label_obj.setText(erreur)
        label_obj.adjustSize()
        label_obj.setVisible(True)

    def slideLeftMenu(self):
        width = self.ui.left_side_menu.width()

        new_width = 190 if width == 50 else 50

        self.animation = QPropertyAnimation(self.ui.left_side_menu, b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(new_width)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()


class AppWindow(QMainWindow):
    def __init__(self):
        super(AppWindow, self).__init__()
        self.ui = Ui_interface1()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon("C:/Users/abdel/OneDrive/Bureau/Projet Geodesie/icon.png"))
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.appProgress)
        self.timer.start(100)

    def appProgress(self):
        global progressBarValue
        self.ui.progressBar.setValue(progressBarValue)
        if progressBarValue > 100:
            self.timer.stop()
            self.ui.loadingprogress.setText("Loading completed succesfully")
            self.main = MainWindow()
            self.main.show()
            self.close()
        elif 20 > progressBarValue > 10:
            self.ui.loadingprogress.setText("Connecting to our App")

        elif 35 > progressBarValue > 20:
            self.ui.loadingprogress.setText("Logging in....")

        elif 50 > progressBarValue > 35:
            self.ui.loadingprogress.setText("Logging in succesfully. Requesting profile .....")

        elif 75 > progressBarValue > 50:
            self.ui.loadingprogress.setText("Profile est to Spinn design....")

        elif 100 > progressBarValue > 75:
            self.ui.loadingprogress.setText("Almost done....")
        progressBarValue += 10


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = AppWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
