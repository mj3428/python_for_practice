# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'latorwho.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QMessageBox
import sys
import pandas as pd
import datetime as dt

df = pd.read_excel('./Sept_res.xlsx')

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(541, 478)
        self.calendarWidget = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 10, 248, 197))
        self.calendarWidget.setObjectName("calendarWidget")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(10, 210, 521, 251))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(260, 70, 121, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(270, 40, 171, 31))
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 70, 121, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)

        self.calendarWidget.clicked['QDate'].connect(self.showdate)
        self.pushButton_2.clicked.connect(self.logging_lator)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "按月查询"))
        self.label.setText(_translate("Form", "查询年月:"+str(self.calendarWidget.selectedDate().year()) + '年' +
                                      str(self.calendarWidget.selectedDate().month()) + '月'))
        self.pushButton_2.setText(_translate("Form", "按日查询"))

    def showdate(self):
        self.label.setText("查询年月:"+str(self.calendarWidget.selectedDate().year()) + '年' +
                                      str(self.calendarWidget.selectedDate().month()) + '月')
    def logging_lator(self):
        qdate = self.calendarWidget.selectedDate()
        qdate_str = qdate.toString('yyyy-MM-dd')
        self.textEdit.clear()
        self.textEdit.setText('查询日期:' + qdate_str + '\n日期类型为'+
                              str(type(dt.datetime(qdate.year(),qdate.month(),qdate.day()))))
        # self.textEdit.append(str(df['日期时间'].dtypes))
        if dt.datetime(qdate.year(),qdate.month(),qdate.day()) in df['日期时间'].to_list():
            today = df.loc[df['日期时间'] == dt.datetime(qdate.year(),qdate.month(),qdate.day())]
            today = today.reset_index(drop=True)
            self.textEdit.append('Yes!!'+'\n')
            for i in range(0, len(today)):
                self.textEdit.append(today.loc[today.index[i], '姓名']+ ', 早上上班:'+today.loc[today.index[i], '早上上班']
                       + ', 中午下班:' + today.loc[today.index[i], '中午下班'] + ', 下午上班:' +
                    today.loc[today.index[i], '下午上班'] + ', 下午下班:' + today.loc[today.index[i], '下午下班'] + '\n')
        else:
            self.textEdit.append('无数据，请导入!!'+'\n')



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
