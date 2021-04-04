from PyQt5 import QtChart
from PyQt5.QtChart import QChartView, QChart
from PyQt5.QtGui import QPainter


class LineCHart(QChartView):
    def __init__(self):
        super().__init__()

    def updateLineChart(self,tabData):
        self.QChart = QChart()
        for i in range(12):
            for temp in tabData:
                data = temp.baseUI.data
                if(data.id=='%d'%i):
                    LineSeries = QtChart.QSplineSeries()
                    LineSeries.setName(data.name)
                    LineSeries.append(data.load_1*100, data.consume_1)
                    LineSeries.append(data.load_2*100, data.consume_2)
                    LineSeries.append(data.load_3*100, data.consume_3)
                    LineSeries.append(data.load_4*100, data.consume_4)
                    self.QChart.addSeries(LineSeries)
        self.QChart.setTitle("图表")
        self.QChart.createDefaultAxes()
        self.QChart.axisX().setTitleText("负荷率")
        # self.QChart.axisX().setRange(30, 100)
        self.QChart.axisX().setLabelFormat("%.0f%%")
        self.QChart.axisX().setTickCount(8)
        self.QChart.axisY().setTitleText("供电煤耗 单位（克/千瓦时）")
        # self.QChart.axisY().setRange(280, 380)
        self.QChart.axisY().setLabelFormat("%.0f")
        self.QChart.axisY().setTickCount(11)
        self.QChart.setTheme(QtChart.QChart.ChartThemeLight)
        self.setChart(self.QChart)
        self.setRenderHint(QPainter.Antialiasing)
