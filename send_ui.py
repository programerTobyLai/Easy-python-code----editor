# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Toby\Desktop\toolbox\Easy Python Code (beta)\mail\send.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets,QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(834, 951)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../img/main.png")), QtGui.QIcon.Normal,QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.sender = QtWidgets.QLineEdit(self.widget)
        self.sender.setInputMask(_fromUtf8(""))
        self.sender.setFrame(False)
        self.sender.setDragEnabled(True)
        self.sender.setObjectName(_fromUtf8("sender"))
        self.gridLayout_2.addWidget(self.sender, 0, 1, 1, 4)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.password = QtWidgets.QLineEdit(self.widget)
        self.password.setFrame(False)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName(_fromUtf8("password"))
        self.gridLayout_2.addWidget(self.password, 1, 1, 1, 4)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.smtp_name = QtWidgets.QLineEdit(self.widget)
        self.smtp_name.setFrame(False)
        self.smtp_name.setObjectName(_fromUtf8("smtp_name"))
        self.gridLayout_2.addWidget(self.smtp_name, 2, 1, 1, 4)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)
        self.to = QtWidgets.QLineEdit(self.widget)
        self.to.setFrame(False)
        self.to.setObjectName(_fromUtf8("to"))
        self.gridLayout_2.addWidget(self.to, 3, 1, 1, 4)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 4, 0, 1, 1)
        self.subject = QtWidgets.QLineEdit(self.widget)
        self.subject.setFrame(False)
        self.subject.setObjectName(_fromUtf8("subject"))
        self.gridLayout_2.addWidget(self.subject, 4, 1, 1, 4)
        self.text = QtWidgets.QPlainTextEdit(self.widget)
        self.text.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.text.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.text.setTabChangesFocus(False)
        self.text.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.text.setOverwriteMode(True)
        self.text.setCenterOnScroll(True)
        self.text.setObjectName(_fromUtf8("text"))
        self.gridLayout_2.addWidget(self.text, 5, 0, 1, 5)
        spacerItem = QtWidgets.QSpacerItem(249, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 6, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(124, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 6, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(125, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 6, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(124, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 6, 3, 1, 1)
        self.send_btn = QtWidgets.QPushButton(self.widget)
        self.send_btn.setObjectName(_fromUtf8("send_btn"))
        self.gridLayout_2.addWidget(self.send_btn, 6, 4, 1, 1)
        self.gridLayout.addWidget(self.widget, 11, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 834, 30))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "send E-mail", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">发送人：</span></p></body></html>", None))
        self.sender.setPlaceholderText(_translate("MainWindow", "xxx@xxx.com", None))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">授权码：</span></p></body></html>", None))
        self.password.setPlaceholderText(_translate("MainWindow", "授权码", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">发送人SMTP服务器：</span></p></body></html>", None))
        self.smtp_name.setPlaceholderText(_translate("MainWindow", "smtp.xxx.com", None))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">收件人：</span></p></body></html>", None))
        self.to.setPlaceholderText(_translate("MainWindow", "xxx@xxx.com", None))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">标题：</span></p></body></html>", None))
        self.subject.setPlaceholderText(_translate("MainWindow", "标题", None))
        self.send_btn.setText(_translate("MainWindow", "发送", None))

