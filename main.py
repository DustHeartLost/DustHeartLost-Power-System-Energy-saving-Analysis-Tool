from view.mainWindow import MainWindow
from PyQt5 import QtWidgets

import sys

def start():
    app=QtWidgets.QApplication(sys.argv)
    mainWindow=QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.setWindowTitle("电力系统节能调度分析辅助工具软件")
    mainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    start()


