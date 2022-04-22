## Ex 3-2. 어플리케이션 아이콘 넣기.

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class MyApp(QWidget):
    def __init__(self):
        super().__init__() # Initialize  Parent
        self.initUI() # 객체 생성시 자동으로 initUI 함수가 실행되게 만들어 놓음

    def initUI(self):
        self.setWindowTitle("Icon")
        self.setWindowIcon(QIcon("web.png"))
        self.setGeometry(50, 100, 400, 200) # x_pos , y_pos , width, height
        self.show()


if __name__ == "__main__": # Start From
    app = QApplication(sys.argv)
    ex = MyApp() # Infinite loop
    app.exec_() # End to
