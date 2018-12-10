from random import choice, randrange


class Card:
    def __init__(self):
        # 카드의 유형, 이름, 값
        self.card_type = ""
        self.card_name = ""
        self.card_stats_value = 0

        # 카드유형 공격, 스탯업그레이드
        self.CARD_TYPE_LIST = ("ATTACK", "STAT", "HEAL")

        # 공격, 스탯카드의 종류
        self.STATS_LIST = ("HP", "AP", "AC", "CC", "AA")
        self.ATTACKS_LIST = ("TRIPLE", "DOUBLE", "NORMAL")
        self.HEALS_LIST = ("MIRACLE", "HOLY", "CURE")

        # 카드 풀 value : 기본세팅
        type_pool_values = [3, 2, 2]
        stats_pool_values = [4, 3, 4, 2, 6]
        attacks_pool_values = [1, 3, 6]
        heals_pool_values = [1, 5, 13]

        # 카드 풀 세팅
        self.card_pool = {"TYPE": [],
                          "STAT": [],
                          "ATTACK": [],
                          "HEAL": []}
        self.card_pool_list = {"TYPE": self.CARD_TYPE_LIST,
                               "STAT": self.STATS_LIST,
                               "ATTACK": self.ATTACKS_LIST,
                               "HEAL": self.HEALS_LIST}
        self.card_pool_values = {"TYPE": type_pool_values,
                                 "STAT": stats_pool_values,
                                 "ATTACK": attacks_pool_values,
                                 "HEAL": heals_pool_values}
        self.set_card_pool()
        
        # 실제 카드 정보 저장
        self.set_random_pool_value()

    # 카드 확률 풀 설정
    def set_card_pool(self, keys=None):
        if keys is None:
            keys = self.card_pool.keys()
        for key in keys:
            for name, value in zip(self.card_pool_list[key], self.card_pool_values[key]):
                self.card_pool[key] += [name] * value
        #print(self.card_pool)

    def set_random_pool_value(self):
        value_scope = {}
        value_list = [(20, 40), (10, 20), (2, 4), (2, 4), (2, 5), (3, 4), (2, 3), (1, 2), (5, 8), (10, 12), (17, 20)]
        for name, value in zip(self.STATS_LIST + self.ATTACKS_LIST + self.HEALS_LIST, value_list):
            value_scope.update({name: value})
        #print(value_scope)
        self.card_type = choice(self.card_pool["TYPE"])
        self.card_name = choice(self.card_pool[self.card_type])
        self.card_stats_value = randrange(value_scope[self.card_name][0], value_scope[self.card_name][1],)

    def get_type(self):
        return self.card_type

    def get_name(self):
        return self.card_name

    def get_value(self):
        return self.card_stats_value

    def get_information(self):
        information = [("TYPE", self.card_type), ("NAME", self.card_name), ("VALUE", self.card_stats_value)]
        for tag, value in information:
            print(tag + " : ", value)
        return information


if __name__ == "__main__":
    c = Card()
    for i in range(100):
        c.set_random_pool_value()
        c.get_information()

