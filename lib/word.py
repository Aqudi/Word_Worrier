from pathlib import Path
import os
import random
import codecs
import re


class Word:
    def __init__(self):
        top_dir = Path(os.getcwd()).parent
        file_name = top_dir / "Data" / "Words.txt"
        with codecs.open(file_name, 'r', "utf-8") as f:
            self.words = [x.rstrip() for x in f.readlines()]
            print("단어DB의 크기 : ", len(self.words))

    def get_random_word(self, length=2):
        word = ""
        while len(word) != 3:
            word = self.words[random.randrange(len(self.words))]
        word = self.extract_hangul(word)
        return word

    @staticmethod
    def extract_hangul(string):
        # 정규식 출처: http: // jokergt.tistory.com / 52[Gun's Knowledge Base]
        hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')  # 한글과 띄어쓰기를 제외한 모든 글자
        result = hangul.sub('', string)  # 한글과 띄어쓰기를 제외한 모든 부분을 제거
        return result

    @staticmethod
    def decompose_hangul(string):
        # 계산식 출처: https: // github.com / neotune / python - korean - handler
        # 라이선스: MIT라이선스

        # 유니코드 한글 시작 : 44032, 끝 : 55199
        BASE_CODE, CHOSUNG= 44032, 588
        # 초성 리스트. 00 ~ 18
        CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

        result = []
        string = Word.extract_hangul(string)

        for char in string:
            char_code = ord(char) - BASE_CODE
            char1 = int(char_code / CHOSUNG)
            result.append(CHOSUNG_LIST[char1])

        return result


if __name__ == "__main__":
    d = Word()
    word = d.get_random_word()
    print(word)
    print(d.decompose_hangul(word))
