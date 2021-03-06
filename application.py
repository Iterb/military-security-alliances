# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import queries_db
from visualization import create_bar_plot
from networks import draw_alliance_graph, draw_buyers_sellers_graph

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(849, 567)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.output_window = QtWidgets.QTextBrowser(self.centralwidget)
        self.output_window.setGeometry(QtCore.QRect(450, 80, 361, 361))
        self.output_window.setObjectName("output_window")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(35, 100, 351, 331))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.alliance_fun_cB = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.alliance_fun_cB.setObjectName("alliance_fun_cB")
        self.gridLayout.addWidget(self.alliance_fun_cB, 3, 2, 1, 1)
        self.country_fun_cB = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.country_fun_cB.setObjectName("country_fun_cB")
        self.gridLayout.addWidget(self.country_fun_cB, 1, 2, 1, 1)
        self.country_cB = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.country_cB.setObjectName("country_cB")
        self.gridLayout.addWidget(self.country_cB, 1, 1, 1, 1)
        self.country_fun_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.country_fun_label.setObjectName("country_fun_label")
        self.gridLayout.addWidget(self.country_fun_label, 0, 2, 1, 1)
        self.alliance_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.alliance_label.setObjectName("alliance_label")
        self.gridLayout.addWidget(self.alliance_label, 2, 1, 1, 1)
        self.country_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.country_label.setObjectName("country_label")
        self.gridLayout.addWidget(self.country_label, 0, 1, 1, 1)
        self.alliance_fun_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.alliance_fun_label.setObjectName("alliance_fun_label")
        self.gridLayout.addWidget(self.alliance_fun_label, 2, 2, 1, 1)
        self.alliance_cB = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.alliance_cB.setObjectName("alliance_cB")
        self.gridLayout.addWidget(self.alliance_cB, 3, 1, 1, 1)
        self.overall_cB = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.overall_cB.setObjectName("overall_cB")
        self.gridLayout.addWidget(self.overall_cB, 6, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.k_core_size_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.k_core_size_lineEdit.sizePolicy().hasHeightForWidth())
        self.k_core_size_lineEdit.setSizePolicy(sizePolicy)
        self.k_core_size_lineEdit.setMaximumSize(QtCore.QSize(1000000, 100000))
        self.k_core_size_lineEdit.setBaseSize(QtCore.QSize(0, 0))
        self.k_core_size_lineEdit.setObjectName("k_core_size_lineEdit")
        self.verticalLayout_2.addWidget(self.k_core_size_lineEdit)
        self.Start_date_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Start_date_lineEdit.sizePolicy().hasHeightForWidth())
        self.Start_date_lineEdit.setSizePolicy(sizePolicy)
        self.Start_date_lineEdit.setMaximumSize(QtCore.QSize(1000000, 100000))
        self.Start_date_lineEdit.setBaseSize(QtCore.QSize(0, 0))
        self.Start_date_lineEdit.setObjectName("Start_date_lineEdit")
        self.verticalLayout_2.addWidget(self.Start_date_lineEdit)
        self.End_date_lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.End_date_lineEdit.sizePolicy().hasHeightForWidth())
        self.End_date_lineEdit.setSizePolicy(sizePolicy)
        self.End_date_lineEdit.setMaximumSize(QtCore.QSize(1000000, 100000))
        self.End_date_lineEdit.setBaseSize(QtCore.QSize(0, 0))
        self.End_date_lineEdit.setObjectName("End_date_lineEdit")
        self.verticalLayout_2.addWidget(self.End_date_lineEdit)
        self.gridLayout.addLayout(self.verticalLayout_2, 9, 2, 1, 1)
        self.network_type_cB = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.network_type_cB.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.network_type_cB.setMinimumContentsLength(2)
        self.network_type_cB.setIconSize(QtCore.QSize(16, 16))
        self.network_type_cB.setDuplicatesEnabled(False)
        self.network_type_cB.setFrame(True)
        self.network_type_cB.setObjectName("network_type_cB")
        self.gridLayout.addWidget(self.network_type_cB, 8, 1, 1, 1)
        self.overall_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.overall_label.setObjectName("overall_label")
        self.gridLayout.addWidget(self.overall_label, 4, 1, 1, 1)
        self.network_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.network_label.setObjectName("network_label")
        self.gridLayout.addWidget(self.network_label, 7, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.k_core_size_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.k_core_size_label.setObjectName("k_core_size_label")
        self.verticalLayout.addWidget(self.k_core_size_label)
        self.start_date_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.start_date_label.setEnabled(True)
        self.start_date_label.setObjectName("start_date_label")
        self.verticalLayout.addWidget(self.start_date_label)
        self.end_date_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.end_date_label.setObjectName("end_date_label")
        self.verticalLayout.addWidget(self.end_date_label)
        self.gridLayout.addLayout(self.verticalLayout, 9, 1, 1, 1)
        self.country_rb = QtWidgets.QRadioButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.country_rb.sizePolicy().hasHeightForWidth())
        self.country_rb.setSizePolicy(sizePolicy)
        self.country_rb.setText("")
        self.country_rb.setChecked(False)
        self.country_rb.setObjectName("country_rb")
        self.gridLayout.addWidget(self.country_rb, 0, 0, 1, 1)
        self.alliance_rb = QtWidgets.QRadioButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alliance_rb.sizePolicy().hasHeightForWidth())
        self.alliance_rb.setSizePolicy(sizePolicy)
        self.alliance_rb.setText("")
        self.alliance_rb.setChecked(False)
        self.alliance_rb.setObjectName("alliance_rb")
        self.gridLayout.addWidget(self.alliance_rb, 2, 0, 1, 1)
        self.overall_rb = QtWidgets.QRadioButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.overall_rb.sizePolicy().hasHeightForWidth())
        self.overall_rb.setSizePolicy(sizePolicy)
        self.overall_rb.setText("")
        self.overall_rb.setChecked(False)
        self.overall_rb.setObjectName("overall_rb")
        self.gridLayout.addWidget(self.overall_rb, 4, 0, 1, 1)
        self.network_rb = QtWidgets.QRadioButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.network_rb.sizePolicy().hasHeightForWidth())
        self.network_rb.setSizePolicy(sizePolicy)
        self.network_rb.setText("")
        self.network_rb.setChecked(True)
        self.network_rb.setObjectName("network_rb")
        self.gridLayout.addWidget(self.network_rb, 7, 0, 1, 1)
        self.calculate_pushbutton = QtWidgets.QPushButton(self.centralwidget)
        self.calculate_pushbutton.setGeometry(QtCore.QRect(135, 460, 121, 61))
        self.calculate_pushbutton.setObjectName("calculate_pushbutton")
        self.draw_pushbutton = QtWidgets.QPushButton(self.centralwidget)
        self.draw_pushbutton.setGeometry(QtCore.QRect(575, 460, 121, 61))
        self.draw_pushbutton.setObjectName("draw_pushbutton")
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


        # Comboboxes setup
        self.country_cB.addItems(queries_db.get_all_countries())
        self.country_fun_cB.addItems(["Tanks quantity", "Alliances involvment", "Tanks orgin"])
        self.country_cB.currentTextChanged.connect(self.deactive_plot_button)
        self.country_fun_cB.currentTextChanged.connect(self.deactive_plot_button)
        self.alliance_cB.addItems(queries_db.get_all_alliances())

        self.alliance_fun_cB.addItems(["Tanks quantity", "Member countries", "Tanks orgin"])
        self.alliance_cB.currentTextChanged.connect(self.deactive_plot_button)
        self.alliance_fun_cB.currentTextChanged.connect(self.deactive_plot_button)

        self.overall_cB.addItems(["Most popular tanks", "Biggest sellers", "Strongest alliances"])
        self.overall_cB.currentTextChanged.connect(self.deactive_plot_button)

        self.network_type_cB.addItems(["Countries in alliances", "Sellers - buyers connections"])

        #BrowserText setup
        self.output_window.horizontalScrollBar().setValue(0)
        self.output_window.setLineWrapMode(0)
        # Button setup
        self.calculate_pushbutton.clicked.connect(self.on_click_calcualte_button)

        self.draw_pushbutton.setDisabled(True)
        self.draw_pushbutton.clicked.connect(self.on_click_draw_button)
        #Font setup
        font = QtGui.QFont("Monospace")
        font.setStyleHint(QtGui.QFont.TypeWriter)
        self.output_window.setFont(font)

    def on_click_calcualte_button(self):
        
        if self.country_rb.isChecked():
            text = str(self.country_cB.currentText())
            function = self.country_fun_cB.currentIndex()
            if function == 0:
                self.draw_pushbutton.setDisabled(False)
                self.output_window.setText(str(queries_db.country_tank_info(text, formated = True)))
            if function == 1:
                self.output_window.setText(str(queries_db.country_aliance_info(text, formated = True)))
            if function == 2:
                self.draw_pushbutton.setDisabled(False)
                self.output_window.setText(str(queries_db.country_tank_seller_origin_info(text, formated = True)))
        if self.alliance_rb.isChecked():
            text = str(self.alliance_cB.currentText())
            function = self.alliance_fun_cB.currentIndex()
            if function == 0:
                self.draw_pushbutton.setDisabled(False)
                self.output_window.setText(str(queries_db.alliance_tanks_info(text, formated = True, max_end_date=1900)))
            if function == 1:
                self.output_window.setText(str(queries_db.alliance_countries_info(text, formated = True)))
            if function == 2:
                self.draw_pushbutton.setDisabled(False)
                self.output_window.setText(str(queries_db.alliance_tanks_origin_info(text, formated = True)))
        if self.overall_rb.isChecked():
            function = self.overall_cB.currentIndex()
            if function == 0:
                self.draw_pushbutton.setDisabled(False)
                self.output_window.setText(str(queries_db.overall_tanks_quantity(formated = True)))
            if function == 1:
                self.draw_pushbutton.setDisabled(False)
                self.output_window.setText(str(queries_db.overall_orgin_quantity(formated = True)))
            if function == 2:
                self.draw_pushbutton.setDisabled(False)
                self.output_window.setText(str(queries_db.overall_alliances_tank_quantity(formated = True)))
        if self.network_rb.isChecked():
            self.output_window.setText("")
            function = self.network_type_cB.currentIndex()
            k_core = self.k_core_size_lineEdit.text()
            if function == 0:
                start_date = self.Start_date_lineEdit.text()
                end_date = self.End_date_lineEdit.text()
                try:
                    k_core = int(k_core)
                    start_date = int(start_date)
                    end_date = int(end_date)
                    draw_alliance_graph(start_date, end_date, k_core)
                except:
                    self.output_window.setText("Please enter correct data")
            if function == 1:
                try:
                    k_core = int(k_core)
                    draw_buyers_sellers_graph(k_core)
                except:
                    self.output_window.setText("Please enter correct data")

    def on_click_draw_button(self):
        if self.country_rb.isChecked():
            text = str(self.country_cB.currentText())
            function = self.country_fun_cB.currentIndex()
            if function == 0:
                create_bar_plot(queries_db.country_tank_info(text), "Overall tank quantity")
            if function == 2:
                create_bar_plot(queries_db.country_tank_seller_origin_info(text), "Tanks origin")
        if self.alliance_rb.isChecked():
            text = str(self.alliance_cB.currentText())
            function = self.alliance_fun_cB.currentIndex()
            if function == 0:
                create_bar_plot(queries_db.alliance_tanks_info(text, max_end_date=1900), "Overall tank quantity")
            if function == 2:
                create_bar_plot(queries_db.alliance_tanks_origin_info(text), "Tanks origin")
        if self.overall_rb.isChecked():
            function = self.overall_cB.currentIndex()
            if function == 0:
                create_bar_plot(queries_db.overall_tanks_quantity(), "Overall tank quantity")
            if function == 1:
                create_bar_plot(queries_db.overall_orgin_quantity(), "Biggest sellers")
            if function == 2:
                create_bar_plot(queries_db.overall_alliances_tank_quantity(), "Strongst alliances")
        if self.network_rb.isChecked():
            self.output_window.setText("")
            function = self.network_type_cB.currentIndex()
            k_core = self.k_core_size_lineEdit.text()
            if function == 0:
                start_date = self.Start_date_lineEdit.text()
                end_date = self.End_date_lineEdit.text()
                try:
                    k_core = int(k_core)
                    start_date = int(start_date)
                    end_date = int(end_date)
                    draw_alliance_graph(start_date, end_date, k_core)
                except:
                    self.output_window.setText("Please enter correct data")
            if function == 1:
                try:
                    k_core = int(k_core)
                    draw_buyers_sellers_graph(k_core)
                except:
                    self.output_window.setText("Please enter correct data")
        
       
    def deactive_plot_button(self):
        self.draw_pushbutton.setDisabled(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.country_fun_label.setText(_translate("MainWindow", "Choose function"))
        self.alliance_label.setText(_translate("MainWindow", "Choose alliance:"))
        self.country_label.setText(_translate("MainWindow", "Choose country:"))
        self.alliance_fun_label.setText(_translate("MainWindow", "Choose function"))
        self.overall_label.setText(_translate("MainWindow", "Additional statistics"))
        self.network_label.setText(_translate("MainWindow", "Network type"))
        self.k_core_size_label.setText(_translate("MainWindow", "K-core size"))
        self.start_date_label.setText(_translate("MainWindow", "Start date"))
        self.end_date_label.setText(_translate("MainWindow", "End date"))
        self.calculate_pushbutton.setText(_translate("MainWindow", "Calculate!"))
        self.draw_pushbutton.setText(_translate("MainWindow", "Create plot"))




if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication([])
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())