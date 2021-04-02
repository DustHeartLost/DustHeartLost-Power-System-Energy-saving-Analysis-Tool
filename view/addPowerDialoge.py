from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt


class AddPowerDialoge(QtWidgets.QDialog):
    def __init__(self,MainWindow):
        QtWidgets.QWidget.__init__(self)
        self.mainWindow=MainWindow
        self.setObjectName("Dialog")
        self.resize(333, 224)
        self.setWindowTitle("添加")
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(60, 170, 251, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 301, 141))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 60, 72, 15))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(100, 60, 191, 21))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 72, 15))
        self.label_2.setObjectName("label_2")
        self.ID = QtWidgets.QLabel(self.groupBox)
        self.ID.setGeometry(QtCore.QRect(100, 100, 72, 15))
        self.ID.setObjectName("ID")

        self.retranslateUi()
        self.comboBox.setCurrentIndex(0)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.comboBox.currentIndexChanged['int'].connect(self.ID.setNum)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "请选择添加的机组型式"))
        self.label.setText(_translate("Dialog", "机组型式:"))
        self.comboBox.setItemText(0, _translate("Dialog", "1000MW级超超临界湿冷"))
        self.comboBox.setItemText(1, _translate("Dialog", "1000MW级超超临界空冷"))
        self.comboBox.setItemText(2, _translate("Dialog", "600MW级超超临界湿冷"))
        self.comboBox.setItemText(3, _translate("Dialog", "600MW级超超临界空冷"))
        self.comboBox.setItemText(4, _translate("Dialog", "600MW级超临界湿冷"))
        self.comboBox.setItemText(5, _translate("Dialog", "600MW级超临界空冷"))
        self.comboBox.setItemText(6, _translate("Dialog", "600MW级亚临界湿冷"))
        self.comboBox.setItemText(7, _translate("Dialog", "600MW级亚临界空冷"))
        self.comboBox.setItemText(8, _translate("Dialog", "300MW级超临界湿冷"))
        self.comboBox.setItemText(9, _translate("Dialog", "300MW级超临界空冷"))
        self.comboBox.setItemText(10, _translate("Dialog", "300MW级亚临界湿冷"))
        self.comboBox.setItemText(11, _translate("Dialog", "300MW级亚临界空冷"))
        self.label_2.setText(_translate("Dialog", "编号："))
        self.ID.setText(_translate("Dialog", "0"))

    def accept(self) -> None:
        # TODO:此处需要更新
        # self.ID.text()
        self.mainWindow.addTab()
        super().accept()



