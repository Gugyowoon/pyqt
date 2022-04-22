## Ex 3-3. 창 닫기.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI() # 계속 동일한 구조

    def initUI(self):
        btn = QPushButton('Quit', self)
#버튼 생성, 이름은 Quit
        btn.move(50, 50)
        btn.resize(btn.sizeHint())

# Basically, there are two ways in order to change the size of btn , one is `resize` method and the other issetGeometry method.
# resize 메소드는 이름 그대로 버튼의 크기를 조절하는 함수.
# sizehint 는 적당한 컴포넌트별 크기를 제시해주는 상수값. This property holds the recommended size for the widget
        btn.clicked.connect(QCoreApplication.instance().quit)
# 객체명.clicked.connect -> 객체 클릭시 발생시킬 시그널
        self.setWindowTitle('Quit Button')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())