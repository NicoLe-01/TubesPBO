from __future__ import annotations
from PyQt5 import QtCore, QtGui, QtWidgets
import form_pengajuan
import login
from PyQt5.QtWidgets import QMessageBox

import mysql.connector as mc
# from PyQt5.QtWidgets import QTableWidgetItem

global user


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_home_page(object):

    def openFormPengajuanFromHomePage(self):
        self.form_pengajuan = QtWidgets.QWidget()
        self.ui = form_pengajuan.Ui_form_pengajuan()
        self.ui.setupUiFormPengajuan(self.form_pengajuan)
        self.form_pengajuan.show()



    def setupUiHomePage(self, home_page):
        home_page.setObjectName("home_page")
        home_page.resize(617, 468)
        home_page.setStyleSheet("background-color: rgb(117, 177, 124);")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(home_page)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(home_page)
        self.label.setStyleSheet("background-color: rgb(72, 213, 11);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.line = QtWidgets.QFrame(home_page)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(home_page)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(428, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.splitter = QtWidgets.QSplitter(home_page)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.tableWidget_home_page = QtWidgets.QTableWidget(self.splitter)
        self.tableWidget_home_page.setStyleSheet("font: 75 8pt \"Arial\";")
        self.tableWidget_home_page.setObjectName("tableWidget_home_page")
        self.tableWidget_home_page.setColumnCount(4)
        self.tableWidget_home_page.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.tableWidget_home_page.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_home_page.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_home_page.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_home_page.setHorizontalHeaderItem(3, item)
        self.label_status_home_page = QtWidgets.QLabel(self.splitter)
        self.label_status_home_page.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status_home_page.setWordWrap(True)
        self.label_status_home_page.setObjectName("label_status_home_page")
        self.verticalLayout_4.addWidget(self.splitter)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(458, 28, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.btn_refresh_home_page = QtWidgets.QPushButton(home_page)
        self.btn_refresh_home_page.setStyleSheet("background-color: rgb(43, 206, 255);\n"
"font: 8pt \"MS Reference Sans Serif\";\n"
"")
        self.btn_refresh_home_page.setObjectName("btn_refresh_home_page")
        self.btn_refresh_home_page.clicked.connect(self.refresh)

        self.horizontalLayout_2.addWidget(self.btn_refresh_home_page)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.label_3 = QtWidgets.QLabel(home_page)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        spacerItem4 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.lineEdit_no_antrian = QtWidgets.QLineEdit(home_page)
        self.lineEdit_no_antrian.setObjectName("lineEdit_no_antrian")
        self.horizontalLayout.addWidget(self.lineEdit_no_antrian)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem6 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem7 = QtWidgets.QSpacerItem(38, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.btn_cekin = QtWidgets.QPushButton(home_page)
        self.btn_cekin.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.914182, y1:0.955, x2:1, y2:1, stop:0 rgba(216, 188, 188, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.btn_cekin.setObjectName("btn_cekin")
        self.btn_cekin.clicked.connect(self.cekIn)

        self.horizontalLayout_4.addWidget(self.btn_cekin)
        spacerItem8 = QtWidgets.QSpacerItem(68, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.btn_cekout = QtWidgets.QPushButton(home_page)
        self.btn_cekout.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.914182, y1:0.955, x2:1, y2:1, stop:0 rgba(216, 188, 188, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.btn_cekout.setObjectName("btn_cekout")
        self.horizontalLayout_4.addWidget(self.btn_cekout)
        self.btn_cekout.clicked.connect(self.cekOut)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        spacerItem10 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem10)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem11)
        self.btn_ajukan_kunjungan = QtWidgets.QPushButton(home_page)
        self.btn_ajukan_kunjungan.setStyleSheet("background-color: rgb(171, 171, 171);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 9pt \"Century Gothic\";")
        self.btn_ajukan_kunjungan.setObjectName("btn_ajukan_kunjungan")
        self.btn_ajukan_kunjungan.clicked.connect(self.openFormPengajuanFromHomePage)

        self.horizontalLayout_3.addWidget(self.btn_ajukan_kunjungan)
        spacerItem12 = QtWidgets.QSpacerItem(78, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem12)
        self.btn_batalkan_kunjungan = QtWidgets.QPushButton(home_page)
        self.btn_batalkan_kunjungan.setStyleSheet("background-color: rgb(171, 171, 171);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 9pt \"Century Gothic\";")
        self.btn_batalkan_kunjungan.setObjectName("btn_batalkan_kunjungan")
        self.btn_batalkan_kunjungan.clicked.connect(self.batalkanKunjungan)
        self.horizontalLayout_3.addWidget(self.btn_batalkan_kunjungan)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem13)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.retranslateUi(home_page)
        QtCore.QMetaObject.connectSlotsByName(home_page)

    def retranslateUi(self, home_page):
        _translate = QtCore.QCoreApplication.translate
        home_page.setWindowTitle(_translate("home_page", "Form"))
        self.label.setText(_translate("home_page", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Selamat Datang di Gerbang ITK</span></p></body></html>"))
        self.label_2.setText(_translate("home_page", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Daftar Kunjungan </span></p></body></html>"))
        item = self.tableWidget_home_page.horizontalHeaderItem(0)
        item.setText(_translate("home_page", "Antrian"))
        item = self.tableWidget_home_page.horizontalHeaderItem(1)
        item.setText(_translate("home_page", "Nama"))
        item = self.tableWidget_home_page.horizontalHeaderItem(2)
        item.setText(_translate("home_page", "Prodi"))
        item = self.tableWidget_home_page.horizontalHeaderItem(3)
        item.setText(_translate("home_page", "Status"))
        self.label_status_home_page.setText(_translate("home_page", "<html><head/><body><p><span style=\" font-weight:600;\">Status </span></p></body></html>"))
        self.btn_refresh_home_page.setText(_translate("home_page", "Refresh"))
        self.label_3.setText(_translate("home_page", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Masukkan No Antiran : </span></p></body></html>"))
        self.btn_cekin.setText(_translate("home_page", "Cek In"))
        self.btn_cekout.setText(_translate("home_page", "Cek Out"))
        self.btn_ajukan_kunjungan.setText(_translate("home_page", "Ajukan Kunjungan"))
        self.btn_batalkan_kunjungan.setText(_translate("home_page", "Batalkan Kunjungan"))


    def show_error_connetion(self):
        message = QMessageBox()
        message.setWindowTitle("Error")
        message.setText('Connection to database failed')
        message.setIcon(QMessageBox.Critical)
        x = message.exec_()

    def show_message_cekIn(self):
        message = QMessageBox()
        message.setWindowTitle('Info')
        message.setText('Data telah diterima, Jangan lupa Cek Out ya ')
        message.setIcon(QMessageBox.Information)
        message.exec_()

    def show_message_KunjunganBatal(self):
        message = QMessageBox()
        message.setWindowTitle('Info')
        message.setText('Kunjungan telah dibatalkan, silahkan tekan refresh')
        message.setIcon(QMessageBox.Information)
        message.exec_()

    def show_message_cekOut(self):
        message = QMessageBox()
        message.setWindowTitle('Info')
        message.setText('Data telah diterima, Hati-hati di jalan :)')
        message.setIcon(QMessageBox.Information)
        message.exec_()



    def refresh(self):
        mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='gerbang_itk'
        )

        mycursor = mydb.cursor()

        query = "SELECT antrian, nama, prodi, status FROM pengunjung"
        mycursor.execute(query)
        result = mycursor.fetchall()

        self.tableWidget_home_page.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget_home_page.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_home_page.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))



    def batalkanKunjungan(self):
        no_antrian = self.lineEdit_no_antrian.text()


        try:
            mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='gerbang_itk'
            )

            mycursor = mydb.cursor()
            query = "DELETE FROM pengunjung WHERE antrian = CONVERT("+ no_antrian +",int)"
            mycursor.execute(query)
            mydb.commit()
            mydb.close()

            self.show_message_KunjunganBatal()
            self.label_status_home_page.setText('Kunjungan telah dibatalkan')


        except mc.Error as e:
            self.show_error_connetion()

    def cekIn(self):
        no_antrian = self.lineEdit_no_antrian.text()
        try:
            mydb = mc.connect(
                host='localhost',
                user='root',
                password='',
                database='gerbang_itk'
            )

            mycursor = mydb.cursor()
            query = "UPDATE pengunjung SET status_kunjungan = 'Cek In', waktu_cek_in = CURRENT_TIMESTAMP WHERE antrian = CONVERT(" + no_antrian + ",int)"
            mycursor.execute(query)
            mydb.commit()
            mydb.close()

            self.label_status_home_page.setText("Anda telah Cek In")
            self.show_message_cekIn()

        except:
            self.show_error_connetion()

    def cekOut(self):
        no_antrian = self.lineEdit_no_antrian.text()
        try:
            mydb = mc.connect(
                host='localhost',
                user='root',
                password='',
                database='gerbang_itk'
            )

            mycursor = mydb.cursor()
            query = "UPDATE pengunjung SET status_kunjungan = 'Cek Out', waktu_cek_out = CURRENT_TIMESTAMP WHERE antrian = CONVERT(" + no_antrian + ",int)"
            mycursor.execute(query)
            mydb.commit()
            mydb.close()

            self.label_status_home_page.setText("Anda telah Cek Out")
            self.show_message_cekOut()

        except:
            pass
            # self.show_error_connetion()







if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    home_page = QtWidgets.QWidget()
    ui = Ui_home_page()
    ui.setupUiHomePage(home_page)
    home_page.show()
    sys.exit(app.exec_())
