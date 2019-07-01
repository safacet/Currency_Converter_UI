import requests
import sys
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Wndow(object):
    def setupUi(self, Wndow):
        Wndow.setObjectName("Wndow")
        Wndow.resize(324, 350)
        self.pushButton = QtWidgets.QPushButton(Wndow)
        self.pushButton.setGeometry(QtCore.QRect(100, 80, 111, 41))
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setObjectName("pushButton")
        self.result = QtWidgets.QTextBrowser(Wndow)
        self.result.setGeometry(QtCore.QRect(10, 130, 301, 181))
        self.result.setObjectName("result")
        self.to_box = QtWidgets.QComboBox(Wndow)
        self.to_box.setGeometry(QtCore.QRect(210, 30, 71, 21))
        self.to_box.setObjectName("to_box")
        self.to_box.addItem("")
        self.to_box.addItem("")
        self.to_box.addItem("")
        self.to_box.addItem("")
        self.to_box.addItem("")
        self.from_box = QtWidgets.QComboBox(Wndow)
        self.from_box.setGeometry(QtCore.QRect(100, 30, 71, 21))
        self.from_box.setObjectName("from_box")
        self.from_box.addItem("")
        self.from_box.addItem("")
        self.from_box.addItem("")
        self.from_box.addItem("")
        self.from_box.addItem("")
        self.from_text = QtWidgets.QLineEdit(Wndow)
        self.from_text.setGeometry(QtCore.QRect(30, 30, 61, 21))
        self.from_text.setObjectName("from_text")
        self.to_label = QtWidgets.QLabel(Wndow)
        self.to_label.setGeometry(QtCore.QRect(180, 30, 31, 21))
        self.to_label.setObjectName("to_label")

        self.retranslateUi(Wndow)
        QtCore.QMetaObject.connectSlotsByName(Wndow)

        self.pushButton.clicked.connect(self.convert)

    def retranslateUi(self, Wndow):
        _translate = QtCore.QCoreApplication.translate
        Wndow.setWindowTitle(_translate("Wndow", "Currency "))
        self.pushButton.setText(_translate("Wndow", "Convert"))
        self.to_box.setItemText(0, _translate("Wndow", "USD"))
        self.to_box.setItemText(1, _translate("Wndow", "TRY"))
        self.to_box.setItemText(2, _translate("Wndow", "EUR"))
        self.to_box.setItemText(3, _translate("Wndow", "GBP"))
        self.to_box.setItemText(4, _translate("Wndow", "CHF"))
        self.from_box.setItemText(0, _translate("Wndow", "TRY"))
        self.from_box.setItemText(1, _translate("Wndow", "USD"))
        self.from_box.setItemText(2, _translate("Wndow", "EUR"))
        self.from_box.setItemText(3, _translate("Wndow", "GBP"))
        self.from_box.setItemText(4, _translate("Wndow", "CHF"))
        self.to_label.setText(_translate("Wndow", "<html><head/><body><p><span style=\" font-size:18pt;\">To:</span></p></body></html>"))

    def convert(self):
        first_currency = self.from_box.currentText()
        second_currency = self.to_box.currentText()
        amount = int(self.from_text.text())

        url = "http://data.fixer.io/api/latest?access_key=ACCESS_KEY&symbols="

        url2 = url + first_currency + "," + second_currency

        response = requests.get(url2)
        jsonlist = response.json()
        now = datetime.now()
        update_time = datetime.fromtimestamp(jsonlist["timestamp"])
        passing_time = now - update_time
        passing_hour, rem = divmod(passing_time.total_seconds(), 3600)
        passing_min, passing_sec = divmod(rem, 60)
        text ="Currency data update time:" + datetime.strftime(update_time, "%d %B %Y %A %X") + "\n"
        text = text + "Passing time from last update: {:02.0f}:{:02.0f}:{:02.0f}\n".format(passing_hour, passing_min, passing_sec)
        result = (jsonlist["rates"][second_currency] / jsonlist["rates"][first_currency]) * amount
        text = text + "Your amount: {:.2f} {}".format(result, second_currency)
        self.result.setText(text)





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Wndow = QtWidgets.QWidget()
    ui = Ui_Wndow()
    ui.setupUi(Wndow)
    Wndow.show()
    sys.exit(app.exec_())

