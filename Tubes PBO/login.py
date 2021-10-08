from __future__ import annotations
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import mysql.connector as mc
import home_page
import admin_page
# from home_page import Ui_home_page
# from admin_page import Ui_admin_page


global user

class Ui_login(object):

    def openHomePage(self):
        self.home_page = QtWidgets.QWidget()
        self.ui = home_page.Ui_home_page()
        self.ui.setupUiHomePage(self.home_page)
        self.home_page.show()
        user = self.lineEdit_login_nim_nip.getTextMargins()
        login.hide()

    def openAdminPage(self):
        self.admin_page = QtWidgets.QWidget()
        self.ui = admin_page.Ui_admin_page()
        self.ui.setupUiAdminPage(self.admin_page)
        self.admin_page.show()
        login.hide()

    def setupUiLogin(self, login):
        login.setObjectName("login")
        login.resize(548, 357)
        login.setStyleSheet("background-color: rgb(117, 177, 124);")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(login)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(login)
        self.label.setStyleSheet("background-color: rgb(72, 213, 11);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.line = QtWidgets.QFrame(login)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        spacerItem2 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(login)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.lineEdit_login_nim_nip = QtWidgets.QLineEdit(login)
        self.lineEdit_login_nim_nip.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.lineEdit_login_nim_nip.setObjectName("lineEdit_login_nim_nip")
        self.horizontalLayout.addWidget(self.lineEdit_login_nim_nip)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(login)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.lineEdit_login_password = QtWidgets.QLineEdit(login)
        self.lineEdit_login_password.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.lineEdit_login_password.setInputMethodHints(QtCore.Qt.ImhDialableCharactersOnly|QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhEmailCharactersOnly|QtCore.Qt.ImhExclusiveInputMask|QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhLatinOnly|QtCore.Qt.ImhLowercaseOnly|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData|QtCore.Qt.ImhUppercaseOnly|QtCore.Qt.ImhUrlCharactersOnly)
        self.lineEdit_login_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_login_password.setObjectName("lineEdit_login_password")
        self.horizontalLayout_2.addWidget(self.lineEdit_login_password)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(login)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        spacerItem7 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.comboBox_user_type = QtWidgets.QComboBox(login)
        self.comboBox_user_type.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.comboBox_user_type.setObjectName("comboBox_user_type")
        self.comboBox_user_type.addItem("")
        self.comboBox_user_type.addItem("")
        self.comboBox_user_type.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_user_type)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem8)
        self.btn_login = QtWidgets.QPushButton(login)
        self.btn_login.setStyleSheet("background-color: rgb(124, 124, 124);")
        self.btn_login.setObjectName("btn_login")

        self.btn_login.clicked.connect(self.login)

        self.verticalLayout_4.addWidget(self.btn_login)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem9)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem10)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)





    def show_error_connetion(self):
        message = QMessageBox()
        message.setWindowTitle("Error")
        message.setText('Connection to database failed')
        message.setIcon(QMessageBox.Critical)
        x = message.exec_()

    def show_error_username_password(self):
        message = QMessageBox()
        message.setWindowTitle('Error')
        message.setText('NIP/NIM/Password salah')
        message.setIcon(QMessageBox.Information)
        x = message.exec_()

    def login(self):
        try:
            mydb = mc.connect(
                host='localhost',
                user='root',
                password='',
                database='gerbang_itk'

            )

            user = self.lineEdit_login_nim_nip.text()
            passwordline = self.lineEdit_login_password.text()
            user_type = self.comboBox_user_type.currentText()

            cursor_login = mydb.cursor()

            if user_type == 'user':
                query_mahasiswa = "SELECT * FROM mahasiswa WHERE login = " + "'" + user + "'" + " and password = " + "'" + passwordline + "'" ""

                cursor_login.execute(query_mahasiswa)

                result_mahasiswa = cursor_login.fetchone()
                if result_mahasiswa != None:
                    self.openHomePage()
                    user = self.lineEdit_login_nim_nip.text()

                else:
                    self.show_error_username_password()

            elif user_type == 'dosen':
                query_dosen = "SELECT * FROM dosen WHERE login = " + "'" + user + "'" + " and password = " + "'" + passwordline + "'" ""

                cursor_login.execute(query_dosen)
                result_dosen = cursor_login.fetchone()
                if result_dosen != None:
                    self.openHomePage()
                    user = self.lineEdit_login_nim_nip.text()
                else:
                    self.show_error_username_password()

            elif user_type == 'admin':
                query_admin = "SELECT * FROM admin WHERE login = " + "'" + user + "'" + " and password = " + "'" + passwordline + "'" ""
                cursor_login.execute(query_admin)
                result_admin = cursor_login.fetchone()
                if result_admin != None:
                    self.openAdminPage()
                else:
                    self.show_error_username_password()

            else:
                self.show_error_username_password()

            mydb.close()

        except mc.Error as e:
            self.show_error_connetion()















    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Form"))
        self.label.setText(_translate("login", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Gerbang ITK</span></p></body></html>"))
        self.label_2.setText(_translate("login", "<html><head/><body><p><span style=\" font-weight:600;\">NIP/NIM</span></p></body></html>"))
        self.label_3.setText(_translate("login", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Password</span></p></body></html>"))
        self.label_4.setText(_translate("login", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Login As</span></p></body></html>"))
        self.comboBox_user_type.setItemText(0, _translate("login", "user"))
        self.comboBox_user_type.setItemText(1, _translate("login", "dosen"))
        self.comboBox_user_type.setItemText(2, _translate("login", "admin"))
        self.btn_login.setText(_translate("login", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = QtWidgets.QWidget()
    ui = Ui_login()
    ui.setupUiLogin(login)
    login.show()
    sys.exit(app.exec_())
