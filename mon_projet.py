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

        self.ui.calculer.clicked.connect(lambda: self.page1(self.ui.a, self.ui.b))

        self.ui.fct2_g2c.clicked.connect(
            lambda: self.page2(0, self.ui.fct2_phi, self.ui.fct2_lambda, self.ui.fct2_h))
        self.ui.fct2_c2g.clicked.connect(
            lambda: self.page2(1, self.ui.fct2_x, self.ui.fct2_y, self.ui.fct2_z))

        self.ui.fct3_altitu_btn.clicked.connect(lambda: self.page3(self.ui.fct3_x))

        self.ui.fct4_cal1.clicked.connect(lambda: self.page4_meridien(self.ui.fct4_phi))
        self.ui.fct4_cal2.clicked.connect(lambda: self.page4_1er_verticale(self.ui.fct4_psi))
        self.ui.fct4_cal3.clicked.connect(
            lambda: self.page4_azimuth(self.ui.fct4_psi1, self.ui.fct4_alpha))

        self.ui.fct5_cal_btn.clicked.connect(
            lambda: self.page5_long_meridienne(self.ui.fct5_phi1, self.ui.fct5_phi2))

        self.ui.fct5_cal_2_btn.clicked.connect(
            lambda: self.page5_long_paralelle(self.ui.fct5_phi21, self.ui.fct5_lambda1,
                                              self.ui.fct5_lambda2))

        self.ui.fct6_calculer_btn.clicked.connect(
            lambda: self.page6(
                self.ui.fct6_alpha1,
                self.ui.fct6_alpha2,
                self.ui.fct6_l1,
                self.ui.fct6_l2)
        )

        self.ERRORS = {
            "FALSE_VALUES": "Merci d'entrer des valeurs valides"
        }

        self.ERROR_LABELS = [
            self.ui.page1_erreur,
            self.ui.page2_erreur,
            self.ui.page3_erreur,
            self.ui.page4_erreur1,
            self.ui.page4_erreur2,
            self.ui.page4_erreur3,
            self.ui.page5_erreur1,
            self.ui.page5_erreur2,
            self.ui.page6_erreur,
        ]

        self.set_errors_visibility(False)

        self.show()

    def page1(self, a, b):
        self.ui.page1_erreur.setVisible(False)
        try:
            a_float = float(a.text())
            b_float = float(b.text())
        except ValueError:
            self.clear_outputs([a, b])
            self.show_error(self.ui.page1_erreur, self.ERRORS["FALSE_VALUES"])
        else:
            res = get_ellipsoid_parameters(a_float, b_float)

            self.ui.applatissement.setText(str(res["applatissement"]))
            self.ui.premier_e.setText(str(res["excentricite_1"]))
            self.ui.deuxieme_e.setText(str(res["excentricite_2"]))
            self.ui.e_angulaire.setText(str(res["excentricite_ang"]))
            self.ui.c_a_pole.setText(str(res["courbure_pole"]))

    def page2(self, cart2geo, a, b, c):
        try:
            a_float = float(a.text())
            b_float = float(b.text())
            c_float = float(c.text())
        except ValueError:
            self.clear_outputs([a, b, c])
            self.show_error(self.ui.page2_erreur, self.ERRORS["FALSE_VALUES"])
        else:
            if cart2geo:
                phi, lamda, h = convert_cart2geo(a_float, b_float, c_float)
                self.ui.fct2_phi.setText(str(phi))
                self.ui.fct2_lambda.setText(str(lamda))
                self.ui.fct2_h.setText(str(h))

            else:
                x, y, z = convert_geo2cart(a_float, b_float, c_float)
                self.ui.fct2_x.setText(str(x))
                self.ui.fct2_y.setText(str(y))
                self.ui.fct2_z.setText(str(z))

    def page3(self, x):
        try:
            x_float = float(x.text())
        except ValueError:
            self.clear_outputs([x])
            self.show_error(self.ui.page3_erreur, self.ERRORS["FALSE_VALUES"])
        else:
            beta, phi, psi = get_3_altitudes(x_float)
            self.ui.fct3_beta.setText(str(beta))
            self.ui.fct3_psi.setText(str(psi))
            self.ui.fct3_phi.setText(str(phi))

    def page4_meridien(self, phi):
        try:
            phi_float = float(phi.text())
        except ValueError:
            self.clear_outputs([phi])
            self.show_error(self.ui.page4_erreur1, self.ERRORS["FALSE_VALUES"])
        else:
            long = get_rayon_courbure(phi_float)
            self.ui.fct4_m.setText(str(long))

    def page4_1er_verticale(self, psi):
        try:
            psi_float = float(psi.text())
        except ValueError:
            self.clear_outputs([psi])
            self.show_error(self.ui.page4_erreur2, self.ERRORS["FALSE_VALUES"])
        else:
            long = get_rayon_1ere_verticale(psi_float)
            self.ui.fct4_n.setText(str(long))

    def page4_azimuth(self, psi, alpha):
        try:
            psi_float = float(psi.text())
            alpha_float = float(alpha.text())
        except ValueError:
            self.clear_outputs([psi, alpha])
            self.show_error(self.ui.page4_erreur3, self.ERRORS["FALSE_VALUES"])
        else:
            courb_azimuth = get_courbure_azimut(alpha_float, psi_float)
            self.ui.fct4_ralpha.setText(str(courb_azimuth))

    def page5_long_meridienne(self, phi1, phi2):
        try:
            phi1_float = float(phi1.text())
            phi2_float = float(phi2.text())
        except ValueError:
            self.clear_outputs([phi1, phi2])
            self.show_error(self.ui.page5_erreur1, self.ERRORS["FALSE_VALUES"])
        else:
            long = get_longeur_meridien(phi1_float, phi2_float)
            self.ui.fct5_s.setText(str(long))

    def page5_long_paralelle(self, phi, lambda1, lambda2):
        try:
            phi_float = float(phi.text())
            lambda1_float = float(lambda1.text())
            lambda2_float = float(lambda2.text())
        except ValueError:
            self.clear_outputs([phi, lambda1, lambda2])
            self.show_error(self.ui.page5_erreur2, self.ERRORS["FALSE_VALUES"])
        else:
            long = get_longueur_parallele(phi_float, lambda1_float, lambda2_float)
            self.ui.fct5_l.setText(str(long))

    def page6(self, phi1, phi2, lambda1, lambda2):
        try:
            phi1_float = float(phi1.text())
            phi2_float = float(phi2.text())
            lambda1_float = float(lambda1.text())
            lambda2_float = float(lambda2.text())
        except ValueError:
            self.clear_outputs([phi1, phi2, lambda1, lambda2])
            self.show_error(self.ui.page6_erreur, self.ERRORS["FALSE_VALUES"])
        else:
            surface = get_surface_partie_terre(lambda1_float, lambda2_float, phi1_float, phi2_float)
            self.ui.fct6_z.setText(str(surface))

    @staticmethod
    def show_error(label_obj, erreur):
        label_obj.setStyleSheet("color: red")
        label_obj.setText(erreur)
        label_obj.adjustSize()
        label_obj.setVisible(True)

    @staticmethod
    def clear_outputs(outputs):
        for text_box in outputs:
            text_box.clear()

    def set_errors_visibility(self, value: bool):
        for label in self.ERROR_LABELS:
            label.setVisible(value)


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
