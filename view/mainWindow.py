from PyQt5 import QtCore, QtWidgets
from view.addPowerDialoge import AddPowerDialoge
from view.baseUI import BaseUI
from view.form import Form
from view.lineChart import LineCHart


class MainWindow(object):
    def setupUi(self, MainWindow):
        self.mainwindow=MainWindow
        self.mainwindow.setObjectName("self.mainwindow")
        self.mainwindow.resize(1900, 900)
        self.mainwindow.setMinimumSize(QtCore.QSize(433, 335))
        # self.mainwindow.setMaximumSize(QtCore.QSize(976, 854))
        self.centralwidget = QtWidgets.QWidget(self.mainwindow)
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
        self.mainwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.mainwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 976, 26))
        self.menubar.setObjectName("menubar")
        self.file = QtWidgets.QMenu(self.menubar)
        self.file.setObjectName("file")
        self.show = QtWidgets.QMenu(self.menubar)
        self.show.setObjectName("show")
        self.mainwindow.setMenuBar(self.menubar)
        self.formView = QtWidgets.QDockWidget(self.mainwindow)
        self.formView.setEnabled(True)
        self.formView.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.formView.setAllowedAreas(QtCore.Qt.RightDockWidgetArea)
        self.formView.setObjectName("formView")
        self.formView.widget=Form()
        self.formView.setWidget(self.formView.widget)
        self.formView.setMinimumSize(980,600)
        self.formView.show()
        self.mainwindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.formView)
        self.lineChartView = QtWidgets.QDockWidget(self.mainwindow)
        self.lineChartView.setFeatures(QtWidgets.QDockWidget.AllDockWidgetFeatures)
        self.lineChartView.setAllowedAreas(QtCore.Qt.RightDockWidgetArea)
        self.lineChartView.setObjectName("lineChartView")
        self.lineChartView.widget=LineCHart()
        self.lineChartView.setWidget(self.lineChartView.widget)
        self.lineChartView.show()
        self.mainwindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.lineChartView)
        self.line_chart = QtWidgets.QAction(self.mainwindow)
        self.line_chart.setObjectName("line_chart")
        self.form = QtWidgets.QAction(self.mainwindow)
        self.form.setObjectName("form")
        self.add = QtWidgets.QAction(self.mainwindow)
        self.add.setCheckable(False)
        self.add.setObjectName("add")
        self.formView.raise_()
        self.lineChartView.raise_()
        self.file.addAction(self.add)
        self.show.addAction(self.form)
        self.show.addAction(self.line_chart)
        self.menubar.addAction(self.file.menuAction())
        self.menubar.addAction(self.show.menuAction())
        self.retranslateUi()
        self.tabWidget.setCurrentIndex(-1)
        self.dataTab=[]

        # 为菜单选项添加点击事件
        self.addClickEventForMenuOption()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.mainwindow.setWindowTitle(_translate("self.mainwindow", "self.mainwindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("self.mainwindow", "首页"))
        self.file.setTitle(_translate("self.mainwindow", "文件"))
        self.show.setTitle(_translate("self.mainwindow", "显示"))
        self.formView.setWindowTitle(_translate("self.mainwindow", "图表"))
        self.lineChartView.setWindowTitle(_translate("self.mainwindow", "折线图"))
        self.line_chart.setText(_translate("self.mainwindow", "数据统计---折线图"))
        self.form.setText(_translate("self.mainwindow", "数据统计---图表"))
        self.add.setText(_translate("self.mainwindow", "添加机组"))

    def addClickEventForMenuOption(self):
        # 为菜单按钮绑定事件
        self.line_chart.triggered.connect(self.lineChartView.show)
        self.form.triggered.connect(self.formView.show)
        self.add.triggered.connect(self.addPowerGroup)
        self.tabWidget.tabCloseRequested.connect(self.closeTab)
        QtCore.QMetaObject.connectSlotsByName(self.mainwindow)

    def addPowerGroup(self):
        ui = AddPowerDialoge(self)
        ui.show()
        ui.exec_()

    def addTab(self,id):
        for temp in self.dataTab:
            if temp.baseUI.data.id==id:
                self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(temp))
                return
        tab = QtWidgets.QWidget()
        self.dataTab.append(tab)
        ui = BaseUI()
        ui.setupUi(tab,id,self)
        self.tabWidget.addTab(tab, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(tab), tab.baseUI.data.name)
        self.tabWidget.setCurrentIndex(self.tabWidget.indexOf(tab))
        self.lineChartView.widget.updateLineChart(self.dataTab)

    def closeTab(self,index):
        for temp in self.dataTab:
            if temp==self.tabWidget.widget(index):
                self.dataTab.remove(temp)
                self.formView.widget.updateForm(self.dataTab)
                self.lineChartView.widget.updateLineChart(self.dataTab)
                break
        self.tabWidget.removeTab(index)

