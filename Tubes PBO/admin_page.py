from __future__ import annotations
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import mysql.connector as mc
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_admin_page(object):
    def setupUiAdminPage(self, admin_page):
        admin_page.setObjectName("admin_page")
        admin_page.resize(741, 442)
        admin_page.setStyleSheet("background-color: rgb(117, 177, 124);")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(admin_page)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(admin_page)
        self.label.setStyleSheet("background-color: rgb(72, 213, 11);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.line = QtWidgets.QFrame(admin_page)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(admin_page)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(428, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget_admin_page = QtWidgets.QTableWidget(admin_page)
        self.tableWidget_admin_page.setObjectName("tableWidget_admin_page")
        self.tableWidget_admin_page.setColumnCount(13)
        self.tableWidget_admin_page.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_admin_page.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_admin_page.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_admin_page.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_admin_page.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_admin_page.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_admin_page.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_admin_page.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_admin_page.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_admin_page.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_admin_page.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_admin_page.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_admin_page.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_admin_page.setHorizontalHeaderItem(12, item)

        self.verticalLayout.addWidget(self.tableWidget_admin_page)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(458, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.btn_refresh_admin_page = QtWidgets.QPushButton(admin_page)
        self.btn_refresh_admin_page.setStyleSheet("background-color: rgb(43, 206, 255);\n"
"font: 8pt \"MS Reference Sans Serif\";\n"
"")
        self.btn_refresh_admin_page.setObjectName("btn_refresh_admin_page")
        self.btn_refresh_admin_page.clicked.connect(self.refresh)

        self.horizontalLayout_2.addWidget(self.btn_refresh_admin_page)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.label_3 = QtWidgets.QLabel(admin_page)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        spacerItem3 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.lineEdit_no_antrian = QtWidgets.QLineEdit(admin_page)
        self.lineEdit_no_antrian.setObjectName("lineEdit_no_antrian")
        self.horizontalLayout_4.addWidget(self.lineEdit_no_antrian)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem5 = QtWidgets.QSpacerItem(646, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.btn_terima_kunjungan = QtWidgets.QPushButton(admin_page)
        self.btn_terima_kunjungan.setStyleSheet("background-color: rgb(171, 171, 171);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 9pt \"Century Gothic\";")
        self.btn_terima_kunjungan.setObjectName("btn_terima_kunjungan")
        self.btn_terima_kunjungan.clicked.connect(self.terimaKunjungan)

        self.horizontalLayout_3.addWidget(self.btn_terima_kunjungan)
        spacerItem7 = QtWidgets.QSpacerItem(98, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.btn_tolak_kunjungan = QtWidgets.QPushButton(admin_page)
        self.btn_tolak_kunjungan.setStyleSheet("background-color: rgb(171, 171, 171);\n"
        "font: 75 8pt \"MS Shell Dlg 2\";\n"
        "font: 9pt \"Century Gothic\";")
        self.btn_tolak_kunjungan.setObjectName("btn_tolak_kunjungan")
        self.horizontalLayout_3.addWidget(self.btn_tolak_kunjungan)
        self.btn_tolak_kunjungan.clicked.connect(self.tolakKunjungan)

        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(admin_page)
        QtCore.QMetaObject.connectSlotsByName(admin_page)

    def retranslateUi(self, admin_page):
        _translate = QtCore.QCoreApplication.translate
        admin_page.setWindowTitle(_translate("admin_page", "Form"))
        self.label.setText(_translate("admin_page", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Selamat Datang</span></p></body></html>"))
        self.label_2.setText(_translate("admin_page", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Daftar Pengunjung</span></p></body></html>"))
        item = self.tableWidget_admin_page.horizontalHeaderItem(0)
        item.setText(_translate("admin_page", "Antrian"))
        item = self.tableWidget_admin_page.horizontalHeaderItem(1)
        item.setText(_translate("admin_page", "Nama"))
        item = self.tableWidget_admin_page.horizontalHeaderItem(2)
        item.setText(_translate("admin_page", "NIP/NIM"))
        item = self.tableWidget_admin_page.horizontalHeaderItem(3)
        item.setText(_translate("admin_page", "Prodi"))
        item = self.tableWidget_admin_page.horizontalHeaderItem(4)
        item.setText(_translate("admin_page", "Alamat"))
        item = self.tableWidget_admin_page.horizontalHeaderItem(5)
        item.setText(_translate("admin_page", "Lokasi Kunjungan"))
        item = self.tableWidget_admin_page.horizontalHeaderItem(6)
        item.setText(_translate("admin_page", "Alasan Datang"))
        item = self.tableWidget_admin_page.horizontalHeaderItem(7)
        item.setText(_translate("admin_page", "Suhu Tubuh"))
        item = self.tableWidget_admin_page.horizontalHeaderItem(8)
        item.setText(_translate("admin_page", "Waktu Kunjungan"))
        item = self.tableWidget_admin_page.horizontalHeaderItem(9)
        item.setText(_translate("admin_page", "Status"))
        item = self.tableWidget_admin_page.horizontalHeaderItem(10)
        item.setText(_translate("admin_page", "Status Kunjungan"))
        item = self.tableWidget_admin_page.horizontalHeaderItem(11)
        item.setText(_translate("admin_page", "Waktu Cek In"))
        item = self.tableWidget_admin_page.horizontalHeaderItem(12)
        item.setText(_translate("admin_page", "Waktu Cek Out"))
        self.btn_refresh_admin_page.setText(_translate("admin_page", "Refresh"))
        self.label_3.setText(_translate("admin_page", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Masukkan No Antiran : </span></p></body></html>"))
        self.btn_terima_kunjungan.setText(_translate("admin_page", "Terima Kunjungan"))
        self.btn_tolak_kunjungan.setText(_translate("admin_page", "Tolak Kunjungan"))

    def show_data_updated(self):
        message = QMessageBox()
        message.setWindowTitle('Info')
        message.setText('Data telah diupdate, Tekan refresh')
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

        query = "SELECT *  FROM pengunjung"
        mycursor.execute(query)
        result = mycursor.fetchall()

        self.tableWidget_admin_page.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget_admin_page.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_admin_page.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        mydb.close()

    def terimaKunjungan(self):
        no_antrian = self.lineEdit_no_antrian.text()

        mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='gerbang_itk'
        )

        mycursor = mydb.cursor()
        query = "UPDATE pengunjung SET status = 'Disetujui' WHERE antrian = CONVERT(" + no_antrian + ",int)"
        mycursor.execute(query)
        mydb.commit()
        mydb.close()

        self.show_data_updated()

    def tolakKunjungan(self):
        no_antrian = self.lineEdit_no_antrian.text()

        mydb = mc.connect(
            host='localhost',
            user='root',
            password='',
            database='gerbang_itk'
        )

        mycursor = mydb.cursor()
        query = "UPDATE pengunjung SET status = 'Ditolak' WHERE antrian = CONVERT(" + no_antrian + ",int)"
        mycursor.execute(query)
        mydb.commit()
        mydb.close()

        self.show_data_updated()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    admin_page = QtWidgets.QWidget()
    ui = Ui_admin_page()
    ui.setupUiAdminPage(admin_page)
    admin_page.show()
    sys.exit(app.exec_())
