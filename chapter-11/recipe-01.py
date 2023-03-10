# recipe-01: 모듈

# ## 방법 1
# import theater_module
# theater_module.price(3)
# theater_module.price_morning(4)
# theater_module.price_soldier(5)

# ## 방법 2
# import theater_module as mv #  모듈의 별명 설정
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# ## 방법 3
# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(5)

# ## 방법 4
# from theater_module import price, price_morning
# price(3)
# price_morning(4)
# # price_soldier(5) # ERROR!!

## 방법 5
from theater_module import price_soldier as price
price(5)