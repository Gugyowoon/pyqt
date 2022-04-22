## Ex 3-7. 툴바 만들기.

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('exit.png'), 'Exit', self) # QIcon 메소드 -> 아이콘 설정 / QAction 메소드 -> 액션 (클릭 시 동작할 기능?) 설정
        exitAction.setShortcut('Ctrl+K') # setShortcut 메소드 -> 입력받은 텍스트로 단축키를 배정하는 듯.
        exitAction.setStatusTip('Exit application') # 마우스 호버링 시 나오는 상태창
        exitAction.triggered.connect(qApp.quit) # 발생시킬 함수 -> 종료 .. qApp은 무슨의미 ?
    # __init__ 모듈에 가보면 qApp = QApplication() 으로 정의되어있음 . 객체에 대한 접근을 쉽게 할 수 있게 만드는 기법인듯
        self.statusBar() # 상태바 객체 생성함

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction) # 위에서 만들어 둔 액션 (대충 subroutine) 호출

        # 이하는 계속 반복됨
        self.setWindowTitle('Toolbar')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication([2])
    ex = MyApp()
    sys.exit(app.exec_())