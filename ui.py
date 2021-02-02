# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(900, 850)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #222")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-10, -10, 921, 121))
        self.frame.setStyleSheet("background-color: #fb5b5d;\n"
"border: 5px solid white;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(250, 20, 391, 81))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;\n"
"border-radius: 30px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.address_input = QtWidgets.QLineEdit(self.centralwidget)
        self.address_input.setGeometry(QtCore.QRect(20, 150, 751, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.address_input.setFont(font)
        self.address_input.setStyleSheet("background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius: 30;\n"
"color: white;")
        self.address_input.setText("")
        self.address_input.setAlignment(QtCore.Qt.AlignCenter)
        self.address_input.setObjectName("address_input")
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(780, 150, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.button.setFont(font)
        self.button.setMouseTracking(False)
        self.button.setStyleSheet("QPushButton {\n"
"background-color: #fb5b5d;\n"
"border-radius: 30;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #fa4244\n"
"}")
        self.button.setObjectName("button")
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(30, 360, 652, 452))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.image.setFont(font)
        self.image.setStyleSheet("border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 15px;\n"
"border-color: #fb5b5d;\n"
"padding: 4px;\n"
"color: white;")
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap("../../../Users/SpankeeZ/Downloads/5400c018145716f40ba0eca0e70e3951.jpg"))
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        self.image.setObjectName("image")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(250, 240, 171, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.plus = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.plus.setFont(font)
        self.plus.setStyleSheet("QPushButton {\n"
"border-radius: 11;\n"
"color: white;\n"
"background-color: #22222e;\n"
"border: 1px solid #f66867;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #fa4244\n"
"}")
        self.plus.setObjectName("plus")
        self.horizontalLayout.addWidget(self.plus)
        self.minus = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.minus.setFont(font)
        self.minus.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.minus.setStyleSheet("QPushButton {\n"
"border-radius: 11;\n"
"color: white;\n"
"background-color: #22222e;\n"
"border: 1px solid #f66867;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #fa4244\n"
"}")
        self.minus.setObjectName("minus")
        self.horizontalLayout.addWidget(self.minus)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(430, 260, 151, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: white")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.type = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.type.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.type.setFont(font)
        self.type.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.type.setStyleSheet("QComboBox {\n"
"background-color: #22222e;\n"
"color: white;\n"
"padding: .75rem 2.5rem .75rem 1rem;\n"
"border-radius: 3px;\n"
"}")
        self.type.setIconSize(QtCore.QSize(19, 19))
        self.type.setObjectName("type")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.horizontalLayout_2.addWidget(self.type)
        self.traffic_check = QtWidgets.QCheckBox(self.centralwidget)
        self.traffic_check.setGeometry(QtCore.QRect(380, 310, 121, 22))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.traffic_check.setFont(font)
        self.traffic_check.setStyleSheet("color: white;")
        self.traffic_check.setObjectName("traffic_check")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(710, 450, 160, 80))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("img/temp.png"))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.temp_label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.temp_label.setFont(font)
        self.temp_label.setStyleSheet("color: white;\n"
"background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius:20px;")
        self.temp_label.setAlignment(QtCore.Qt.AlignCenter)
        self.temp_label.setObjectName("temp_label")
        self.horizontalLayout_3.addWidget(self.temp_label)
        self.conditionlabel = QtWidgets.QLabel(self.centralwidget)
        self.conditionlabel.setGeometry(QtCore.QRect(760, 560, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.conditionlabel.setFont(font)
        self.conditionlabel.setStyleSheet("color: white;\n"
"background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius:20px;")
        self.conditionlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.conditionlabel.setObjectName("conditionlabel")
        self.condition_icon = QtWidgets.QLabel(self.centralwidget)
        self.condition_icon.setGeometry(QtCore.QRect(710, 560, 51, 51))
        self.condition_icon.setText("")
        self.condition_icon.setPixmap(QtGui.QPixmap("img/ovc.svg"))
        self.condition_icon.setAlignment(QtCore.Qt.AlignCenter)
        self.condition_icon.setObjectName("condition_icon")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(710, 630, 161, 80))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("img/humidity.png"))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.humidity_label = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.humidity_label.setFont(font)
        self.humidity_label.setStyleSheet("color: white;\n"
"background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius:20px;")
        self.humidity_label.setAlignment(QtCore.Qt.AlignCenter)
        self.humidity_label.setObjectName("humidity_label")
        self.horizontalLayout_4.addWidget(self.humidity_label)
        self.language = QtWidgets.QComboBox(self.centralwidget)
        self.language.setEnabled(True)
        self.language.setGeometry(QtCore.QRect(740, 238, 121, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.language.setFont(font)
        self.language.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.language.setStyleSheet("QComboBox {\n"
"background-color: #22222e;\n"
"color: white;\n"
"padding: .75rem 2.5rem .75rem 1rem;\n"
"border-radius: 3px;\n"
"}")
        self.language.setIconSize(QtCore.QSize(19, 19))
        self.language.setObjectName("language")
        self.language.addItem("")
        self.language.addItem("")
        self.measurement = QtWidgets.QComboBox(self.centralwidget)
        self.measurement.setEnabled(True)
        self.measurement.setGeometry(QtCore.QRect(750, 298, 111, 25))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.measurement.setFont(font)
        self.measurement.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.measurement.setStyleSheet("QComboBox {\n"
"background-color: #22222e;\n"
"color: white;\n"
"padding: .75rem 2.5rem .75rem 1rem;\n"
"border-radius: 3px;\n"
"}")
        self.measurement.setIconSize(QtCore.QSize(19, 19))
        self.measurement.setObjectName("measurement")
        self.measurement.addItem("")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(682, 240, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: white;\n"
"background-color: #22222e;")
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(670, 230, 201, 41))
        self.label_8.setStyleSheet("color: white;\n"
"background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius:20px;")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(682, 300, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: white;\n"
"background-color: #22222e;")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(670, 290, 201, 41))
        self.label_10.setStyleSheet("color: white;\n"
"background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius:20px;")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_8.raise_()
        self.label_6.raise_()
        self.label_10.raise_()
        self.label_9.raise_()
        self.condition_icon.raise_()
        self.frame.raise_()
        self.address_input.raise_()
        self.button.raise_()
        self.image.raise_()
        self.horizontalLayoutWidget.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.traffic_check.raise_()
        self.horizontalLayoutWidget_3.raise_()
        self.conditionlabel.raise_()
        self.horizontalLayoutWidget_4.raise_()
        self.language.raise_()
        self.measurement.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "КАРТА И ПОГОДА"))
        self.button.setText(_translate("MainWindow", "КАРТА"))
        self.label_2.setText(_translate("MainWindow", "МАСШТАБ: "))
        self.plus.setText(_translate("MainWindow", "+"))
        self.minus.setText(_translate("MainWindow", "–"))
        self.label_3.setText(_translate("MainWindow", "ТИП:"))
        self.type.setItemText(0, _translate("MainWindow", "Схема"))
        self.type.setItemText(1, _translate("MainWindow", "Спутник"))
        self.type.setItemText(2, _translate("MainWindow", "Гибрид"))
        self.traffic_check.setText(_translate("MainWindow", "ПРОБКИ"))
        self.temp_label.setText(_translate("MainWindow", "20°C"))
        self.conditionlabel.setText(_translate("MainWindow", "Дождь со снегом"))
        self.humidity_label.setText(_translate("MainWindow", "81%"))
        self.language.setItemText(0, _translate("MainWindow", "Русский"))
        self.language.setItemText(1, _translate("MainWindow", "Украинский"))
        self.measurement.setItemText(0, _translate("MainWindow", "Российские"))
        self.label_6.setText(_translate("MainWindow", "Язык:"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p>Ед. изм.:</p></body></html>"))
