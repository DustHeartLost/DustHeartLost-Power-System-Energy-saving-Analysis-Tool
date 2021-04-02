from PyQt5 import QtCore, QtWidgets

from view.addPowerDialoge import AddPowerDialoge
from view.baseUI import BaseUI


class MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("mainWindow")
        MainWindow.resize(976, 785)
        MainWindow.setMinimumSize(QtCore.QSize(433, 335))
        # MainWindow.setMaximumSize(QtCore.QSize(976, 854))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("home")
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 976, 26))
        self.menubar.setObjectName("menubar")
        self.file = QtWidgets.QMenu(self.menubar)
        self.file.setObjectName("file")
        self.show = QtWidgets.QMenu(self.menubar)
        self.show.setObjectName("show")
        MainWindow.setMenuBar(self.menubar)
        self.formView = QtWidgets.QDockWidget(MainWindow)
        self.formView.setEnabled(True)
        self.formView.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.formView.setAllowedAreas(QtCore.Qt.BottomDockWidgetArea)
        self.formView.setObjectName("formView")
        self.formContents = QtWidgets.QWidget()
        self.formContents.setObjectName("formContents")
        self.formView.setWidget(self.formContents)
        self.formView.hide()
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.formView)
        self.lineChartView = QtWidgets.QDockWidget(MainWindow)
        self.lineChartView.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.lineChartView.setAllowedAreas(QtCore.Qt.BottomDockWidgetArea)
        self.lineChartView.setObjectName("lineChartView")
        self.lineChartViewContents = QtWidgets.QWidget()
        self.lineChartViewContents.setObjectName("lineChartViewContents")
        self.lineChartView.setWidget(self.lineChartViewContents)
        self.lineChartView.hide()
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.lineChartView)
        self.line_chart = QtWidgets.QAction(MainWindow)
        self.line_chart.setObjectName("line_chart")
        self.form = QtWidgets.QAction(MainWindow)
        self.form.setObjectName("form")
        self.add = QtWidgets.QAction(MainWindow)
        self.add.setCheckable(False)
        self.add.setObjectName("add")
        self.formView.raise_()
        self.lineChartView.raise_()
        self.file.addAction(self.add)
        self.show.addAction(self.form)
        self.show.addAction(self.line_chart)
        self.menubar.addAction(self.file.menuAction())
        self.menubar.addAction(self.show.menuAction())
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)

        # 为菜单选项添加点击事件
        self.addClickEventForMenuOption(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "首页"))
        self.file.setTitle(_translate("MainWindow", "文件"))
        self.show.setTitle(_translate("MainWindow", "显示"))
        self.formView.setWindowTitle(_translate("MainWindow", "图表"))
        self.lineChartView.setWindowTitle(_translate("MainWindow", "折线图"))
        self.line_chart.setText(_translate("MainWindow", "数据统计---折线图"))
        self.form.setText(_translate("MainWindow", "数据统计---图表"))
        self.add.setText(_translate("MainWindow", "添加机组"))

    def addClickEventForMenuOption(self, MainWindow):
        # 为菜单按钮绑定事件
        self.line_chart.triggered.connect(self.lineChartView.show)
        self.form.triggered.connect(self.formView.show)
        self.add.triggered.connect(self.addPowerGroup)
        self.tabWidget.tabCloseRequested.connect(self.closeTab)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def addPowerGroup(self):
        ui = AddPowerDialoge(self)
        ui.show()
        ui.exec_()

    def addTab(self):
        # TODO: 需要更新增加tab后的折线图和图表
        tab = QtWidgets.QWidget()
        ui = BaseUI()
        ui.setupUi(tab)
        self.tabWidget.addTab(tab, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(tab), "机组")
        self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(tab))
        # tab.setObjectName("home")


    def closeTab(self):
        # TODO: 需要更新关闭tab后的折线图和图表
        self.tabWidget.removeTab(self.tabWidget.currentIndex())