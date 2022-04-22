## Ex 3-8. 창을 화면의 가운데로.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Centering')
        self.resize(500, 350)
       # self.move(20,20)
        self.center() # Use center method which made below
        self.show()

    def center(self):
        qr = self.frameGeometry() # qr은 윈도의 GeoMetry() 정보를 읽어와 화면과 동일한 가상의 사각형을 만든다.
        #cp = QDesktopWidget().availableGeometry().center() 이 부분도 공부가 필요하다
        # This is crux of this module / 사용자 모니터 정보를 읽어와서 정확한 화면의 중앙정보를 표시한다.
        #qr.moveCenter(cp) 이 부분 공부가 좀더 필요할듯
        self.move(qr.topRight()) # topLeft는 프레임 왼쪽 상단의 coordinate
        print(qr.topRight()) # 499 반환함 -> 설정해준 프레임의 width
        print(qr.bottomLeft()) # 349 반환함 -> 설정해준 프레임의 height

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())