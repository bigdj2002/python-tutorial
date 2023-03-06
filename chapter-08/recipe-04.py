# recipe-04: pickle

import pickle # 프로그램 상에서 사용중인 데이터를 파일 형태로 관리

profile_file = open("profile.pickle", "wb") # pickle은 무조건 binary
profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile로 불러오기
print(profile)
profile_file.close()