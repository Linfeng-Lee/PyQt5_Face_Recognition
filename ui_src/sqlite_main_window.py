# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sqlite_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SqliteMainWindow(object):
    def setupUi(self, SqliteMainWindow):
        SqliteMainWindow.setObjectName("SqliteMainWindow")
        SqliteMainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(SqliteMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_table = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_table.setGeometry(QtCore.QRect(30, 30, 120, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox_table.setFont(font)
        self.groupBox_table.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_table.setCheckable(False)
        self.groupBox_table.setObjectName("groupBox_table")
        self.groupBox_field = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_field.setGeometry(QtCore.QRect(170, 30, 120, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox_field.setFont(font)
        self.groupBox_field.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_field.setObjectName("groupBox_field")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 450, 55, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 460, 431, 26))
        self.lineEdit.setObjectName("lineEdit")
        self.tableView_content = QtWidgets.QTableView(self.centralwidget)
        self.tableView_content.setGeometry(QtCore.QRect(320, 60, 301, 281))
        self.tableView_content.setObjectName("tableView_content")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(150, 360, 153, 37))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(680, 170, 84, 94))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_del = QtWidgets.QPushButton(self.widget1)
        self.pushButton_del.setObjectName("pushButton_del")
        self.verticalLayout.addWidget(self.pushButton_del)
        self.pushButton_add = QtWidgets.QPushButton(self.widget1)
        self.pushButton_add.setObjectName("pushButton_add")
        self.verticalLayout.addWidget(self.pushButton_add)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.pushButton_query = QtWidgets.QPushButton(self.widget1)
        self.pushButton_query.setObjectName("pushButton_query")
        self.verticalLayout_2.addWidget(self.pushButton_query)
        SqliteMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SqliteMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        SqliteMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SqliteMainWindow)
        self.statusbar.setObjectName("statusbar")
        SqliteMainWindow.setStatusBar(self.statusbar)
        self.actionOpen_File = QtWidgets.QAction(SqliteMainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.menuFile.addAction(self.actionOpen_File)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(SqliteMainWindow)
        QtCore.QMetaObject.connectSlotsByName(SqliteMainWindow)

    def retranslateUi(self, SqliteMainWindow):
        _translate = QtCore.QCoreApplication.translate
        SqliteMainWindow.setWindowTitle(_translate("SqliteMainWindow", "Sqlite Main Window"))
        self.groupBox_table.setTitle(_translate("SqliteMainWindow", "表"))
        self.groupBox_field.setTitle(_translate("SqliteMainWindow", "字段"))
        self.label.setText(_translate("SqliteMainWindow", "命令"))
        self.radioButton_2.setText(_translate("SqliteMainWindow", "全不选"))
        self.radioButton.setText(_translate("SqliteMainWindow", "全选"))
        self.pushButton_del.setText(_translate("SqliteMainWindow", "删除"))
        self.pushButton_add.setText(_translate("SqliteMainWindow", "添加"))
        self.pushButton_query.setText(_translate("SqliteMainWindow", "查询"))
        self.menuFile.setTitle(_translate("SqliteMainWindow", "File"))
        self.actionOpen_File.setText(_translate("SqliteMainWindow", "Open File"))
