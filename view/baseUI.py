# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'baseUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class BaseUI(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(853, 478)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(12, 27, 641, 41))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_6.setHorizontalSpacing(30)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)
        self.ID = QtWidgets.QLabel(self.groupBox_2)
        self.ID.setObjectName("ID")
        self.gridLayout_6.addWidget(self.ID, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_6.addWidget(self.label_3, 0, 2, 1, 1)
        self.name = QtWidgets.QLabel(self.groupBox_2)
        self.name.setObjectName("name")
        self.gridLayout_6.addWidget(self.name, 0, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_6.addWidget(self.label_5, 0, 4, 1, 1)
        self.capacity = QtWidgets.QLabel(self.groupBox_2)
        self.capacity.setObjectName("capacity")
        self.gridLayout_6.addWidget(self.capacity, 0, 5, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 80, 791, 211))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_4.setHorizontalSpacing(20)
        self.gridLayout_4.setVerticalSpacing(10)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.consume_coal_1 = QtWidgets.QLabel(self.groupBox_3)
        self.consume_coal_1.setObjectName("consume_coal_1")
        self.gridLayout_4.addWidget(self.consume_coal_1, 1, 5, 1, 1)
        self.input_4 = QtWidgets.QLineEdit(self.groupBox_3)
        self.input_4.setObjectName("input_4")
        self.gridLayout_4.addWidget(self.input_4, 4, 3, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.groupBox_3)
        self.label_22.setObjectName("label_22")
        self.gridLayout_4.addWidget(self.label_22, 0, 1, 1, 1)
        self.consume_1 = QtWidgets.QLabel(self.groupBox_3)
        self.consume_1.setObjectName("consume_1")
        self.gridLayout_4.addWidget(self.consume_1, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 0, 5, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.groupBox_3)
        self.label_25.setObjectName("label_25")
        self.gridLayout_4.addWidget(self.label_25, 0, 4, 1, 1)
        self.input_1 = QtWidgets.QLineEdit(self.groupBox_3)
        self.input_1.setObjectName("input_1")
        self.gridLayout_4.addWidget(self.input_1, 1, 3, 1, 1)
        self.load_4 = QtWidgets.QLabel(self.groupBox_3)
        self.load_4.setObjectName("load_4")
        self.gridLayout_4.addWidget(self.load_4, 4, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.groupBox_3)
        self.label_20.setObjectName("label_20")
        self.gridLayout_4.addWidget(self.label_20, 0, 2, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox_3)
        self.label_21.setObjectName("label_21")
        self.gridLayout_4.addWidget(self.label_21, 0, 3, 1, 1)
        self.consume_2 = QtWidgets.QLabel(self.groupBox_3)
        self.consume_2.setObjectName("consume_2")
        self.gridLayout_4.addWidget(self.consume_2, 2, 1, 1, 1)
        self.load_1 = QtWidgets.QLabel(self.groupBox_3)
        self.load_1.setObjectName("load_1")
        self.gridLayout_4.addWidget(self.load_1, 1, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.groupBox_3)
        self.label_23.setObjectName("label_23")
        self.gridLayout_4.addWidget(self.label_23, 0, 0, 1, 1)
        self.input_2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.input_2.setObjectName("input_2")
        self.gridLayout_4.addWidget(self.input_2, 2, 3, 1, 1)
        self.load_3 = QtWidgets.QLabel(self.groupBox_3)
        self.load_3.setObjectName("load_3")
        self.gridLayout_4.addWidget(self.load_3, 3, 0, 1, 1)
        self.consume_4 = QtWidgets.QLabel(self.groupBox_3)
        self.consume_4.setObjectName("consume_4")
        self.gridLayout_4.addWidget(self.consume_4, 4, 1, 1, 1)
        self.input_3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.input_3.setObjectName("input_3")
        self.gridLayout_4.addWidget(self.input_3, 3, 3, 1, 1)
        self.state_4 = QtWidgets.QComboBox(self.groupBox_3)
        self.state_4.setObjectName("state_4")
        self.state_4.addItem("")
        self.state_4.addItem("")
        self.state_4.addItem("")
        self.gridLayout_4.addWidget(self.state_4, 4, 2, 1, 1)
        self.power_self_1 = QtWidgets.QLabel(self.groupBox_3)
        self.power_self_1.setObjectName("power_self_1")
        self.gridLayout_4.addWidget(self.power_self_1, 1, 4, 1, 1)
        self.state_1 = QtWidgets.QComboBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.state_1.sizePolicy().hasHeightForWidth())
        self.state_1.setSizePolicy(sizePolicy)
        self.state_1.setMinimumSize(QtCore.QSize(0, 10))
        self.state_1.setObjectName("state_1")
        self.state_1.addItem("")
        self.state_1.addItem("")
        self.state_1.addItem("")
        self.gridLayout_4.addWidget(self.state_1, 1, 2, 1, 1)
        self.power_self_3 = QtWidgets.QLabel(self.groupBox_3)
        self.power_self_3.setObjectName("power_self_3")
        self.gridLayout_4.addWidget(self.power_self_3, 3, 4, 1, 1)
        self.power_self_2 = QtWidgets.QLabel(self.groupBox_3)
        self.power_self_2.setObjectName("power_self_2")
        self.gridLayout_4.addWidget(self.power_self_2, 2, 4, 1, 1)
        self.consume_3 = QtWidgets.QLabel(self.groupBox_3)
        self.consume_3.setObjectName("consume_3")
        self.gridLayout_4.addWidget(self.consume_3, 3, 1, 1, 1)
        self.load_2 = QtWidgets.QLabel(self.groupBox_3)
        self.load_2.setObjectName("load_2")
        self.gridLayout_4.addWidget(self.load_2, 2, 0, 1, 1)
        self.state_3 = QtWidgets.QComboBox(self.groupBox_3)
        self.state_3.setObjectName("state_3")
        self.state_3.addItem("")
        self.state_3.addItem("")
        self.state_3.addItem("")
        self.gridLayout_4.addWidget(self.state_3, 3, 2, 1, 1)
        self.power_self_4 = QtWidgets.QLabel(self.groupBox_3)
        self.power_self_4.setObjectName("power_self_4")
        self.gridLayout_4.addWidget(self.power_self_4, 4, 4, 1, 1)
        self.state_2 = QtWidgets.QComboBox(self.groupBox_3)
        self.state_2.setObjectName("state_2")
        self.state_2.addItem("")
        self.state_2.addItem("")
        self.state_2.addItem("")
        self.gridLayout_4.addWidget(self.state_2, 2, 2, 1, 1)
        self.consume_coal_2 = QtWidgets.QLabel(self.groupBox_3)
        self.consume_coal_2.setObjectName("consume_coal_2")
        self.gridLayout_4.addWidget(self.consume_coal_2, 2, 5, 1, 1)
        self.consume_coal_3 = QtWidgets.QLabel(self.groupBox_3)
        self.consume_coal_3.setObjectName("consume_coal_3")
        self.gridLayout_4.addWidget(self.consume_coal_3, 3, 5, 1, 1)
        self.consume_coal_4 = QtWidgets.QLabel(self.groupBox_3)
        self.consume_coal_4.setObjectName("consume_coal_4")
        self.gridLayout_4.addWidget(self.consume_coal_4, 4, 5, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setGeometry(QtCore.QRect(510, 310, 281, 121))
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setHorizontalSpacing(30)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.label_33 = QtWidgets.QLabel(self.groupBox_4)
        self.label_33.setObjectName("label_33")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_33)
        self.power_all = QtWidgets.QLabel(self.groupBox_4)
        self.power_all.setObjectName("power_all")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.power_all)
        self.label_35 = QtWidgets.QLabel(self.groupBox_4)
        self.label_35.setObjectName("label_35")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_35)
        self.coal_all = QtWidgets.QLabel(self.groupBox_4)
        self.coal_all.setObjectName("coal_all")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.coal_all)
        self.label_37 = QtWidgets.QLabel(self.groupBox_4)
        self.label_37.setObjectName("label_37")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_37)
        self.average_coal = QtWidgets.QLabel(self.groupBox_4)
        self.average_coal.setObjectName("average_coal")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.average_coal)
        self.gridLayout_3.addLayout(self.formLayout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "基本信息"))
        self.label.setText(_translate("Form", "编号"))
        self.ID.setText(_translate("Form", "0"))
        self.label_3.setText(_translate("Form", "机组型式"))
        self.name.setText(_translate("Form", "1000MW级超超临界湿冷"))
        self.label_5.setText(_translate("Form", "装机总量"))
        self.capacity.setText(_translate("Form", "584454"))
        self.groupBox_3.setTitle(_translate("Form", "参数"))
        self.consume_coal_1.setText(_translate("Form", "1234"))
        self.label_22.setText(_translate("Form", "煤耗"))
        self.consume_1.setText(_translate("Form", "305"))
        self.label_8.setText(_translate("Form", "每种负荷的煤耗（吨）"))
        self.label_25.setText(_translate("Form", "每种负荷的发电量（GWh）"))
        self.load_4.setText(_translate("Form", "0.4"))
        self.label_20.setText(_translate("Form", "运行状态"))
        self.label_21.setText(_translate("Form", "运行时长长"))
        self.consume_2.setText(_translate("Form", "310"))
        self.load_1.setText(_translate("Form", "1"))
        self.label_23.setText(_translate("Form", "负荷"))
        self.load_3.setText(_translate("Form", "0.5"))
        self.consume_4.setText(_translate("Form", "340"))
        self.state_4.setItemText(0, _translate("Form", "100%负荷运行时间"))
        self.state_4.setItemText(1, _translate("Form", "75%负荷运行时间"))
        self.state_4.setItemText(2, _translate("Form", "50%负荷运行时间"))
        self.power_self_1.setText(_translate("Form", "116500"))
        self.state_1.setItemText(0, _translate("Form", "100%负荷运行时间"))
        self.state_1.setItemText(1, _translate("Form", "75%负荷运行时间"))
        self.state_1.setItemText(2, _translate("Form", "50%负荷运行时间"))
        self.power_self_3.setText(_translate("Form", "216600"))
        self.power_self_2.setText(_translate("Form", "113100"))
        self.consume_3.setText(_translate("Form", "327"))
        self.load_2.setText(_translate("Form", "0.75"))
        self.state_3.setItemText(0, _translate("Form", "100%负荷运行时间"))
        self.state_3.setItemText(1, _translate("Form", "75%负荷运行时间"))
        self.state_3.setItemText(2, _translate("Form", "50%负荷运行时间"))
        self.power_self_4.setText(_translate("Form", "555412"))
        self.state_2.setItemText(0, _translate("Form", "100%负荷运行时间"))
        self.state_2.setItemText(1, _translate("Form", "75%负荷运行时间"))
        self.state_2.setItemText(2, _translate("Form", "50%负荷运行时间"))
        self.consume_coal_2.setText(_translate("Form", "667"))
        self.consume_coal_3.setText(_translate("Form", "9987"))
        self.consume_coal_4.setText(_translate("Form", "5444"))
        self.groupBox_4.setTitle(_translate("Form", "统计"))
        self.label_33.setText(_translate("Form", "总发电量（GWh）"))
        self.power_all.setText(_translate("Form", "321988"))
        self.label_35.setText(_translate("Form", "总煤耗（吨）"))
        self.coal_all.setText(_translate("Form", "453511"))
        self.label_37.setText(_translate("Form", "年平均供电煤耗"))
        self.average_coal.setText(_translate("Form", "212121"))