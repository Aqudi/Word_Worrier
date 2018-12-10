from lib.word import Word
from lib.searcher import Searcher


class WordGame:
    def __init__(self):
        self.word = Word()
        self.searcher = Searcher()
        self.correct_answer = ""
        self.definition = ""

    def game_setting(self, length):
        # 제대로된 검색결과를 받을 때까지 반복
        while self.correct_answer == "error" or self.correct_answer == "" or self.definition == "":
            # 받아오는 데이터 형식 ---> 단어: 단어의 뜻
            information = self.searcher.get_word_information(self.word.get_random_word(length))
            information = information.split(": ")

            # 한글이 아닌 내용이 있을 시 제거 (예시) 맏-손자 -> 맏손자
            self.correct_answer = information[0]
            self.definition = information[1]
            return (self.correct_answer, self.definition)

    def guess(self, answer):
        # 치트키
        if answer == "hint":
            return self.correct_answer

        if answer == self.correct_answer:
            return True
        else:
            return False

    @staticmethod
    def consol_test(correct_answer, definition):
        answer = ""
        while answer != correct_answer:
            print("단어의 길이 : ", len(correct_answer))
            print("단어의 뜻: ", definition)
            answer = input("답을 입력하세요: ")
            if answer == "hint":
                print(correct_answer)
            elif answer != correct_answer:
                print("다시입력하세요.")
        print("정답")


if __name__ == "__main__":
    w = WordGame()
    correct_answer, definition = w.game_setting(3)
    w.consol_test(correct_answer, definition)
