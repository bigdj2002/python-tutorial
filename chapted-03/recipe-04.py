from random import *

print(random()) # 0이상, 1미만의 임의의 값 생성
print(random() * 10) # 0이상, 10미만의 임의의 값 생성
print(int(random() * 10)) # 0이상, 10미만의 임의의 정수값 생성
print(int(random() * 10)) # 0이상, 10미만의 임의의 정수값 생성
print(int(random() * 10)) # 0이상, 10미만의 임의의 정수값 생성
print(int(random() * 10) + 1) # 0이상, 10이하의 임의의 정수값 생성
print(int(random() * 10) + 1) # 0이상, 10이하의 임의의 정수값 생성
print(int(random() * 10) + 1) # 0이상, 10이하의 임의의 정수값 생성

# 로또 번호 출력
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)

print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성

print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성