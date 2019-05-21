

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(700, 715)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 20, 631, 606))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 9, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(318, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 8, 0, 1, 4)
        self.connection_list = QtGui.QListWidget(self.layoutWidget)
        self.connection_list.setMaximumSize(QtCore.QSize(16777215, 192))
        self.connection_list.setObjectName(_fromUtf8("connection_list"))
        self.gridLayout.addWidget(self.connection_list, 3, 4, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(348, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 10, 0, 1, 6)
        self.running_status = QtGui.QLabel(self.layoutWidget)
        self.running_status.setText(_fromUtf8(""))
        self.running_status.setObjectName(_fromUtf8("running_status"))
        self.gridLayout.addWidget(self.running_status, 5, 1, 1, 5)
        self.quit_button = QtGui.QPushButton(self.layoutWidget)
        self.quit_button.setObjectName(_fromUtf8("quit_button"))
        self.gridLayout.addWidget(self.quit_button, 11, 5, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(508, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 11, 0, 1, 5)
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.start_button = QtGui.QPushButton(self.layoutWidget)
        self.start_button.setObjectName(_fromUtf8("start_button"))
        self.gridLayout.addWidget(self.start_button, 0, 4, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(318, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 6, 0, 1, 6)
        self.terminal_button = QtGui.QPushButton(self.layoutWidget)
        self.terminal_button.setObjectName(_fromUtf8("terminal_button"))
        self.gridLayout.addWidget(self.terminal_button, 0, 5, 1, 1)
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.input_window = QtGui.QTextEdit(self.layoutWidget)
        self.input_window.setObjectName(_fromUtf8("input_window"))
        self.gridLayout.addWidget(self.input_window, 7, 0, 1, 6)
        self.chat_window = QtGui.QListWidget(self.layoutWidget)
        self.chat_window.setMaximumSize(QtCore.QSize(16777215, 192))
        self.chat_window.setObjectName(_fromUtf8("chat_window"))
        self.gridLayout.addWidget(self.chat_window, 3, 0, 1, 4)
        self.port = QtGui.QLineEdit(self.layoutWidget)
        self.port.setObjectName(_fromUtf8("port"))
        self.gridLayout.addWidget(self.port, 0, 3, 1, 1)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.send_button = QtGui.QPushButton(self.layoutWidget)
        self.send_button.setObjectName(_fromUtf8("send_button"))
        self.gridLayout.addWidget(self.send_button, 8, 5, 1, 1)
        # *** send file button
        self.send_file_button = QtGui.QPushButton(self.layoutWidget)
        self.send_file_button.setObjectName(_fromUtf8("send_file_button"))
        self.gridLayout.addWidget(self.send_file_button, 8, 6, 1, 1)
        # **** end
        self.clear_button = QtGui.QPushButton(self.layoutWidget)
        self.clear_button.setObjectName(_fromUtf8("clear_button"))
        self.gridLayout.addWidget(self.clear_button, 8, 4, 1, 1)
        self.ip = QtGui.QLineEdit(self.layoutWidget)
        self.ip.setObjectName(_fromUtf8("ip"))
        self.gridLayout.addWidget(self.ip, 0, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.layoutWidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 1, 4, 1, 2)
        self.label_6 = QtGui.QLabel(self.layoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 4)
        self.private_chat = QtGui.QComboBox(self.layoutWidget)
        self.private_chat.setObjectName(_fromUtf8("private_chat"))
        self.gridLayout.addWidget(self.private_chat, 9, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        # self.toolBar_2 = QtGui.QToolBar(MainWindow)
        # self.toolBar_2.setObjectName(_fromUtf8("toolBar_2"))
        # MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        # self.toolBar_3 = QtGui.QToolBar(MainWindow)
        # self.toolBar_3.setObjectName(_fromUtf8("toolBar_3"))
        # MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_3)
        # self.toolBar_4 = QtGui.QToolBar(MainWindow)
        # self.toolBar_4.setObjectName(_fromUtf8("toolBar_4"))
        # MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_4)
        # self.toolBar_5 = QtGui.QToolBar(MainWindow)
        # self.toolBar_5.setObjectName(_fromUtf8("toolBar_5"))
        # MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_5)
        # self.toolBar_6 = QtGui.QToolBar(MainWindow)
        # self.toolBar_6.setObjectName(_fromUtf8("toolBar_6"))
        # MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_6)
        # self.toolBar_7 = QtGui.QToolBar(MainWindow)
        # self.toolBar_7.setObjectName(_fromUtf8("toolBar_7"))
        # MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_7)
        # self.toolBar_8 = QtGui.QToolBar(MainWindow)
        # self.toolBar_8.setObjectName(_fromUtf8("toolBar_8"))
        # MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_8)
        # self.toolBar_9 = QtGui.QToolBar(MainWindow)
        # self.toolBar_9.setObjectName(_fromUtf8("toolBar_9"))
        # MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_9)
        # self.toolBar_10 = QtGui.QToolBar(MainWindow)
        # self.toolBar_10.setObjectName(_fromUtf8("toolBar_10"))
        # MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_10)
        # self.toolBar_11 = QtGui.QToolBar(MainWindow)
        # self.toolBar_11.setObjectName(_fromUtf8("toolBar_11"))
        # MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_11)
        # self.toolBar_12 = QtGui.QToolBar(MainWindow)
        # self.toolBar_12.setObjectName(_fromUtf8("toolBar_12"))
        # MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_12)
        # self.toolBar_13 = QtGui.QToolBar(MainWindow)
        # self.toolBar_13.setObjectName(_fromUtf8("toolBar_13"))
        # MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_13)
        # self.toolBar_14 = QtGui.QToolBar(MainWindow)
        # self.toolBar_14.setObjectName(_fromUtf8("toolBar_14"))
        # MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_14)
        # self.toolBar_15 = QtGui.QToolBar(MainWindow)
        # self.toolBar_15.setObjectName(_fromUtf8("toolBar_15"))
        # MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_15)
        # self.toolBar_16 = QtGui.QToolBar(MainWindow)
        # self.toolBar_16.setObjectName(_fromUtf8("toolBar_16"))
        # MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_16)
        # self.toolBar_17 = QtGui.QToolBar(MainWindow)
        # self.toolBar_17.setObjectName(_fromUtf8("toolBar_17"))
        # MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_17)
        # self.toolBar_18 = QtGui.QToolBar(MainWindow)
        # self.toolBar_18.setObjectName(_fromUtf8("toolBar_18"))
        # MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_18)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_2.setText(_translate("MainWindow", "Private chat with", None))
        self.quit_button.setText(_translate("MainWindow", "Quit", None))
        self.label.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.label.setText(_translate("MainWindow", "IP:", None))
        self.start_button.setText(_translate("MainWindow", "Connect", None))
        self.terminal_button.setText(_translate("MainWindow", "Close", None))
        self.label_5.setText(_translate("MainWindow", "Status:", None))
        self.input_window.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_3.setText(_translate("MainWindow", "Port:", None))
        self.send_button.setText(_translate("MainWindow", "Send", None))
        # **send_file button
        self.send_file_button.setText(_translate("MainWindow", "Send file", None))
        # **
        self.clear_button.setText(_translate("MainWindow", "Clear", None))
        self.label_7.setText(_translate("MainWindow", "Connection List", None))
        self.label_6.setText(_translate("MainWindow", "Chat Room", None))
        # self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        # self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2", None))
        # self.toolBar_3.setWindowTitle(_translate("MainWindow", "toolBar_3", None))
        # self.toolBar_4.setWindowTitle(_translate("MainWindow", "toolBar_4", None))
        # self.toolBar_5.setWindowTitle(_translate("MainWindow", "toolBar_5", None))
        # self.toolBar_6.setWindowTitle(_translate("MainWindow", "toolBar_6", None))
        # self.toolBar_7.setWindowTitle(_translate("MainWindow", "toolBar_7", None))
        # self.toolBar_8.setWindowTitle(_translate("MainWindow", "toolBar_8", None))
        # self.toolBar_9.setWindowTitle(_translate("MainWindow", "toolBar_9", None))
        # self.toolBar_10.setWindowTitle(_translate("MainWindow", "toolBar_10", None))
        # self.toolBar_11.setWindowTitle(_translate("MainWindow", "toolBar_11", None))
        # self.toolBar_12.setWindowTitle(_translate("MainWindow", "toolBar_12", None))
        # self.toolBar_13.setWindowTitle(_translate("MainWindow", "toolBar_13", None))
        # self.toolBar_14.setWindowTitle(_translate("MainWindow", "toolBar_14", None))
        # self.toolBar_15.setWindowTitle(_translate("MainWindow", "toolBar_15", None))
        # self.toolBar_16.setWindowTitle(_translate("MainWindow", "toolBar_16", None))
        # self.toolBar_17.setWindowTitle(_translate("MainWindow", "toolBar_17", None))
        # self.toolBar_18.setWindowTitle(_translate("MainWindow", "toolBar_18", None))
