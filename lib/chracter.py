import random


class Character:
    def __init__(self, name, health_point, attack_point, avoid_chance, critical_chance, image):
        self.name = name
        self.image = image
        self.hp = health_point
        self.ap = attack_point
        self.ac = avoid_chance
        self.cc = critical_chance

    def modify_hp(self, point):
        self.hp += point

    def modify_ap(self, point):
        self.ap += point

    def modify_ac(self, point):
        self.ac += point

    def modify_cc(self, point):
        self.cc += point

    def get_hp(self):
        return self.hp

    def get_ap(self):
        return self.ap

    def get_ac(self):
        return self.ac

    def get_cc(self):
        return self.cc

    def get_name(self):
        return self.name

    def get_information(self):
        information = [("name", self.name), ("HP", self.hp), ("AP", self.ap), ("AC", self.ac), ("CC", self.cc)]
        for tag, value in information:
            print(tag, ": ", value)
        print()

    def jackpot(self, point):
        point = int(point * 10)  # 99.9%의 경우에는 99.9로 저장되므로 *10을 해서 정수로 바꿔준다.
        percent_list = [1 for x in range(point)] + [0 for x in range(1000 - point)]
        return random.choice(percent_list) == 1

    def attack(self, target):
        # 크리티컬 판정
        damage = self.ap
        if self.jackpot(self.cc):
            damage *= 2
            print("크리티컬! 데미지 2배")

        print("{} -> {} 공격! 데미지 : {}".format(self.name, target.get_name(), damage))
        target.damaged(damage)

    def damaged(self, damage):
        # 회피 판정
        avoidance_level = 0
        for i in range(3):
            if self.jackpot(self.cc):
                avoidance_level += 1
        damage = int(damage - damage * avoidance_level * 33 / 100)
        print("{} {}단계 회피! 피해량 {}%감소! 피해량 : {}\n".format(self.name, avoidance_level, avoidance_level*33, damage))
        self.modify_hp(damage * -1)

    def check_alive(self):
        return self.hp <= 0


class Villain(Character): 
    pass


class Hero(Character):
    pass


if __name__ == "__main__":
    import Data.Resource_rc
    villain = Villain("최빵빵", 5000, 200, 50, 10, ":/newPrefix/First Boss.PNG",)
    hero = Hero("김큐티", 5000, 150, 3, 25, ":/newPrefix/Hero.PNG",)
    while hero.check_alive() is False and villain.check_alive() is False:
        villain.attack(hero)
        hero.attack(villain)

        villain.get_information()
        hero.get_information()