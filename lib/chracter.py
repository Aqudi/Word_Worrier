import random


class Character:
    def __init__(self, name, health_point, attack_point, avoid_chance, critical_chance,image, auto_attack=1):
        self.name = name
        self.image = image
        self.max_hp = health_point
        self.hp = self.max_hp
        self.ap = attack_point
        self.ac = avoid_chance
        self.cc = critical_chance
        self.aa = auto_attack
        self.get_information()

    def modify_hp(self, point):
        if self.hp + point <= self.max_hp:
            self.hp += point
        else:
            self.hp = self.max_hp

    def modify_max_hp(self, point):
        amount = int(self.max_hp * (1+point/100))
        self.max_hp = amount
        self.modify_hp(self.max_hp * point/100)
        print("hp ", self.hp, "max_hp ", self.max_hp)

    def modify_ap(self, point):
        self.ap = int(self.ap * (1+point/100))

    def modify_ac(self, point):
        self.ac = round(self.ac * (1+point/100), 1)

    def modify_cc(self, point):
        self.cc = round(self.cc * (1+point/100), 1)

    def modify_aa(self, point):
        self.aa = point

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def get_ap(self):
        return self.ap

    def get_ac(self):
        return self.ac

    def get_cc(self):
        return self.cc

    def get_name(self):
        return self.name

    def get_aa(self):
        return self.aa

    def get_image(self):
        return self.image

    def get_information(self):
        information = [("name", self.name), ("HP", self.hp), ("AP", self.ap), ("AC", self.ac), ("CC", self.cc), ("AA", self.aa)]
        #for tag, value in information:
        #    print(tag, ": ", value)
        return information

    def jackpot(self, point):
        point = int(point * 10)  # 99.9%의 경우에는 99.9로 저장되므로 *10을 해서 정수로 바꿔준다.
        percent_list = [1 for x in range(point)] + [0 for x in range(1000 - point)]
        return random.choice(percent_list) == 1

    def attack(self, target, buff=0):
        attack_result = ""
        # 크리티컬 판정
        damage = self.ap + buff
        if self.jackpot(self.cc):
            damage *= 2
            attack_result += "크리티컬! 데미지 2배\n"
        attack_result += "{} -> {} 공격! 데미지 : {}".format(self.name, target.get_name(), damage)
        damaged_result = target.damaged(damage)
        return (attack_result, damaged_result)

    def damaged(self, damage):
        damaged_result = ""
        # 회피 판정
        avoidance_level = 0
        for i in range(3):
            if self.jackpot(self.cc):
                avoidance_level += 1
        damage = int(damage - damage * avoidance_level * 33 / 100)
        damaged_result += "{} {}단계 회피! 피해량 {}%감소! 피해량 : {}\n".format(self.name, avoidance_level, avoidance_level*33, damage)
        self.check_alive()
        #print(damaged_result)
        self.modify_hp(damage * -1)

        return damaged_result

    def check_alive(self):
        if self.hp <= 0:
            self.hp = 0
        return self.hp <= 0


class Villain(Character):
    def __init__(self, name="최빵빵", health_point=5000, attack_point=250, avoid_chance=5, critical_chance=5, image=":/newPrefix/First Boss.PNG", auto_attack=5):
        super().__init__(name, health_point, attack_point, avoid_chance, critical_chance, image, auto_attack)

    @staticmethod
    def get_images_resource():
        images = [":/newPrefix/First Boss.PNG", ":/newPrefix/Second Boss.PNG", ":/newPrefix/Third Boss.PNG",
                  ":/newPrefix/Fourth Boss.PNG", ":/newPrefix/Final Boss.PNG"]
        return images

class Hero(Character):
    def __init__(self, name="김큐티", health_point=1000, attack_point=150, avoid_chance=10, critical_chance=15, image=":/newPrefix/Hero.PNG", auto_attack=1):
        super().__init__(name, health_point, attack_point, avoid_chance, critical_chance, image, auto_attack)


if __name__ == "__main__":
    import Data.Resource_rc
    villain = Villain("최빵빵", 5000, 200, 50, 10, ":/newPrefix/First Boss.PNG",)
    hero = Hero("김큐티", 5000, 150, 3, 15, ":/newPrefix/Hero.PNG",)
    while hero.check_alive() is False and villain.check_alive() is False:
        villain.attack(hero)
        hero.attack(villain)

        villain.get_information()
        hero.get_information()