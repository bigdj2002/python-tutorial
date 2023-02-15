python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Jave"))

index = python.index("n") # python 문장에서 첫번째 n이 몇번째 인덱스인지?
print(index)
index = python.index("n", index + 1) # python 문장에서 2번째 n이 몇번째 인덱스인지?
print(index)

print(python.find("Java")) # Java 문자열이 없으므로 -1 리턴
# print(python.index("Java")) # index 함수에서는 찾는 문자열이 없으면 에러 리턴
print("hi")
print(python.count("n"))