# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 325)
        MainWindow.setMinimumSize(QtCore.QSize(600, 325))
        MainWindow.setMaximumSize(QtCore.QSize(600, 325))
        MainWindow.setStyleSheet("background-color: rgb(146, 250, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(600, 325))
        self.centralwidget.setMaximumSize(QtCore.QSize(600, 325))
        self.centralwidget.setMouseTracking(False)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 20, 600, 351))
        self.stackedWidget.setMinimumSize(QtCore.QSize(600, 330))
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.home_page = QtWidgets.QWidget()
        self.home_page.setObjectName("home_page")
        self.rec_btn = QtWidgets.QPushButton(self.home_page)
        self.rec_btn.setGeometry(QtCore.QRect(240, 150, 121, 91))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rec_btn.sizePolicy().hasHeightForWidth())
        self.rec_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.rec_btn.setFont(font)
        self.rec_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 59, 0);\n"
"    border-radius: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(210, 59, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px black;\n"
"    border-style: inset;\n"
"}\n"
"\n"
"")
        self.rec_btn.setObjectName("rec_btn")
        self.home_save_btn = QtWidgets.QPushButton(self.home_page)
        self.home_save_btn.setGeometry(QtCore.QRect(10, 260, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.home_save_btn.setFont(font)
        self.home_save_btn.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px grey;\n"
"    border-style: inset;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(222, 222, 222);\n"
"}")
        self.home_save_btn.setObjectName("home_save_btn")
        self.home_title_lbl = QtWidgets.QLabel(self.home_page)
        self.home_title_lbl.setGeometry(QtCore.QRect(200, 0, 281, 34))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.home_title_lbl.setFont(font)
        self.home_title_lbl.setObjectName("home_title_lbl")
        self.layoutWidget = QtWidgets.QWidget(self.home_page)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 90, 421, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.drop_down_hboxlayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.drop_down_hboxlayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.drop_down_hboxlayout.setContentsMargins(0, 0, 0, 0)
        self.drop_down_hboxlayout.setSpacing(20)
        self.drop_down_hboxlayout.setObjectName("drop_down_hboxlayout")
        self.date_cbo = QtWidgets.QComboBox(self.layoutWidget)
        self.date_cbo.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.date_cbo.sizePolicy().hasHeightForWidth())
        self.date_cbo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.date_cbo.setFont(font)
        self.date_cbo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.date_cbo.setObjectName("date_cbo")
        self.date_cbo.addItem("")
        self.date_cbo.addItem("")
        self.date_cbo.addItem("")
        self.date_cbo.addItem("")
        self.date_cbo.addItem("")
        self.date_cbo.addItem("")
        self.date_cbo.addItem("")
        self.date_cbo.addItem("")
        self.date_cbo.addItem("")
        self.date_cbo.addItem("")
        self.date_cbo.addItem("")
        self.date_cbo.addItem("")
        self.date_cbo.addItem("")
        self.date_cbo.addItem("")
        self.date_cbo.addItem("")
        self.date_cbo.addItem("")
        self.date_cbo.addItem("")
        self.date_cbo.addItem("")
        self.date_cbo.addItem("")
        self.date_cbo.addItem("")
        self.date_cbo.addItem("")
        self.date_cbo.addItem("")
        self.date_cbo.addItem("")
        self.date_cbo.addItem("")
        self.date_cbo.addItem("")
        self.date_cbo.addItem("")
        self.date_cbo.addItem("")
        self.date_cbo.addItem("")
        self.date_cbo.addItem("")
        self.date_cbo.addItem("")
        self.date_cbo.addItem("")
        self.date_cbo.addItem("")
        self.drop_down_hboxlayout.addWidget(self.date_cbo)
        self.month_cbo = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.month_cbo.sizePolicy().hasHeightForWidth())
        self.month_cbo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.month_cbo.setFont(font)
        self.month_cbo.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.month_cbo.setObjectName("month_cbo")
        self.month_cbo.addItem("")
        self.month_cbo.addItem("")
        self.month_cbo.addItem("")
        self.month_cbo.addItem("")
        self.month_cbo.addItem("")
        self.month_cbo.addItem("")
        self.month_cbo.addItem("")
        self.month_cbo.addItem("")
        self.month_cbo.addItem("")
        self.month_cbo.addItem("")
        self.month_cbo.addItem("")
        self.month_cbo.addItem("")
        self.drop_down_hboxlayout.addWidget(self.month_cbo)
        self.year_cbo = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.year_cbo.setFont(font)
        self.year_cbo.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.year_cbo.setObjectName("year_cbo")
        self.drop_down_hboxlayout.addWidget(self.year_cbo)
        self.layoutWidget1 = QtWidgets.QWidget(self.home_page)
        self.layoutWidget1.setGeometry(QtCore.QRect(90, 40, 211, 36))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.name__hboxlayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.name__hboxlayout.setContentsMargins(0, 0, 0, 0)
        self.name__hboxlayout.setSpacing(21)
        self.name__hboxlayout.setObjectName("name__hboxlayout")
        self.subject_lbl = QtWidgets.QLabel(self.layoutWidget1)
        self.subject_lbl.setObjectName("subject_lbl")
        self.name__hboxlayout.addWidget(self.subject_lbl)
        self.subject_txt = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.subject_txt.setFont(font)
        self.subject_txt.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid blue;\n"
