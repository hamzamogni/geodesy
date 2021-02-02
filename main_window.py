# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\GeoInfo2\tout\Projet Geodesie\main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(793, 600)
        MainWindow.setMinimumSize(QtCore.QSize(793, 600))
        MainWindow.setMaximumSize(QtCore.QSize(793, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_header = QtWidgets.QFrame(self.centralwidget)
        self.main_header.setMinimumSize(QtCore.QSize(793, 30))
        self.main_header.setMaximumSize(QtCore.QSize(793, 30))
        self.main_header.setStyleSheet("QFrame{\n"
"   border-bottom: 1px solid #000;\n"
"   \n"
"    background-color: rgb(131, 131, 131);\n"
"}\n"
"")
        self.main_header.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_header.setObjectName("main_header")
        self.framebutton = QtWidgets.QFrame(self.main_header)
        self.framebutton.setGeometry(QtCore.QRect(0, 0, 51, 30))
        self.framebutton.setMinimumSize(QtCore.QSize(50, 30))
        self.framebutton.setMaximumSize(QtCore.QSize(190, 30))
        self.framebutton.setStyleSheet("QFrame{\n"
"   background-color: #9aa298;\n"
"}\n"
"QPushButton{\n"
"   padding: 5px 10px;\n"
"   border: none;\n"
"   border-radius: 5px;\n"
"   background-color: #9aa298;\n"
"   color: #fff;\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: #101010;\n"
"}")
        self.framebutton.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.framebutton.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framebutton.setObjectName("framebutton")
        self.pushButton_leftMenu = QtWidgets.QPushButton(self.framebutton)
        self.pushButton_leftMenu.setGeometry(QtCore.QRect(0, 0, 50, 30))
        self.pushButton_leftMenu.setMinimumSize(QtCore.QSize(50, 30))
        self.pushButton_leftMenu.setMaximumSize(QtCore.QSize(190, 30))
        self.pushButton_leftMenu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_leftMenu.setStyleSheet("image: url(:/buttons/cil-menu.png);\n"
"")
        self.pushButton_leftMenu.setText("")
        self.pushButton_leftMenu.setObjectName("pushButton_leftMenu")
        self.verticalLayout.addWidget(self.main_header)
        self.main_body = QtWidgets.QFrame(self.centralwidget)
        self.main_body.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.main_body.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body.setObjectName("main_body")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.main_body)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_side_menu = QtWidgets.QFrame(self.main_body)
        self.left_side_menu.setMinimumSize(QtCore.QSize(50, 0))
        self.left_side_menu.setMaximumSize(QtCore.QSize(50, 16777215))
        self.left_side_menu.setStyleSheet("QFrame{\n"
"   background-color: #9aa298;\n"
"   z-index:0;\n"
"}\n"
"QPushButton{\n"
"   padding: 5px 10px;\n"
"   border: none;\n"
"   border-radius: 5px;\n"
"   background-color: #9aa298;\n"
"   color: #fff;\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: #101010;\n"
"}\n"
"")
        self.left_side_menu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.left_side_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_side_menu.setObjectName("left_side_menu")
        self.fct1 = QtWidgets.QPushButton(self.left_side_menu)
        self.fct1.setGeometry(QtCore.QRect(60, 40, 111, 31))
        self.fct1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fct1.setStyleSheet("")
        self.fct1.setObjectName("fct1")
        self.fct2 = QtWidgets.QPushButton(self.left_side_menu)
        self.fct2.setGeometry(QtCore.QRect(60, 100, 111, 31))
        self.fct2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fct2.setObjectName("fct2")
        self.fct3 = QtWidgets.QPushButton(self.left_side_menu)
        self.fct3.setGeometry(QtCore.QRect(60, 160, 111, 31))
        self.fct3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fct3.setObjectName("fct3")
        self.fct4 = QtWidgets.QPushButton(self.left_side_menu)
        self.fct4.setGeometry(QtCore.QRect(60, 222, 111, 31))
        self.fct4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fct4.setObjectName("fct4")
        self.fct5 = QtWidgets.QPushButton(self.left_side_menu)
        self.fct5.setGeometry(QtCore.QRect(60, 280, 111, 31))
        self.fct5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fct5.setObjectName("fct5")
        self.fct6 = QtWidgets.QPushButton(self.left_side_menu)
        self.fct6.setGeometry(QtCore.QRect(60, 340, 111, 31))
        self.fct6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fct6.setObjectName("fct6")
        self.fct7 = QtWidgets.QPushButton(self.left_side_menu)
        self.fct7.setGeometry(QtCore.QRect(60, 400, 111, 31))
        self.fct7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fct7.setObjectName("fct7")
        self.fct8 = QtWidgets.QPushButton(self.left_side_menu)
        self.fct8.setGeometry(QtCore.QRect(60, 460, 111, 31))
        self.fct8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fct8.setObjectName("fct8")
        self.img2 = QtWidgets.QFrame(self.left_side_menu)
        self.img2.setGeometry(QtCore.QRect(10, 100, 31, 31))
        self.img2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.img2.setStyleSheet("image: url(:/buttons/12.png);")
        self.img2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.img2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.img2.setObjectName("img2")
        self.img3 = QtWidgets.QFrame(self.left_side_menu)
        self.img3.setGeometry(QtCore.QRect(10, 40, 31, 31))
        self.img3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.img3.setStyleSheet("image: url(:/buttons/12.png);")
        self.img3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.img3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.img3.setObjectName("img3")
        self.img4 = QtWidgets.QFrame(self.left_side_menu)
        self.img4.setGeometry(QtCore.QRect(10, 160, 31, 31))
        self.img4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.img4.setStyleSheet("image: url(:/buttons/12.png);")
        self.img4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.img4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.img4.setObjectName("img4")
        self.img8 = QtWidgets.QFrame(self.left_side_menu)
        self.img8.setGeometry(QtCore.QRect(10, 220, 31, 31))
        self.img8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.img8.setStyleSheet("image: url(:/buttons/12.png);")
        self.img8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.img8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.img8.setObjectName("img8")
        self.img5 = QtWidgets.QFrame(self.left_side_menu)
        self.img5.setGeometry(QtCore.QRect(10, 280, 31, 31))
        self.img5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.img5.setStyleSheet("image: url(:/buttons/12.png);")
        self.img5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.img5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.img5.setObjectName("img5")
        self.img6 = QtWidgets.QFrame(self.left_side_menu)
        self.img6.setGeometry(QtCore.QRect(10, 340, 31, 31))
        self.img6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.img6.setStyleSheet("image: url(:/buttons/12.png);")
        self.img6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.img6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.img6.setObjectName("img6")
        self.img7 = QtWidgets.QFrame(self.left_side_menu)
        self.img7.setGeometry(QtCore.QRect(10, 400, 31, 31))
        self.img7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.img7.setStyleSheet("image: url(:/buttons/12.png);")
        self.img7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.img7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.img7.setObjectName("img7")
        self.img1 = QtWidgets.QFrame(self.left_side_menu)
        self.img1.setGeometry(QtCore.QRect(10, 460, 31, 31))
        self.img1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.img1.setStyleSheet("image: url(:/buttons/12.png);")
        self.img1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.img1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.img1.setObjectName("img1")
        self.horizontalLayout.addWidget(self.left_side_menu)
        self.center_main_items = QtWidgets.QFrame(self.main_body)
        self.center_main_items.setMinimumSize(QtCore.QSize(500, 518))
        self.center_main_items.setMaximumSize(QtCore.QSize(700, 16777215))
        self.center_main_items.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.center_main_items.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.center_main_items.setFrameShadow(QtWidgets.QFrame.Raised)
        self.center_main_items.setObjectName("center_main_items")
        self.stackedWidget = QtWidgets.QStackedWidget(self.center_main_items)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 691, 521))
        self.stackedWidget.setStyleSheet("QLineEdit{\n"
" border-radius: 5px;\n"
" border: 1px solid #00aa7f;\n"
"}\n"
"")
        self.stackedWidget.setObjectName("stackedWidget")
        self.fonction1 = QtWidgets.QWidget()
        self.fonction1.setStyleSheet("")
        self.fonction1.setObjectName("fonction1")
        self.titlef1 = QtWidgets.QLabel(self.fonction1)
        self.titlef1.setGeometry(QtCore.QRect(30, 10, 531, 81))
        self.titlef1.setObjectName("titlef1")
        self.label_3 = QtWidgets.QLabel(self.fonction1)
        self.label_3.setGeometry(QtCore.QRect(40, 140, 41, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.fonction1)
        self.label_4.setGeometry(QtCore.QRect(40, 200, 41, 31))
        self.label_4.setObjectName("label_4")
        self.calculer = QtWidgets.QPushButton(self.fonction1)
        self.calculer.setGeometry(QtCore.QRect(100, 270, 81, 41))
        self.calculer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calculer.setStyleSheet("QPushButton{\n"
"   padding: 5px 10px;\n"
"   border: none;\n"
"   border-radius: 5px;\n"
"   background-color: #9aa298;\n"
"   color: #fff;\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: #101010;\n"
"}")
        self.calculer.setObjectName("calculer")
        self.a = QtWidgets.QLineEdit(self.fonction1)
        self.a.setGeometry(QtCore.QRect(100, 140, 121, 31))
        self.a.setStyleSheet("")
        self.a.setObjectName("a")
        self.b = QtWidgets.QLineEdit(self.fonction1)
        self.b.setGeometry(QtCore.QRect(100, 200, 121, 31))
        self.b.setObjectName("b")
        self.applatissement = QtWidgets.QLineEdit(self.fonction1)
        self.applatissement.setEnabled(False)
        self.applatissement.setGeometry(QtCore.QRect(480, 150, 151, 31))
        self.applatissement.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.applatissement.setObjectName("applatissement")
        self.premier_e = QtWidgets.QLineEdit(self.fonction1)
        self.premier_e.setEnabled(False)
        self.premier_e.setGeometry(QtCore.QRect(480, 200, 151, 31))
        self.premier_e.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.premier_e.setObjectName("premier_e")
        self.deuxieme_e = QtWidgets.QLineEdit(self.fonction1)
        self.deuxieme_e.setEnabled(False)
        self.deuxieme_e.setGeometry(QtCore.QRect(480, 250, 151, 31))
        self.deuxieme_e.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.deuxieme_e.setObjectName("deuxieme_e")
        self.e_angulaire = QtWidgets.QLineEdit(self.fonction1)
        self.e_angulaire.setEnabled(False)
        self.e_angulaire.setGeometry(QtCore.QRect(480, 300, 151, 31))
        self.e_angulaire.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.e_angulaire.setObjectName("e_angulaire")
        self.c_a_pole = QtWidgets.QLineEdit(self.fonction1)
        self.c_a_pole.setEnabled(False)
        self.c_a_pole.setGeometry(QtCore.QRect(480, 350, 151, 31))
        self.c_a_pole.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.c_a_pole.setObjectName("c_a_pole")
        self.line = QtWidgets.QFrame(self.fonction1)
        self.line.setGeometry(QtCore.QRect(250, 110, 20, 361))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_5 = QtWidgets.QLabel(self.fonction1)
        self.label_5.setGeometry(QtCore.QRect(300, 150, 131, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.fonction1)
        self.label_6.setGeometry(QtCore.QRect(290, 200, 151, 21))
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.fonction1)
        self.label_7.setGeometry(QtCore.QRect(280, 250, 171, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.fonction1)
        self.label_8.setGeometry(QtCore.QRect(270, 300, 191, 31))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.fonction1)
        self.label_9.setGeometry(QtCore.QRect(290, 350, 161, 31))
        self.label_9.setObjectName("label_9")
        self.stackedWidget.addWidget(self.fonction1)
        self.fonction2 = QtWidgets.QWidget()
        self.fonction2.setStyleSheet("")
        self.fonction2.setObjectName("fonction2")
        self.titlef2 = QtWidgets.QLabel(self.fonction2)
        self.titlef2.setGeometry(QtCore.QRect(20, 10, 371, 81))
        self.titlef2.setObjectName("titlef2")
        self.frame = QtWidgets.QFrame(self.fonction2)
        self.frame.setGeometry(QtCore.QRect(40, 140, 61, 161))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 0, 41, 41))
        self.frame_2.setStyleSheet("image: url(:/buttons/phi.png);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(10, 60, 41, 41))
        self.frame_3.setStyleSheet("image: url(:/buttons/lambda.png);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(10, 120, 41, 41))
        self.frame_4.setStyleSheet("image: url(:/buttons/h.png);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.lineEdit = QtWidgets.QLineEdit(self.fonction2)
        self.lineEdit.setGeometry(QtCore.QRect(130, 140, 121, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.fonction2)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 260, 121, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.fonction2)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 200, 121, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.line_2 = QtWidgets.QFrame(self.fonction2)
        self.line_2.setGeometry(QtCore.QRect(320, 130, 20, 311))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.calculer_3 = QtWidgets.QPushButton(self.fonction2)
        self.calculer_3.setGeometry(QtCore.QRect(150, 340, 81, 41))
        self.calculer_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calculer_3.setStyleSheet("QPushButton{\n"
"   padding: 5px 10px;\n"
"   border: none;\n"
"   border-radius: 5px;\n"
"   background-color: #9aa298;\n"
"   color: #fff;\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: #101010;\n"
"}")
        self.calculer_3.setObjectName("calculer_3")
        self.frame_9 = QtWidgets.QFrame(self.fonction2)
        self.frame_9.setGeometry(QtCore.QRect(360, 130, 51, 171))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.frame_10 = QtWidgets.QFrame(self.frame_9)
        self.frame_10.setGeometry(QtCore.QRect(10, 10, 31, 31))
        self.frame_10.setStyleSheet("image: url(:/buttons/1X.png);")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.frame_11 = QtWidgets.QFrame(self.frame_9)
        self.frame_11.setGeometry(QtCore.QRect(0, 60, 41, 41))
        self.frame_11.setStyleSheet("image: url(:/buttons/1Y.png);")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.frame_12 = QtWidgets.QFrame(self.frame_9)
        self.frame_12.setGeometry(QtCore.QRect(10, 120, 31, 41))
        self.frame_12.setStyleSheet("image: url(:/buttons/1Z.png);")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.fonction2)
        self.lineEdit_7.setGeometry(QtCore.QRect(440, 260, 121, 31))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.fonction2)
        self.lineEdit_8.setGeometry(QtCore.QRect(440, 200, 121, 31))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.fonction2)
        self.lineEdit_9.setGeometry(QtCore.QRect(440, 140, 121, 31))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.calculer_4 = QtWidgets.QPushButton(self.fonction2)
        self.calculer_4.setGeometry(QtCore.QRect(460, 340, 81, 41))
        self.calculer_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calculer_4.setStyleSheet("QPushButton{\n"
"   padding: 5px 10px;\n"
"   border: none;\n"
"   border-radius: 5px;\n"
"   background-color: #9aa298;\n"
"   color: #fff;\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: #101010;\n"
"}")
        self.calculer_4.setObjectName("calculer_4")
        self.stackedWidget.addWidget(self.fonction2)
        self.fonction3 = QtWidgets.QWidget()
        self.fonction3.setStyleSheet("")
        self.fonction3.setObjectName("fonction3")
        self.titlef3 = QtWidgets.QLabel(self.fonction3)
        self.titlef3.setGeometry(QtCore.QRect(20, 10, 331, 81))
        self.titlef3.setObjectName("titlef3")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.fonction3)
        self.lineEdit_10.setGeometry(QtCore.QRect(120, 190, 121, 31))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.frame_13 = QtWidgets.QFrame(self.fonction3)
        self.frame_13.setGeometry(QtCore.QRect(60, 190, 31, 31))
        self.frame_13.setStyleSheet("image: url(:/buttons/1X.png);")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.calculer_5 = QtWidgets.QPushButton(self.fonction3)
        self.calculer_5.setGeometry(QtCore.QRect(140, 270, 81, 41))
        self.calculer_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calculer_5.setStyleSheet("QPushButton{\n"
"   padding: 5px 10px;\n"
"   border: none;\n"
"   border-radius: 5px;\n"
"   background-color: #9aa298;\n"
"   color: #fff;\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: #101010;\n"
"}")
        self.calculer_5.setObjectName("calculer_5")
        self.line_5 = QtWidgets.QFrame(self.fonction3)
        self.line_5.setGeometry(QtCore.QRect(273, 140, 20, 261))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.frame_14 = QtWidgets.QFrame(self.fonction3)
        self.frame_14.setGeometry(QtCore.QRect(310, 140, 41, 181))
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.frame_15 = QtWidgets.QFrame(self.frame_14)
        self.frame_15.setGeometry(QtCore.QRect(0, 140, 41, 31))
        self.frame_15.setStyleSheet("image: url(:/buttons/beta.png);")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.frame_16 = QtWidgets.QFrame(self.frame_14)
        self.frame_16.setGeometry(QtCore.QRect(0, 70, 41, 41))
        self.frame_16.setStyleSheet("image: url(:/buttons/psi.png);")
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.frame_17 = QtWidgets.QFrame(self.frame_14)
        self.frame_17.setGeometry(QtCore.QRect(0, 10, 41, 41))
        self.frame_17.setStyleSheet("image: url(:/buttons/delta.png);")
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.fonction3)
        self.lineEdit_11.setGeometry(QtCore.QRect(380, 160, 121, 31))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.fonction3)
        self.lineEdit_12.setGeometry(QtCore.QRect(380, 220, 121, 31))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.fonction3)
        self.lineEdit_13.setGeometry(QtCore.QRect(380, 280, 121, 31))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.stackedWidget.addWidget(self.fonction3)
        self.fonction4 = QtWidgets.QWidget()
        self.fonction4.setStyleSheet("")
        self.fonction4.setObjectName("fonction4")
        self.titlef4 = QtWidgets.QLabel(self.fonction4)
        self.titlef4.setGeometry(QtCore.QRect(10, 10, 331, 81))
        self.titlef4.setObjectName("titlef4")
        self.tabWidget = QtWidgets.QTabWidget(self.fonction4)
        self.tabWidget.setGeometry(QtCore.QRect(40, 100, 611, 381))
        self.tabWidget.setObjectName("tabWidget")
        self.ray_m = QtWidgets.QWidget()
        self.ray_m.setObjectName("ray_m")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.ray_m)
        self.lineEdit_14.setGeometry(QtCore.QRect(100, 80, 121, 31))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.calculer_6 = QtWidgets.QPushButton(self.ray_m)
        self.calculer_6.setGeometry(QtCore.QRect(110, 170, 81, 41))
        self.calculer_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calculer_6.setStyleSheet("QPushButton{\n"
"   padding: 5px 10px;\n"
"   border: none;\n"
"   border-radius: 5px;\n"
"   background-color: #9aa298;\n"
"   color: #fff;\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: #101010;\n"
"}")
        self.calculer_6.setObjectName("calculer_6")
        self.frame_18 = QtWidgets.QFrame(self.ray_m)
        self.frame_18.setGeometry(QtCore.QRect(30, 70, 41, 41))
        self.frame_18.setStyleSheet("image: url(:/buttons/phi.png);")
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.line_6 = QtWidgets.QFrame(self.ray_m)
        self.line_6.setGeometry(QtCore.QRect(270, 40, 20, 261))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.frame_19 = QtWidgets.QFrame(self.ray_m)
        self.frame_19.setGeometry(QtCore.QRect(320, 100, 41, 41))
        self.frame_19.setStyleSheet("image: url(:/buttons/phi.png);")
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.lineEdit_26 = QtWidgets.QLineEdit(self.ray_m)
        self.lineEdit_26.setGeometry(QtCore.QRect(410, 110, 121, 31))
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.tabWidget.addTab(self.ray_m, "")
        self.ray_v = QtWidgets.QWidget()
        self.ray_v.setObjectName("ray_v")
        self.calculer_7 = QtWidgets.QPushButton(self.ray_v)
        self.calculer_7.setGeometry(QtCore.QRect(120, 170, 81, 41))
        self.calculer_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calculer_7.setStyleSheet("QPushButton{\n"
"   padding: 5px 10px;\n"
"   border: none;\n"
"   border-radius: 5px;\n"
"   background-color: #9aa298;\n"
"   color: #fff;\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: #101010;\n"
"}")
        self.calculer_7.setObjectName("calculer_7")
        self.line_7 = QtWidgets.QFrame(self.ray_v)
        self.line_7.setGeometry(QtCore.QRect(270, 40, 20, 261))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.ray_v)
        self.lineEdit_15.setGeometry(QtCore.QRect(100, 80, 121, 31))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.frame_26 = QtWidgets.QFrame(self.ray_v)
        self.frame_26.setGeometry(QtCore.QRect(40, 70, 41, 41))
        self.frame_26.setStyleSheet("image: url(:/buttons/phi.png);")
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.frame_29 = QtWidgets.QFrame(self.ray_v)
        self.frame_29.setGeometry(QtCore.QRect(300, 110, 41, 41))
        self.frame_29.setStyleSheet("image: url(:/buttons/phi.png);")
        self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.ray_v)
        self.lineEdit_24.setGeometry(QtCore.QRect(370, 120, 121, 31))
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.tabWidget.addTab(self.ray_v, "")
        self.ray_alpha = QtWidgets.QWidget()
        self.ray_alpha.setObjectName("ray_alpha")
        self.calculer_8 = QtWidgets.QPushButton(self.ray_alpha)
        self.calculer_8.setGeometry(QtCore.QRect(130, 160, 81, 41))
        self.calculer_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calculer_8.setStyleSheet("QPushButton{\n"
"   padding: 5px 10px;\n"
"   border: none;\n"
"   border-radius: 5px;\n"
"   background-color: #9aa298;\n"
"   color: #fff;\n"
"}\n"
"QPushButton:hover{\n"
"   background-color: #101010;\n"
"}")
        self.calculer_8.setObjectName("calculer_8")
        self.line_8 = QtWidgets.QFrame(self.ray_alpha)
        self.line_8.setGeometry(QtCore.QRect(280, 40, 20, 261))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.ray_alpha)
        self.lineEdit_16.setGeometry(QtCore.QRect(120, 70, 121, 31))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.frame_30 = QtWidgets.QFrame(self.ray_alpha)
        self.frame_30.setGeometry(QtCore.QRect(50, 60, 41, 41))
        self.frame_30.setStyleSheet("image: url(:/buttons/phi.png);")
        self.frame_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_30.setObjectName("frame_30")
        self.frame_33 = QtWidgets.QFrame(self.ray_alpha)
        self.frame_33.setGeometry(QtCore.QRect(330, 100, 41, 41))
        self.frame_33.setStyleSheet("image: url(:/buttons/phi.png);")
        self.frame_33.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_33.setObjectName("frame_33")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.ray_alpha)
        self.lineEdit_22.setGeometry(QtCore.QRect(400, 110, 121, 31))
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.tabWidget.addTab(self.ray_alpha, "")
        self.stackedWidget.addWidget(self.fonction4)
        self.fonction5 = QtWidgets.QWidget()
        self.fonction5.setStyleSheet("")
        self.fonction5.setObjectName("fonction5")
        self.titlef5 = QtWidgets.QLabel(self.fonction5)
        self.titlef5.setGeometry(QtCore.QRect(160, 10, 331, 81))
        self.titlef5.setObjectName("titlef5")
        self.stackedWidget.addWidget(self.fonction5)
        self.fonction6 = QtWidgets.QWidget()
        self.fonction6.setStyleSheet("")
        self.fonction6.setObjectName("fonction6")
        self.titlef6 = QtWidgets.QLabel(self.fonction6)
        self.titlef6.setGeometry(QtCore.QRect(170, 10, 331, 81))
        self.titlef6.setObjectName("titlef6")
        self.stackedWidget.addWidget(self.fonction6)
        self.fonction7 = QtWidgets.QWidget()
        self.fonction7.setStyleSheet("")
        self.fonction7.setObjectName("fonction7")
        self.titlef7 = QtWidgets.QLabel(self.fonction7)
        self.titlef7.setGeometry(QtCore.QRect(170, 10, 331, 81))
        self.titlef7.setObjectName("titlef7")
        self.stackedWidget.addWidget(self.fonction7)
        self.fonction8 = QtWidgets.QWidget()
        self.fonction8.setStyleSheet("")
        self.fonction8.setObjectName("fonction8")
        self.titlef8 = QtWidgets.QLabel(self.fonction8)
        self.titlef8.setGeometry(QtCore.QRect(180, 10, 331, 81))
        self.titlef8.setObjectName("titlef8")
        self.stackedWidget.addWidget(self.fonction8)
        self.Home = QtWidgets.QWidget()
        self.Home.setStyleSheet("")
        self.Home.setObjectName("Home")
        self.label = QtWidgets.QLabel(self.Home)
        self.label.setGeometry(QtCore.QRect(70, 10, 551, 91))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.imageff = QtWidgets.QFrame(self.Home)
        self.imageff.setGeometry(QtCore.QRect(100, 130, 431, 291))
        self.imageff.setStyleSheet("image: url(:/buttons/2.png);")
        self.imageff.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.imageff.setFrameShadow(QtWidgets.QFrame.Raised)
        self.imageff.setObjectName("imageff")
        self.stackedWidget.addWidget(self.Home)
        self.horizontalLayout.addWidget(self.center_main_items)
        self.right_side_menu = QtWidgets.QFrame(self.main_body)
        self.right_side_menu.setMaximumSize(QtCore.QSize(45, 16777215))
        self.right_side_menu.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.right_side_menu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.right_side_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right_side_menu.setObjectName("right_side_menu")
        self.homeButton = QtWidgets.QPushButton(self.right_side_menu)
        self.homeButton.setGeometry(QtCore.QRect(0, 0, 45, 41))
        self.homeButton.setMinimumSize(QtCore.QSize(45, 0))
        self.homeButton.setMaximumSize(QtCore.QSize(45, 16777215))
        self.homeButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.homeButton.setStyleSheet("image: url(:/buttons/cil-home.png);\n"
"background-color: rgb(0, 0, 0);")
        self.homeButton.setText("")
        self.homeButton.setObjectName("homeButton")
        self.horizontalLayout.addWidget(self.right_side_menu)
        self.verticalLayout.addWidget(self.main_body)
        self.main_footer = QtWidgets.QFrame(self.centralwidget)
        self.main_footer.setMaximumSize(QtCore.QSize(16777215, 50))
        self.main_footer.setStyleSheet("QFrame{\n"
"   border-bottom: 1px solid #000;\n"
"   \n"
"    background-color: rgb(131, 131, 131);\n"
"}\n"
"")
        self.main_footer.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main_footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_footer.setObjectName("main_footer")
        self.label_2 = QtWidgets.QLabel(self.main_footer)
        self.label_2.setGeometry(QtCore.QRect(250, 10, 291, 21))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.main_footer)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(3)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "projet Géodésie"))
        self.fct1.setText(_translate("MainWindow", "Fonction 1"))
        self.fct2.setText(_translate("MainWindow", "Fonction 2"))
        self.fct3.setText(_translate("MainWindow", "Fonction 3"))
        self.fct4.setText(_translate("MainWindow", "Fonction 4"))
        self.fct5.setText(_translate("MainWindow", "Fonction 5"))
        self.fct6.setText(_translate("MainWindow", "Fonction 6"))
        self.fct7.setText(_translate("MainWindow", "Fonction 7"))
        self.fct8.setText(_translate("MainWindow", "Fonction 8"))
        self.titlef1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:26pt; color:#00aa7f;\">Les paramètres d\'une ellipsoïde :</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#000000;\">a</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#000000;\">b</span></p></body></html>"))
        self.calculer.setText(_translate("MainWindow", "Calculer"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#000000;\">applatissement</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#000000;\">1er excentricite</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#000000;\">2eme excentricite</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#000000;\">excentricite angulaire</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#000000;\">courbure au pole</span></p></body></html>"))
        self.titlef2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:48pt; color:#00aa7f;\">Fonction 2:</span></p></body></html>"))
        self.calculer_3.setText(_translate("MainWindow", "Convertir"))
        self.calculer_4.setText(_translate("MainWindow", "Convertir"))
        self.titlef3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:48pt; color:#00aa7f;\">Fonction 3:</span></p></body></html>"))
        self.calculer_5.setText(_translate("MainWindow", "Calculer"))
        self.titlef4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:48pt; color:#00aa7f;\">Fonction 4:</span></p></body></html>"))
        self.calculer_6.setText(_translate("MainWindow", "Calculer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ray_m), _translate("MainWindow", "Rayon du courbure méridiane"))
        self.calculer_7.setText(_translate("MainWindow", "Calculer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ray_v), _translate("MainWindow", "Rayon du courbure 1er vertical"))
        self.calculer_8.setText(_translate("MainWindow", "Calculer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ray_alpha), _translate("MainWindow", "Rayon du courbure selon l\'azimut ALPHA"))
        self.titlef5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:48pt; color:#00aa7f;\">Fonction 5:</span></p></body></html>"))
        self.titlef6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:48pt; color:#00aa7f;\">Fonction 6:</span></p></body></html>"))
        self.titlef7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:48pt; color:#00aa7f;\">Fonction 7:</span></p></body></html>"))
        self.titlef8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:48pt; color:#00aa7f;\">Fonction 8:</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#aa557f;\">Bienvenue dans notre Application</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Designed By : MEJDOUB Abdelkader &amp; MOGNI Hamza</span></p></body></html>"))
import button
