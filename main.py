import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtCore import QTimer
import random
from lib.AA_Timer import AAThread
from lib.chracter import Hero, Villain
from lib.word_game import WordGame
import lib.word
from lib.card import Card
from lib.game_main_window import Ui_MainWindow as Main_Window
from lib.start_page_window import Ui_MainWindow as Start_Window
import Data.Resource_rc


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
        self.UpgradeButton1.setDisabled(True)
        self.UpgradeButton2.setDisabled(True)
        self.UpgradeButton3.setDisabled(True)
        self.UpgradeButton4.setDisabled(True)
        
        # 시작버튼을 누를 시 시작
        self.check.setText("시작")
        self.wordInput.setReadOnly(True)
        self.wordInput.setText("시작버튼을 눌러주세요.")
        self.check.clicked.connect(self.button_clicked)

        # 이벤트카드 생성
        self.cards = [Card(), Card(), Card(), Card()]
        self.card_buttons = [self.UpgradeButton1, self.UpgradeButton2, self.UpgradeButton3, self.UpgradeButton4]

        # 이벤트카드 누를 시
        self.UpgradeButton1.clicked.connect(self.action)
        self.UpgradeButton2.clicked.connect(self.action)
        self.UpgradeButton3.clicked.connect(self.action)
        self.UpgradeButton4.clicked.connect(self.action)

        # 스테이지 설정
        self.stage = 1

        # 캐릭터 생성
        self.hero = Hero()

        # 타이머 쓰레드
        self.timer = AAThread()
        self.timer.start()

        # 시그널 슬롯 연결
        self.timer.change_value.connect(self.auto_attack)

        # 단어 퀴즈
        self.word_game = WordGame()

    def auto_attack(self, count):
        self.AA_villain.setValue(count)
        if count == 100:
            self.villain.attack(self.hero)

    def button_clicked(self):
        button = self.sender()
        cmd = button.text()
        if cmd == "입력":
            pass
        elif cmd == "시작":
            self.game_init()

    # 이벤트 카드의 이벤트를 실행해준다..
    def action(self):
        button = self.sender()
        idx = self.card_buttons.index(button)
        card = self.cards[idx]

        if card.get_type() is "ATTACK":
            fight_result = self.hero.attack(self.villain, buff=self.hero.get_ap()*card.get_value())
            string = "{}공격, {}연타!\n{} \n{}".format(card.get_name(), card.get_value(), fight_result[0], fight_result[1])
            print(string)
            self.attackSummary.setText(string)

        elif card.get_type() is "STAT":
            modify_stat = {"HP": self.hero.modify_max_hp, "AP": self.hero.modify_ap,
                           "AC": self.hero.modify_ac, "CC": self.hero.modify_cc,
                           "AA": self.hero.modify_aa}
            modify_stat[card.get_name()](card.get_value())

        elif card.get_type() is "HEAL":
            self.hero.modify_hp(card.get_value())

        # 바뀐 게임 정보 갱신
        self.cards[idx].set_random_pool_value()
        self.event_card_setting(self.cards[idx], self.card_buttons[idx])

        self.show_chracter_information()
        # 게임이 끝났는지 여부를 체크
        self.game_over()

    def event_card_setting(self, content, card):
        text = ""
        content = content.get_information()
        TYPE = content[0][1]
        content = content[1:]

        # 카드 타입 명시
        if TYPE is "ATTACK":
            text = "공격 카드\n"
        elif TYPE is "STAT":
            text = "스탯 카드\n"
        elif TYPE is "HEAL":
            text = "회복 카드\n"
        # 액션 종류, 상세 값 명시
        for tag, value in content:
            text = text + str(value) + " "
            if value in ("HP", "AP", "AC", "CC", "MIRACLE", "HOLY", "CURE"):
                text += "%"

        # 카드 타입마다 종결어미 변경
        if TYPE is "ATTACK":
            text += "번 공격"
        elif TYPE is "STAT":
            text += "증가"
        elif TYPE is "HEAL":
            text += "회복"
        card.setText(text)

    def create_villain(self):
        # 캐릭터 info 인자 name, hp, ap, ac, cc, image, aa
        names = ["최빵빵부하1", "최빵빵부하2", "최빵빵"]
        images = Villain.get_images_resource()
        stage_info = {1: dict(name=names[0], health_point=5000, attack_point=250, avoid_chance=5, critical_chance=5,
                              image=images[self.stage-1], auto_attack=10),
                      2: dict(name=names[1], health_point=10000, attack_point=400, avoid_chance=15, critical_chance=15,
                              image=images[self.stage-1], auto_attack=50),
                      3: dict(name=names[2], health_point=15000, attack_point=600, avoid_chance=30, critical_chance=10,
                              image=images[self.stage-1], auto_attack=10),
                      4: dict(name=names[1], health_point=25000, attack_point=600, avoid_chance=40, critical_chance=15,
                              image=images[self.stage - 1], auto_attack=10),
                    5: dict(name=names[2], health_point=25000, attack_point=1000, avoid_chance= 50, critical_chance=10,
                              image=images[self.stage - 1], auto_attack=10)
                      }

        return Villain(**stage_info[self.stage])

    def show_chracter_information(self):
        self.AP_Hero.setText(str(self.hero.get_ap()))
        self.AC_Hero.setText(str(self.hero.get_ac()))
        self.CC_Hero.setText(str(self.hero.get_cc()))
        self.HeroHPBar.setMaximum(self.hero.get_max_hp())
        print(self.hero.get_hp())
        self.HeroHPBar.setProperty("value", self.hero.get_hp())
        self.HeroPicture.setPixmap(QtGui.QPixmap(self.hero.get_image()))

        self.AP_villain.setText(str(self.villain.get_ap()))
        self.AC_villain.setText(str(self.villain.get_ac()))
        self.CC_villain.setText(str(self.villain.get_cc()))
        self.villainHPBar.setMaximum(self.villain.get_max_hp())
        self.villainHPBar.setProperty("value", self.villain.get_hp())
        self.VillainPicture.setPixmap(QtGui.QPixmap(self.villain.get_image()))

    def game_init(self):
        # 게임 시작
        # 입력버튼, 입력창 초기화
        self.check.setText("입력")
        self.wordInput.setReadOnly(False)
        self.wordInput.setText("이벤트 카드를 선택해주세요  -------->")

        # 이벤트카드 활성화
        self.UpgradeButton1.setDisabled(False)
        self.UpgradeButton2.setDisabled(False)
        self.UpgradeButton3.setDisabled(False)
        self.UpgradeButton4.setDisabled(False)

        # 이벤트 카드 셋팅
        for i in range(len(self.cards)):
            self.event_card_setting(self.cards[i], self.card_buttons[i])

        # 악당생성
        self.villain = self.create_villain()
        self.timer.set_multi(self.villain.get_aa())

        # 캐릭터 정보 표시
        self.show_chracter_information()

    def game_reset(self):# 시작버튼을 누를 시 시작
        self.UpgradeButton1.setDisabled(True)
        self.UpgradeButton2.setDisabled(True)
        self.UpgradeButton3.setDisabled(True)
        self.UpgradeButton4.setDisabled(True)

        self.check.setText("시작")
        self.wordInput.setReadOnly(True)
        self.wordInput.setText("시작버튼을 눌러주세요.")
        self.check.clicked.connect(self.button_clicked)

    def game_over(self):
        if self.hero.check_alive():
            self.show_chracter_information()
            self.stage = 1
            self.game_reset()
            self.attackSummary.setText("주금...\n스테이지 1부터 다시 시작합니다.")
        elif self.villain.check_alive():
            self.show_chracter_information()
            self.stage += 1
            self.game_reset()
            self.attackSummary.setText("잡았다!")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    start = StartWindow()
    start.show()
    app.exec_()