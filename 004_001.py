## Ex 4-1. 절대적 배치.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
# 이상 설명 생략. 그냥 Pattern 으로 인식
    def initUI(self):
        pose = 20
        label1 = QLabel('Label1', self) # 라벨 인스턴스 생성
        label1.move(pose, 20)
        label2 = QLabel('Label2', self) # 라벨 인스턴스 2 생성
        label2.move(20, 60)

        btn1 = QPushButton('Button1', self) # 버튼 인스턴스 생성
        btn1.move(80, 13)
        btn2 = QPushButton('Button2', self) # 버튼 인스턴스 2 생성
        btn2.move(80, 53)

        self.setWindowTitle('Absolute Positioning') # 프레임 제목 설정
        self.setGeometry(300, 300, 400, 200) # 넓이 400 높이 200
        self.show()


if __name__ == '__main__':
    app = QApplication(["hh"])
    print("p_1")
    ex = MyApp()
    app.exec_() # 여기에서 무한루프 도는구나..
    print("p_2")