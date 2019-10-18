import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from AboutPage import Ui_About_Page
from ContactPage import Ui_ContactForm

CURRENTVERSION = 1.2

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(496, 206)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setWindowIcon(QtGui.QIcon('Hashing_Tool\Icons\hash.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(90, 20, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Sha1")
        self.comboBox.addItem("Sha256")
        self.comboBox.addItem("Sha512")
        self.comboBox.addItem("Sha384")
        self.Status_label = QtWidgets.QLabel(self.centralwidget)
        self.Status_label.setGeometry(QtCore.QRect(175, 20, 200, 22))
        self.Status_label.setObjectName("Status_label")
        self.Status_label.setText("Chose A File")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(16, 21, 61, 20))
        self.label.setObjectName("label")
        self.label_Path = QtWidgets.QLabel(self.centralwidget)
        self.label_Path.setGeometry(QtCore.QRect(20, 60, 451, 31))
        self.label_Path.setText("")
        self.label_Path.setObjectName("label_Path")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 110, 61, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(90, 110, 61, 23))
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(QtCore.QRect(160, 110, 61, 23))
        self.pushButton3.setObjectName("pushButton3")
        self.HashOutput = QtWidgets.QLineEdit(self.centralwidget)
        self.HashOutput.setGeometry(QtCore.QRect(20, 140, 401, 20))
        self.HashOutput.setReadOnly(True)
        self.HashOutput.setObjectName("HashOutput")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(430, 140, 61, 20))
        self.toolButton.setObjectName("toolButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 496, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuhelp = QtWidgets.QMenu(self.menubar)
        self.menuhelp.setObjectName("menuhelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionCheck_for_Updates = QtWidgets.QAction(MainWindow)
        self.actionCheck_for_Updates.setObjectName("actionCheck_for_Updates")
        self.actionContact_Me = QtWidgets.QAction(MainWindow)
        self.actionContact_Me.setObjectName("actionContact_Me")
        self.menuFile.addAction(self.actionAbout)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuhelp.addAction(self.actionCheck_for_Updates)
        self.menuhelp.addAction(self.actionContact_Me)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HashingTool"))
        self.pushButton.clicked.connect(self.openFileNameDialog)
        self.comboBox.setItemText(0, _translate("MainWindow", "Sha1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Sha256"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Sha512"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Sha384"))
        self.label.setText(_translate("MainWindow", "Hash Type"))
        self.pushButton.setText(_translate("MainWindow", "Browse"))
        self.pushButton2.setText(_translate("MainWindow", "Hash"))
        self.pushButton3.setText(_translate("MainWindow", "Clear"))
        self.pushButton2.clicked.connect(self.Hash)
        self.pushButton3.clicked.connect(self.clear)
        self.toolButton.setText(_translate("MainWindow", "Copy"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuhelp.setTitle(_translate("MainWindow", "help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.triggered.connect(QtWidgets.qApp.quit)
        self.actionCheck_for_Updates.setText(_translate("MainWindow", "Check for Updates"))
        self.actionContact_Me.setText(_translate("MainWindow", "Contact Me"))

    def clear(self):
        self.Status_label.setText("Chose A File")
        self.HashOutput.setText("")
        self.label_Path.setText("")

    def Copy(self):
        if not self.HashOutput.text() == "":
            from clipboard import copy
            copy(self.HashOutput.text())
            self.Status_label.setText("Hash Copied")
        else:
            self.Status_label.setText("Nothing To Copy Hash File First")

    def Hash(self):
        import hashlib
        hashed = False
        if not self.label_Path.text() == "":
            if self.comboBox.currentIndex() == 0:
                hasher = hashlib.sha1()
                with open(self.label_Path.text(), 'rb') as file:
                    buf = file.read()
                    hasher.update(buf)
                self.HashOutput.setText(hasher.hexdigest().upper())
                hashed = True
            elif self.comboBox.currentIndex() == 1:
                hasher = hashlib.sha256()
                with open(self.label_Path.text(), 'rb') as file:
                    buf = file.read()
                    hasher.update(buf)
                self.HashOutput.setText(hasher.hexdigest().upper())
                hashed = True
            elif self.comboBox.currentIndex() == 2:
                hasher = hashlib.sha512()
                with open(self.label_Path.text(), 'rb') as file:
                    buf = file.read()
                    hasher.update(buf)
                self.HashOutput.setText(hasher.hexdigest().upper())
                hashed = True
            elif self.comboBox.currentIndex() == 3:
                hasher = hashlib.sha384()
                with open(self.label_Path.text(), 'rb') as file:
                    buf = file.read()
                    hasher.update(buf)
                self.HashOutput.setText(hasher.hexdigest().upper())
                hashed = True
        else :
            self.Status_label.setText("Chose A File To Hash")
        if hashed:
            self.Status_label.setText("Hashed")

    def openFileNameDialog(self)-> str: 
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(
            None, "QFileDialog.getOpenFileName()", "", "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            self.label_Path.setText(fileName)
            self.Status_label.setText("Ready To Hash!")
        return fileName

    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(
            self, "QFileDialog.getOpenFileNames()", "", "All Files (*);;Python Files (*.py)", options=options)
        if files:
            print(files)

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(
            self, "QFileDialog.getSaveFileName()", "", "All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)

    def checkForUpdates(self):
        import urllib.request
        box = QMessageBox()
        print('Beginning file download')
        url = "https://raw.githubusercontent.com/VbaGGz/Hashing_Tool/master/TEMP/VERSION.txt"
        urllib.request.urlretrieve(url, "Hashing_Tool\TEMP\VERSION.txt")
        with open("Hashing_Tool\TEMP\VERSION.txt", 'r') as file:
            line = file.read()
            if CURRENTVERSION >= float(line):
                box.setWindowTitle("Update Check")
                box.setWindowIcon(QtGui.QIcon('Hashing_Tool\Icons\hash.png'))
                box.setText("Your software is up to date!")
                box.exec_()
            else:
                box.setWindowTitle("Update Check")
                box.setWindowIcon(QtGui.QIcon('Hashing_Tool\Icons\hash.png'))
                box.setText("There is an Update Download at https://github.com/VbaGGz/Hashing_Tool")
                box.exec_()

def buttonTriggers(object,About_Page):
    object.actionAbout.triggered.connect(About_Page.show)

    
def App_SetUp():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    About_Page = QtWidgets.QWidget()
    Contact_Page = QtWidgets.QWidget()
    Contact_ui = Ui_ContactForm()
    About_ui = Ui_About_Page()
    ui = Ui_MainWindow()

    ui.setupUi(MainWindow)
    About_ui.setupUi(About_Page)
    Contact_ui.setupUi(Contact_Page)
    ui.actionContact_Me.triggered.connect(Contact_Page.show)
    ui.actionAbout.triggered.connect(About_Page.show)
    ui.toolButton.clicked.connect(ui.Copy)
    ui.actionCheck_for_Updates.triggered.connect(ui.checkForUpdates)

    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    App_SetUp()
    pass
