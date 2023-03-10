# recipe-01: 클래스
# Using 스타크래프트

name = "마린"
hp = 40
damage = 5

print("{} 유닛 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}".format(hp, damage))

tank_name = "탱크"
tank_hp = 150
tank_damage = 35

tank2_name = "탱크"
tank2_hp = 150
tank2_damage = 35

print("{} 유닛 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(\
        name, location, damage))
    
attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
attack(tank2_name, "1시", tank2_damage)
print("\n")


# 위의 코드를 아래와 같이 간편하게! Using class
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{} 유닛 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
        
marine = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)