# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(849, 567)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 120, 351, 281))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.overall_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.overall_label.setObjectName("overall_label")
        self.gridLayout.addWidget(self.overall_label, 4, 0, 1, 1)
        self.overall_cB = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overall_cB.setObjectName("overall_cB")
        self.gridLayout.addWidget(self.overall_cB, 5, 0, 1, 1)
        self.alliance_fun_cB = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.alliance_fun_cB.setObjectName("alliance_fun_cB")
        self.gridLayout.addWidget(self.alliance_fun_cB, 3, 1, 1, 1)
        self.country_fun_cB = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.country_fun_cB.setObjectName("country_fun_cB")
        self.gridLayout.addWidget(self.country_fun_cB, 1, 1, 1, 1)
        self.alliance_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.alliance_label.setObjectName("alliance_label")
        self.gridLayout.addWidget(self.alliance_label, 2, 0, 1, 1)
        self.country_cB = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.country_cB.setObjectName("country_cB")
        self.gridLayout.addWidget(self.country_cB, 1, 0, 1, 1)
        self.alliance_cB = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.alliance_cB.setObjectName("alliance_cB")
        self.gridLayout.addWidget(self.alliance_cB, 3, 0, 1, 1)
        self.country_fun_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.country_fun_label.setObjectName("country_fun_label")
        self.gridLayout.addWidget(self.country_fun_label, 0, 1, 1, 1)
        self.country_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.country_label.setObjectName("country_label")
        self.gridLayout.addWidget(self.country_label, 0, 0, 1, 1)
        self.alliance_fun_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.alliance_fun_label.setObjectName("alliance_fun_label")
        self.gridLayout.addWidget(self.alliance_fun_label, 2, 1, 1, 1)
        self.output_window = QtWidgets.QTextBrowser(self.centralwidget)
        self.output_window.setGeometry(QtCore.QRect(500, 110, 256, 301))
        self.output_window.setObjectName("output_window")
        self.calculate_pushbutton = QtWidgets.QPushButton(self.centralwidget)
        self.calculate_pushbutton.setGeometry(QtCore.QRect(180, 440, 121, 61))
        self.calculate_pushbutton.setObjectName("calculate_pushbutton")
        self.overall_rb = QtWidgets.QRadioButton(self.centralwidget)
        self.overall_rb.setGeometry(QtCore.QRect(40, 330, 16, 16))
        self.overall_rb.setText("")
        self.overall_rb.setChecked(True)
        self.overall_rb.setObjectName("overall_rb")
        self.alliance_rb = QtWidgets.QRadioButton(self.centralwidget)
        self.alliance_rb.setGeometry(QtCore.QRect(40, 240, 16, 16))
        self.alliance_rb.setText("")
        self.alliance_rb.setChecked(False)
        self.alliance_rb.setObjectName("alliance_rb")
        self.country_rb = QtWidgets.QRadioButton(self.centralwidget)
        self.country_rb.setGeometry(QtCore.QRect(40, 150, 16, 16))
        self.country_rb.setText("")
        self.country_rb.setChecked(False)
        self.country_rb.setObjectName("country_rb")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 849, 21))
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
        self.overall_label.setText(_translate("MainWindow", "Additional statistics"))
        self.alliance_label.setText(_translate("MainWindow", "Choose alliance:"))
        self.country_fun_label.setText(_translate("MainWindow", "Choose function"))
        self.country_label.setText(_translate("MainWindow", "Choose country:"))
        self.alliance_fun_label.setText(_translate("MainWindow", "Choose function"))
        self.calculate_pushbutton.setText(_translate("MainWindow", "Calculate!"))
