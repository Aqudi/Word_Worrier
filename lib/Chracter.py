import random

class Character:
    def __init__(self, name, healthPoint, attackPoint, avoidChance, criticalChance):
        self.name = name
        self.HP = healthPoint
        self.AP = attackPoint
        self.AC = avoidChance
        self.CC = criticalChance

    def modifyHP(self, point):
        self.HP += point

    def modifyAP(self, point):
        self.AP += point

    def modifyAC(self, point):
        self.AC += point

    def modifyCC(self, point):
        self.CC += point

    def getHP(self):
        return self.HP

    def getAP(self):
        return self.AP

    def getAC(self):
        return self.AC

    def getCC(self):
        return self.CC

    def getName(self):
        return self.name

    def getInformation(self):
        information = [self.name, self.HP, self.AP, self.AC, self.CC]
        for i in information:
            print(i)
        print()

    def jackpot(self, point):
        point = int(point * 10)  # 99.9%의 경우에는 99.9로 저장되므로 *10을 해서 정수로 바꿔준다.
        percentList = [1 for x in range(point)] + [0 for x in range(1000 - point)]
        return random.choice(percentList) == 1

    def attack(self, target):
        # 크리티컬 판정
        damage = self.getAP()
        if self.jackpot(self.getCC()):
            damage *= 2
            print("크리티컬! 데미지 2배")

        print("{} -> {} 공격! 데미지 : {}".format(self.name, target.getName(), damage))
        target.damaged(damage)

    def damaged(self, damage):
        # 회피 판정
        avoidanceLevel = 0
        for i in range(3):
            if self.jackpot(self.getCC()):
                avoidanceLevel += 1
        damage = int(damage - damage * avoidanceLevel * 33 / 100)
        print("{} {}단계 회피! 피해량 {}%감소! 피해량 : {}\n".format(self.name, avoidanceLevel, avoidanceLevel*33, damage))
        self.modifyHP(damage * -1)

    def checkAlive(self):
        return self.HP <= 0


class Villain(Character):
    pass


class Hero(Character):
    pass


if __name__ == "__main__":
    villain = Villain("조커", 5000, 200, 10, 40)
    hero = Hero("슈퍼맨", 5000, 150, 50, 13.5)
    while hero.checkAlive() is False and villain.checkAlive() is False:
        villain.attack(hero)
        hero.attack(villain)

        villain.getInformation()
        hero.getInformation()