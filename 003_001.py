## Ex 3-1. 창 띄우기.

import sys
from PyQt5.QtWidgets import QApplication, QWidget


class MyApp(QWidget):
    def __init__(self): # self means literally Created Instance itself
        super().__init__() # Must init upper class (parent)
        self.initUI() # 보통 여기까지는 모든 모듈에서 공통으로 가지는 코드

    def initUI(self):
        self.setWindowTitle("My First Application")
        self.move(0, 100) # Move Position of Instance // Origin is Left Above point of your Monitor , (x_pos , y_pos)
        self.resize(400, 200) # width , height
        self.show()


if __name__ == "__main__":
# Execute Only Directly Called Situation
     app = QApplication([])
#    app = QApplication(sys.argv) -> 굳이 sys.argv를 사용하지 않아도 됨
# QApplication -> It manage whole control class in pyQT.
# QApplication takes a list of strings as input.
#  For any GUI application using Qt, there is precisely one QApplication object - 모든 파이큐티 기반 gui는 한개 이상의 큐어플리케이션 객체를 생성해야 한다.
     ex = MyApp()
# Make Instance from above class
# 왜 만들어 놓고 안쓰지 ?? ex는 어디에서 쓰이는건가
     app.exec()
    #app.exec_()
    #sys.exit(app.exec_()) -> pyqt5에서는 굳이 sys.exit 를 사용할 필요가 x
    # exec_ 에서 언더바가 있는 이유는 파이썬 버젼 2까지는 exec 가 예약어 (reserved) 였기 때문임. 이제는 걍 exec 써도 됨
# Raise a system exception, signaling an intention to exit the interpreter.
# Exit from Python
