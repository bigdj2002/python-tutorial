# recipe-08: 외장함수

# Refer to keyword "list of python modules" in Google
# https://docs.python.org/3/py-modindex.html

# glob: 경로 내의 폴더 / 파일 목록 조회 (윈도우에서의 dir)
# import glob
# print(glob.glob("*.py"))

# os: 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd()) # 현재 디렉토리

# folder = "sample_dir"
# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder)
#     print(folder, "폴더를 생성하였습니다.")

# print(os.listdir())

# time: 시간 관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M-%S"))

# datatime: 날짜 관련 함수
import datetime
print("오늘 날짜는 ", datetime.date.today())
today = datetime.date.today()
td = datetime.timedelta(days=100) # timedelta : 두 날짜 사이의 간격
print("우리가 만난지 100일은", today + td)
