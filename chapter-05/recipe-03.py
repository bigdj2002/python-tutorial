# recipe-03: 튜플
# 리스트보다 빠름

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선가스") // ERROR!

name = "김종국"
age = 50
hobby = "축구"
print(name, age, hobby)
(name, age, hobby) = ("조세호", 30, "요리")
print(name, age, hobby)