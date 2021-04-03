import math
import sys
import random

from PyQt5 import QtChart
from PyQt5.QtChart import QDateTimeAxis, QValueAxis, QSplineSeries, QChart, QChartView, QLineSeries
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget
from PyQt5.QtGui import QPainter, QBrush
from PyQt5.QtCore import QDateTime, Qt, QTimer, QPointF


class ChartView(QChartView,QChart):
    def __init__(self, *args, **kwargs):
        super(ChartView, self).__init__(*args, **kwargs)
        self.resize(800, 600)
        self.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
        self.chart_init()
        self.timer_init()
    # def timer_init(self):
    #     #使用QTimer，2秒触发一次，更新数据
    #     self.timer = QTimer(self)
    #     self.timer.timeout.connect(self.drawLine)
    #     self.timer.start(1000)
    # def chart_init(self):
    #     self.chart = QChart()
    #     self.chart.setTheme(QChart.ChartThemeDark)
    #     self.series = QSplineSeries()
    #     #设置曲线名称
    #     self.series.setName("控制电压")
    #
    #     #把曲线添加到QChart的实例中
    #     self.chart.addSeries(self.series)
    #     #声明并初始化X轴，Y轴
    #     self.dtaxisX = QDateTimeAxis()
    #     self.vlaxisY = QValueAxis()
    #     #设置坐标轴显示范围
    #     self.dtaxisX.setMin(QDateTime.currentDateTime().addSecs(-300*1))
    #     self.dtaxisX.setMax(QDateTime.currentDateTime().addSecs(0))
    #     self.vlaxisY.setMin(0)
    #     self.vlaxisY.setMax(50)
    #     #设置X轴时间样式
    #     self.dtaxisX.setFormat("hh:mm:ss")
    #     #设置坐标轴上的格点
    #     self.dtaxisX.setTickCount(6)
    #     self.vlaxisY.setTickCount(11)
    #     #设置坐标轴名称
    #     self.dtaxisX.setTitleText("时间")
    #     self.vlaxisY.setTitleText("电压")
    #     #设置网格不显示
    #     self.vlaxisY.setGridLineVisible(False)
    #     #把坐标轴添加到chart中
    #     self.chart.addAxis(self.dtaxisX,Qt.AlignBottom)
    #     self.chart.addAxis(self.vlaxisY,Qt.AlignLeft)
    #     #把曲线关联到坐标轴
    #     self.series.attachAxis(self.dtaxisX)
    #     self.series.attachAxis(self.vlaxisY)
    #
    #     self.setChart(self.chart)
    #
    #
    # def drawLine(self):
    #     #获取当前时间
    #     bjtime = QDateTime.currentDateTime()
    #     #更新X轴坐标
    #     self.dtaxisX.setMin(QDateTime.currentDateTime().addSecs(-300*1))
    #     self.dtaxisX.setMax(QDateTime.currentDateTime().addSecs(0))
    #     #当曲线上的点超出X轴的范围时，移除最早的点
    #     if(self.series.count()>149):
    #         self.series.removePoints(0,self.series.count()-149)
    #     #产生随即数
    #     yint = random.randint(0,50)
    #     #添加数据到曲线末端
    #     self.series.append(bjtime.toMSecsSinceEpoch(),yint)


if __name__ == "__main__":
    # app = QApplication(sys.argv)
    # view = ChartView()
    # view.show()
    # sys.exit(app.exec_())
    app = QApplication(sys.argv)

    wnd = QMainWindow()
    wnd.setWindowTitle("Qt Line Chart")
    wnd.resize(1000, 700)
    #
    LineSeries = QtChart.QSplineSeries()
    LineSeries.setName("1000MW级超超临界湿冷")

    #
    LineSeries.append(100, 282)
    LineSeries.append(75, 286)
    LineSeries.append(50, 303)
    LineSeries.append(40, 332)
    #

    chart1 = QtChart .QChart()
    chart1.addSeries(LineSeries)
    chart1.setTitle("图表")
    chart1.createDefaultAxes()
    chart1.axisX().setTitleText("负荷率")
    chart1.axisX().setRange(30 , 100)
    chart1.axisX().setLabelFormat("%.0f%%")

    chart1.axisX().setTickCount(8)
    chart1.axisY().setTitleText("供电煤耗 单位（克/千瓦时）")
    chart1.axisY().setRange(280, 380)
    chart1.axisY().setLabelFormat("%.0f")
    chart1.axisY().setTickCount(11)
    chart1.setTheme(QtChart.QChart.ChartThemeLight)

    chartView1 = QtChart.QChartView()
    chartView1.setChart(chart1)
    chartView1.setRenderHint(QPainter.Antialiasing)

    gridLayout = QGridLayout()
    gridLayout.addWidget(chartView1, 0, 0, 1, 1)

    widget = QWidget()
    widget.setLayout(gridLayout)
    wnd.setCentralWidget(widget)
    wnd.show()

    sys.exit(app.exec_())
