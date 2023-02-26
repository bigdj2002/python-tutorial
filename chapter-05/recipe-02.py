# recipe-02: 사전

cabinet = {3:"유재석", 100:"김태호"} # 사전은 괄호 {key, data}, 리스트는 괄호 []
print(cabinet[3])
# print(cabinet[5]) // ERROR!
print(cabinet[100])

print(cabinet.get(3))
print(cabinet.get(5))
print(cabinet.get(5, "사용 가능")) # 대체 출력
print(cabinet.get(100))

print(3 in cabinet)
print(5 in cabinet)

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새로운 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 손님이 떠남
del cabinet["A-3"]
print(cabinet)

# Key 정보 출력
print(cabinet.keys())

# Value 정보 출력
print(cabinet.values())

# Key, Value 쌍 출력
print(cabinet.items())

# 폐점
cabinet.clear()
print(cabinet)
