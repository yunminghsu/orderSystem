# -*- coding: utf-8 -*-
"""點餐系統.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17muTK84mcUFXcXXQTXXW987ht2r3DOwl
"""

orderMenu={
    "漢堡":80,"薯條":50,"大杯可口可樂":45,"蘋果派":60,
}
order={}

totalPrice=0

print("歡迎光臨")
print("菜單：")
for i in orderMenu:
  print(i,":",orderMenu[i],"元")

while True:
  choice=input("請輸入餐點品項，輸入Q以跳出：")
  if choice.lower()=="q":
    break
  elif choice not in orderMenu:
    print("查無餐點")
    continue
  qty=int(input("請問要幾份"))
  order[choice]=qty
  totalPrice += qty*orderMenu[choice]
print("=========")
print("您點了")
for item,qty in order.items():
  print(item,"x",qty)
print(totalPrice,"元")