"    \n"
"}")
        self.subject_txt.setObjectName("subject_txt")
        self.name__hboxlayout.addWidget(self.subject_txt)
        self.home_delete_btn = QtWidgets.QPushButton(self.home_page)
        self.home_delete_btn.setGeometry(QtCore.QRect(450, 260, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.home_delete_btn.setFont(font)
        self.home_delete_btn.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px grey;\n"
"    border-style: inset;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(222, 222, 222);\n"
"}")
        self.home_delete_btn.setObjectName("home_delete_btn")
        self.home_db_btn = QtWidgets.QPushButton(self.home_page)
        self.home_db_btn.setGeometry(QtCore.QRect(230, 260, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.home_db_btn.setFont(font)
        self.home_db_btn.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px grey;\n"
"    border-style: inset;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(222, 222, 222);\n"
"}")
        self.home_db_btn.setObjectName("home_db_btn")
        self.rec_pause_btn = QtWidgets.QPushButton(self.home_page)
        self.rec_pause_btn.setGeometry(QtCore.QRect(240, 150, 121, 91))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rec_pause_btn.sizePolicy().hasHeightForWidth())
        self.rec_pause_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.rec_pause_btn.setFont(font)
        self.rec_pause_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 59, 0);\n"
"    border-radius: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(210, 59, 0);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px black;\n"
"    border-style: inset;\n"
"}\n"
"\n"
"")
        self.rec_pause_btn.setObjectName("rec_pause_btn")
        self.stackedWidget.addWidget(self.home_page)
        self.db_page = QtWidgets.QWidget()
        self.db_page.setObjectName("db_page")
        self.db_search_btn = QtWidgets.QPushButton(self.db_page)
        self.db_search_btn.setGeometry(QtCore.QRect(460, 50, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.db_search_btn.setFont(font)
        self.db_search_btn.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px grey;\n"
"    border-style: inset;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(222, 222, 222);\n"
"}")
        self.db_search_btn.setObjectName("db_search_btn")
        self.db_delete_btn = QtWidgets.QPushButton(self.db_page)
        self.db_delete_btn.setGeometry(QtCore.QRect(450, 260, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.db_delete_btn.setFont(font)
        self.db_delete_btn.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px grey;\n"
"    border-style: inset;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(222, 222, 222);\n"
"}")
        self.db_delete_btn.setObjectName("db_delete_btn")
        self.db_tbl_widget = QtWidgets.QTableWidget(self.db_page)
        self.db_tbl_widget.setGeometry(QtCore.QRect(10, 90, 571, 161))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.db_tbl_widget.sizePolicy().hasHeightForWidth())
        self.db_tbl_widget.setSizePolicy(sizePolicy)
        self.db_tbl_widget.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.db_tbl_widget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.db_tbl_widget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.db_tbl_widget.setColumnCount(5)
        self.db_tbl_widget.setObjectName("db_tbl_widget")
        self.db_tbl_widget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.db_tbl_widget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.db_tbl_widget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.db_tbl_widget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.db_tbl_widget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.db_tbl_widget.setHorizontalHeaderItem(4, item)
        self.db_tbl_widget.horizontalHeader().setDefaultSectionSize(110)
        self.db_tbl_widget.horizontalHeader().setMinimumSectionSize(48)
        self.db_back_btn = QtWidgets.QPushButton(self.db_page)
        self.db_back_btn.setGeometry(QtCore.QRect(20, 260, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.db_back_btn.setFont(font)
        self.db_back_btn.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px grey;\n"
"    border-style: inset;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(222, 222, 222);\n"
"}")
        self.db_back_btn.setObjectName("db_back_btn")
        self.db_title_lbl = QtWidgets.QLabel(self.db_page)
        self.db_title_lbl.setGeometry(QtCore.QRect(200, 0, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.db_title_lbl.setFont(font)
        self.db_title_lbl.setObjectName("db_title_lbl")
        self.layoutWidget2 = QtWidgets.QWidget(self.db_page)
        self.layoutWidget2.setGeometry(QtCore.QRect(140, 45, 311, 41))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.db_drop_down_hboxlayout = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.db_drop_down_hboxlayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.db_drop_down_hboxlayout.setContentsMargins(0, 0, 0, 0)
        self.db_drop_down_hboxlayout.setSpacing(20)
        self.db_drop_down_hboxlayout.setObjectName("db_drop_down_hboxlayout")
        self.db_date_cbo = QtWidgets.QComboBox(self.layoutWidget2)
        self.db_date_cbo.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.db_date_cbo.sizePolicy().hasHeightForWidth())
        self.db_date_cbo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.db_date_cbo.setFont(font)
        self.db_date_cbo.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.db_date_cbo.setObjectName("db_date_cbo")
        self.db_date_cbo.addItem("")
        self.db_date_cbo.setItemText(0, "")
        self.db_date_cbo.addItem("")
        self.db_date_cbo.addItem("")
        self.db_date_cbo.addItem("")
        self.db_date_cbo.addItem("")
        self.db_date_cbo.addItem("")
        self.db_date_cbo.addItem("")
        self.db_date_cbo.addItem("")
        self.db_date_cbo.addItem("")
        self.db_date_cbo.addItem("")
        self.db_date_cbo.addItem("")
        self.db_date_cbo.addItem("")
        self.db_date_cbo.addItem("")
        self.db_date_cbo.addItem("")
        self.db_date_cbo.addItem("")
        self.db_date_cbo.addItem("")
        self.db_date_cbo.addItem("")
        self.db_date_cbo.addItem("")
        self.db_date_cbo.addItem("")
        self.db_date_cbo.addItem("")
        self.db_date_cbo.addItem("")
        self.db_date_cbo.addItem("")
        self.db_date_cbo.addItem("")
        self.db_date_cbo.addItem("")
        self.db_date_cbo.addItem("")
        self.db_date_cbo.addItem("")
        self.db_date_cbo.addItem("")
        self.db_date_cbo.addItem("")
        self.db_date_cbo.addItem("")
        self.db_date_cbo.addItem("")
        self.db_date_cbo.addItem("")
        self.db_date_cbo.addItem("")
        self.db_drop_down_hboxlayout.addWidget(self.db_date_cbo)
        self.db_month_cbo = QtWidgets.QComboBox(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.db_month_cbo.sizePolicy().hasHeightForWidth())
        self.db_month_cbo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.db_month_cbo.setFont(font)
        self.db_month_cbo.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.db_month_cbo.setObjectName("db_month_cbo")
        self.db_month_cbo.addItem("")
        self.db_month_cbo.setItemText(0, "")
        self.db_month_cbo.addItem("")
        self.db_month_cbo.addItem("")
        self.db_month_cbo.addItem("")
        self.db_month_cbo.addItem("")
        self.db_month_cbo.addItem("")
        self.db_month_cbo.addItem("")
        self.db_month_cbo.addItem("")
        self.db_month_cbo.addItem("")
        self.db_month_cbo.addItem("")
        self.db_month_cbo.addItem("")
        self.db_month_cbo.addItem("")
        self.db_month_cbo.addItem("")
        self.db_drop_down_hboxlayout.addWidget(self.db_month_cbo)
        self.db_year_cbo = QtWidgets.QComboBox(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.db_year_cbo.setFont(font)
        self.db_year_cbo.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.db_year_cbo.setObjectName("db_year_cbo")
        self.db_year_cbo.addItem("")
        self.db_year_cbo.setItemText(0, "")
        self.db_drop_down_hboxlayout.addWidget(self.db_year_cbo)
        self.db_search_txt = QtWidgets.QLineEdit(self.db_page)
        self.db_search_txt.setGeometry(QtCore.QRect(10, 50, 111, 34))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.db_search_txt.setFont(font)
        self.db_search_txt.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid blue;\n"
"    \n"
"}")
        self.db_search_txt.setText("")
        self.db_search_txt.setObjectName("db_search_txt")
        self.db_select_btn = QtWidgets.QPushButton(self.db_page)
        self.db_select_btn.setGeometry(QtCore.QRect(230, 260, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.db_select_btn.setFont(font)
        self.db_select_btn.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px grey;\n"
"    border-style: inset;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(222, 222, 222);\n"
"}")
        self.db_select_btn.setObjectName("db_select_btn")
        self.stackedWidget.addWidget(self.db_page)
        self.note_page = QtWidgets.QWidget()
        self.note_page.setObjectName("note_page")
        self.trans_txt = QtWidgets.QTextEdit(self.note_page)
        self.trans_txt.setGeometry(QtCore.QRect(50, 60, 511, 171))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.trans_txt.setFont(font)
        self.trans_txt.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.trans_txt.setObjectName("trans_txt")
        self.trans_lbl = QtWidgets.QLabel(self.note_page)
        self.trans_lbl.setGeometry(QtCore.QRect(50, 40, 231, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.trans_lbl.setFont(font)
        self.trans_lbl.setObjectName("trans_lbl")
        self.note_play_btn = QtWidgets.QPushButton(self.note_page)
        self.note_play_btn.setGeometry(QtCore.QRect(190, 250, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.note_play_btn.setFont(font)
        self.note_play_btn.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px grey;\n"
"    border-style: inset;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(222, 222, 222);\n"
"}\n"
"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
"<ui version=\"4.0\">\n"
" <widget name=\"__qt_fake_top_level\">\n"
"  <widget class=\"QPushButton\" name=\"note_play_btn\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>230</x>\n"
"     <y>260</y>\n"
"     <width>141</width>\n"
"     <height>41</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"font\">\n"
"    <font>\n"
"     <pointsize>14</pointsize>\n"
"    </font>\n"
"   </property>\n"
"   <property name=\"styleSheet\">\n"
"    <string notr=\"true\">QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px grey;\n"
"    border-style: inset;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(222, 222, 222);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: rgb(255, 0, 0);\n"
"}</string>\n"
"   </property>\n"
"   <property name=\"text\">\n"
"    <string>Play</string>\n"
"   </property>\n"
"   <property name=\"checkable\">\n"
"    <bool>true</bool>\n"
"   </property>\n"
"  </widget>\n"
" </widget>\n"
" <resources/>\n"
"</ui>\n"
"")
        self.note_play_btn.setCheckable(False)
        self.note_play_btn.setObjectName("note_play_btn")
        self.note_back_btn = QtWidgets.QPushButton(self.note_page)
        self.note_back_btn.setGeometry(QtCore.QRect(10, 260, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.note_back_btn.setFont(font)
        self.note_back_btn.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px grey;\n"
"    border-style: inset;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(222, 222, 222);\n"
"}")
        self.note_back_btn.setObjectName("note_back_btn")
        self.note_delete_btn = QtWidgets.QPushButton(self.note_page)
        self.note_delete_btn.setGeometry(QtCore.QRect(450, 260, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.note_delete_btn.setFont(font)
        self.note_delete_btn.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px grey;\n"
"    border-style: inset;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(222, 222, 222);\n"
"}")
        self.note_delete_btn.setObjectName("note_delete_btn")
        self.note_pause_btn = QtWidgets.QPushButton(self.note_page)
        self.note_pause_btn.setGeometry(QtCore.QRect(320, 250, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.note_pause_btn.setFont(font)
        self.note_pause_btn.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 2px grey;\n"
"    border-style: inset;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(222, 222, 222);\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: rgb(198, 198, 198);\n"
"}")
        self.note_pause_btn.setCheckable(True)
        self.note_pause_btn.setObjectName("note_pause_btn")
        self.name_of_file_lbl = QtWidgets.QLabel(self.note_page)
        self.name_of_file_lbl.setGeometry(QtCore.QRect(50, 0, 511, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.name_of_file_lbl.setFont(font)
        self.name_of_file_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.name_of_file_lbl.setObjectName("name_of_file_lbl")
        self.stackedWidget.addWidget(self.note_page)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.year_cbo.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.rec_btn.setText(_translate("MainWindow", "▶️"))
        self.home_save_btn.setText(_translate("MainWindow", "📁Save"))
        self.home_title_lbl.setText(_translate("MainWindow", "Record a new note"))
        self.date_cbo.setItemText(0, _translate("MainWindow", "1"))
        self.date_cbo.setItemText(1, _translate("MainWindow", "2"))
        self.date_cbo.setItemText(2, _translate("MainWindow", "3"))
        self.date_cbo.setItemText(3, _translate("MainWindow", "4"))
        self.date_cbo.setItemText(4, _translate("MainWindow", "5"))
        self.date_cbo.setItemText(5, _translate("MainWindow", "6"))
        self.date_cbo.setItemText(6, _translate("MainWindow", "7"))
        self.date_cbo.setItemText(7, _translate("MainWindow", "8"))
        self.date_cbo.setItemText(8, _translate("MainWindow", "9"))
        self.date_cbo.setItemText(9, _translate("MainWindow", "10"))
        self.date_cbo.setItemText(10, _translate("MainWindow", "11"))
        self.date_cbo.setItemText(11, _translate("MainWindow", "12"))
        self.date_cbo.setItemText(12, _translate("MainWindow", "13"))
        self.date_cbo.setItemText(13, _translate("MainWindow", "14"))
        self.date_cbo.setItemText(14, _translate("MainWindow", "15"))
        self.date_cbo.setItemText(15, _translate("MainWindow", "16"))
        self.date_cbo.setItemText(16, _translate("MainWindow", "17"))
        self.date_cbo.setItemText(17, _translate("MainWindow", "18"))
        self.date_cbo.setItemText(18, _translate("MainWindow", "19"))
        self.date_cbo.setItemText(19, _translate("MainWindow", "20"))
        self.date_cbo.setItemText(20, _translate("MainWindow", "21"))
        self.date_cbo.setItemText(21, _translate("MainWindow", "22"))
        self.date_cbo.setItemText(22, _translate("MainWindow", "23"))
        self.date_cbo.setItemText(23, _translate("MainWindow", "24"))
        self.date_cbo.setItemText(24, _translate("MainWindow", "25"))
        self.date_cbo.setItemText(25, _translate("MainWindow", "26"))
        self.date_cbo.setItemText(26, _translate("MainWindow", "26"))
        self.date_cbo.setItemText(27, _translate("MainWindow", "27"))
        self.date_cbo.setItemText(28, _translate("MainWindow", "28"))
        self.date_cbo.setItemText(29, _translate("MainWindow", "29"))
        self.date_cbo.setItemText(30, _translate("MainWindow", "30"))
        self.date_cbo.setItemText(31, _translate("MainWindow", "31"))
        self.month_cbo.setItemText(0, _translate("MainWindow", "Jan"))
        self.month_cbo.setItemText(1, _translate("MainWindow", "Feb"))
        self.month_cbo.setItemText(2, _translate("MainWindow", "Mar"))
        self.month_cbo.setItemText(3, _translate("MainWindow", "Apr"))
        self.month_cbo.setItemText(4, _translate("MainWindow", "May"))
        self.month_cbo.setItemText(5, _translate("MainWindow", "Jun"))
        self.month_cbo.setItemText(6, _translate("MainWindow", "Jul"))
        self.month_cbo.setItemText(7, _translate("MainWindow", "Aug"))
        self.month_cbo.setItemText(8, _translate("MainWindow", "Sep"))
        self.month_cbo.setItemText(9, _translate("MainWindow", "Oct"))
        self.month_cbo.setItemText(10, _translate("MainWindow", "Nov"))
        self.month_cbo.setItemText(11, _translate("MainWindow", "Dec"))
        self.subject_lbl.setText(_translate("MainWindow", "Subject:"))
        self.subject_txt.setText(_translate("MainWindow", "SDD"))
        self.home_delete_btn.setText(_translate("MainWindow", "🗑️Delete"))
        self.home_db_btn.setText(_translate("MainWindow", "🔎Database"))
        self.rec_pause_btn.setText(_translate("MainWindow", "||"))
        self.db_search_btn.setText(_translate("MainWindow", "🔎Search"))
        self.db_delete_btn.setText(_translate("MainWindow", "🗑️Delete"))
        item = self.db_tbl_widget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Subject"))
        item = self.db_tbl_widget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Date"))
        item = self.db_tbl_widget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Month"))
        item = self.db_tbl_widget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Year"))
        item = self.db_tbl_widget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Time"))
        self.db_back_btn.setText(_translate("MainWindow", "⬅Back"))
        self.db_title_lbl.setText(_translate("MainWindow", "Search for a note"))
        self.db_date_cbo.setItemText(1, _translate("MainWindow", "1"))
        self.db_date_cbo.setItemText(2, _translate("MainWindow", "2"))
        self.db_date_cbo.setItemText(3, _translate("MainWindow", "3"))
        self.db_date_cbo.setItemText(4, _translate("MainWindow", "4"))
        self.db_date_cbo.setItemText(5, _translate("MainWindow", "5"))
        self.db_date_cbo.setItemText(6, _translate("MainWindow", "6"))
        self.db_date_cbo.setItemText(7, _translate("MainWindow", "7"))
        self.db_date_cbo.setItemText(8, _translate("MainWindow", "8"))
        self.db_date_cbo.setItemText(9, _translate("MainWindow", "9"))
        self.db_date_cbo.setItemText(10, _translate("MainWindow", "10"))
        self.db_date_cbo.setItemText(11, _translate("MainWindow", "11"))
        self.db_date_cbo.setItemText(12, _translate("MainWindow", "12"))
        self.db_date_cbo.setItemText(13, _translate("MainWindow", "13"))
        self.db_date_cbo.setItemText(14, _translate("MainWindow", "14"))
        self.db_date_cbo.setItemText(15, _translate("MainWindow", "15"))
        self.db_date_cbo.setItemText(16, _translate("MainWindow", "16"))
        self.db_date_cbo.setItemText(17, _translate("MainWindow", "17"))
        self.db_date_cbo.setItemText(18, _translate("MainWindow", "18"))
        self.db_date_cbo.setItemText(19, _translate("MainWindow", "19"))
        self.db_date_cbo.setItemText(20, _translate("MainWindow", "20"))
        self.db_date_cbo.setItemText(21, _translate("MainWindow", "21"))
        self.db_date_cbo.setItemText(22, _translate("MainWindow", "22"))
        self.db_date_cbo.setItemText(23, _translate("MainWindow", "23"))
        self.db_date_cbo.setItemText(24, _translate("MainWindow", "24"))
        self.db_date_cbo.setItemText(25, _translate("MainWindow", "25"))
        self.db_date_cbo.setItemText(26, _translate("MainWindow", "26"))
        self.db_date_cbo.setItemText(27, _translate("MainWindow", "27"))
        self.db_date_cbo.setItemText(28, _translate("MainWindow", "28"))
        self.db_date_cbo.setItemText(29, _translate("MainWindow", "29"))
        self.db_date_cbo.setItemText(30, _translate("MainWindow", "30"))
        self.db_date_cbo.setItemText(31, _translate("MainWindow", "31"))
        self.db_month_cbo.setItemText(1, _translate("MainWindow", "Jan"))
        self.db_month_cbo.setItemText(2, _translate("MainWindow", "Feb"))
        self.db_month_cbo.setItemText(3, _translate("MainWindow", "Mar"))
        self.db_month_cbo.setItemText(4, _translate("MainWindow", "Apr"))
        self.db_month_cbo.setItemText(5, _translate("MainWindow", "May"))
        self.db_month_cbo.setItemText(6, _translate("MainWindow", "Jun"))
        self.db_month_cbo.setItemText(7, _translate("MainWindow", "Jul"))
        self.db_month_cbo.setItemText(8, _translate("MainWindow", "Aug"))
        self.db_month_cbo.setItemText(9, _translate("MainWindow", "Sep"))
        self.db_month_cbo.setItemText(10, _translate("MainWindow", "Oct"))
        self.db_month_cbo.setItemText(11, _translate("MainWindow", "Nov"))
        self.db_month_cbo.setItemText(12, _translate("MainWindow", "Dec"))
        self.db_select_btn.setText(_translate("MainWindow", "Select"))
        self.trans_txt.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Comic Sans MS\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"docs-internal-guid-7b7bfebb-7fff-5092-a033-c7d0c68be7b2\"></a><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:transparent;\">A</span><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:transparent;\"> core functionality of the software will be its ability to attempt and transcribe the student’s recordings into written text through the use of the SpeechRecognition python library when retrieving and viewing a recording from the database.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"docs-internal-guid-7b7bfebb-7fff-5092-a033-c7d0c68be7b2\"></a><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:transparent;\">A</span><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:transparent;\"> core functionality of the software will be its ability to attempt and transcribe the student’s recordings into written text through the use of the SpeechRecognition python library when retrieving and viewing a recording from the database.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"docs-internal-guid-7b7bfebb-7fff-5092-a033-c7d0c68be7b2\"></a><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:transparent;\">A</span><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:transparent;\"> core functionality of the software will be its ability to attempt and transcribe the student’s recordings into written text through the use of the SpeechRecognition python library when retrieving and viewing a recording from the database.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a name=\"docs-internal-guid-7b7bfebb-7fff-5092-a033-c7d0c68be7b2\"></a><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:transparent;\">A</span><span style=\" font-family:\'Arial\'; font-size:11pt; color:#000000; background-color:transparent;\"> core functionality of the software will be its ability to attempt and transcribe the student’s recordings into written text through the use of the SpeechRecognition python library when retrieving and viewing a recording from the database.</span></p></body></html>"))
        self.trans_lbl.setText(_translate("MainWindow", "Attempted Transcription:"))
        self.note_play_btn.setText(_translate("MainWindow", "▶️"))
        self.note_back_btn.setText(_translate("MainWindow", "⬅Back"))
        self.note_delete_btn.setText(_translate("MainWindow", "🗑️Delete"))
        self.note_pause_btn.setText(_translate("MainWindow", "||"))
        self.name_of_file_lbl.setText(_translate("MainWindow", "Name of file"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
