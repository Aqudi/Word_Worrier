from pathlib import Path
import os
import random
import codecs
import re


class Word:
    def __init__(self):
        topDir = Path(os.getcwd()).parent
        fileName = topDir / "Data" / "Words.txt"
        with codecs.open(fileName, 'r', "utf-8") as f:
            self.words = [x.rstrip() for x in f.readlines()]
            print("단어의 수 : ", len(self.words))

    def getRandomWord(self, length=2):
        word = ""
        while len(word) != 3:
            word = self.words[random.randrange(len(self.words))]
        word = self.extractHangul(word)
        return word

    def extractHangul(self, string):
        # 정규식 출처: http: // jokergt.tistory.com / 52[Gun's Knowledge Base]
        hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')  # 한글과 띄어쓰기를 제외한 모든 글자
        result = hangul.sub('', string)  # 한글과 띄어쓰기를 제외한 모든 부분을 제거
        return result

    def decomposeHangul(self, string):
        pass

if __name__ == "__main__":
    d = Word()
    print(d.getRandomWord())
