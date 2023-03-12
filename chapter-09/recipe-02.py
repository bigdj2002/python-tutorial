# recipe-02: _init_
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{} 유닛 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
        
marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

# marine3 = Unit("마린") # Error!
# marine4 = Unit("마린", 40) # Error!
# Init에 정의된 인자의 갯수만큼 생성자 함수에 인자가 들어가야함 (반드시)