from bs4 import BeautifulSoup
import requests
import configparser
from word import Word


class Searcher:
    def __init__(self):
        config = configparser.RawConfigParser()
        config.read("config.ini")
        self.API_KEY = config.get('Default', 'api_key')

    #
    def getWordInformation(self, word, start=1):
        BASE_URL = "https://opendict.korean.go.kr/api/search"
        parameters = {"key": self.API_KEY, 'target_type': 'search',
                      'part': 'word', 'q': word,
                      'sort': 'dict', 'start': start,
                      'num': 10,
                      }

        with requests.Session() as s:
            request = s.get(BASE_URL, params=parameters)
            if request.status_code == 200 and request.ok:
                soup = BeautifulSoup(request.text, 'html.parser')
                wordName = soup.find("word").string
                wordDefinition = soup.find("definition").string
                if wordName is None or wordDefinition is None:
                    return "error: 없는데이터"
                else:
                    return wordName + ": " + wordDefinition
            else:
                return "error: Request에러"


if __name__ == "__main__":
    d = Searcher()
    word = input("검색하고 싶은 단어를 입력해주세요 : ")
    result = d.getWordInformation(word)
    print(result)
    w = Word()
    result = d.getWordInformation(w.getRandomWord())
    print(result)
