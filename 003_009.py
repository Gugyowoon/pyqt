## Ex 3-9. 날짜와 시간 표시하기.

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QDate, Qt


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
#       print(self.date) -> PyQt5.QtCore.QDate(2022, 4, 21) 반환
# 현재 날짜와 시간을 시스템 시계에서 받아옴 -> Returns the current date, as reported by the system clock.
        self.initUI()
# 자동으로 아래 함수 실행되도록 __init__에 넣어놓음


    def initUI(self):
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))
# statusBar() 란 , QMainWindow가 하단부에 생성하는 Bar이다. 옵셔널.
# https://doc.qt.io/qt-5/qmainwindow.html Qt Main Window Framework 참조
# The status bar can be retrieved using the QMainWindow::statusBar() function
#       print(self.date.toString(Qt.DefaultLocaleLongDate)) -> 2022년 4월 21일 목요일" 반환

        self.setWindowTitle('Date')
        self.setGeometry(300, 300, 400, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())