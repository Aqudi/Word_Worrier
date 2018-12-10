from PyQt5.QtCore import Qt
from PyQt5.QtCore import QThread
from PyQt5.QtCore import QWaitCondition
from PyQt5.QtCore import QMutex
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import pyqtSlot


class AAThread(QThread):
    # 시그널 선언
    change_value = pyqtSignal(int)

    def __init__(self, multi=10):
        QThread.__init__(self)
        self.cond = QWaitCondition()
        self.mutex = QMutex()
        self.count = 0
        self._status = True
        self.multi = multi
        print(multi)

    def set_multi(self, multi):
        self.multi = multi

    def __del__(self):
        self.wait()

    def run(self):
        while True:
            self.mutex.lock()

            if not self._status:
                self.cond.wait(self.mutex)

            if 100 < self.count:
                self.count = 0
            self.count += 1
            self.change_value.emit(self.count)
            self.msleep(10000//self.multi)

            self.mutex.unlock()

    @property
    def status(self):
        return self._status

