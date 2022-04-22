## Ex 3-4. 툴팁 나타내기.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QFont


class MyApp(QWidget):

    def __init__(self):
        super().__init__() # 부모 초기화
        self.initUI() # 만들어진 클래스 타입 객체로 함수 호출

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10)) # 툴팁 객체의 폰트 설정 , 산세리프 10짜리 크기인듯
        self.setToolTip('This is a <b>QWidget</b> widget2') # 볼드체 처리한 텍스트가 커서를 가져다 대면 나롤듯

        btn = QPushButton('Button', self) # 버튼객체 생성
        btn.setToolTip('This is a <b>QPushButton</b> widget3') # 만들어 지는 순간 self.setToolTip 메서드가 실행되기 때문에 굳이 없어도 되는 코드이지만, 있다면 나중에 시행된 코드 결과가 반영됨
        btn.move(50, 50)
        btn.resize(btn.sizeHint()) # 어제 한거랑 마찬가지, constant 값 받아서 적당한 크기로 사이징

        self.setWindowTitle('Tooltips') # 제목 설정
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    app.exec()