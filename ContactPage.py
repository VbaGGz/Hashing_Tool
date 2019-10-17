# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Contact.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ContactForm(object):
    def setupUi(self, ContactForm):
        ContactForm.setObjectName("ContactForm")
        ContactForm.resize(343, 297)
        ContactForm.setWindowIcon(QtGui.QIcon('Hashing_Tool\Icons\hash.png'))
        self.pushButton = QtWidgets.QPushButton(ContactForm)
        self.pushButton.setGeometry(QtCore.QRect(260, 270, 75, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        self.label_Name = QtWidgets.QLabel(ContactForm)
        self.label_Name.setGeometry(QtCore.QRect(20, 20, 61, 21))
        self.label_Name.setObjectName("label_Name")
        self.TextBox_Name = QtWidgets.QLineEdit(ContactForm)
        self.TextBox_Name.setGeometry(QtCore.QRect(90, 20, 231, 20))
        self.TextBox_Name.setObjectName("TextBox_Name")
        self.label_Email = QtWidgets.QLabel(ContactForm)
        self.label_Email.setGeometry(QtCore.QRect(20, 60, 51, 16))
        self.label_Email.setObjectName("label_Email")
        self.TextBox_Email = QtWidgets.QLineEdit(ContactForm)
        self.TextBox_Email.setGeometry(QtCore.QRect(90, 60, 231, 20))
        self.TextBox_Email.setObjectName("TextBox_Email")
        self.label_Subject = QtWidgets.QLabel(ContactForm)
        self.label_Subject.setGeometry(QtCore.QRect(20, 100, 51, 16))
        self.label_Subject.setObjectName("label_Subject")
        self.NameTextBox_3 = QtWidgets.QLineEdit(ContactForm)
        self.NameTextBox_3.setGeometry(QtCore.QRect(90, 100, 231, 20))
        self.NameTextBox_3.setObjectName("NameTextBox_3")
        self.label = QtWidgets.QLabel(ContactForm)
        self.label.setGeometry(QtCore.QRect(20, 140, 60, 20))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(ContactForm)
        self.textEdit.setGeometry(QtCore.QRect(90, 140, 231, 121))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(ContactForm)
        QtCore.QMetaObject.connectSlotsByName(ContactForm)

    def retranslateUi(self, ContactForm):
        _translate = QtCore.QCoreApplication.translate
        ContactForm.setWindowTitle(_translate("ContactForm", "Contact Me"))
        self.pushButton.setText(_translate("ContactForm", "Send"))
        self.label_Name.setText(_translate("ContactForm", "Name : "))
        self.label_Email.setText(_translate("ContactForm", "Email :"))
        self.label_Subject.setText(_translate("ContactForm", "Subject :"))
        self.label.setText(_translate("ContactForm", "Message :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ContactForm = QtWidgets.QWidget()
    ui = Ui_ContactForm()
    ui.setupUi(ContactForm)
    ContactForm.show()
    sys.exit(app.exec_())
