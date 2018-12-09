from bs4 import BeautifulSoup
import requests
import configparser
from word import Word


class Searcher:
    def __init__(self):
        config = configparser.RawConfigParser()
        config.read("config.ini")
        self.API_KEY = config.get('Default', 'api_key')
        self.BASE_URL = "https://opendict.korean.go.kr/api/search"

    def get_word_information(self, word, start=1):
        parameters = {"key": self.API_KEY, 'target_type': 'search',
                      'part': 'word', 'q': word,
                      'sort': 'dict', 'start': start, 'num': 10,
                      }

        with requests.Session() as s:
            for i in range(1, 5):
                # 결과가 예상한 것과 다를 경우 표제어의 번호를 바꿔가며 재시도
                parameters[start] = i
                print("{}번째 요청".format(i))

                # 우리말샘 API에 검색결과를 요청
                request = s.get(self.BASE_URL, params=parameters)
                if request.status_code == 200 and request.ok:
                    soup = BeautifulSoup(request.text, 'html.parser')

                    # 한글이외의 내용들 제거 (예시) 맏-손자 -> 맏손자
                    word_name = Word.extract_hangul(soup.find("word").string)
                    word_definition = soup.find("definition").string

                    # 검색결과와 검색 키워드가 달라질경우 : 단어의 길이 우선적으로 검사 
                    if len(word_name) != len(word):
                        continue
                    elif word_name is None or word_definition is None:
                        return "error: 없는데이터"
                    else:
                        return word_name + ": " + word_definition
                else:
                    return "error: Request에러"

            # 제대로된 결과를 얻지 못했을 경우
            return "error: 없는데이터"


if __name__ == "__main__":
    d = Searcher()
    
    # 원하는 단어 검색 테스트
    word = input("검색하고 싶은 단어를 입력해주세요 : ")
    result = d.get_word_information(word)
    print(result)
    print()
    
    # 랜덤단어 검색 테스트
    w = Word()
    result = d.get_word_information(w.get_random_word())
    print(result)
