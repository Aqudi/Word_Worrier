import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QUrl, QThread
from lib.chracter import Hero, Villain
import lib.word_game as word_game
from lib.card import Card
from lib.game_main_window import Ui_MainWindow as Main_Window
from lib.start_page_window import Ui_MainWindow as Start_Window


class StartWindow(QMainWindow, Start_Window):
    def __init__(self):
        super().__init__()
        # 초기화
        self.setupUi(self)
        self.word_worrier_main = MainWindow()
        self.pushButton.clicked.connect(self.start_button_clicked)

    def start_button_clicked(self):
        self.word_worrier_main.show()
        self.close()


class MainWindow(QMainWindow, Main_Window):
    def __init__(self):
        super().__init__()
        # 초기화
        self.setupUi(self)
        
        # 시작버튼을 누를 시 시작
        self.check.setText("시작")
        self.wordInput.setReadOnly(True)
        self.wordInput.setText("시작버튼을 눌러주세요.")
        self.check.clicked.connect(self.game_start)

    def game_start(self):
        # 게임 시작
        # 입력버튼, 입력창 초기화
        self.check.setText("입력")
        self.wordInput.setReadOnly(False)
        self.wordInput.setText("")

        # 이벤트 카드 셋팅
        self.event_card_setting()

    def event_card_setting(self):
        self.cards = [Card(), Card(), Card(), Card()]
        self.card_buttons = [self.UpgradeButton1, self.UpgradeButton2, self.UpgradeButton3, self.UpgradeButton4]
        for content, card in zip(self.cards, self.card_buttons):
            text = ""
            content = content.get_information()
            TYPE = content[0][1]
            content = content[1:]

            # 카드 타입 명시
            if TYPE is "ATTACK":
                text = "공격 카드\n"
            elif TYPE is "STAT":
                text = "스탯 카드\n"
            # 액션 종류, 상세 값 명시
            for tag, value in content:
                text = text + str(value) + " "
                print("text", text)
                if value in ("HP", "AP", "AC", "CC"):
                    text += "%"


            if TYPE is "ATTACK":
                text += "번 공격"
            elif TYPE is "STAT":
                text += "증가"
            card.setText(text)


        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    start = StartWindow()
    start.show()
    app.exec_()