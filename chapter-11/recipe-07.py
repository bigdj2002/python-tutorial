# recipe-07: 내장함수

# Refer to keyword "list of python builtins" in Google
# https://docs.python.org/3/library/functions.html

# iuput : 사용자 입력을 받는함수
# language = input("무슨 언어를 좋아하세요? ")
# print("{0} 아주 좋은 언어야!".format(language))

# dir : 어떤 객체를 넘겨줬을 때, 해당 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())
print("\n")
import random
print(dir())
print("\n")
import pickle
print(dir())
print("\n")
print(dir(random))
print("\n")

lst = [1, 2, 3]
print(dir(lst))
print("\n")

name = "Jim"
print(dir(name))
print("\n")