import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QUrl, QThread
from lib.chracter import Hero, Villain
import lib.word_game as word_game
import lib.card as card
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    start = StartWindow()
    start.show()
    app.exec_()