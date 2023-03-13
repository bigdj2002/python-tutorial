# recipe-02: 패키지

## 모듈의 집합

# ## 방법 1
# import travel.thailland # (import only - class, function 호출 불가)
# trip_to = travel.thailland.ThaillandPackage()
# trip_to.detail()

# ## 방법 2
# from travel.thailland import ThaillandPackage # (from / import - class, function 호출 가능)
# trip_to = ThaillandPackage()
# trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()